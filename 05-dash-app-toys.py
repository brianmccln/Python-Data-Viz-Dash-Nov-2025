# Dashboard: Interactive Toy Sales Explorer

# This script starts a web server and serves an *interactive* dashboard built with **Dash**. If you can run this file and see a page in your browser, you're officially building dashboards.

# - This app wraps Input and Output in a function that is called in response to user interaction
# - Plotly for the interactive charts (plotly.express)
# - Dash for the web UI + reactivity
# - The graphs update whenever the user changes the filters (region, product, date range, line mode)
# dash + boot is Dash core + Bootstrap components for clean layout

# About the dropdown menus for filtering
# ------------------------
# - The Region/Product dropdowns use `multi=True`, which allow multiple choices to be made from the same menu 
# - By default all regions and products are selected
# - The current selection shows up as "chips" (little blue tags). 
# - Click the **X** on a chip to remove it
# - Click the empty space in the dropdown to re-open it so you can add items back.

# 0, Import packages ----------
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as boot
import sqlite3

# 1. Instantiate the Dash App and set the Bootstrap theme
app = Dash(__name__, external_stylesheets=[boot.themes.ZEPHYR])
# Available themes: CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR

# 2. Load the toy-sales.csv dataset
# the first col, 'date' has dates which need to be parsed OR else
# they will come in as just strings, which we don't want
# date,region,product,revenue,units
# 2023-01-01,North,Widget,112.66,22
toys_from_csv_df = pd.read_csv("./csv/toy-sales.csv", parse_dates=["date"])
print("toys_from_csv_df:", toys_from_csv_df.shape) # (636, 5)
print(toys_from_csv_df.head())

# load the toys data into a df again BUT this time from the SQL DB:
# connect to the toys db, saving result as a connection object
conn_toys = sqlite3.connect("./toys.db")
# load all records from the toys table
toys_df = pd.read_sql("SELECT * from toys",conn_toys)
# check if we got our data from the SQL DB:
print("toys_df from sql:", toys_df.shape) # (636, 5)
print(toys_df.head())
# close the db connection
conn_toys.close()

# 3. Make the groupby df for the revenue by date, called rev_by_date_df;
#   for use by line chart:
rev_by_date_df = toys_df.groupby("date", as_index=False)["revenue"].sum()
print("rev_by_date_df:", rev_by_date_df.shape) # (53, 2)
print(rev_by_date_df.tail())

# 4. Make a line Chart
# y-ticks are the revenue numbers; format 1500 as $1,500
line_chart = px.line(
    rev_by_date_df,
    x="date",
    y="revenue",
    title="Weekly Toy Sales Revenue (2023)",
    # puts dots on the points connected by the line    
    markers=True,  
)

# 5. Make a groupby df called units_by_prod_df, for use by bar chart:
avg_units_by_prod_df = toys_df.groupby("product", as_index=False)["units"].mean().sort_values(by="units", ascending=False)

print("avg_units_by_prod_df:", avg_units_by_prod_df.shape) # (3, 2)
print(avg_units_by_prod_df)

# 6. Make the bar chart from the units_by_prod_df:
bar_chart = px.bar(
    avg_units_by_prod_df,
    x="product",
    y="units",
    title="Avg Units Sold by Product"
)

# 7. Heat Map: make a df for the heat map


# 8. Pivot the heatmap df so that each of the three products has its own column and each of the four regions has its own row
# and revenue is the value for each cell

# 9. Plot the heatmap from the heatmap_pivoted_df

# 10. Have the 3 charts update any time changes are made to the UI controls:



# UI CONTROLS
# 11. Make the region chooser dropdown menu component; start my getting the unique requions into a list
# menu option example dict: {"label":"East", "value":"East"}
# unique_regions = ["East","West","North","South"]
# better to get the unique regions directly from the df:

# print('unique_regions:',unique_regions)

# 12. Using list comprehension, populate region_menu_options list w 4 dictionaries:


# the dropdown menu component will be passed this list of dictionaries
# print('region_menu_options:',region_menu_options)
# default_regions = uniq

# 13. Make a new empty dictionary to hold the menu options

# menu option example dict: {"label":"Doodad", "value":"Doodad"}
# unique_proudcts = ["Doodad","Gadget","Widget"]

# 14. get the unique products directly from the df:


# print('unique_products:',unique_products)

# 15. using list comprehension, populate product_menu_options list w 4 dictionaries:

# the dropdown menu component will be passed this list of dictionaries
# print('product_menu_options:',product_menu_options)

# UI CONTROL HOLDER
# controls go inside a Bootstrap Card component holder
# each UI control gets a Bootstrap Label to identify it
# the control itself -- the dropdown menu -- is a dcc component
# contols will consist of a Region and Product dropdown menu

# 16. define the controls as a 

# 17. Assign label for the Region dropdown menu

# 18. Define the Region dropdown menu, which requires the following properties: 
#     id, options, value, multi, clearable and placeholder props

        # the dropdown menu choices

            # allows user to select more than one region
            # must have at least ONE region selected
            # prompts the user

# 19. Assign label for the Product dropdown menu

        
# 20. Define the Product dropdown menu, which requires the following properties: 
#     id, options, value, multi, clearable and placeholder props
        
        # the dropdown menu choices

            # allows user to select more than one region
            # must have at least ONE region selected
            # prompts the user


# 21. Assign label for the Line Chart (called Line Mode as it is interactive)

# 22. Define the Line Mode options as Radio Buttons (can only choose one)

            
# 23. Specify the options for the radio button set

        # radio buttons run horiz -- not stacked

# 24. Assign label to Date Range picker
      
        
# 24. Define the DatePickerRange with these properties:
# min_date_allowed, max_date_allowed, start_date, end_date, display_format

    # add drop shadow w rounded corners


# Layout App Dashboard with its 3 Charts

# 25. Define a layout for the app, starting with a Div as a test of a simpler layout: 
# app.layout = html.Div([
#     html.H1("Toys Sales Dashboard"),
#     html.P("by Brian McClain"),
#     dcc.Graph(figure=line_chart),
# ])
# once the Div test works, switch to bootstrap layout, which is more complex and nested
app.layout = boot.Container([
    
    boot.Row([ # 26. Define a Row and a Col inside of the Row
        boot.Col([ # 26B. Define a Col
            html.H1("Toys Sales Dashboard"),
            html.P("by Brian McClain"),
        ],
        # 27. Give a style to the Col className="bg-primary text-light p-4"
        className="bg-primary text-light p-4"
        ), # end Col
     ]), # end Row
                        
    boot.Row([ # 28. Make another row
        # 29. Make a col to hold toys.jpg image
        #     toys.jpg file goes inside assets/images folders
        boot.Col([
            html.Img(
                src="./assets/images/toys.jpg",
                # 29B.style the toy image
                style={
                    # set and constrain its width and height
                    # (no distortion, stays inside its Col box)
                    "height": "270px",
                    "width": "405px",
                    "maxWidth":"100%",
                    "maxHeight":"auto",
                    # center the image within its Col box:
                    "display": "block",
                    "margin": "0 auto",
                }
            ),
        ],
            # 29C. Style col containing toy pic; 
            # UI controls go under here in new row, same col
            style = {
                "border": "3px solid #cbcbcb88",
                "padding": "10px",
                "background-color": "#cbcbcb88",
                # "margin": "10px 20px 20px 0", 
                # T-R-B-L (clockwise from 12:00)
                # "height": "50vh",
            },
            md=4 # when browser is large, toggle to 4-8 split
            # where this col is 4 units wide and all other col(s)
            # must total the other 8 (of 12) units
        ),
        # 30. make another Col (same Row) to hold the graphs
        boot.Col([
            dcc.Graph(figure=line_chart,
                style={"height": "450px",}),
            dcc.Graph(figure=bar_chart,
                style={"height": "450px",}),
        ],
        md=8
        ),
    ],
    className="mt-2"
    )
    ],
    fluid=True,
) # close bootstrap container



# 31. define the app callback decorator function which has no name but just runs automatically whenever UI component
# such as Dropdown menu is changed

    # 32. specify the output, which are the update figrues; the output has an id which goes here and in the layout
    # what this says is: go to the layout and update the item, which has this id, and update the figureff

    # 33. instruct the function to get its inputs from the UI
    # component that has the following id and get its value
    # here we tell the func to get the value of the region menu


# 34. under the app callback decorator which handled Input Output
#   define a function that actually updates the menu and line chart
#   this function can be called whatever you want and it does NOT
#   get called in the code explicitly by you -- the decorate and this
#   func are connected cuz this is directly under the @app.callback
#   this func receives Input as its param and Output is its return value

    
    # 35. get all the rows that have a 'region' value in unique_regions
    # this is ALL rows, cuz EVERY region is in unique_regions
    # the return value is saved as mask by convention

     
    # 36. make a copy of the df for use in rebuilding line chart
    # df.loc[mask] select only those rows where the region is selected
    # filter out unselected regions
    
    # 37. update / redeclare the rev_by_date_df using only selected regions
 

    # 38. check which radio btn is selected and use that to make the line chart
    # if Aggregate btn is selected, make unified line

        
        # 39. update / redeclare the line chart using the updated rev_by_date_df df

        # puts dots on the points connected by the line      
        
    # 40. else check if the radio button choice is region

        # 41. update / redeclare the line chart using the updated rev_by_date_df df

        # puts dots on the points connected by the line      
        
    # 42. else the radio button choice must be product
    # mode is "product"

        # 43. update the line chart

       # puts dots on the points connected by the line      
        
    # 44. upldate the axes

    # 45. update / redeclare the units_by_prod_df using only selected regions

    # 46. update / redeclare the bar chart using the updated rev_by_date_df df

    # 47. redeclare the heatmap using the updated rev_by_date_df df

    # 48. update the heatmap

    # 49. return the updated line chart as specified in Output


#  50. run app inside if block:
if __name__ == "__main__":
    app.run(debug=True)

# means app can only be run here from the command line (terminal)
# so if this file is imported into some other file it won't work; this is a Flask server thing -- not Dash specific

# "__main__" and name are SAME but ONLY if the app is being executed HERE via COMMAND LINE

# parse_dates ensures the 'date' column becomes a real datetime64[ns] (important for filtering & plotting). Otherwise, date will come in as just a string, with no actual time value, so not sortable by date time

# Precompute dropdown options
# map unique regions/products to [{'label': 'North', 'value': 'North'}, ...].
# Dash dropdowns expect this structure.
# ---------- Precompute dropdown options ----------
# Loop way (easier to read at first)
# sorted(list) 

# List comprehension way (more concise)

# ---------- Create the Dash app ----------
# external_stylesheets loads a Bootstrap theme to avoid custom CSS on Day 1.


# ---------- Controls (left column) ----------
# We build a small *component tree* and wrap it in a Bootstrap Card for a tidy panel.
# In Dash, lists become "children" rendered top-to-bottom in the order you specify.
# Each interactive control gets a unique `id` so the @app.callback can read/write its value.

        # ---- Title inside the card

        # ---- REGION: label + multi-select dropdown
        # dbc.Label is just a visual label here (not auto-bound with `for=` like raw HTML).
            # Default selection: start with *all* regions selected.
            # This uses a list comprehension to pull out the "value" from each option dict.

        # ---- PRODUCT: label + multi-select dropdown (same idea as Region)

        # ---- DATE RANGE: pick a start and end date
        # We set the allowed range to the min/max in the CSV and default to "select everything".

        # ---- LINE MODE: radio buttons to choose how the line chart groups data
            # Each radio option has a user-facing label and a compact value we check in the callback.

        # ---- A thin divider line for visual separation

        # ---- A small helper note (UX tip) about how multi-select dropdowns behave
    # ---- Card-level props

# ---------- Page layout (WHAT renders where) ----------
# We compose the whole page as a *tree of components*.
# - dbc.Container is the outer wrapper
# - Inside it: a heading, a short paragraph, a Row with two Columns, and a footer.
# - The right column contains three Cards; each Card wraps one dcc.Graph.
#
# Notes:
# • In Dash, "children" is just a Python list rendered top-to-bottom.
# • dcc.Graph is a *placeholder* that will display whatever Plotly figure
#   the callback returns to the Graph's `figure` property.
# • We use Bootstrap’s grid: 12 columns per row. md=4 means 4/12 on medium+ screens;
#   on small screens columns stack vertically (mobile-friendly).

        # ---- Header row: title + blurb on the left, toy image on the right

        # ---- One Bootstrap row that holds two columns
                # LEFT COLUMN: the controls panel we built above
                # md=4 -> this column is 4/12 (one-third) width on medium+ screens
                # On small screens (phones), columns stack and this will be full width.

                # RIGHT COLUMN: three cards, each with one chart
                # md=8 -> this column is 8/12 (two-thirds) width on medium+ screens
                        # Card 1: Line chart

                        # Card 2: Bar chart

                        # Card 3: Heatmap

        # ---- A small footer line (semantic <footer>) with muted styling and vertical margin

    # Container props:
    # • fluid=True -> full-width container that adapts to the viewport (nice for dashboards).
    #   If you prefer a fixed max width (like a document page), set fluid=False (the default).


# ---------- The callback (the "reactive" engine) ----------
# The @app.callback decorator *wires up* UI → function → UI.
# • Each Output(...) targets a component's *property* (here: each Graph's "figure")
# • Each Input(...) listens to a component's *property* (dropdown values, dates, etc.)
# When ANY Input changes, Dash calls the function with the *current* values (in this order),
# and expects you to return one value per Output (in the same order as declared).

    # --- Outputs: we will RETURN three Plotly figures in this exact order ---

    # --- Inputs: Dash will PASS these into the function in this exact order ---

    # """
    # WHAT this function does (pure function mindset):
    #   1) Use the current UI selections to FILTER the DataFrame.
    #   2) Build three Plotly figures (line, bar, heatmap) from the filtered slice.
    #   3) Return the figures in the same order as the Outputs.

    # WHY do it this way?
    #   - Keeping all filtering *inside* the callback ensures graphs always match the UI.
    #   - Pandas boolean masks are fast, readable, and chain well.
    #   - The groupby/pivot steps mirror what you did in the notebook; here we return
    #     Plotly figures so the graphs are interactive (tooltips, zoom, legend toggles).
    # """

    # ----- 1) FILTER the DataFrame with a boolean mask -----
    # We create a True/False Series for each condition and combine them with & (AND).
    # Notes:
    # • .isin(list) tests membership (region in selected regions, etc.)
    # • Dates come in as strings; wrap with pd.to_datetime for robust comparison
    # • .loc[mask] keeps rows where mask is True

    # ----- 2) LINE: Revenue over time -----
    # We can aggregate in three ways based on the radio button ("mode"):
    #   - agg     -> one total line (sum across regions/products)
    #   - region  -> one line per region (color encodes region)
    #   - product -> one line per product (color encodes product)



    # Cosmetic: show currency-like ticks and give the chart some breathing room

    # ----- 3) BAR: Average units by product -----
    # For the current slice, compute the mean "units" for each product and order it.

    # ----- 4) HEATMAP: Revenue by Region × Product -----
    # Turn totals into a 2D table: rows=region, columns=product, values=revenue.
    # px.imshow expects a 2D array-like and will read the index/columns as tick labels.

    
    # ---- add logo to BAR chart ----

    # IMPORTANT: return values must align 1-to-1 with Outputs declared above.

    # (Optional teaching note / not included in Day 1 to keep it simple)
    # - If you want to guard against empty selections, you can return "no_update"
    #   or a placeholder figure. Example:
    #     if dff.empty:
    #         from dash import no_update
    #         return no_update, no_update, no_update
    
    


# ---------- Run the app (Dash 3.x) ----------
    # debug=True gives you hot-reload (server restarts when you edit this file)
    # and rich error messages in the browser.
