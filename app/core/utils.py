# send slack webhook
def send_slack_notification(message, username, icon_emoji):
    """
    Send a slack notification
    """
    import requests
    import os
    import json

    if url := os.getenv('SLACK_WEBHOOK_URL'):
        payload = {
            'username': username,
            'icon_emoji': icon_emoji,
            'text': message
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(payload), headers=headers)
