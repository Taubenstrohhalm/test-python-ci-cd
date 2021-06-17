import dash
import dash_html_components as html
import dash_core_components as dcc

#from app import app


layout = html.Div(children=[
    html.H1(children='Choose Location'),

    html.Div(children='''
        The location is needed to find information about the climate in your region.
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)