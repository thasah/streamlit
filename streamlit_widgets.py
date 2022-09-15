import streamlit as st
import datetime
#___________________________________________________
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
#___________________________________________________
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
#___________________________________________________
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
#___________________________________________________
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

#___________________________________________________
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

#___________________________________________________
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

#___________________________________________________
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

#___________________________________________________
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)
