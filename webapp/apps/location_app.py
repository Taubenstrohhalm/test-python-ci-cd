import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from app import app

from model.building import location

layout = html.Div(children=[
    html.H1(children='Choose Location'),

    html.Div(children='''
        Please enter your post code.
    '''),
    dcc.Input(id="input", type="text", placeholder="Enter post code", value = ''),
    html.Button(children = 'Submit', id="submit_button", n_clicks=0),
    html.Div(id='location_output',children='')
])

@app.callback(
    Output('location_output','children'),
    Input('submit_button','n_clicks'),
    State('input','value')
)
def show_latlong(n_clicks, value):
    if n_clicks == 0:
        return ''
    loc = location.conv_zip_to_location(value)
    if loc == None:
        return f'Sorry we could not set up a building for that location.'
    city = loc['city']
    return f'Your building will be placed in: {city}.'

if __name__ == '__main__':
    app.run_server(debug=True)