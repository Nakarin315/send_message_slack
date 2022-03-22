import requests
import sys
import getopt
from time import perf_counter
# Ref: https://youtu.be/lEQ68HhpO4g Slack API Tutorial: Post Slack Messages Using Python!

# Send Slack message using Slack API
# Slack alerts-strontium URL: 'https://hooks.slack.com/services/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'

class MessageSender:
    def __init__(self, delay=300):
        self.messages = dict()
        self.delay = delay

    def send_slack_message(self, message):
        index = list(message.split('\n'))[0]
        if index not in self.messages or (perf_counter() - self.messages[index] > self.delay):
            self.messages[index] = perf_counter()
            MessageSender._send_slack_message(message)

    @staticmethod
    def _send_slack_message(message):
        payload = '{"text":"%s"}' % message
        response = requests.post('https://hooks.slack.com/services/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',data=payload)

send_slack_message = MessageSender().send_slack_message
