#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
from scipy import stats
import urllib.request
import pandas as pd
import numpy as np
import streamlit as st
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib as mpl
import altair as alt


st.set_page_config(layout="wide", initial_sidebar_state='expanded')
st.sidebar.header('Player Scouting Dashboard')
df=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSwMdNgfS2HwFKh8X72hFPbtc-7AtwvwK3_Q26kX-Z9wEqHCxQ8VE8D0cPx68GUL64HxyHepC7psZsr/pub?output=csv')
selection= df[['Season', 'Competition', 'Role', 'Team', 'Name']]

#st.sidebar.markdown('Select a Season')
season= st.sidebar.selectbox("Select a Season", (selection['Season'].unique()))
selection= selection[selection['Season']==season]

#st.sidebar.markdown('Select a Competition')
competition= st.sidebar.selectbox("Select a Competition ", (selection['Competition'].unique()))
selection=selection[selection['Competition']== competition]

#st.sidebar.markdown('Select a Team')
team= st.sidebar.selectbox("Select a Team", (selection['Team'].unique()))
selection=selection[selection['Team']== team]

#st.sidebar.markdown('Select a Position')
position= st.sidebar.selectbox("Select a Position", (selection['Role'].unique()))
selection=selection[selection['Role']== position]

#st.sidebar.markdown('Select a Player')
player= st.sidebar.selectbox("Select a Player", (selection['Name'].unique()))


  
scolumn1,scolumn2= st.sidebar.columns(2)

with scolumn1:
    urllib.request.urlretrieve( 'https://iftwc.com/wp-content/uploads/2023/01/Fl4GO8JX0AANhPb-edited.jpeg',"vision.jpeg")
    img=Image.open("vision.jpeg")
    width, height = img.size
    area = (0, 0, width, height/1.32)
    vision = img.crop(area)
    vision = vision.resize((100, 50))
    st.sidebar.image(vision,use_column_width = False)
    
with scolumn2:
    urllib.request.urlretrieve(
  'https://upload.wikimedia.org/wikipedia/en/thumb/0/07/All_India_Football_Federation_Logo.svg/640px-All_India_Football_Federation_Logo.svg.png',
   "aiff.png")
    aiff=Image.open("aiff.png")
    aiff = aiff.resize((100, 50))
    st.sidebar.image(aiff,use_column_width = False)    

st.sidebar.markdown('created by **_Sourav Kamalkar_**')

df= df[(df['Season']==season) & (df['Competition']==competition) & (df['Role']==position)]
df=df.reset_index(drop=True)

for i in range(0, len(df)):
        if ((df['Name'][i] == player) & (df['Team'][i] == team)) :
            j = i
            break
        else:
            continue

Attr=['Non-Pen Goals', 'Total shots', 'Succ. dribbles',
       'Key passes', 'Accurate crosses', 'Total passes', 'Accurate passes %',
       'Accurate final third passes', 'Accurate own half passes',
       'Accurate opposition half passes', 'Tackles', 'Clearances',
       'Interceptions', 'Ground duels won', 'Aerial duels won']
Perc=[round(stats.percentileofscore(df['Non-Pen Goals'], df['Non-Pen Goals'][j])),
      round(stats.percentileofscore(df['Total shots'], df['Total shots'][j])),
      round(stats.percentileofscore(df['Succ. dribbles'], df['Succ. dribbles'][j])),
      round(stats.percentileofscore(df[ 'Key passes'], df[ 'Key passes'][j])),
      round(stats.percentileofscore(df['Accurate crosses'], df['Accurate crosses'][j])),
      round(stats.percentileofscore(df['Total passes'], df['Total passes'][j])),
      round(stats.percentileofscore(df['Accurate passes %'], df['Accurate passes %'][j])),
      round(stats.percentileofscore(df['Accurate final third passes'], df['Accurate final third passes'][j])),
      round(stats.percentileofscore(df['Accurate own half passes'], df['Accurate own half passes'][j])),
      round(stats.percentileofscore(df['Accurate opposition half passes'], df['Accurate opposition half passes'][j])),
      round(stats.percentileofscore(df[ 'Tackles'], df[ 'Tackles'][j])),
      round(stats.percentileofscore(df['Clearances'], df['Clearances'][j])),
      round(stats.percentileofscore(df['Interceptions'], df['Interceptions'][j])),
      round(stats.percentileofscore(df['Ground duels won'], df['Ground duels won'][j])),
      round(stats.percentileofscore(df['Aerial duels won'], df['Aerial duels won'][j]))]
                                       
values= [round(df['Non-Pen Goals'][j],2),
         round(df['Total shots'][j],2),
         round(df['Succ. dribbles'][j],2),
         round(df['Key passes'][j],2),
         round(df['Accurate crosses'][j],2),
         round(df['Total passes'][j],2),
         round(df['Accurate passes %'][j],2),
         round(df['Accurate final third passes'][j],2),
         round(df['Accurate own half passes'][j],2),
         round(df['Accurate opposition half passes'][j],2),
         round(df['Tackles'][j],2),
         round(df['Clearances'][j],2),
         round(df['Interceptions'][j],2),
         round(df['Ground duels won'][j],2),
         round(df['Aerial duels won'][j],2)]



#First Row 
c1,c2= st.columns(2)

with c1:
    st.header('Player Details')
with c2:
    st.header('Season Stats' )
    
#Second Row
col1,col2,col4,col5,col6=st.columns([1,2,1,1,1])

with col1:
    urllib.request.urlretrieve('https://cdn-icons-png.flaticon.com/512/607/607445.png',
   "avatar.png")
    Avatar=Image.open("avatar.png")
    st.image(Avatar)

with col2:
    st.subheader(player)
    st.write("**Team:** " + team)
    st.write('**Competition:** ' + competition )    
    st.write('**Position:** ' + df['Position'][j])
    st.write('**Season:** ' + season)
    
with col4:
    st.metric('Appearances', value= df['Appearances'][j])
    st.metric('Goals', value= df['Goals'][j])

with col5:
    st.metric('Started', value= df['Started'][j])
    st.metric('Assists', value= df['Assists'][j])

with col6:
    st.metric('Minutes played', value= df['Minutes played'][j])
    st.metric('Clean sheets', value= df['Clean sheets'][j])

#Third Row
overall=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTp0qr1bTEK9L0zYNjsWA1aOI8yEhJCk06JEiiQ90olkzi6sZdiphfVIWi9WNO8u_pgb5PckobuhSHd/pub?output=csv')
per_90=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRv059UgPrTUcQRXqP11UsfWjV-aHDEQPKlsKLmmcqt2zw64IJbinEdhhASa9NwR5Wm1wKlNyTwS-JQ/pub?output=csv')

for t in range(0, len(overall)):
        if ((overall['Name'][t] == player) & (overall['Team'][t] == team)) :
            k = t
            break
        else:
            continue


st.header('Detailed Stats')
tab1, tab2 = st.tabs(["**Overall**", "**Per 90**"])
with tab1:
  CC1,CC2,CC3= st.columns(3)
  with CC1:
      st.subheader('Goal Contributions' )
      st.write('**Goals**: ' + str(overall['Goals'][k] ))
      st.write('**Total Shots:** ' + str(overall['Total shots'][k] ))
      st.write('**Goal Conversion %:** ' + str(overall['Goal conversion %'][k])+'%')
      st.write('**Shots on target:** ' +  str(overall['Shots on target'][k] ))
      st.write('**Shots from set piece:** ' +  str(overall['Shots from set piece'][k] ))
      st.write('**Penalty goals:** ' +  str(overall['Penalty goals'][k] ))
      st.write('**Headed goals:** ' +  str(overall['Headed goals'][k] ))
      st.write('**Big chances missed:** ' +  str(overall['Big chances missed'][k] ))

      st.subheader('Creativity' )
      st.write('**Assists:** ' +  str(overall['Assists'][k] ))
      st.write('**Key passes:** ' +  str(overall['Key passes'][k] ))
      st.write('**Passes to assist:** ' +  str(overall['Passes to assist'][k] ))
      st.write('**Dribbles Attempted:** ' +  str(overall['Total Dribbles'][k] ))
      st.write('**Successful Dribbles %:** ' +  str(overall['Successful dribbles %'][k] ))
      st.write('**Total Crosses:** ' +  str(overall['Total Crosses'][k] ))
      st.write('**Crossing Accuracy %:** ' +  str(overall['Accurate crosses %'][k] )+'%')



  with CC2:
      st.write('**Penalties won:** ' +  str(overall['Penalty won'][k] ))

      st.subheader('Passing & Ball Distribution' )
      st.write('**Total passes:** ' +  str(overall['Total passes'][k] ))
      st.write('**Passing Accuracy %:** ' +  str(overall['Accurate passes %'][k] )+ '%')
      st.write('**Accurate final third passes:** ' +  str(overall['Accurate final third passes'][k] ))
      st.write('**Accurate own half passes:** ' +  str(overall['Accurate own half passes'][k] ))
      st.write('**Accurate opposition half passes:** ' +  str(overall['Accurate opposition half passes'][k] ))
      st.write('**Long Balls Attempted:** ' +  str(overall['Long Balls Attempted'][k] ))
      st.write('**Long Balls Accuracy %:** ' +  str(overall['Accurate long balls %'][k] )+'%')

      st.subheader('Defensive Ability' )
      st.write('**Tackles:** ' +  str(overall['Tackles'][k] ))
      st.write('**Interceptions:** ' +  str(overall['Interceptions'][k] ))
      st.write('**Clearances:** ' +  str(overall['Clearances'][k] ))
      st.write('**Blocks:** ' +  str(overall['Blocked shots'][k] ))
      st.write('**Total Duels:** ' +  str(overall['Total Duels '][k] ))
      st.write('**Total duels won %:** ' +  str(overall['Total duels won %'][k] )+'%')
      st.write('**Ground Duels:** ' +  str(overall['Ground Duels'][k] ))


  with CC3:
      st.write('**Ground duels won %:** ' +  str(overall['Ground duels won %'][k] )+'%')
      st.write('**Aerial Duels:** ' +  str(overall['Aerial Duels'][k] ))
      st.write('**Aerial duels won %:** ' +  str(overall['Aerial duels won %'][k] )+'%')

      st.subheader('Other' )
      st.write('**Fouls:** ' +  str(overall['Fouls'][k] ))
      st.write('**Yellow cards:** ' +  str(overall['Yellow cards'][k] ))
      st.write('**Red cards:** ' +  str(overall['Red cards'][k] ))

with tab2:
  CC1,CC2,CC3= st.columns(3)
  with CC1:
    st.subheader('Goal Contributions' )
    st.write('**Goals:** ' + str(per_90['Goals'][k] ))
    st.write('**Total Shots:** ' + str(per_90['Total shots'][k] ))
    st.write('**Goal Conversion %:** ' + str(per_90['Goal conversion %'][k] )+'%')
    st.write('**Shots on target:** ' + str(per_90['Shots on target'][k] ))
    st.write('**Shots from set piece:** ' + str(per_90['Shots from set piece'][k] ))
    st.write('**Penalty goals:** ' + str(per_90['Penalty goals'][k] ))
    st.write('**Headed goals:** ' + str(per_90['Headed goals'][k] ))
    st.write('**Big chances missed:** ' + str(per_90['Big chances missed'][k] ))

    st.subheader('Creativity' )
    st.write('**Assists:** ' + str(per_90['Assists'][k] ))
    st.write('**Key passes:** ' + str(per_90['Key passes'][k] ))
    st.write('**Passes to assist:** ' + str(per_90['Passes to assist'][k] ))
    st.write('**Dribbles Attempted:** ' + str(per_90['Total Dribbles'][k] ))
    st.write('**Successful Dribbles %:** ' + str(per_90['Successful dribbles %'][k] )+'%')
    st.write('**Total Crosses:** ' + str(per_90['Total Crosses'][k] ))
    st.write('**Crossing Accuracy %:** ' + str(per_90['Accurate crosses %'][k] )+'%')



  with CC2:
    st.write('**Penalties won**' + str(overall['Penalty won'][k] ))

    st.subheader('Passing & Ball Distribution' )
    st.write('**Total passes:** ' + str(per_90['Total passes'][k] ))
    st.write('**Passing Accuracy:** ' + str(per_90['Accurate passes %'][k] )+'%')
    st.write('**Accurate final third passes:** ' + str(per_90['Accurate final third passes'][k] ))
    st.write('**Accurate own half passes:** ' + str(per_90['Accurate own half passes'][k] ))
    st.write('**Accurate opposition half passes:** ' + str(per_90['Accurate opposition half passes'][k] ))
    st.write('**Long Balls Attempted:** ' + str(per_90['Long Balls Attempted'][k] ))
    st.write('**Long Balls Accuracy %:** ' + str(per_90['Accurate long balls %'][k])+'%')

    st.subheader('Defensive Ability' )
    st.write('**Tackles:** ' + str(per_90['Tackles'][k] ))
    st.write('**Interceptions:** ' + str(per_90['Interceptions'][k] ))
    st.write('**Clearances:** ' + str(per_90['Clearances'][k] ))
    st.write('**Blocks:** ' + str(per_90['Blocked shots'][k] ))
    st.write('**Total Duels:** ' + str(per_90['Total Duels '][k] ))
    st.write('**Total duels won %:** ' + str(per_90['Total duels won %'][k] )+'%')
    st.write('**Ground Duels:** ' + str(per_90['Ground Duels'][k] ))


  with CC3:
    st.write('**Ground duels won %:** ' + str(per_90['Ground duels won %'][k] )+'%')
    st.write('**Aerial Duels:** ' + str(per_90['Aerial Duels'][k] ))
    st.write('**Aerial duels won %:** ' + str(per_90['Aerial duels won %'][k] )+'%')

    st.subheader('Other' )
    st.write('**Fouls:** ' + str(per_90['Fouls'][k] ))
    st.write('**Yellow cards:** ' + str(per_90['Yellow cards'][k] ))
    st.write('**Red cards:** ' + str(per_90['Red cards'][k] ))

   

st.header(player + ' Scouting Report')
st.subheader('vs.'+' '+ df['Role'][j] + 's in ' + df['Competition'][j] + ' '+ df['Season'][j] )
test={'Attributes': ['Non-Pen Goals',
                 'Total shots',
                 'Succ. dribbles',
                 'Key passes',
                 'Accurate crosses',
                 'Total passes',
                 'Accurate passes %',
                 'Accurate final third passes',
                 'Accurate own half passes',
                 'Accurate opp. half passes',
                 'Tackles',
                 'Clearances',
                 'Interceptions',
                 'Ground duels won',
                 'Aerial duels won'],
                        'Percentile': Perc}
test = pd.DataFrame(test)

bars = alt.Chart(test).mark_bar().encode(
      x=alt.X('Percentile:Q', sort= 'ascending',
              axis=alt.Axis(title='Percentile',labels=False, ticks=False,titlePadding= 25,titleFontSize=20,grid= False,
               domain=False            )
             ),
      y=alt.Y( 'Attributes:O',sort=['Non-Pen Goals','Total shots','Succ. dribbles','Key passes','Accurate crosses','Total passes','Accurate passes %','Accurate final third passes',
'Accurate own half passes','Accurate opp. half passes','Tackles','Clearances','Interceptions','Ground duels won','Aerial duels won'],
              axis=alt.Axis(title=None,labels=True, ticks=False, labelPadding=10,grid= False
                           , labelFontSize=13,domain=False,labelFontWeight='bold'))

)
text = bars.mark_text(
      align='left',
      baseline='middle',
      dx=3  # Nudges text to right so it doesn't appear on top of the bar
  ).encode(
      text='Percentile:Q'
  )
chart = (bars + text).properties(height=600,width=400).configure_view(stroke=None)
st.altair_chart(chart, use_container_width=True)

st.caption('*Player compared to positional peers in'+ ' '+competition +' '+ 'over the'+' ' + season)
st.caption('*Percentiles are calculated based on Per 90 values.')
    




#Fourth Row 
column1,column2= st.columns(2)

with column1:
    urllib.request.urlretrieve( 'https://iftwc.com/wp-content/uploads/2023/01/Fl4GO8JX0AANhPb-edited.jpeg',"vision.jpeg")
    img=Image.open("vision.jpeg")
    width, height = img.size
    area = (0, 0, width, height/1.32)
    vision = img.crop(area)
    vision = vision.resize((200, 100))
    st.image(vision)
    
with column2:
    urllib.request.urlretrieve(
  'https://upload.wikimedia.org/wikipedia/en/thumb/0/07/All_India_Football_Federation_Logo.svg/640px-All_India_Football_Federation_Logo.svg.png',
   "aiff.png")
    aiff=Image.open("aiff.png")
    aiff = aiff.resize((200, 100))
    st.image(aiff,use_column_width = False)
   
    
    
    
    


    

