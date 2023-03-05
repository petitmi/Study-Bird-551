import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import Dash, dcc, html
import plotly.express as px
import numpy as np
import altair as alt
from vega_datasets import data
import pandas as pd
import base64
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
    dbc.NavItem(dbc.NavLink("Artist", id="page-artist",href="artist")),
    dbc.NavItem(dbc.NavLink("Lyrics", id="page-lyrics",href="lyrics")),
    dbc.NavItem(dbc.NavLink("Tracks", id="page-tracks",href="tracks"))]

# group three tabs together and list them virtically
nav = dbc.Nav(nav_items, vertical=True)


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
    dcc.Location(id='url', refresh=False),
    dbc.Row([html.Div([   
                html.H3("BillBoard Top100 Hot 🔥🔥Songs🔥🔥 Analysis", className="display-4"),
                html.H5("Study Bird 551"),
                html.Hr()])]),
    dbc.Row([
    # sidebar includes 2 labels and 3 tabs
    dbc.Col([nav],style=SIDEBAR_STYLE),
    
    # content page includes 1 time slider at the top and 3 graphs below
    dbc.Col([dcc.RangeSlider(id='year-slider',min=2012,max=2022,value=[2012, 2022],step=1,marks=mark),
            html.Div(id="page-content"),
            html.Iframe(id='chart1',style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            html.Div(id="describe1"),
            html.Iframe(id='chart2',style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            html.Div(id="describe2"),
            html.Iframe(id='chart3',style={'border-width': '0', 'width': '100%', 'height': '400px'}),
            html.Div(id="describe3")],style=CONTENT_STYLE),]),
    dbc.Row([html.Hr(),
            html.P("Data from BillBoard, Spotify, Musixmatch and Genius.")])],
    fluid=True,)

# 4 outputs (one page content and three charts) and 4 inputs (three tabs and one year slider)
@app.callback(
    [Output("page-content", "children"),
    Output("chart1", "srcDoc"),
    Output("describe1", "children"),
    Output("chart2", "srcDoc"),
    Output("describe2", "children"),
    Output("chart3", "srcDoc"),
    Output("describe3", "children")],
    [Input('url', 'pathname'),
    Input("year-slider", "value")])


# render page content
def render_page_content(pathname,year):
    if "artist" in pathname:
        return generate_page_content("Artist Analysis", year)
    elif "lyrics" in pathname:
        return generate_page_content("Lyrics Analysis", year)
    elif "tracks" in  pathname:
        return generate_page_content("Tracks Analysis", year)
    else:
        return generate_page_content("Artist Analysis", year)

# output page content
def generate_page_content(page_title, year):
    start_year=int(year[0])
    end_year=int(year[1])
    alt.renderers.set_embed_options(theme='dark')
    if page_title=="Artist Analysis":
        df = pd.read_csv('../data/processed/artist_process_data.csv',encoding="ISO-8859-1")
        df = df.loc[(start_year <= df['Year']) & (df['Year'] <= end_year)]
        df1 = df.drop_duplicates(subset=['Artist'])
        df1['year']=pd.DatetimeIndex(df1['first_year']).year
        df2=df1[df1['popularity']>60]
        df3=df.drop_duplicates(subset=['year_range'])
        def word_cloud(string,i):
            from wordcloud import WordCloud
            import os

            wordcloud_pic = f"../data/processed/wordcloud_{i}.png"
            wordcloud = WordCloud(
                background_color='white',
                collocations=False,                
                colormap='Set3_r',                
                max_words=1200,                 
                max_font_size=100,                 
                scale=1,                 
                random_state=1,                
                width=1200,
                height=200).generate_from_frequencies(string)
            wordcloud.to_file(f'{wordcloud_pic}')     
            return wordcloud_pic

        a = dict(zip(df1['Artist'], df1['count']))
        b = dict(zip(df1['Artist'], df1['popularity']))

        word_cloud(a,1)
        word_cloud(b,2)

        image_filename1 = '../data/processed/wordcloud_1.png'
        encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
        
        image_filename2 = '../data/processed/wordcloud_2.png'
        encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())
        
        def word_count(str):
            counts = dict()
            words = str.split()
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
            return counts

        c=[]
        for i in df1['genres']:
            res=i.strip('][').split(', ')
            for j in res:
                res1=j.replace("'","").replace(" ","-")
                c.append(res1)
        d=' '.join(c)
        my_dict=word_count(d)
        df4=pd.DataFrame(list(my_dict.items()),columns=['genres','Artist number'])
    
        chart=alt.Chart(df2,title='Artist\'s Song Quality vs Popularity').mark_point(filled=True,size=100).encode(
                                y=alt.Y('popularity:Q',scale=alt.Scale(zero=False),title='Artist popularity'),
                                x=alt.X('count:Q',scale=alt.Scale(zero=False),title='Number of times on top'),
                                size=alt.Size('size',legend=None),
                                color=alt.Color('size',legend=None),
                                tooltip=['Artist','genres']
                                ).properties(width=1100,height=310).interactive()
        
        chart1=alt.Chart(df1,title='Debut year distribution').mark_bar().encode(
                        y=alt.Y('count()',scale=alt.Scale(zero=False),title='Artist number'),
                        x=alt.X('first_year',scale=alt.Scale(zero=False),title='Debut year'),
                        ).properties(width=650,height=310)
        
        chart1=chart1|alt.Chart(df1,title='Debut year percentage').mark_arc().encode(    
            theta=alt.Theta("range_count:Q"),    
            color=alt.Color("year_range:N"),
            tooltip=['year_range','range_count']
            ).properties(width=350,height=310)
        
        chart2=alt.Chart(df4[df4['Artist number']>10],title='genres distribution').mark_bar().encode(
            x=alt.X('Artist number',scale=alt.Scale(zero=False),title='Artist number'),
            y=alt.Y('genres',title='genres',sort='-x'),
            color='Artist number'
            ).properties(width=900,height=320)
        
        chart_describ=[dcc.Markdown("""
        - The **size** and **color** represents the combination of Artist's popularity and song's quality.
        - The singer in the **upper right** corner has the strongest overall strength.
        - We filtered out singers whose popularity was less than **60**.
        """),html.Div([html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()))]),dcc.Markdown("""
        - Artists with the highest popularity.
        """),html.Div([html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()))]),dcc.Markdown("""
        - Artists with the highest number of songs on the Top 100.
        """)]
        chart1_describ=dcc.Markdown("""
        - The chart on the **left** represents the **distribution of singers by year of debut**.
        - The chart on the **right** represents the **percentage of the year of debut of the top artists**.
        - The **range** of debut years is every **10** years.
        """)
        chart2_describ=dcc.Markdown("""
        - Represented **the type of singer** with the **highest** number of top. 
        """)
        
    elif page_title=="Lyrics Analysis":
        
        df = pd.read_excel('../data/processed/lyrics_dataset.xlsx')
        df = df.loc[(start_year <= df['Year']) & (df['Year'] <= end_year)]
        df['rank_bin'] = pd.cut(df['Rank'],bins=4,labels=['1-25','26-50','51-75','76-100'])
        df_bin = df.groupby(['rank_bin','Year']).mean().reset_index()
        sentiment_counts = df['Sentiment'].value_counts()
        source = pd.DataFrame({"category": ['Positive','Negative','Neutral'], "sentiment_counts": [sentiment_counts[0], sentiment_counts[1], sentiment_counts[2]]})
        df['rank_bin10'] = pd.cut(df['Rank'],bins=10,labels=['1-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100'])
        df_bin10 = df.groupby(['rank_bin10','Year']).mean().reset_index()
   



        
        if start_year==end_year:
            chart = alt.Chart(df_bin10).mark_bar(interpolate='basis').encode(
                x=alt.X('Year:N'),
                y=alt.Y('Frequency_love:Q', stack=True,axis=alt.Axis(title='Frequency')),
                color='rank_bin10:O').properties(
                title={'text':"Frequency of 'love' in {}".format(year), "anchor": "middle"},width=780)
        else:
            chart = alt.Chart(df_bin10).mark_area(interpolate='basis').encode(
                x=alt.X('Year:N'),
                y=alt.Y('Frequency_love:Q', stack=True,axis=alt.Axis(title='Frequency')),
                color='rank_bin10:O').properties(
                title={'text':"Frequency of 'love' in {}".format(year), "anchor": "middle"},width=780)
            
        chart1 = alt.Chart(df_bin).mark_bar().encode(
            x='Year:N',
            y=alt.Y('Word Count:Q', axis=alt.Axis(title='Lyrics Length')),
            column=alt.Column('rank_bin:O',title=None),
            color='Year:N',
            ).properties(
            title={'text':"Lyrics Length and Rank by Year", "anchor": "middle"},width=180)
        
        chart2 = alt.Chart(source).mark_arc().encode(
            theta=alt.Theta(field="sentiment_counts", type="quantitative"),
            color=alt.Color(field="category", type="nominal"),
            tooltip=["sentiment_counts","category"]).properties(
            title={'text':"Sentiment Counts in {}".format(year), "anchor": "middle"})
        
        chart3 = alt.Chart(df).mark_boxplot().encode(
            x=alt.X('Year:N'),
            y=alt.Y('Sentiment Polarity:Q', axis=alt.Axis(title='Sentiment Score')),
           ).properties(
            title={'text':"Boxplot of Sentiment Score in {}".format(year), "anchor": "middle"},width=300)
        
        chart2 = alt.hconcat(
            chart2,
            chart3,
            spacing=120)
        
        chart2 = chart2.configure_legend(
            orient='left',
            symbolSize=150, 
            symbolType='circle')
        
        

        
        chart_describ=[dcc.Markdown("""
        - Divide the top 100 songs into 10 groups; 
        - The X-axis represents the year; 
        - The Y-axis is the frequency of the keyword 'love'; 
        - From the figure, we can see the frequency of 'love' and the trend of their frequency every year.
        """)]
    
        chart1_describ=dcc.Markdown("""
        - Divide the top 100 songs into 4 groups; 
        - The X-axis represents the year; 
        - The Y-axis is the lyrics length; 
        - From the figure, From the figure, we can compare each year's lyrics length in the four rank groups.
        """)
        try:
            df['word cloud'] = df['Clean Lyrics']
            remove_words = ['verse', 'chorus', 'oh', 'want', 'yeah', 'wan', 'na', 'got', 'might','feat']
            for word in remove_words:
                df['word cloud'] = df['word cloud'].str.replace(fr'\b{word}\b', '', regex=True)
            text = ' '.join(df['word cloud'])
            wordcloud = WordCloud(width=1200, height=300, background_color='white').generate(text)
            image_filename = '../data/processed/wordcloud.png'
            plt.switch_backend('Agg') 
            plt.figure(figsize = (12, 4), facecolor = None)
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.tight_layout(pad = 0)
            plt.savefig(image_filename,dpi = 80)
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())
            chart2_describ=[dcc.Markdown("""
            - Chart on the left is a pie chart representing the proportion of positive, negative and neutral lyrics in the selected year. 
            - Placing the mouse on the pie chart can show the specific number of songs; 
            - The chart on the right is the boxplot which displays ranges within sentiment scores for the selected year; 
            - sentiment score ranges from -1 to 1. (-1 is the most negative, 1 is the most positive, and 0 is neutral).
            """),html.Div([html.Img(src=f'data:image/png;base64, {encoded_image.decode()}',alt="Red dot")])]
        except:
            chart2_describ=""""""

        
        
    elif page_title=="Tracks Analysis":

        from tracks import TrackChart
        tracks = TrackChart(start_year,end_year)
        chart, chart_describ = tracks.get_tracks_chart()
        chart1,  chart1_describ= tracks.get_tracks_chart1()
        chart2, chart2_describ = tracks.get_tracks_chart2()

    return html.Div(
        [html.H4(f"{page_title} between {year[0]} and {year[1]}:"),]
        # html.Div("This is data visualization content for {} in {}:".format(page_title, year))]
    ),chart.to_html(),html.Div(chart_describ),chart1.to_html(),html.Div(chart1_describ),chart2.to_html(),html.Div(chart2_describ)

if __name__ == "__main__":
    app.run_server(debug=True)
