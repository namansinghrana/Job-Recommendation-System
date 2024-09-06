import streamlit as st
import pandas as pd
import pickle

df = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommendation(title):
    idx = df[df['job_title'] == title].index[0]
    idx = df.index.get_loc(idx)
    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])[1:20]

    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].job_title)

    return jobs

#Web APP
st.title("Linkedin Job Search System")
tt = st.selectbox('search job',df['job_title'])
 

jobs = recommendation(tt)


if jobs:
    st.write(jobs)    