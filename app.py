import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from last_fm import *
import streamlit.components.v1 as components
from tone import tone_dict, tone_analize

st.set_page_config(
     page_title="Music Recommender App",
     page_icon="🎶",
)



# Function to Show the DataFrame in the App
def plotTable(data):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(data.columns[:2]),
                    fill_color='#1E847F',
                    font=dict(color='white', size=18),
                    align='left'),
        cells=dict(values=[data.Song, data.Artist],
                   fill_color='#ecc19c',
                   align='left',
                   height=30)),
    ])
    fig.update_layout(width = 1020, height = 500)
    return fig

def plotArtistTable(data):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(data.columns[:2]),
                    fill_color='#1E847F',
                    font=dict(color='white', size=18),
                    align='left'),
        cells=dict(values=[data.Artist, data.Percentage],
                   fill_color='#ecc19c',
                   align='left',
                   height=30)),
    ])
    fig.update_layout(width = 1020, height = 500)
    return fig


# Function to draw a stylecloud


# Function to Plot the Chart
def plotData(data):
    fig = px.bar(data, x='Tone', y='Score', title = 'Mood based on Model',color_discrete_sequence =['#1e847f'], width = 1020)
    fig.update_layout(paper_bgcolor="#ecc19c")
    fig.update_layout(plot_bgcolor="#ecc19c")
    fig.update_layout(title_font_color = '#1e847f', title_font_size = 30, font_color = '#1e847f')
    return fig


# Function to adjust the width of the App
def _max_width_():
    max_width_str = f'max-width: 1051px';

    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )
_max_width_()

def home():
    music = Image.open('music.png')
    t1, t2 = st.columns([0.10000000000000003, 0.5])
    t1.image(music, width=150)
    t2.header('')
    t2.header('Song Recommender based on emotions')
    form = st.form(key='my-form')
    text = form.text_input('How are you feeling today')
    submit = form.form_submit_button('Submit')

    if submit:
        dict = tone_dict(text)
        tone_lst = dict['Tone']
        dict = pd.DataFrame(dict)
        fig = plotData(dict)
        st.plotly_chart(fig)
        st.header('Based on your mood, we recommend you these songs')
        df = getAllSong(tone_lst)
        fig1 = plotTable(df.iloc[:15,:])
        st.plotly_chart(fig1)
        st.header('Based on your mood, we recommend you these artists')
        artist = df['Artist'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
        artist_df = pd.DataFrame({'Artist':artist.index, 'Percentage':artist.values})
        fig2 = plotArtistTable(artist_df)
        st.plotly_chart(fig2)




image = Image.open('image.png')
st.sidebar.image(image)
home()

