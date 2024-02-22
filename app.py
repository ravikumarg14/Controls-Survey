import calendar  # Core Python Module
import datetime  # Core Python Module
import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
import pandas as pd
import database as db  # local import

# -------------- SETTINGS --------------

page_title = "Controls Software Demonstration – Survey"
page_icon = ":globe_with_meridians:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
demoTypes = ["Electrical" ,"GT","ST","PCS","Combined Cycle"]
attendeeTypes = ["EPC","End Customer"]


# --- DATABASE INTERFACE ---
# def get_all_periods():
#     items = db.fetch_all_periods()
#     periods = [item["key"] for item in items]
#     return periods


# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

# --- INPUT & SAVE PERIODS ---
if selected == "Data Entry":
# st.header(f"Data Entry in {currency}")
    with st.form("entry_form", clear_on_submit=True):
        
        projectName=st.text_input("Project Name:", key="projectName")
        demodate = st.date_input("Demonstration Date: ", key="demodate")
        demodate = str(demodate)
        location=st.text_input("Location",key="location")
        attendeeName=st.text_input("Attendee Name",key="attendeeName")
        attendeetype = st.selectbox("Select Attendee Type:", attendeeTypes,key="attendeetype")
        demoType = st.selectbox("Type of Demonstration:",demoTypes,key="demoType")
        st.header("Pre-Demonstration:")
        expectation= st.text_area("What are your expectations of this event? What are the 3 most important things to you?", placeholder="Enter your Expectation here ...")
        st.header("Post-Demonstration:")
        likes= st.text_area("What did you really like about this event?", placeholder="Enter your likes here ...")
        dislikes= st.text_area("What did you dislike? What would you change?", placeholder="Enter your dislikes here ...")
        satisfaction=st.slider("Overall, how satisfied are you with the quality and execution of this event?",min_value = 0,max_value=10,step=1)
        recommendation=st.slider("Based on your experience of this event, would you recommend a GE Control System to others? ",min_value = 0,max_value=10,step=1)
        
       
    
    
        
        
        # Demodate = st.date_input("Demonstration Date: ", value=None, min_value=None, max_value=None, key="Demodate", on_change=None, args=None, kwargs=None)
        # enddate = st.date_input("End Date", value=None, min_value=startdate, max_value=None, key=None, on_change=None, args=None, kwargs=None)
        "---"
        submitted = st.form_submit_button("Submit")
        if submitted:
            db.insert_period(projectName,demodate,location,attendeeName,attendeetype,demoType,expectation,likes,dislikes,satisfaction,recommendation)
            st.success("Thank you for taking time to provide some feedback.")
    

if selected == "Data Visualization":
    st.header("Data Visualization")
    df=pd.DataFrame(db.fetch_all_periods())
    finaldf=pd.DataFrame(columns=['Project Name', 'Demonstration Date', 'Location', 'Attendee Name','Attendee Type','Type of Demonstration','Expectations','Likes','Dislikes','Satisfaction','Recommendation'])        
    finaldf['Project Name']=df['projectName']
    finaldf['Demonstration Date']=df['demodate']
    finaldf['Location']=df['location']
    finaldf['Attendee Name']=df['attendeeName']
    finaldf['Attendee Type']=df['attendeetype']
    finaldf["Type of Demonstration"]=df['demoType']
    finaldf['Expectations']=df['expectation']
    finaldf['Likes']=df['likes']
    finaldf['Dislikes']=df['dislikes']
    finaldf['Satisfaction']=df['satisfaction']
    finaldf['Recommendation']=df['recommendation']
    st.dataframe(finaldf)
