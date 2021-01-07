# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Imports from this application
from app import create_app, server
from pages import index, predictions, user, about

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Spotify Song Prediction',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('About', href='/about', className='nav-link')), 
        #dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
    ],
    sticky='top',
    color='primary', 
    light=False, 
    dark=True
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                   html.Span('Lambda School Data Science Project', className='mr-2'), 
                   html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/Build-Week-Spotify-Song-Suggestion'), 
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    cdd.Store(id='session', storage_type='session')
    dcc.Location(id='url', refresh=False), 
    html.Table([
        html.Thead([
            html.Tr(html.Th('Click to store in:', colSpan="1")),
            html.Tr([
                html.Th(html.Button('sessionStorage', id='session-button'))
            ]),
            html.Tr([
                html.Th('Session clicks')
            ])
        ]),
        html.Tbody([
            html.Tr([
                html.Td(0, id='session-clicks')
            ])
        ])
    ])
])
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])


