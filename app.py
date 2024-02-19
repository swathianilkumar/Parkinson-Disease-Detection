#import streamlit as st
#st.title('hello')

#import streamlit as st
#st.title('Facebook')

#user_name= st.text_input( 'Username')
#password=st.text_input('password')



import streamlit as st

st.title('Login Page')

user_id = st.text_input('User ID')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if user_id == 'your_username' and password == 'your_password':
        st.success('Login successful!')
    else:
        st.error('Invalid credentials. Please try again.')
