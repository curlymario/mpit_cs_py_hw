from pubnub import Pubnub

PUB_KEY = 'pub-c-bab40884-15d8-42a3-8675-21d381efc60e'
SUB_KEY = 'sub-c-d3ff6da6-faa9-11e5-8180-0619f8945a4f'

pubnub = Pubnub(publish_key=keys.PUB_KEY, subscribe_key=keys.SUB_KEY)

def _callback(message, channel):
    print(message)

def _error(message):
    print(message)

pubnub.subscribe(channels="my_channel_sf23", callback=_callback, error=_error)

while True:
    pass