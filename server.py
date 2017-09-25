from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.secret_key = "b'\x95=\xb1\t\xb2\x8eL\r\xed\x17\x07MQ\xf5\x86\xb3\xac\xed<\x92\x05Z\xb6\xae'"
    app.run(
        debug=True,
        port=5000
    )