# routingの基本。
# Debug し終えたら、アプリを閉じ忘れないように。
from flask import Flask
from flask import request

app = Flask(__name__)

# トップへルーティング
@app.route("/")
# ユーザがアプリ（=トップのURLhttp://127.0.0.1:5000）へ
# アクセスすると続けてindex関数が実施される。
def index():
    return "Hello, Flask!"

#ソースコードをここから追加。

#複数のルーティングを設定する。
#（１） http://127.0.0.1:5000/about という追加ページ。
@app.route('/about')
def about():
    return "This is the about page."

#（２）パスパラメータを使う.
#URLの一部に動的に値を指定し、さらにそれを引数で受け取る.
@app.route("/hello/<username>")
def greet_user(username):
    return f"Hello, {username}!"

#（３）パスパラメータの型を指定.
@app.route("/user/<int:user_id>")
def show_user(user_id):
    return f"UserID is {user_id}"

#（４）クエリパラメータ requestオブジェクトで取得。
# http://127.0.0.1:5000/search?query=apple
@app.route('/search') #/search にアクセスが来たらこの関数を
def search():
    query = request.args.get('query')
    # ↑URLの ?query=〇〇 の「〇〇」を取り出す
    return f"Search results for: {query}"

# ソースコードここまで


if __name__ == "__main__":
    app.run(debug = True)

