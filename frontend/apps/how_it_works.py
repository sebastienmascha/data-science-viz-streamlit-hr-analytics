import streamlit as st
import pandas as pd
import numpy as np

from .toc import Toc


def toc_content(toc: Toc):
    st.image("https://drive.google.com/uc?id=1yBn2g5h_16b5w2Bv5072OZbiN1rHJW07")
    toc.placeholder()

    # ----- HR Analytics: Job Change of Data Scientists -----
    toc.title("Abstract")
    st.markdown("A UC Berkeley research by [Sébastien Mascha](https://www.linkedin.com/in/sebastienmascha) and [Thomas Lecouedic](https://www.linkedin.com/in/thomas-lecouedic) advised by Professor Seema Saharan.")
    st.markdown("""
        A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which conduct by the company. Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training or looking for a new employment because it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates. Information related to demographics, education, experience are in hands from candidates signup and enrollment.

        This dataset designed to understand the factors that lead a person to leave current job for HR researches too. By model(s) that uses the current credentials,demographics,experience data you will predict the probability of a candidate to look for a new job or will work for the company, as well as interpreting affected factors on employee decision.

        The whole data divided to train and test . Target isn't included in test but the test target values data file is in hands for related tasks. A sample submission correspond to enrollee_id of test set provided too with columns : enrollee _id , target

        **Dataset:**

        Link to the dataset: https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists

        Data Source: Kaggle (https://www.kaggle.com)

        **Features:**

        - enrollee_id : Unique ID for candidate

        - city: City code

        - city_ development _index : Developement index of the city (scaled)

        - gender: Gender of candidate

        - relevent_experience: Relevant experience of candidate

        - enrolled_university: Type of University course enrolled if any

        - education_level: Education level of candidate

        - major_discipline :Education major discipline of candidate

        - experience: Candidate total experience in years

        - company_size: No of employees in current employer's company

        - company_type : Type of current employer

        - lastnewjob: Difference in years between previous job and current job

        - training_hours: training hours completed

        - target: 0 – Not looking for job change, 1 – Looking for a job change

        **Note:**

        - The dataset is imbalanced so it might affect our result if we dont handle it;
        - Most features are categorical (Nominal, Ordinal, Binary), some with high cardinality so encoding methods and techniques will help to boost models performance;
        - Missing imputation strategy might affect the results so it can be a part of your pipeline as well.
    """)
    toc.header("Research Questions")
    st.markdown("""
        **Target Prediction:**

        1. Does the number of training hours have an impact on the final decision?
        1. Are people with many years of experience and working in a large company more likely to stay in the company?
        1. Are young graduates more likely to stay in the company?
        1. Are people working in the field of data science but without experience willing to look for a new job?
        1. Are people in vocational retraining more willing than others to look for a new job?
        1. Are employees already working in the field of data Science more likely to refuse the job?
        1. Are people working in an Early Stage Startup more likely to stay in the company?
        1. Are undergraduate students not specialised in data science more likely to refuse the job?
        1. Are students enrolled in a part-time data science program more likely to decline the offer?
        1. To what extent is gender correlated with the target?
        1. Are people working in private companies more likely to stay in the company than people working in the public sector?
        1. Are people working in highly developed cities with many hours of training more likely to leave their jobs?
        1. Are small business employees ready to look for a new job, considering people who are not enrolled in any university?


        **Correlation between features:**
        
        14. Do people working in large companies have a high city development index?
        1. Do people who left their previous job more than two years ago generally take more hours of training? 
        1. Are large companies mostly located in developed cities?
        1. Do people with a Master's or PhD degree have fewer hours of training than others? 
        1. Are people coming from an underprivileged city and with a high education level looking for a new job?
        1. To what extent people without relevant experience will need more training hours?
        1. Do people who have taken a major discipline other than STEM take more hours of training?
    """)


    # ----- Data Science Pipeline -----
    toc.title("Data Science Pipeline")
    toc.header("Workspace: Dataiku & Colab")
    toc.header("Methods & Results")

    # ----- Deployment in Production -----
    toc.title("Deployment in Production")
    toc.header("Docker: FastAPI + Streamlit")
    toc.header("Load Balancer: Traefik")
    toc.header("Kubernetes")
    toc.header("Data Persistence - Microsoft SQL")
    st.markdown("""
        We decided to keep this website as stateless for privacy reason.\n\
        Nevertheless, we planned and tested the implementation of Microsoft SQL.
        """)

    # ----- Conclusion -----
    toc.title("Deployment in Production")

    # ----- References -----
    toc.title("References")


def app():

    toc = Toc()
    st.sidebar.markdown("# Table of Contents")
    toc_content(toc)
    toc.generate()
