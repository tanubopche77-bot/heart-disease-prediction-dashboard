import streamlit as st
import pandas as pd
import joblib

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="❤️ Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# ---------------- Load Model ----------------
model = joblib.load("model.pkl")

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

.stApp{
    background:linear-gradient(to right,#74ebd5,#ACB6E5);
}

.title{
    text-align:center;
    color:#d90429;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#222;
    font-size:18px;
}

[data-testid="stSidebar"]{
    background:#1f3b73;
}

[data-testid="stSidebar"] label{
    color:white;
    font-weight:bold;
}

.stButton>button{
    background:#ff4b4b;
    color:white;
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#00b894;
    color:white;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0 5px 10px rgba(0,0,0,0.2);
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------

st.markdown("<h1 class='title'>❤️ Heart Disease Prediction Dashboard</h1>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Machine Learning Based Heart Disease Prediction System</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- Sidebar ----------------

st.sidebar.title("🩺 Patient Details")

age = st.sidebar.slider("Age",18,100,40)

sex = st.sidebar.selectbox(
    "Sex",
    ["M","F"]
)

cp = st.sidebar.selectbox(
    "Chest Pain Type",
    ["ATA","NAP","ASY","TA"]
)

bp = st.sidebar.number_input(
    "Resting Blood Pressure",
    80,220,120
)

chol = st.sidebar.number_input(
    "Cholesterol",
    0,700,200
)

fbs = st.sidebar.selectbox(
    "Fasting Blood Sugar",
    [0,1]
)

ecg = st.sidebar.selectbox(
    "Resting ECG",
    ["Normal","LVH","ST"]
)

hr = st.sidebar.slider(
    "Maximum Heart Rate",
    60,220,150
)

angina = st.sidebar.selectbox(
    "Exercise Angina",
    ["Y","N"]
)

oldpeak = st.sidebar.slider(
    "Old Peak",
    0.0,
    6.5,
    1.0
)

slope = st.sidebar.selectbox(
    "ST Slope",
    ["Up","Flat","Down"]
)

# ---------------- Dashboard ----------------

st.subheader("📊 Patient Dashboard")

c1,c2,c3,c4=st.columns(4)

c1.metric("👤 Age",age)
c2.metric("🫀 Max HR",hr)
c3.metric("🩸 BP",bp)
c4.metric("🧪 Cholesterol",chol)

st.markdown("---")

left,right=st.columns([2,1])

with left:

    st.subheader("📋 Patient Information")

    patient=pd.DataFrame({

        "Feature":[
            "Age",
            "Sex",
            "Chest Pain",
            "Resting BP",
            "Cholesterol",
            "Fasting BS",
            "Resting ECG",
            "Max HR",
            "Exercise Angina",
            "Old Peak",
            "ST Slope"
        ],

        "Value":[
            age,
            sex,
            cp,
            bp,
            chol,
            fbs,
            ecg,
            hr,
            angina,
            oldpeak,
            slope
        ]

    })

    st.dataframe(patient,use_container_width=True)

with right:

    st.subheader("❤️ Health Status")

    st.progress(75)

    st.info("Fill all patient details and click Predict.")
    