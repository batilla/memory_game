from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/memory', methods=['GET'])
def game_page():
    #data = request.form.to_dict()
    #{"row":"5", "column": "6"}
    rows = request.args.get('row')
    cols = request.args.get('column')
    num = int(rows) * int(cols)
    return render_template('game.html', num=num)

if __name__ == '__main__':
    app.secret_key = "b'\x95=\xb1\t\xb2\x8eL\r\xed\x17\x07MQ\xf5\x86\xb3\xac\xed<\x92\x05Z\xb6\xae'"
    app.run(
        debug=True,
        port=5000
    )
