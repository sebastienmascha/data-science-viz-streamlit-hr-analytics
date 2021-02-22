import os

import streamlit as st
import seaborn as sns


def app():
    st.title("Research & Analysis")
    
    path_boxplot_city_dev_index_experience = os.getcwd() + "/res/img/boxplot_city_dev_index_experience.png"
    st.image(path_boxplot_city_dev_index_experience)
    st.markdown("This boxplot allows us to highlight that the people with a lot of experience are living essentially in developed cities whereas for Junior and Confirmed the distribution is more dispersed and on average they live in slightly less developed cities than Senior.")


