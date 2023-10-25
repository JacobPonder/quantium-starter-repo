# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import pandas
from dash import Dash, html, dcc, Input, Output, callback
from plotly.express import line

COLORS = {
    "primary": "#F44537",
    "secondary": "#000000",
    "font": "#FFFFFF"
}

data = pandas.read_csv('data/Pink_sales_data.csv')
data = data.sort_values(by="Date")
app = Dash(__name__)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
def makechart(data):
    chart = line(data, x="Date", y="Sales", title="Pink Morsel Sales")
    chart.update_layout(
        plot_bgcolor=COLORS["primary"],
        paper_bgcolor=COLORS["secondary"],
        font_color=COLORS["font"]
    )
    return chart


visual = dcc.Graph(
    id='line_graph',
    figure=makechart(data)
)
radio = dcc.RadioItems(
    ['north', 'east', 'south', 'west', 'All'],
    'All',
    id='region',
    inline=True
)
region_picker_wrapper = html.Div(
    [
        radio
    ],
    style={
        "font-size": "150%"
    }
)
# header
header = html.H1(
    "Pink Morsel Sales",
    id="Header",
    style={"background-color": COLORS["secondary"],
           "color": COLORS["font"],
           "border-radius": "20px"}
)


@callback(
    Output('line_graph', 'figure'),
    Input('region', 'value'))
def update_graph(region):
    if region == "All":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]
    chart = makechart(trimmed_data)
    return chart


# layout
app.layout = html.Div(
    [header,
     radio,
     visual],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
)

if __name__ == '__main__':
    app.run()
