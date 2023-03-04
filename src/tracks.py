import pandas as pd
import altair as alt
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import Dash, dcc, html

class TrackChart:
    def __init__(self,start_year,end_year):
        hits = pd.read_csv('../data/processed/audio_data_processed.csv')
        hits.drop(["Unnamed: 0",'type','uri','track_href','analysis_url','id'], axis=1, inplace=True)
        hits['rank_bin'] = pd.cut(hits['Rank'],bins=10,labels=['1-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91-100'])
        self.titleParams = [alt.TitleParams(text = x,subtitle=y,anchor='start',fontSize = 24) for (x,y) in [
                        ("Vibe Features Over Rank","Energy, speechiness, instrumentalness,valence in different strata of the charts"),
                        ("Rhythm Features Over Year", "Time signature, tempo, duration occurences"),
                        ("Musical Features Interaction", "Musical key, mode occurences")]]
        self.hits = hits
        self.hits_c = hits[(start_year <= hits['Year']) & (hits['Year'] <= end_year)]
        alt.renderers.set_embed_options(theme='dark')

    def get_tracks_chart(self):
            
        chart_describ = dcc.Markdown("""
        - The **energy** represents the intensity and activity; 
        - The **speechness** detects the degree of presence spoken words; 
        - The **instrumentalness** predicts whether a track contains no vocals; 
        - The **valence** describing the musical positiveness.
        """)
        hits_c_bin = self.hits_c.groupby('rank_bin').mean().reset_index()
        hits_c_bin = hits_c_bin[['rank_bin','popularity','energy','speechiness','instrumentalness','valence']].set_index(['rank_bin','popularity']).stack().reset_index(name='value').rename(columns={'level_2':'features'})
        charts=[]


        for i in ['energy','speechiness','instrumentalness','valence']:
            charts.append(alt.Chart(hits_c_bin[hits_c_bin['features'] == i]).mark_point(filled=True).encode(
            x=alt.X('rank_bin:N',title='Rank bins'),
            y=alt.Y('value',scale=alt.Scale(zero=False),title='Occurences'),
            color='features:N',
            opacity='popularity:Q',
            size= 'popularity:Q',
            shape='features:N'
            ))
        chart = (charts[0]+charts[1]+charts[2]+charts[3]).properties(
                width=900,height=250, title = self.titleParams[0])
        return chart, chart_describ


    def get_tracks_chart1(self):            
        hits_c1 = self.hits.groupby(['Year','time_signature']).size().reset_index(name='cnt')
        hits_c1['ts_perct']=hits_c1['cnt']/100
        chart1 = (alt.Chart(hits_c1[hits_c1['time_signature']==4]).mark_line(point=True).encode(
            x=alt.X('Year',scale=alt.Scale(zero=False)),
            y=alt.Y('ts_perct:Q',scale=alt.Scale(zero=False),title=' ')
        ).properties(width=250,height=250,title="4/4 Time signature percentage")| alt.Chart(self.hits[['Year','duration_ms','tempo']]).mark_boxplot().encode(
            x=alt.X('Year',scale=alt.Scale(zero=False)),
            y=alt.Y('tempo:Q',title=' ')
        ).properties(width=250,height=250,title="Tempo")| alt.Chart(self.hits[['Year','duration_ms','tempo']]).mark_boxplot().encode(
            x=alt.X('Year',scale=alt.Scale(zero=False)),
            y=alt.Y('duration_ms:Q',title=' ')
        ).properties(width=250,height=250,title="Duration(ms)")).properties(title=self.titleParams[1])

        chart1_describ = dcc.Markdown("""
        - The **time signiture** (aka. meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4"; 
        - The **tempo** (aka. beats per minute, BPM), which is the speed or pace of a given piece and derives directly from the average beat duration; 
        - The **duration** is the duration of the track in milliseconds.
        """)
        return chart1,chart1_describ
            
    def get_tracks_chart2(self):        
        hits_c2 = self.hits.groupby(['key','mode']).size().reset_index(name='cnt')

        # hits_c2_2 = hits[['Year','tempo','duration_ms']].set_index(['Year']).stack().reset_index(name='value').rename(columns={'level_1':'features'})
        chart2 = alt.Chart(hits_c2).mark_bar().encode(
            x=alt.X('key:N',title='Musical Key'),
            y=alt.Y('cnt:Q',title='Occurrence'),
            color='mode:N'
        ).properties(width=900,height=250, title=self.titleParams[2])

        chart2_describ = dcc.Markdown("""
        - The **musical** key represents the scale, where values are integers that can map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on; 
        - The **mode** indicates the modality (major or minor), which is the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
        """)

        return chart2,chart2_describ
    

