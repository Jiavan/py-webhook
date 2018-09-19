# webhook.py
import os
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # exec shell
    os.system('./opshell.sh')

    print('Finish!')
    return [b'Execute webhook success!']
