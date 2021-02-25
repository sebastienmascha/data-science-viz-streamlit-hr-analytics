import os

import streamlit as st
import seaborn as sns


def app():
    st.title("Research & Analysis")

    path_barplot_experience_company_type = os.getcwd() + "/res/img/barplot_experience_companytype.png"
    st.image(path_barplot_experience_company_type)
    st.markdown("This barplot shows us, considering our study, that startup employees have less experience than employees from other company types. We can deduce from this graph that it is rather people who are starting or just beginning their professional career who are entering the world of startup and innovation.")

    path_barplot_last_new_job_enrolled_university = os.getcwd() + "/res/img/barplot_lastnewjob_enrolleduniversity.png"
    st.image(path_barplot_last_new_job_enrolled_university)
    st.markdown("This barplot shows us, considering our study, that the people without any enrollment took on average more time to find their actual job then those who are following courses.")

    path_boxplot_city_dev_index_experience = os.getcwd() + "/res/img/boxplot_city_dev_index_experience.png"
    st.image(path_boxplot_city_dev_index_experience)
    st.markdown("This boxplot allows us to highlight that the people with a lot of experience are living essentially in developed cities whereas for Junior and Confirmed the distribution is more dispersed and on average they live in slightly less developed cities than Senior.")

    path_boxplot_education_level_last_new_job = os.getcwd() + "/res/img/boxplot_educationlevel_lastnewjob.png"
    st.image(path_boxplot_education_level_last_new_job)
    st.markdown("We can notice on this graph a lot of heterogeneity. What is relevant is the large interval for PhDs which may be due to the fact that these employees started their professional career and then decided to do a thesis in the course of their professional career which would explain the particular shape of this red box.")

    path_histo_experience_group_by_enrolled_university = os.getcwd() + "/res/img/histo_experience_groupby_enrolleduniversity.png"
    st.image(path_boxplot_education_level_last_new_job)
    st.markdown("We can see on that histogram, that the more work experience people have, the less they are enrolled in full time or part time course.")

    st.markdown("""
    **You can find more relevant descriptive analysis in the "Descriptive Analysis" part of the notebook, [here](https://github.com/sebastienmascha/data-science-viz-streamlit-hr-analytics/blob/main/Python3_6_Notebook.ipynb).**
    """)




    




