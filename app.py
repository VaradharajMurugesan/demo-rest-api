from flask import Flask,request,jsonify
from datetime import datetime
from logging.config import dictConfig


dictConfig(
  {
    "version": 1,
    'formatters': {'default': {
    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(funcName)s : %(lineno)d : %(message)s',
    }},
    "handlers": {
      "time-rotate": {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": r"Log/estimator_log.log",
        "when": "D",
        "interval": 1,
        "backupCount": 20,
        "formatter": "default",
      },
    },
    "root": {
      "level": "DEBUG",
      "handlers": ["time-rotate"],
    },
  }
)

app = Flask(__name__)




@app.route('/')
def home():
    try:        
        return jsonify("Data Successfully Uploded")    
    except Exception as e:
        app.logger.error('An error occurred: %s', str(e))
        return jsonify(e,"An ERROR occurred in table POST Method") 
    

if __name__ == '__main__':
    app.run(debug=True)