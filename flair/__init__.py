from flask import Flask 
from flair.view import view




def create_app():

    app = Flask("__name__" )

    app.register_blueprint(view, url_prefix ='/view')

    return app
    

    