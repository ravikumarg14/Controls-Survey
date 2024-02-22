import calendar  # Core Python Module
import datetime  # Core Python Module
import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
# from streamlit_option_menu import option_menu  # pip install streamlit-option-menu

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
# selected = option_menu(
#     menu_title=None,
#     options=["Data Entry", "Data Visualization"],
#     icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
#     orientation="horizontal",
# )

# --- INPUT & SAVE PERIODS ---
# if selected == "Data Entry":
# st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
    
    projectName=st.text_input("Project Name:", key="projectName")
    demodate = st.date_input("Demonstration Date: ", key="demodate")
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


# --- PLOT PERIODS ---
# if selected == "Data Visualization":
# st.header("Data Visualization")
# with st.form("saved_periods"):
#     period = st.selectbox("Select Period:", get_all_periods())
#     submitted = st.form_submit_button("Plot Period")
#     if submitted:
#         # Get data from database
#         period_data = db.get_period(period)
#         comment = period_data.get("comment")
#         expenses = period_data.get("expenses")
#         incomes = period_data.get("incomes")

#         # Create metrics
#         total_income = sum(incomes.values())
#         total_expense = sum(expenses.values())
#         remaining_budget = total_income - total_expense
#         col1, col2, col3 = st.columns(3)
#         col1.metric("Total Income", f"{total_income} {currency}")
#         col2.metric("Total Expense", f"{total_expense} {currency}")
#         col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
#         st.text(f"Comment: {comment}")

#         # Create sankey chart
#         label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
#         source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
#         target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
#         value = list(incomes.values()) + list(expenses.values())

#         # Data to dict, dict to sankey
#         link = dict(source=source, target=target, value=value)
#         node = dict(label=label, pad=20, thickness=30, color="#E694FF")
#         data = go.Sankey(link=link, node=node)

#         # Plot it!
#         fig = go.Figure(data)
#         fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
#         st.plotly_chart(fig, use_container_width=True)