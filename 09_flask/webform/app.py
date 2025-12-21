# index.htmlと連携したflask利用のコードをかく

from flask import Flask, request, render_template

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)  #(呪文。)

# ルート '/' にアクセスした際に 'index.html' を表示させる
@app.route('/')
def index():
    return render_template('index.html')

# ルート '/submit' にPOSTリクエストが来たときの処理
@app.route('/submit', methods=['POST'])
def submit():
    
    # フォームから送信された 'name' と 'email' を取得
    name = request.form.get('name')
    email = request.form.get('email')

    # サーバー側のバリデーション
    if not name or not email: # 引数が空だった場合の処理
        return "Error: All fields are required!"
    if "@" not in email: # emailに@が含まれない場合の処理
        return "Error: Invalid email address!"

    # 取得したデータを 'submit.html' テンプレートに渡して表示
    return render_template('submit.html', name=name, email=email)

# アプリケーションをデバッグモードで実行(呪文。)
if __name__ == '__main__':
    app.run(debug=True)
