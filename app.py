# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import pandas
from dash import Dash, html, dcc
from plotly.express import line

data = pandas.read_csv('data/Pink_sales_data.csv')
data = data.sort_values(by="Date")
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


chart = line(data, x="Date", y="Sales", title="Pink Morsel Sales")
visual = dcc.Graph(
    id='line_graph',
    figure=chart
)

#header
header = html.H1("Pink Morsel Sales",id="Header")
#layout
app.layout = html.Div([header,visual])
if __name__ == '__main__':
    app.run()
