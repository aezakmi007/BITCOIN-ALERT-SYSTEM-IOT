import conf, json, time, requests
from boltiot import Sms, Bolt
import json , time


maximum_price = 400
minimum_price = 100


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)



def get_bitcoin_price():
                                 URL = "https://min-api.cryptocompare.com/data/price"
                                 queryString = {"fsym":"BTC","tsyms":"USD"}
                                 response = requests.request("GET", URL, params=queryString)
                                 response = json.loads(response.text)
                                 current_price = response['USD']
                                 return current_price
while True:



               
               print("Checking for Threshold breach") 
               price = get_bitcoin_price()
               print("Current value of Bit Coin in USD is:" +str(price))
               if price > maximum_price or price < minimum_price :
                     mybolt.digitalWrite(0,"HIGH")
                     time.sleep(5)
                     mybolt.digitalWrite(0,"LOW")
                     
                     print("Making Request to Twilio")
                     res = sms.send_sms("The current bitcoint value in USD is:" +str(price))
                     print("Response received from TWILIO is:" +str(res))


               time.sleep(10)
