####### Returns the Siglos Queue in data format. ########
import json
from pprint import pprint

import requests
from lxml import html
import xml.etree.ElementTree as ET



#### The API call returns an XML document representing the current queue   #####
#### We will convert it to an array of objects  #####




def getQueue(proxy):
    mysecondres = requests.get(f'https://connectkaraoke.com/proxy/{proxy}/searchsongquery?mode=5')
    root = ET.fromstring(mysecondres.content)  # parse the XML string to Element object

    queue_list = []

    for i, song in enumerate(root.findall('song')):
        singername = song.find('singername').text
        songid = song.find('songid').text
        songname = song.find('songname').text
        time = song.find('time').text
        canedit = song.find('canedit').text
        canmoveup = song.find('canmoveup').text
        canmovedown = song.find('canmovedown').text

        song_dict = {
            "index": i,
            "singername": singername,
            "siglosid": songid,
            "songname": songname,
            "estimatedtime": time,
            "canedit": canedit,
            "canmoveup": canmoveup,
            "canmovedown": canmovedown
        }

        queue_list.append(song_dict)


    return queue_list

def getCurrentSinger():
    url = 'https://catandbarz.com/graphql'

    data = {'query': '''
                query{
     getCurrentSinger{
      userID
      stageName
      bio
      photo

    }

    }

            '''}

    response = requests.post(url, json=data)


    if response.status_code == 200:
        res = response.json()
        return response.json()
    else:
        print('Request failed with status code', response.status_code)
        return -1

