import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('final_model.pkl')

# Page Config
st.set_page_config(page_title="Bank Term Deposit Prediction", layout="wide")

# Title
st.title("Bank Term Deposit Prediction")
st.write("Fill the information below to predict if the client will subscribe to a term deposit.")

# Form Layout
with st.form(key='prediction_form'):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=18, max_value=100, value=30)
        job = st.selectbox('Job', [
            'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
            'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'
        ])
        marital = st.selectbox('Marital Status', ['divorced', 'married', 'single', 'unknown'])
        education = st.selectbox('Education', [
            'basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree', 'unknown'
        ])
        contact = st.selectbox('Contact Communication Type', ['cellular', 'telephone'])
        duration = st.number_input('Call Duration (seconds)', min_value=0, max_value=5000, value=100)
        st.caption("Please enter the call duration of the last contact, in seconds (e.g., 100).")

    with col2:
        default = st.selectbox('Has Credit in Default?', ['no', 'yes'])
        housing = st.selectbox('Has Housing Loan?', ['no', 'yes'])
        loan = st.selectbox('Has Personal Loan?', ['no', 'yes'])
        month = st.selectbox('Last Contact Month', [
            'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
        ])
        day_of_week = st.selectbox('Last Contact Day of the Week', ['mon', 'tue', 'wed', 'thu', 'fri'])

    with col3:
        campaign = st.number_input('Number of Contacts During Campaign', min_value=1, max_value=50, value=1)
        pdays = st.number_input('Days Passed After Last Contact', min_value=-1, max_value=999, value=999)
        previous = st.number_input('Number of Previous Contacts', min_value=0, max_value=50, value=0)
        poutcome = st.selectbox('Outcome of the Previous Campaign', ['failure', 'nonexistent', 'success'])

    st.subheader("Economic Indicators")
    col4, col5, col6 = st.columns(3)
    with col4:
        emp_var_rate = st.number_input('Employment Variation Rate', value=0.0, step=0.01)
    with col5:
        cons_price_idx = st.number_input('Consumer Price Index', value=93.0, step=0.01)
    with col6:
        cons_conf_idx = st.number_input('Consumer Confidence Index', value=-40.0, step=0.1)

    col7, col8 = st.columns(2)
    with col7:
        euribor3m = st.number_input('Euribor 3 Month Rate', value=4.0, step=0.01)
    with col8:
        nr_employed = st.number_input('Number of Employees', value=5000.0, step=1.0)

    submit_button = st.form_submit_button(label='Predict')

# Encoding Categorical Variables
job_mapping = {'admin.':0, 'blue-collar':1, 'entrepreneur':2, 'housemaid':3, 'management':4,
               'retired':5, 'self-employed':6, 'services':7, 'student':8, 'technician':9, 'unemployed':10, 'unknown':11}
marital_mapping = {'divorced':0, 'married':1, 'single':2, 'unknown':3}
education_mapping = {'basic.4y':0, 'basic.6y':1, 'basic.9y':2, 'high.school':3, 'illiterate':4, 'professional.course':5, 'university.degree':6, 'unknown':7}
binary_mapping = {'no':0, 'yes':1}
contact_mapping = {'cellular':0, 'telephone':1}
month_mapping = {'jan':0, 'feb':1, 'mar':2, 'apr':3, 'may':4, 'jun':5, 'jul':6, 'aug':7, 'sep':8, 'oct':9, 'nov':10, 'dec':11}
day_mapping = {'mon':0, 'tue':1, 'wed':2, 'thu':3, 'fri':4}
poutcome_mapping = {'failure':0, 'nonexistent':1, 'success':2}

if submit_button:
    input_data = pd.DataFrame({
        'age': [age],
        'job': [job_mapping[job]],
        'marital': [marital_mapping[marital]],
        'education': [education_mapping[education]],
        'default': [binary_mapping[default]],
        'housing': [binary_mapping[housing]],
        'loan': [binary_mapping[loan]],
        'contact': [contact_mapping[contact]],
        'month': [month_mapping[month]],
        'day_of_week': [day_mapping[day_of_week]],
        'duration': [duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous],
        'poutcome': [poutcome_mapping[poutcome]],
        'emp.var.rate': [emp_var_rate],
        'cons.price.idx': [cons_price_idx],
        'cons.conf.idx': [cons_conf_idx],
        'euribor3m': [euribor3m],
        'nr.employed': [nr_employed]
        
    })

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.success(f"The client is likely to SUBSCRIBE. (Probability: {probability:.2f})")
    else:
        st.error(f"The client is NOT likely to subscribe. (Probability: {probability:.2f})")