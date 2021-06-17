import dash
import dash_html_components as html
import dash_core_components as dcc

from app import app


layout = html.Div(children=[
    html.H1(children='Welcome to REhome'),

    html.Div(children='''
        An awesome webapp that lets you explore the carbondioxide emissions of buildings.
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)