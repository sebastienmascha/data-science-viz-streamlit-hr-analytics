import streamlit as st
import pandas as pd
import numpy as np

from .toc import Toc


def toc_content(toc: Toc):
    st.title('How it works?')
    st.markdown("< PHOTO >")
    toc.placeholder()

    # ----- HR Analytics: Job Change of Data Scientists -----
    toc.title("HR Analytics")
    toc.header("Abstract")
    toc.header("Research Questions")

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
