from flask import Flask
app = Flask(__name__)


@app.route("/flask")
def hello():
    return """
    <h1 style='color:blue'>Hello There!</h1>
    <h2>
        flask
    </h2>
    """

if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0')
    # host='0.0.0.0' red local