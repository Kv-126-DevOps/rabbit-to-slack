# Rabbit-to-slack

This application grabs data from RabbitMQ queue and send to Slack

### Create Slack Webhook URL

In the article "Sending an automated message to slack using python" you can find how to connect "Incoming Webhooks to slack" create Webhook URL that will be as SLACK_URL variable  [link](https://medium.com/@sharan.aadarsh/sending-notification-to-slack-using-python-8b71d4f622f3)
Channel for slack is specified during "Incoming Webhooks to slack" configuration.

### Run rabbit-to-slack
    git clone --branch 1-rabbit-to-slack-code-refactoring https://github.com/Kv-126-DevOps/rabbit_to_slack.git /opt/rabbit-to-slack
    docker run --network=kv126 -e RABBIT_HOST=rabbit -e RABBIT_PORT=5672 -e RABBIT_USER=mquser -e RABBIT_PW=mqpass -e RABBIT_QUEUE=slack -e SLACK_URL="<Get from https://devopskv-126.slack.com/services/3459809187923?updated=1 -> Webhook URL>" -d --name rabbit-to-slack -v /opt/rabbit-to-slack:/app python:3.9-slim sleep infinity
    docker exec rabbit-to-slack  pip install -r /app/requirements.txt
    docker exec -d rabbit-to-slack bash -c "cd /app && python ./app.py"

    When  json-filter and rabbit-to-slack are configured , messages for new issues in the connected Github repo will be appeared in the configured for integration slack channel.
	

