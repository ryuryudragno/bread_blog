# モジュール
import json

# JSONファイルを読み込む関数
def load_json(JSONFILE):
  # JSONファイルをロードする
  json_file = json.load(open(JSONFILE, 'r'))
  # 処理した結果を返す
  return json_file
