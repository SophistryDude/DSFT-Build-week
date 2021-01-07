# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ##### Find the song ID of a song you enjoy listening to and paste it into the prediction generator to disvover new music.
            In order to find the song ID, open spotify and search for the song you would like to use. Click on "..." next to the song and navigate to the share tab. Copy the song link and paste it into a notes page.
            The result should look something like,
            https://open.spotify.com/track/5ervA7lbl13K2ekOUFmgKe
            The numbers and letters following /track/ are the song ID. Input this into the prediction generator to discover new music.

            """
        ),
    ],
    md=6,
)

input_types = ['text']
column2 = dbc.Col(
    [
        html.H2('Your next favorite song', className='mb-5'),
        html.Label('Input your track ID:  '),
        dcc.Input(
            placeholder = 'Track ID',
            type = 'text',
            value = ''
        )
        # html.Div([
        #     dcc.input(
        #         id='my_{}'.format(x),
        #         type=x,
        #         placeholder="insert{}".format(x),
        #     ) for x in input_types

    ]
)

# ["Input: ", dcc.Input(id='my-input', value='initial value', type='text')]

layout = dbc.Row([column1, column2])


# # 1:07:29 in the unit 2 build 3 dash inputs and outputs video
# @app.callback(
#     Output(''),
#     Input(component_id='my-input', component_property='value')
# )