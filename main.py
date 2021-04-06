# モジュール
from __main__ import app
from flask import render_template, request, redirect, send_from_directory
from load_json import load_json
from save_json import save_json
from datetime import datetime
import os


# ===== 閲覧・記事投稿機能 =====
# 記事一覧のページ
@app.route('/', methods=['GET'])
def view_articles_route():
  # JSONファイルのデータを読み込む
  articles = load_json('articles.json')
  # 記事一覧のページを表示する
  return render_template('index.html', articles = articles)

# 記事の投稿：送信ボタンを押したとき
@app.route('/', methods=['POST'])
def create_article_route():
  # フォームから送信したテキストデータを受け取る
  title = request.form['title']
  # ファイル選択のフォームから送信した画像データを受け取る
  image_data = request.files['image_data']

  # タイトルが入力されている＆ファイルを添付しているとき
  if title and image_data:
    # 投稿したデータを保存する関数を呼び出す
    create_article(title, image_data)
  # 記事一覧のページを表示する
  return redirect('/')

# ===== 画像表示機能 =====
# 画像を表示
@app.route('/uploads/<image_name>', methods=['GET'])
def view_images_route(image_name):
  # uploadsフォルダにある画像データを返す
  return send_from_directory('uploads', image_name)


# ===== 投稿データを保存する関数 =====
# 画像を保存してファイル名を返す関数
def save_image(image_data):
  # 画像データからファイル名を受け取る
  image_name = image_data.filename
  # 画像データをuploadsフォルダに保存する
  image_data.save(os.path.join('uploads', image_name))
  # ファイル名を返す
  return image_name


# 現在の時間を返す関数
def current_time():
  # 現在の日付と時間を受け取る
  time_now = datetime.now()
  # 日付と時間のフォーマットを変換
  post_time = time_now.strftime('%Y年%m月%d日 %H:%M')
  # 時間を返す
  return post_time


# 投稿データを保存する関数
def create_article(title, image_data):
  # JSONファイルのデータを読み込む
  articles = load_json('articles.json')
  # 画像を保存してファイル名を受け取る
  image_name = save_image(image_data)
  # 現在の日付と時間を返す関数を呼び出す
  time = current_time()

  # フォームから送信した情報を追加する
  articles.append({
    "title": title,
    "image_name": image_name,
    "time": time
  })
  # JSONファイルを保存する
  save_json('articles.json', articles)
