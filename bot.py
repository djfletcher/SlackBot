from slackclient import SlackClient

slack_token = 'xoxb-203931756929-eyHe3QYwJYBDmwqrUE9OhlKb'
bot_name = 'hooray'
bot_id = 'U5ZTDN8TB'

# initialize slack client
sc = SlackClient(slack_token)

sc.api_call(
    'chat.postMessage',
    channel="#general",
    text="oodelolly oodelolly golly whatta day",
    as_user=True
)
