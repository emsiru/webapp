# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    # primary graph background color
    #plot_bgcolor = colors['background'],
    # secondary graph background color
    #paper_bgcolor = colors['background'],
    font_color = colors['text'])

app.layout = html.Div(children=[
    html.H1(children='Hello Dash',
        style = {'textAlign': 'center',
            'color': colors['text']}),

    html.Div(children="Dash: A web application framework for your data.",
        style = {'textAlign': 'center',
        'color': colors['text']}),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)