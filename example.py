from flask import Flask
app = Flask(__name__)

from src.logger import logger
logger.register(app)

@app.route('/')
def home():
    logger.log("This is test message")
    return 'Welcome'

if __name__ == '__main__':
    app.run(debug=True)