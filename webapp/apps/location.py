import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from app import app

layout = html.Div(children=[
    html.H1(children='Choose Location'),

    html.Div(children='''
        Please enter your zip code.
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
    return f'Your building is placed at: {value}.'

if __name__ == '__main__':
    app.run_server(debug=True)