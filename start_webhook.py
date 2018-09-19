# start_webhook.py
#!/usr/bin/env python
# coding=utf-8

from wsgiref.simple_server import make_server
from webhook import application

httpd = make_server('', 10777, application)
print('Serving HTTP on port 10777...')
httpd.serve_forever()
