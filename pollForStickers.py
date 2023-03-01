# imports


#################################

###### function to poll backend for changes in stickers ############
# Please note that the query does not yet exist on the backend.
# I will update when it does.
# Most of the returned items from the query are fairly self-evident.
# This function is just to poll for updates
# I may have to change the query to a mutation as I believe I will probably
# update a field called isProcessed so the query doesn't try to fetch messages we have already received.
# I will look at the graphql documentation. Hopefully I can just keep it as a query if I am only doing a simple
# call to the database to set isProcessed to true.

# I don't believe that we will need to send any variables with the query, but just let me know if we do. It
# won't be hard to add in.

# The rest of the comments are just ideas on how to implement the UI
# stickerCode is an integer to display a sticker on the screen for 5? seconds?
# includeStars is an integer with the amount of stars sent in message.
# stars will streak down from the top of the screen to the bottom, possibly with randomised trajectories and frequency
# I'm not sure how easy it will be to get the current singer. Unless I can get it from the connectkaraoke api, there
# are some factors that may not make it not accurate just getting it from queue, such as if the singer is changed due
# the original singer not being available. I will try to handle that from the host computer to manually
# enter the current singer

import requests


def fetch_new_messages():
    url = 'https://catandbarz.com/graphql'
    data = {'query': '''
        query {
          pollNewMessages {
            messageID
            messageIsFor
            messageIsFrom
            messageBody
            currentSinger
            songName
            stickerCode
            includeStars
          }
        }
    '''}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print('Error:', response.status_code)


url = 'https://catandbarz.com/graphql'

data = {'query': '''
    query {
      pollNewMessages {
        messageID
        messageIsFor
        messageIsFrom
        messageBody
        currentSinger
        songName
        stickerCode
      }
    }
'''}

response = requests.post(url, json=data)

if response.status_code == 200:
    res = response.json()
else:
    print('Error:', response.status_code)
