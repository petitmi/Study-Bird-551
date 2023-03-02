import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import Dash, dcc, html
import plotly.express as px
import numpy as np
import altair as alt
from vega_datasets import data

#举个例子用cars的数据
cars = data.cars()

# create a dash
app = dash.Dash(external_stylesheets=[dbc.themes.QUARTZ])

# location settings for sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem"}

# location settings for sidebar
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem"}

# create three tabs in the sidebar
nav_items = [
    dbc.NavItem(dbc.NavLink("Artist", id="page-1-link",href="artist")),
    dbc.NavItem(dbc.NavLink("Lyrics", id="page-2-link",href="lyrics")),
    dbc.NavItem(dbc.NavLink("Audio", id="page-3-link",href="audio")),]

# group three tabs together and list them virtically
nav = dbc.Nav(nav_items, vertical=True)

# create three page contents for three tabs
page_1 = html.Div("This is page for Artist")
page_2 = html.Div("This is page for Lyrics")
page_3 = html.Div("This is page for Audio")

years=[]
mark = {}
for i in range(2012,2023):
    years.append(str(i))
for year in years:
    mark[year] = {
        'label': year,
        'style': {'color': 'white'}}
    
# layout of the dash app
app.layout = dbc.Container([dbc.Row([
    # sidebar includes 2 labels and 3 tabs
    dbc.Col([html.Div([   
                html.H3("Study Bird 551", className="display-4"),
                html.Hr(),
                html.P("Selection Bar", className="lead")]),
             nav],style=SIDEBAR_STYLE),
    
    # content page includes 1 time slider at the top and 3 graphs below
    dbc.Col([
            dcc.RangeSlider(
                id='year-slider',
                min=2018,
                max=2022,
                value=[2018, 2019],
                step=1,
                marks=mark),
            html.Div(id="page-content",children=page_1),
            html.Iframe(id='chart1',style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            html.Iframe(id='chart2',style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            html.Iframe(id='chart3',style={'border-width': '0', 'width': '100%', 'height': '400px'})],style=CONTENT_STYLE),])],
    fluid=True,)

# 4 outputs (one page content and three charts) and 4 inputs (three tabs and one year slider)
@app.callback(
    [Output("page-content", "children"),
    Output("chart1", "srcDoc"),
    Output("chart2", "srcDoc"),
    Output("chart3", "srcDoc")],
    [Input("page-1-link", "n_clicks"), 
    Input("page-2-link", "n_clicks"), 
    Input("page-3-link", "n_clicks"), 
    Input("year-slider", "value")])

# render page content
def render_page_content(page_1_clicks, page_2_clicks, page_3_clicks, year):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "page-1-link" in changed_id:
        return generate_page_content("Artist Analysis", year)
    elif "page-2-link" in changed_id:
        return generate_page_content("Lyrics Analysis", year)
    elif "page-3-link" in changed_id:
        return generate_page_content("Audio Analysis", year)
    else:
        return generate_page_content("Artist Analysis", year)

# output page content
def generate_page_content(page_title, year):
    if page_title=="Lyrics Analysis":
        chart = alt.Chart(cars).mark_circle(size=60).encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin',
            tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']).interactive()
        chart1 = alt.Chart(cars).mark_circle(size=60).encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin',
            tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']).interactive()
        chart2 = alt.Chart(cars).mark_circle(size=60).encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin',
            tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']).interactive()
        
    elif page_title=="Artist Analysis":
        chart = alt.Chart(cars).mark_bar().encode(
            x='Horsepower',
            y='count()',
            color='Origin')
        chart1 = alt.Chart(cars).mark_bar().encode(
            x='Horsepower',
            y='count()',
            color='Origin')
        chart2 = alt.Chart(cars).mark_bar().encode(
            x='Horsepower',
            y='count()',
            color='Origin')
        
    elif page_title=="Audio Analysis":
        chart = alt.Chart(cars).mark_line().encode(
            x='Year',
            y='mean(Miles_per_Gallon)',
            color='Origin')
        chart1 = alt.Chart(cars).mark_line().encode(
            x='Year',
            y='mean(Miles_per_Gallon)',
            color='Origin')
        chart2 = alt.Chart(cars).mark_line().encode(
            x='Year',
            y='mean(Miles_per_Gallon)',
            color='Origin')
        

    return html.Div(
        [html.H2(page_title),
        html.Div("This is some data visualization content for {} in {}:".format(page_title, year))]
    ),chart.to_html(),chart1.to_html(),chart2.to_html()

if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)
