import sys
import os
from werkzeug.middleware.proxy_fix import ProxyFix
import create_app
print(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))


if __name__ == '__main__':
    #from wsgiref.simple_server import make_server
    #make_server('0.0.0.0',8000,application).serve_forever()
    #application.wsgi_app = ProxyFix(application.wsgi_app)
    application = create_app()
    application.run()
