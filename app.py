# モジュール
from flask import Flask, request
from flask_cors import CORS, cross_origin
from urllib.parse import urlparse

# アプリケーションの本体を作成
app = Flask(__name__)
CORS(app)

import main

# キャッシュをコントロールする
@app.after_request
def add_header(r):
  r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
  r.headers["Pragma"] = "no-cache"
  r.headers["Expires"] = "0"
  r.headers['Cache-Control'] = 'public, max-age=0'
  if "location" in r.headers:
    parsed = urlparse(request.url)
    r.headers['location'] = "https://" + parsed.hostname + r.headers["location"]
  return r

# ファイルを実行したら、サーバーを起動する
if __name__ == '__main__':
  app.debug = True
  app.run(host= '0.0.0.0', port=8080)
