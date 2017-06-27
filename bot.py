import slackclient

slack_api_token = 'xoxb-203931756929-eyHe3QYwJYBDmwqrUE9OhlKb'
slack_bot_name = 'hooray'

# initialize slack client
slack_client = slackclient.SlackClient(slack_api_token)

# check if everything is alright
is_ok = slack_client.api_call("users.list").get('ok')
print(is_ok)

# find the id of our slack bot
if(is_ok):
    for user in slack_client.api_call("users.list").get('members'):
        if user.get('name') == slack_bot_name:
            print(user.get('id'))
