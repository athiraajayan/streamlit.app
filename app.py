import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
st.snow()


st.title("Athira Ajayan")

#Elevator Pitch. Your Branding
st.subheader("One day there won't be any FEMALE LEADERS, just leaders")
col1, col2= st.columns([3,1])
with col1:
    st.subheader("About Me")
    st.text("Passionate about the power of data to drive insights and\ninnovation, I bring a wealth of experience in \nProject Management and Change Management to the world \nof Data Science.")
with col2:
    image = Image.open('DSC_7660.JPG')
    st.image(image,width = 250)

#Sidebar w/ Download
st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: athiraajayan1998@gmail.com')
#rb means converting pdf file to raw binary format
pdf_file = open('RESUME.pdf', 'rb')
st.sidebar.download_button('Download Resume',pdf_file,file_name='RESUME.pdf',mime='pdf')

tab_skills,tab_exp,tab_cont,tab_pic = st.tabs(['skills','Experience','Projects','Contact me',"Take a picture"])
with tab_exp:
    #Experience
    st.subheader("Relevant Experience")
    experience_table = pd.DataFrame({
            "Job Title":["Estimation Engineer"],
            "Company":["Puthooppillil Builders"],
            "Job Description":["To estimate the cost and average time to finish a project."],
    })
    experience_table = experience_table.set_index('Job Title')
    st.table(experience_table)

with tab_cont:
    #Projects GRID
    st.subheader("Projects")
    titanic_data = pd.read_csv('titanic.csv')
    interval = alt.selection_interval()
    scatter = alt.Chart(titanic_data).mark_point().encode(
        x = 'Age',
        y = 'Fare',
        color=alt.condition(interval,'Sex', alt.value('lightgray'))
    ).add_selection(
        interval
        ).properties(
            width=300,height=200)

    bar = alt.Chart(titanic_data).mark_bar().encode(
        x='sum(Survived):Q',
        y='Pclass:N',
        color='Pclass:N',
        ).properties(
            width=300,
            height=200
        ).transform_filter(
            interval
        )
    st.altair_chart(scatter | bar)

with tab_skills:
    #Skills Section - In the form of a bar chart
    skill_data = pd.DataFrame(
        {
            "Skills Level":[90,60,60,40],
            "Skills":["Python","Taableau","MySQL","RStudio"]
        }
    )
    skill_data = skill_data.set_index("Skills")
    with st.container():
        st.subheader("Skills")
        st.bar_chart(skill_data)
        with st.expander("See More Skills"):
            st.write("Business Analysis, People Management, Communication, Adaptability, Team Spirit")

#Streamlit Form
form = st.form("my_form")
fullname = form.text_input(label = "Enter your full name",value='')
age = st.slider("Select your Age")
gender = st.radio("Select your gender",('Male','Female','Other'))
message = form.text_area(label="Your Message",value ='',height =100)
terms =st.checkbox("Accept terms and condition")
submit = form.form_submit_button(label="Submit")

#Handle form Submission
if submit:
    if terms:
        st.success("Form Completed: Thankyou for visiting")
    else:
        st.error("Please aacept the terms and conditions")
st.write("Name: ",fullname,"Age: ",age,"Gender: ",gender,"Message: ",message)

#Add a Map
## Create a dataframe with latitute and longitute
data = {
    'Location': ['Kitchner','Waterloo','Guelph','Cambridge'],
    'LAT':[43.451639,43.464258,43.5467,43.3616],
    'LON':[-80.492533,-80.520410,-80.2482,-80.3144]
}
df = pd.DataFrame(data)
st.map(df)
with tab_pic:
    # PIcture using Camera
        picture = st.camera_input("Take a picture with me")
        if picture:
            st.image(picture)