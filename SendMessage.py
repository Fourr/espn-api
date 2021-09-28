import requests
import json


def send_discord_message(msg: str, channel_id: str = '<your channel id>'):

    TOKEN = 'token'

    # set all the required headers to make a request to discord end point api
    headers = {
        'Authorization': f'Bot {TOKEN}',
        'Content-Type': 'application/json'
    }

    # convert this dict in to json object
    message = json.dumps({'content': msg})

    # make a post request to discord end point api with all the data we've set up above
    r = requests.post(f'https://discordapp.com/api/channels/{channel_id}/messages', headers=headers, data=message)

    # if the returned status code is not 200 (OK), it means there's an error
    if r.status_code != 200:
        # log the error so we know our post request was failed and react accordingly
        print(f'Failed to send message, returned status code: {r.status_code}')
