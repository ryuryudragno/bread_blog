# モジュール
import json

# JSONファイルを保存する関数
def save_json(JSONFILE, data):
  # JSONファイルを保存する
  json.dump(data, open(JSONFILE, 'w'), ensure_ascii = False, indent = 2)
