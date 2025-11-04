# Dash app Stock Prices

# 0. import modules (dcc = dash core components, e.g. Graphs)
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
# plotly is like the matplotlib of a dash app BUT it's JS-based

# 1. instatiate dash app
app = Dash(__name__)

# 2. load stock prices csv into pandas df
stocks_df = pd.read_csv('./csv/stock-prices.csv')

# 3. get the top 5 stocks by volume
top_5_stocks_by_vol_df = stocks_df.sort_values(by="Volume",ascending=False)[:5]
print("\nTop 5 Stocks by Volume")
print(top_5_stocks_by_vol_df.shape) # (5, 8)
print(top_5_stocks_by_vol_df)

# 3B. output a simple message to browser, just to get started:
# app.layout = html.H1("Hello World from Dash App in the Broswer")

# 4. define a Plotly (px) pie chart for the top 5 stocks
pie_chart = px.pie(
    top_5_stocks_by_vol_df,
    values="Volume", # specifiy col of df w values for setting slice size
    names="Company", # specify names to serve as labels for pie slices
    title="Pie: Top 5 Stocks by Volume"
)
    
# 5. define a bar chart version of same data as pie chart
# by default bars are vertical, but they can be horizontal
bar_chart = px.bar(
    top_5_stocks_by_vol_df,
    # specifiy x axis values
    x="Company",
    # specify y axis values
    y="Volume",
    # "v" for vertical is default
    orientation="v",
    title="Bar: Top 5 Stocks by Volume"
)

# 6. define a horiz bar chart of same data as reg bar chart, but with orientation set to "h" reversed
barh_chart = px.bar(
    top_5_stocks_by_vol_df,
    # specifiy x axis values
    x="Volume",
    # specify y axis values
    y="Company",
    # "v" for vertical is default
    orientation="h", # flips bars to run horizontally
    title="Horiz Bar: Top 5 Stocks by Volume"
)

# 7. define a scatter plot
scatter_plot = px.scatter(
    top_5_stocks_by_vol_df,
    # Values for x and y must BOTH be numeric
    x="Volume",
    y="Close",
    title="Scatter: Closing Price by Volume"
)

# 8. make the app layout: output the charts to the Dash-Plotly app in the browser
# charts go inside dcc Graph, which goes inside html Div box
# which goes onto an html (web) page viewable in the browser
# multiple items (text and charts) go into the div as a list
app.layout = html.Div([
    html.H1("Dash-Plotly Stock Prices"),
    html.P("by Brian McClain"),
    dcc.Graph(figure=pie_chart),
    dcc.Graph(figure=bar_chart),
    dcc.Graph(figure=barh_chart),
    dcc.Graph(figure=scatter_plot),
])

# 9. run the app (quit any running app first)
if __name__ == '__main__':
    app.run(debug=True)

# 10. run this terminal command:
# python 03-dash-app-stocks.py

