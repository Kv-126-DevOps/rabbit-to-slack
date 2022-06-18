import logging
import sys

import pika
import pika.exceptions

from common import parseJson
from config import *
from slack import *

import ssl

#logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

def main():
    
    RABBIT_HOST = os.environ.get("RABBIT_HOST")
    RABBIT_PORT = os.environ.get("RABBIT_PORT")
    RABBIT_USER = os.environ.get("RABBIT_USER")
    RABBIT_PW = os.environ.get("RABBIT_PW")
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
    parameters = pika.URLParameters(f"amqp://{RABBIT_USER}:{RABBIT_PW}@{RABBIT_HOST}:{RABBIT_PORT}")
    parameters.ssl_options = pika.SSLOptions(context=ssl_context)
    
    def callback(channel, method, properties, body):
        data = parseJson(body.decode())
        print(body.decode())
        sendToSlack(data)
        print("Quenee clear")
        channel.basic_ack(delivery_tag=method.delivery_tag)

    while True:
        logging.info("Pika was started.")
        try:
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            # channel.basic_qos(prefetch_count=1)
            channel.queue_declare(queue=RABBIT_QUEUE)
            channel.basic_consume(RABBIT_QUEUE, callback)
            try:
                channel.start_consuming()
            except KeyboardInterrupt as ex:
                channel.stop_consuming()
                connection.close()
                break
        except pika.exceptions.ConnectionClosedByBroker as ex:
            #logging.info(f"ConnectionClosedByBroker - {ex}")
            continue
        except pika.exceptions.AMQPChannelError as ex:
            #logging.info(f"AMQPChannelError - {ex}")
            break
        except pika.exceptions.AMQPConnectionError as ex:
            #logging.info(f"AMQPConnectionError - {ex}")
            continue
        except Exception as ex:
            print(f"Exception - {ex}")
            #logging.info(f"Exception - {ex}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            exit(0)
