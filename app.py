from flask import Flask, render_template

# 創建 Flask 應用
app = Flask(__name__)

# 設定首頁路由
@app.route('/')
def home():
    return 'Hello 你好'

if __name__ == '__main__':
    app.run(debug=True)