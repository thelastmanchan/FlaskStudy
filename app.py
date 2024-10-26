from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", title="민찬의 홈페이지", message="환영합니다")

if __name__ == '__main__':
    app.run(debug=True)
