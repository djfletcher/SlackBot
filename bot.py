from slackclient import SlackClient
import time

slack_token = 'xoxb-203931756929-eyHe3QYwJYBDmwqrUE9OhlKb'
bot_name = 'hooray'
bot_id = 'U5ZTDN8TB'

# initialize slack client
sc = SlackClient(slack_token)

def is_for_me(event):
    type = event.get('type')
    if type and type == 'message' and not event.get('user') == bot_id:
        return is_private(event) or im_mentioned(event)

def is_private(event):
    channel = event.get('channel')
    return channel.startswith('D')

def im_mentioned(event):
    text = event.get('text')
    return '<@{}>'.format(bot_id) in text.strip().split()

def handle_message(message, user, channel):
    # TODO Implement later
    post_message(message=message, channel=channel)

def post_message(message, channel):
    sc.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)
def run():
    if sc.rtm_connect():
        print "Connected"
        while True:
            event_list = sc.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(1)
    else:
        print('Connection to Slack failed')

if __name__=='__main__':
    run()
