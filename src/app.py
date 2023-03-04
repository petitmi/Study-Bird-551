import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import Dash, dcc, html
import plotly.express as px
import numpy as np
import altair as alt
from vega_datasets import data
import pandas as pd


# create a dash
app = dash.Dash(external_stylesheets=[dbc.themes.QUARTZ])

# location settings for sidebar
SIDEBAR_STYLE = {
    # "position": "fixed",
    "top": '10px',
    "flex":'0 1 10%',
    "left": 0,
    "bottom": 0,
    "width": "10px",
    "padding": "2px 1px"}

# location settings for sidebar
CONTENT_STYLE = {
    "margin-left": "2rem",
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
app.layout = dbc.Container([
    dbc.Row([html.Div([   
                html.H3("BillBoard Top100 Hot 🔥🔥Songs🔥🔥 Analysis", className="display-4"),
                html.H5("Study Bird 551"),
                html.Hr()])]),
    dbc.Row([
    # sidebar includes 2 labels and 3 tabs
    dbc.Col([nav], className="lead",style=SIDEBAR_STYLE),
    
    # content page includes 1 time slider at the top and 3 graphs below
    dbc.Col([dcc.RangeSlider(id='year-slider',min=2012,max=2022,value=[2012, 2022],step=1,marks=mark),
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
    start_year=int(year[0])
    end_year=int(year[1])
    
    if page_title=="Artist Analysis":
        chart=None
        chart1=None
        chart2=None
        pass
    #     chart = alt.Chart(cars).mark_circle(size=60).encode(
    #         x='Horsepower',
    #         y='Miles_per_Gallon',
    #         color='Origin',
    #         tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']).interactive()
    #     chart1 = alt.Chart(cars).mark_circle(size=60).encode(
    #         x='Horsepower',
    #         y='Miles_per_Gallon',
    #         color='Origin',
    #         tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']).interactive()
    #     chart2 = alt.Chart(cars).mark_circle(size=60).encode(
    #         x='Horsepower',
    #         y='Miles_per_Gallon',
    #         color='Origin',
    #         tooltip=['Name', 'Horsepower', 'Miles_per_Gallon']).interactive()
        
    elif page_title=="Lyrics Analysis":
        df = pd.read_excel('../data/processed/lyrics_dataset.xlsx')
        df = df.loc[(start_year <= df['Year']) & (df['Year'] <= end_year)]
        sentiment_counts = df['Sentiment'].value_counts()
        source = pd.DataFrame({"category": ['Positive','Negative','Neutral'], "sentiment_counts": [sentiment_counts[0], sentiment_counts[1], sentiment_counts[2]]})

        chart = alt.Chart(df).mark_bar().encode(
            x='Year:N',
            y=alt.Y('Word Count:Q', axis=alt.Axis(title='Lyrics Length')),
            column='Rank:O',
            color='Year:N',
            tooltip=['Year','Rank','Artist']).properties(
            title="Lyrics Length and Rank by Year").interactive()
        
        chart1 = alt.Chart(source).mark_arc().encode(
            theta=alt.Theta(field="sentiment_counts", type="quantitative"),
            color=alt.Color(field="category", type="nominal"),
            tooltip=["sentiment_counts","category"]).properties(
            title="Sentiment Counts in {}".format(year))
        
        chart2 = alt.Chart(df).mark_line(interpolate='basis').encode(
            x=alt.X('Rank', scale=alt.Scale(domain=[0, 100])),
            y=alt.Y('Frequency_love:Q', axis=alt.Axis(title='Frequency')),
            color='Year:N',
            tooltip=['Year','Frequency_love','Artist']).properties(
            title="Frequency of 'love' in {}".format(year)).interactive()
        
    elif page_title=="Audio Analysis":
        hits = pd.read_csv('../data/processed/audio_data_processed.csv')
        hits.drop("Unnamed: 0", axis=1, inplace=True)
        hits['rank_bin'] = pd.cut(hits['Rank'],bins=10,labels=['1-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100'])

        hits_c1 = hits[(start_year <= hits['Year']) & (hits['Year'] <= end_year)]
        hits_c1_bin = hits_c1.groupby('rank_bin').mean().reset_index()
        hits_c1_bin = hits_c1_bin[['rank_bin','energy','popularity','speechiness','liveness','valence']].set_index(['rank_bin','popularity']).stack().reset_index(name='value').rename(columns={'level_2':'features'})

        chart = alt.Chart(hits_c1_bin).mark_bar().encode(
            x='features:N',
            y=alt.Y('value',scale=alt.Scale(zero=False)),
            column='rank_bin:N',
            color='features:N',
            opacity='popularity:Q'
        )
        chart1 = alt.Chart(hits_c1_bin).mark_bar().encode(
            x='features:N',
            y=alt.Y('value',scale=alt.Scale(zero=False)),
            column='rank_bin:N',
            color='features:N',
            opacity='popularity:Q'
        )
        chart2 = alt.Chart(hits_c1_bin).mark_bar().encode(
            x='features:N',
            y=alt.Y('value',scale=alt.Scale(zero=False)),
            column='rank_bin:N',
            color='features:N',
            opacity='popularity:Q'
        )
        # chart1 = alt.Chart(cars).mark_line().encode(
        #     x='Year',
        #     y='mean(Miles_per_Gallon)',
        #     color='Origin')
        # chart2 = alt.Chart(cars).mark_line().encode(
        #     x='Year',
        #     y='mean(Miles_per_Gallon)',
        #     color='Origin')
        

    return html.Div(
        [html.H2(page_title),
        html.Div("This is data visualization content for {} in {}:".format(page_title, year))]
    ),chart.to_html(),chart1.to_html(),chart2.to_html()

if __name__ == "__main__":
    app.run_server(debug=True)
