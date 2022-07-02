import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
   hostname=socket.gethostname()
   ipAddr=socket.gethostbyname(hostname)
   return "<h1>Hello123555, "+hostname+", "+ipAddr+"</h1>"

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
