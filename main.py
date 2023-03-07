from flask import Flask
from francais import home_page_fr
app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Welcome to the home page!'


@app.route('/fr/')
def fr():
    return home_page_fr()


if __name__ == '__main__':
    app.run(debug=True)
