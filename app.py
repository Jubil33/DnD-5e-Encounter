#!/usr/bin/env python3
import os

from flask import Flask
#from Class.Encounter import Encounter
#from Class.generateEncounter import generateEncounter

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    #Encounter blueprint    
    #from Class.generateEncounter import encounter
    #from Class.Encounter import generateEncounter
    from .Encounter import EncounterController
    app.register_blueprint(EncounterController.bp)

    #monster blueprint

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World! poop'

    return app
    #Error: Failed to find Flask application or factory in module 'DnD-5e-Encounter.app'. Use 'DnD-5e-Encounter.app:name' to specify one.