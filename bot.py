from slackclient import SlackClient
import time

class SlackBot:

    slack_token = 'xoxb-203931756929-eyHe3QYwJYBDmwqrUE9OhlKb'
    bot_id = 'U5ZTDN8TB'

    # initialize slack client
    def __init__(self):
        self.sc = SlackClient(self.slack_token)

    def is_for_me(self, event):
        type = event.get('type')
        if type and type == 'message' and not event.get('user') == self.bot_id:
            return self.is_private(event) or self.im_mentioned(event)

    def is_private(self, event):
        channel = event.get('channel')
        return channel.startswith('D')

    def im_mentioned(self, event):
        text = event.get('text')
        return '<@{}>'.format(self.bot_id) in text.strip().split()

    def is_hi(self, message):
        tokens = [word.lower() for word in message.strip().split()]
        greetings = ['hello', 'hey', 'hi', 'hiya', 'sup', 'yo']
        return any(greeting in tokens for greeting in greetings)

    def is_bye(self, message):
        tokens = [word.lower() for word in message.strip().split()]
        goodbyes = ['bye', 'goodbye', 'cya']
        return any(bye in tokens for bye in goodbyes)

    def handle_message(self, message, user, channel):
        user_mention = '<@{}>'.format(user)
        if self.is_hi(message):
            self.post_message(message="Hiya, {}".format(user_mention), channel=channel)
        elif self.is_bye(message):
            self.post_message(message="Goodbye indeed, {}".format(user_mention), channel=channel)
        else:
            self.post_message(message="Sorry, {}, I didn't get that!".format(user_mention), channel=channel)

    def post_message(self, message, channel):
        self.sc.api_call('chat.postMessage', channel=channel, text=message, as_user=True)

    def run(self):
        if self.sc.rtm_connect():
            print "Connected"
            while True:
                event_list = self.sc.rtm_read()
                if len(event_list) > 0:
                    for event in event_list:
                        if self.is_for_me(event):
                            self.handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
                time.sleep(1)
        else:
            print 'Connection to Slack failed'


if __name__=='__main__':
    bot = SlackBot()
    bot.run()
