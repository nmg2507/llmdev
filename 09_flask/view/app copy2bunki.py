# テンプレートの基本

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<user_name>')
def index(user_name):
    return render_template('index.html', name=user_name)
# Flaskが templates フォルダから index.html を探して表示
# その際、name へ user_nameを代入

if __name__ == '__main__':
    app.run(debug=True)

