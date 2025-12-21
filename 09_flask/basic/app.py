# app.py　は、アプリのエントリーポイントとなるファイル
# flaskライブラリからFlaskクラスをインポート
from flask import Flask

# Flaskアプリのインスタンスを作成
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask!!"

if __name__ == '__main__':
    app.run(debug=True) #


"""
__name__ はFlaskがアプリのテンプレ等のリソースを
読み込むために使う特別な名前。


@app.route('/')はﾃﾞｺﾚｰﾀｰ構文。どの関数を実行するかを設定。
”/”　はトップページを指す。

"""