import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main{
        background-color:#0E1117;
    }

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        padding-left:3rem;
        padding-right:3rem;
    }

    .big-title{
        text-align:center;
        font-size:48px;
        font-weight:bold;
        color:white;
    }

    .sub-title{
        text-align:center;
        color:#BDBDBD;
        font-size:18px;
        margin-bottom:25px;
    }

    .metric-card{
        background:#1E1E1E;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:1px solid #333;
        box-shadow:0 0 12px rgba(0,255,100,0.15);
    }

    .metric-title{
        color:#BDBDBD;
        font-size:16px;
    }

    .metric-value{
        color:#00FF7F;
        font-size:28px;
        font-weight:bold;
    }

    .result-box{
        background:#12351D;
        border:2px solid #22C55E;
        border-radius:18px;
        padding:25px;
        text-align:center;
        margin-top:20px;
    }

    .footer{
        text-align:center;
        color:#9CA3AF;
        font-size:15px;
        margin-top:20px;
    }

    </style>
    """, unsafe_allow_html=True)