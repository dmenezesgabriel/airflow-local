import os
from slack import WebClient
from slack.errors import SlackApiError


slack_token = os.environ['SLACK_API_TOKEN']
client = WebClient(token=slack_token)


def send_message(**kwargs):
    try:
        message = kwargs['message']
        channel = kwargs['channel']
        response = client.chat_postMessage(
            # Slack Channel
            channel=channel,
            # Message
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"{message}:"
                    }
                }
            ]
        )
        return response
    except SlackApiError as error:
        pass
