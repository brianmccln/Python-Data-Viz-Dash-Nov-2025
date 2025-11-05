# Dash app for Chipotle
# 0. import modules
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as boot
import pandas as pd

# 1. instantiate dash app
app = Dash(__name__, external_stylesheets=[boot.themes.COSMO])
# Available themes: CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR

# 2. load the chipotle csv into a df
chip_df = pd.read_csv("./csv/chipotle-changed.csv")
print(chip_df.shape)
print(chip_df.head())

# 2B. test the layout just to make sure app runs in browser:
# app.layout = html.H1("Hola from Chipotle Dash App!")

# 3. group the items by name (there are 50 unique item names)
#.   and get the price (sales) sum total for each group
item_by_tot_sales_df = chip_df.groupby("item_name")[["price_num"]].sum()
# print(item_by_tot_sales_df.shape)
# print(item_by_tot_sales_df)

# 4. get the top 5 sellers by total sales value
top_5_items_by_sales_rev_df = item_by_tot_sales_df.sort_values(by="price_num",ascending=False)[:5]
print(top_5_items_by_sales_rev_df.shape)
print(top_5_items_by_sales_rev_df)

# 5. make a pie chart for the top 5 items by sales revenue
# the index of the df provides pie slice names--the names are
# NOT in a column.. this df has just ONE col "item_price_num")
pie_chart = px.pie(
    top_5_items_by_sales_rev_df,
    names = top_5_items_by_sales_rev_df.index,
    values = "price_num",
)

# 6. make bar charts (v and h) for the top 5 items by rev
bar_chart = px.bar(
    top_5_items_by_sales_rev_df,
    x = top_5_items_by_sales_rev_df.index,
    y = "price_num"
)

# 7. make horizontal bar charts for the top 5 items by rev
barh_chart = px.bar(
    top_5_items_by_sales_rev_df,
    x = "price_num",
    y = top_5_items_by_sales_rev_df.index,
)

# 8. make scatter plot for the top 5 items by rev
scatter_plot = px.scatter(
    top_5_items_by_sales_rev_df,
    x = "price_num",
    y = top_5_items_by_sales_rev_df.index,
)

# 9. make bootstrap layout as container of 2 rows of 2 cols each
app.layout = boot.Container([
    
    boot.Row([
        boot.Col(html.H1("Dash App with Bootstrap Layout"))
    ]),
    
    boot.Row([
        boot.Col(dcc.Graph(figure=pie_chart), lg=7),
        boot.Col(dcc.Graph(figure=bar_chart), lg=5),
    ]),
    
    boot.Row([
        boot.Col(dcc.Graph(figure=barh_chart), xl=7),
        boot.Col(dcc.Graph(figure=scatter_plot), xl=5),
    ]),
    
])


# 10. run the app
if __name__ == "__main__":
    app.run(debug=True)

# 11. run this terminal command:
# python 04-dash-app-chipotle.py