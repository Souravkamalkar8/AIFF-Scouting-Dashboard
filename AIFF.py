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
    st.text('Team:' + team)
    st.text('Competition:' + competition )    
    st.text('Position:' + df['Position'][j])
    st.text('Season:' + season)
    
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
st.header(player + ' Scouting Report')
st.subheader('vs.'+' '+ df['Role'][j] + 's in ' + df['Competition'][j] + ' '+ df['Season'][j] )
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(Attr, Perc)
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

#Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()
 
# Add annotation to bars
k=0
for i in ax.patches:
    if(k<=14):
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
             values[k],
             fontsize = 10, fontweight ='bold',
             color ='black')
        k=k+1
    
    elif(k==15):
        break

#Add Plot Title
#ax.set_title('vs.'+df['Role'][j] + 's in ' + df['Competition'][j] + ' '+ df['Season'][j] ,
             #loc ='left', )
plt.xlabel('Percentile', fontweight ='bold', fontsize = 15)
plt.xlim(0, 100,20)

st.caption('*Player compared to positional peers in'+' ' + df['Competition'][j]+ ' '+ 'over the Season'+ ' ' + df['Season'][j]+'.')
st.caption('*Values at the end of each bar are Per 90 values. ')
 
# Add Text
#fig.text(0.43, 0.00, '*Player compared to positional peers in'+' ' + df['Competition'][j]+ ' '+ 'over the Season'+ ' ' + df['Season'][j]+'.' , fontsize = 9,
         #color ='black', ha ='right', va ='bottom',
         #alpha = 0.7)
#fig.text(0.3, 0.02, '*Values at the end of each bar are Per 90 values. ' , fontsize = 9,
         #color ='black', ha ='right', va ='bottom',
         #alpha = 0.7)

# Show Plot
#plt.show()

st.pyplot(fig)

#Fourth Row 
column1,column2= st.columns(2)

with column1:
    urllib.request.urlretrieve( 'https://iftwc.com/wp-content/uploads/2023/01/Fl4GO8JX0AANhPb-edited.jpeg',"vision.jpeg")
    img=Image.open("vision.jpeg")
    width, height = img.size
    area = (0, 0, width, height/1.32)
    vision = img.crop(area)
    st.image(vision)
    
with column2:
    urllib.request.urlretrieve(
  'https://upload.wikimedia.org/wikipedia/en/thumb/0/07/All_India_Football_Federation_Logo.svg/640px-All_India_Football_Federation_Logo.svg.png',
   "aiff.png")
    aiff=Image.open("aiff.png")
    st.image(aiff)
   
    
    
    
    


    

