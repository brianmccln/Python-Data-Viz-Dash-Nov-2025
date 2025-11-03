# Dash app Stock Prices

# 0. import modules (dcc = dash core components, e.g. Graphs)
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
# plotly is like the matplotlib of a dash app

# 1. instatiate dash app
app = Dash()

# 2. load stock prices csv into pandas df
csv_path = "./csv/stock-prices.csv"
stocks_df = pd.read_csv(csv_path)

# 3. get the top 5 stocks by volume
top_5_stocks_df = stocks_df.sort_values(by="Volume", ascending=False)[:5]
print("\nTop 5 Stocks by Volume")
print(top_5_stocks_df.shape) # (5, 8)
print(top_5_stocks_df)

# 4. define a Plotly (px) pie chart for the top 5 stocks
stocks_pie_chart = px.pie(
    top_5_stocks_df,
    # specifiy col of df w values for setting slice size
    values="Volume",
    # specify names to server as labels for pie slices
    names="Company",
    title="Pie Chart: Top 5 Stocks by Volume"
)

# 5. define a bar chart version of same data as pie chart
# by default bars are vertical, but they can be horizontal
stocks_bar_chart = px.bar(
    top_5_stocks_df,
    # specifiy x axis values
    x="Company",
    # specify y axis values
    y="Volume",
    orientation="v", # "v" for vertical is default
    title="Bar Chart: Top 5 Stocks by Volume"
)

# 6. define a horiz bar chart of same data as reg bar chart, but with orientation set to "h" reversed
stocks_barh_chart = px.bar(
    top_5_stocks_df,
    # specifiy x axis values
    x="Volume",
    # specify y axis values
    y="Company",
    orientation="h", # flips bars to run horizontally
    title="Horiz Bar Chart: Top 5 Stocks by Volume"
)

# 7. define a scatter plot
stocks_scatter_plot = px.scatter(
    top_5_stocks_df,
    x="Volume",
    y="Close", # Values for x and y must BOTH be numeric
    title="Scatter Plot: Closing Price by Volume"
)

# 8. output the charts to the Dash-Plotly app in the browser
# charts go inside dcc Graph, which goes inside html Div box
# which goes onto an html (web) page viewable in the browser
# multiple items (text and charts) go into the div as a list
app.layout = html.Div([
    html.H1("Dash-Plotly Visualization"),
    html.P("by Brian McClain"),
    dcc.Graph(figure=stocks_pie_chart),
    dcc.Graph(figure=stocks_bar_chart),
    dcc.Graph(figure=stocks_barh_chart),
    dcc.Graph(figure=stocks_scatter_plot),
])

# 9. run the app (quit any running app first)
app.run(debug=True)

# 10. run this terminal command:
# python 03-dash-app-stocks.py