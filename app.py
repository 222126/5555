import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 設定 LINE Bot API
CHANNEL_SECRET = '你的Channel Secret'
CHANNEL_ACCESS_TOKEN = '你的Channel Access Token'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
line_handler = WebhookHandler(CHANNEL_SECRET)

# 設定 Webhook 路由
@app.route("/callback", methods=['POST'])
def callback():
    # 確認 X-Line-Signature 是否正確
    signature = request.headers['X-Line-Signature']
    
    # 取得請求的 body 資料
    body = request.get_data(as_text=True)
    
    try:
        # 驗證 webhook 並處理事件
        line_handler.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
        abort(400)
    
    return 'OK'


# 處理來自 LINE 的訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text  # 使用者發送的文字訊息
    reply_token = event.reply_token  # 回覆訊息的 token

    try:
        # 回覆用戶的訊息
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text=f"你說: {text}")
        )
    except LineBotApiError as e:
        print(f"Error: {e}")

# 主頁路由
@app.route("/")
def index():
    return "LINE Bot is running"

if __name__ == "__main__":
    app.run(debug=True)
