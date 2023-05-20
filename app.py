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

line_bot_api = LineBotApi('W+xBMc7CYH/D6oTwS6o90qJbp/lQKH9pnyJ03Zga9njCDN5Dd+ee3UrQrP9uGgixhXeQetHbFch5WYFhIppiMRoLZbkHr6qF4f88bS6Rzd5D6/J6iriVVMvZVEwehn6KB6L9Bn+DvoI8V0GHg8AM6QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('899f4bfe74277f6fcb659d3bce178e4a')


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
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎？'))


if __name__ == "__main__":
    app.run()