from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def top():
    return "This page is My Website"

@app.route('/<user_name>')
def index(user_name):
    item_list = ["Apple", "Banana", "Cherry"]
    return render_template(
        'index.html', name=user_name, items=item_list
        )

# Flaskが templates フォルダから index.html を探して表示
# その際、name へ user_name,itemsを受け取って代入

if __name__ == '__main__':
    app.run(debug=True)