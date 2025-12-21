# テンプレートの基本

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# Flaskが templates フォルダから index.html を探して表示

if __name__ == '__main__':
    app.run(debug=True)

