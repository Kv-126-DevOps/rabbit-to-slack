# Rabbit-to-slack

This application grabs data from RabbitMQ queue and send to Slack


### Create project folderdd
    sudo git clone https://github.com/DevOps-Kv-116/rabbit_to_slack
    cd rabbit_to_slack

### Create rabbit_to_postgres container
	docker build --tag="slack" .

### Create Slack Webhook URL
	In this artictle you can see how to create url [link](https://medium.com/@sharan.aadarsh/sending-notification-to-slack-using-python-8b71d4f622f3)

### Run rabbit_to_postgres container
	docker run -h slack --name slack --net bridge_issue -d --rm -e RABBIT_HOST=34.118.33.143 -e RABBIT_PORT=5672 -e RABBIT_USER=devops -e RABBIT_PW=softserve -e RABBIT_QUEUE=slack -e SLACK_URL=URL -e SLACK_CHANNEL=#chanel slack

