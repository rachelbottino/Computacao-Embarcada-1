#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost


ref[] http://stackoverflow.com/questions/8928730/processing-http-get-input-parameter-on-server-side-in-python
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
from urllib.parse import urlparse, parse_qs

# s :
#  -1 : status
#   0 : clear
#   1 : set
def updateLed(s):
  with open('LED.json', 'r+') as f:
    LED = json.load(f)
    if(s == 0) :
      LED['LED'] = 0
    elif(s == 1) :
      LED['LED'] = 1 
    f.seek(0)
    f.truncate()
    json.dump(LED, f)   
    f.close()
    return(LED['LED'])    

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        # Send response status code
        self.send_response(200)
        print("GET")

        # Send headers
        #self.send_header('OLA VOCE ','RAFA')
        self.end_headers()
        # Send message back to client
        message = "Erro no comando: /?led=status ou /?led=set ou /?led=clear " 

        # parsing GET command
        query_components = parse_qs(urlparse(self.path).query)
        if(query_components) :
          status = query_components["led"] 
          if status[0] == "status":
            led = updateLed(-1)
            if led == 1 :
              message = "Turn Led ON ! "
            else :
              message = "Turn Led OFF ! "
          elif status[0] == "set":
            led = updateLed(1)
            message = "Ok : " + format(led)
          elif status[0] == "clear":
            led = updateLed(0)
            message = "Ok : " + format(led)
        else :
          message = "Erro no comando: /?led=status ou /?led=set ou /?led=clear "  
        
        # Write content as utf-8 data
        print(message)
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self.send_response(200)  # OK
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd...")
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
