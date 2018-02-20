import os 
from flask_platform import app 

def runApp ():
    app.run(host='0.0.0.0', port=5000)
    
if __name__ == "__main__": 
    runApp()