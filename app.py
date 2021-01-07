"""main app for routing file for Twitoff"""

from os import getenv
from models import DB, User, MIGRATE
#from .username import 
import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.LUX, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags = [
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]


def create_app():
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
    app.config.suppress_callback_exceptions = True # see https://dash.plot.ly/urls
    app.title = 'Spotify Song Prediction' # appears in browser title bar
    DB.init_app(app)
    MIGRATE.init_app(app, DB)

        
    # URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
    @app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':
            return index.layout
        elif pathname == '/about':
            return about.layout
        elif pathname == '/user':
            return user.layout
        elif pathname == '/reset':
            def reset():
                DB.drop_all()
                DB.create_all()
                return index.layout
        else:
            return dcc.Markdown('## Go back to predict another song!')

    return app
