import streamlit as st


st.title("Tittle -> Geeks for Geeks, Welcome to GeeksForGeeks")
st.header("Header -> Geeks for Geeks")
st.text("Text -> Geeks for Geeks")

st.markdown("# Hi")
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("#### Hi")
st.markdown("##### Hi")


st.success('Success!')
st.info('Information')
st.warning('Warning!')
st.error('Error!')


st.exception(ZeroDivisionError('Division not possible with 0'))
st.help(ZeroDivisionError)
st.write('range(1,10)')
st.write(range(1,10))

st.write('1+2+3')
st.write(1+2+3)
st.code('x=10 \n'
        'for i in range(x): \n'
        '    print(i)')

if(st.checkbox('Veg')):
    st.write("You should be strong!")
if(st.checkbox('Non Veg')):
    st.write("You should be smart!")

radioButton = st.radio('Select : ', ('Male', 'Female', 'Other'))
if(radioButton == 'Male'):
    st.write("Male!")
elif(radioButton == 'Female'):
    st.write("Female!")
elif(radioButton == 'Other'):
    st.write("Okay!")

st.subheader('Select Box')
selectBox = st.selectbox("Data Science : ", ['Data Analysis', 'Web scraping', 'Machine Learning', 'Deep Learning', 'Natural Language processing', 'Computer Vision', 'Image Processing'])
st.write("You've Selected :    ", selectBox)
mulSelBox = st.multiselect("Data Science : ", ['Data Analysis', 'Web scraping', 'Machine Learning', 'Deep Learning', 'Natural Language processing', 'Computer Vision', 'Image Processing'])
st.write("You've Selected :    ", len(mulSelBox), 'courses')
st.subheader("Button")
if(st.button("Click me")):
    st.write("Thanks for Clicking")

vol = st.slider("Select from 1 to 10", 1, 10, step = 1)
st.write("Volume is : ", vol)

st.subheader("Text Input")
name = st.text_input("Name :")
Password = st.text_input("Password", type = 'password')

st.header("Text Area")
textArea = st.text_area("Write Briefly")
st.write(textArea)

st.subheader("Input Number")
st.number_input("Select Your age", 18, 150)

st.subheader("Date Input")
st.date_input("Select your DOB : ")

st.subheader("Time Input")
st.time_input("Time : ")

