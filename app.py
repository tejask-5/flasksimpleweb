import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
   hostname=socket.gethostname()
   ipAddr=socket.gethostbyname(hostname)
   return "<h1>Hello, welcome to the demo session and get to know more about FortiDevSEc 30th Nov Good Day!" +hostname+", "+ipAddr+"</h1>"

@app.route('/8d7ed8ec-203c-4677-adda-a5bcde82b1c4.html')
def uuidchecking():
   return ""

@app.route('/forti-uuid.html')
def uuidDetailCheck():
   return "<forti-uuid hidden>8d7ed8ec-203c-4677-adda-a5bcde82b1c4</forti-uuid>"

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8001)
