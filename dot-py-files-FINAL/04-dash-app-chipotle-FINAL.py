# Dash app for Chipotle
# 0. import modules
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# 1. instantiate dash app
app = Dash(external_stylesheets=[dbc.themes.COSMO])

# 2. load the chipotle csv into a df
chip_df = pd.read_csv("./csv/chipotle-updated.csv")
print(chip_df.shape)
print(chip_df.head())

# 3. group the items by name (there are 50 unique item names)
#.   and get the price (sales) sum total for each group
items_by_rev_df = chip_df.groupby("item_name")[["item_price_num"]].sum()
print(items_by_rev_df.shape, type(items_by_rev_df))
print(items_by_rev_df)

# 4. sort items_by_rev_df by price in desc order, then get the top 5
top_5_items_by_rev_df = items_by_rev_df.sort_values(by="item_price_num", ascending=False)[:5]
print(top_5_items_by_rev_df.shape, type(top_5_items_by_rev_df))
print(top_5_items_by_rev_df)
# item_names from index
top_5_item_names = top_5_items_by_rev_df.index

# 5. make a pie chart for the top 5 items by sales revenue
pie_chart = px.pie(
    top_5_items_by_rev_df,
    values="item_price_num",
    # the index of the df provides pie slice names--the names are
    # NOT in a column.. this df has just ONE col "item_price_num")
    names=top_5_item_names,
    # legend=False
)

# 6. make bar charts (v and h) for the top 5 items by rev
bar_chart = px.bar(
    top_5_items_by_rev_df,
    x=top_5_item_names,
    y="item_price_num"
)

# 7. make horizontal bar charts for the top 5 items by rev
barh_chart = px.bar(
    top_5_items_by_rev_df,
    y=top_5_item_names,
    x="item_price_num",
    orientation="h"
)

# 8. make scatter plot for the top 5 items by rev
scatter_plot = px.scatter(
    top_5_items_by_rev_df,
    x=top_5_item_names,
    y="item_price_num",
)

# 9. make bootstrap layout as container of 2 rows of 2 cols each
app.layout = dbc.Container([
    
    dbc.Row([
        dbc.Col(dcc.Graph(figure=pie_chart), xl=6),
        dbc.Col(dcc.Graph(figure=bar_chart), xl=6),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=barh_chart), xl=6),
        dbc.Col(dcc.Graph(figure=scatter_plot), xl=6),
    ]),

])

# 10. run the app
app.run(debug=True)

# 11. run this terminal command:
# python 04-dash-app-chipotle.py