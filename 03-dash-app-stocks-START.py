# Dash app Stock Prices

# 0. import modules (dcc = dash core components, e.g. Graphs)

# plotly is like the matplotlib of a dash app

# 1. instatiate dash app


# 2. load stock prices csv into pandas df


# 3. get the top 5 stocks by volume

print("\nTop 5 Stocks by Volume")
# (5, 8)

# 4. define a Plotly (px) pie chart for the top 5 stocks

    # specifiy col of df w values for setting slice size

    # specify names to server as labels for pie slices

    # "Pie Chart: Top 5 Stocks by Volume"


# 5. define a bar chart version of same data as pie chart
# by default bars are vertical, but they can be horizontal

    # specifiy x axis values

    # specify y axis values

    # "v" for vertical is default
    # "Bar Chart: Top 5 Stocks by Volume"


# 6. define a horiz bar chart of same data as reg bar chart, but with orientation set to "h" reversed

    # specifiy x axis values

    # specify y axis values

    # flips bars to run horizontally
    # "Horiz Bar Chart: Top 5 Stocks by Volume"


# 7. define a scatter plot

    # Values for x and y must BOTH be numeric
    # "Scatter Plot: Closing Price by Volume"


# 8. output the charts to the Dash-Plotly app in the browser
# charts go inside dcc Graph, which goes inside html Div box
# which goes onto an html (web) page viewable in the browser
# multiple items (text and charts) go into the div as a list

# "Dash-Plotly Visualization"

# 9. run the app (quit any running app first)


# 10. run this terminal command:
# python 03-dash-app-stocks.py

