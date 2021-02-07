import sys
import time
import urllib.request
import json
from datetime import datetime
from playsound import playsound
from google_speech import Speech

#usage: <scriptname> <cryptonamefiat (ETHUSD)> <unixtime> <threshold>

api_domain = "https://api.kraken.com"
api_path = "/0/public/"
api_method = "Trades"
api_data = ""

play_file = 'Erebor_Horn.wav'


if len(sys.argv) < 1:
    print('usage <scriptname> <cryptonamefiat (ETHUSD)> <unixtime> <threshold>')
    sys.exit(1)

api_symbol = sys.argv[1].upper()
api_start = str(int(time.time()) - 1) + "999999999"
#api_start = str(time.time()-5).split('.')[0]
#api_end = str(time.time()).split('.')[0]


if len(sys.argv) > 4:
    api_end = sys.argv[4]
else:
    api_end = "9999999999"


last_price = 0
crypto_dict = {'XETHZUSD':'Etherium is ', 'GRTUSD':'Graph is ', 'XLTCZUSD':'Litecoin is ', 'XXRPZUSD':'Ripple is '} #coin labels that I found to work


try:
    while True:
        api_data = "?pair=%(pair)s&since=%(since)s" % {"pair":api_symbol, "since":api_start}
        #print(api_data) #for debugging
        api_request = urllib.request.Request(api_domain + api_path + api_method + api_data)
        try:
            api_data = urllib.request.urlopen(api_request).read()
        except Exception:
            time.sleep(5)
            continue
        api_data = json.loads(api_data)
        if len(api_data["error"]) != 0:
            time.sleep(5)
            continue
        #print(api_data["result"]) #for debugging
        for trade in api_data["result"][api_symbol]:
            if int(trade[2]) < int(api_end):
                #print(datetime.utcfromtimestamp(trade[2]+10800).strftime('%Y-%m-%d %H:%M:%S')+" "+api_symbol+" = %(price)s" % {"price":trade[0]}) #for debugging
                text = crypto_dict[sys.argv[1]] + trade[0][:4] + " dollars s"
                speech = Speech(text, 'en')
                if trade[0][:4] != last_price:
                    print(datetime.utcfromtimestamp(trade[2]+10800).strftime('%Y-%m-%d %H:%M:%S')+" "+api_symbol+" = %(price)s" % {"price":trade[0]})
                    speech.play()
                    last_price = trade[0][:4]
                if float(trade[0]) >= float(sys.argv[3]): #threshold for alarm
                    playsound(play_file)
            else:
                sys.exit(0)
            api_start = api_data["result"]["last"]
except KeyboardInterrupt:
    None

sys.exit(0)