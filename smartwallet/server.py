from waitress import serve
from django import *
    
from smartwallet.wsgi import application
    
if __name__ == '__main__':
    serve(application, port='8000')