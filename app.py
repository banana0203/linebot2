from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('fVXbw7Zx8oCultrzMTU7Gdf3H5fRz1Q1ZgqnD4sQcAaKHmxlIzNounZa1IAZD+T8rGK+xzkFBu3KS+e3NsfbKOUXszku9D6MsYSxO/jkr7gE2hx/CGdR0Qiv5+Q++GDm+zifq/Sk8F2HzaSkG4EQewdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('58ec22d0b73d114a91c2ce881c615838')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()