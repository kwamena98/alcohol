import time
from flask import *
import requests
import tweepy


app=Flask(__name__)


@app.route('/')
def api_root():
    return "Wow"

@app.route('/chance',methods=['POST'])
def webhook():
    # print(request.data)
    data=request.data
    print(data)
    # symbol=str(data['symbol'])
    # price=str(data['price'])
    # message=symbol+"Cross" +price
    data=data.decode('utf-8')


    r=data.replace("\n" ,"")
    r = r.replace("\'","")
    r = r.replace("|","")
    print(r)

    if "}" not in r:
        r += "}"
    j=json.loads(r)

    j=j
    symbol=j["symbol"]
    price=j["price"]
    text=j["message"]
    link=j["html"]

    message="${},{},{},{}".format(symbol,text,price,link)
    print(message)

    send_tweet(message)

    print(message)
    




    return message


def send_tweet(message):
    API_KEY="wFo6C5wN3BTN3artixVHYKaDl"
    API_KEY_SECRET="veaPuL4mitT0qaUbt6mnbU79YUxKDMsETlguqPmHnDubOD1ygD"
    ACCESS_TOKEN="1444344183129583624-4QmudzpmszR4IRxF9FaqoLVEZOQiZT"
    ACCESS_TOKEN_SECRET="YN0ogpmPYLH0Q2Kpr8t6mCezJZvwm5wgakSGLAND8c9z5"

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    api.update_status(message)
    time.sleep(60*15)

        


if __name__=="__main__":
    app.run(debug=True)


