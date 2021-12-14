import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


def getEnvVariable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected env variable {name} not set."
        raise Exception(message)

SLACK_URL = getEnvVariable("SLACK_URL")
SLACK_BUG = getEnvVariable("SLACK_BUG")
SLACK_US = getEnvVariable("SLACK_US")
SLACK_TC = getEnvVariable("SLACK_TC")



#POSTGRES_HOST = getEnvVariable("POSTGRES_HOST")
#POSTGRES_PORT = getEnvVariable("POSTGRES_PORT")
#POSTGRES_USER = getEnvVariable("POSTGRES_USER")
#POSTGRES_PW = getEnvVariable("POSTGRES_PW")
#POSTGRES_DB = getEnvVariable("POSTGRES_DB")

RABBIT_HOST = getEnvVariable("RABBIT_HOST")
RABBIT_PORT = getEnvVariable("RABBIT_PORT")
RABBIT_USER = getEnvVariable("RABBIT_USER")
RABBIT_PW = getEnvVariable("RABBIT_PW")
RABBIT_QUEUE = getEnvVariable("RABBIT_QUEUE")


#POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

#DB_URL = POSTGRES_URL

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'HelloWorld'
