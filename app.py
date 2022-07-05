import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
   hostname=socket.gethostname()
   ipAddr=socket.gethostbyname(hostname)
   return "<h1>Hello Jew, "+hostname+", "+ipAddr+"</h1>"

@app.route('/e3540078-1fed-4f26-9d80-2060b71c00d0.html')
def uuidchecking():
   return ""

@app.route('/forti-uuid.html')
def uuidDetailCheck():
   return "<forti-uuid hidden>e3540078-1fed-4f26-9d80-2060b71c00d0</forti-uuid>"

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=8000)
