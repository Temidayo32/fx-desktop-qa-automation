import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Your OAuth access token
token = os.getenv("SLACK_KEY")

# Initialize a Web API client
client = WebClient(token=token)

try:
    response = client.chat_postMessage(
        channel="#desktop-qa-monitoring-notifier",  # Channel ID or name (e.g., #general)
        text="from actions... 1",
    )
    print("i have sent the message.")
except SlackApiError as e:
    print(f"Error sending message: {e.response['error']}")


# {
#     "display_information": {
#         "name": "Demo App"
#     },
#     "settings": {
#         "org_deploy_enabled": false,
#         "socket_mode_enabled": false,
#         "is_hosted": false,
#         "token_rotation_enabled": false
#     }
# }
