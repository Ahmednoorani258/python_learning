# https://docs.streamlit.io/library/api-reference/chat/st.chat_input

# import streamlit as st

# prompt = st.chat_input("Say something")

# if 'data' not in st.session_state:
#     st.session_state.data  = []

# if prompt:
#     st.session_state.data.append(prompt)
#     for text in st.session_state.data:
#         st.write(f"User has sent the following prompt: {text}")

# st.write(st.session_state.data)


# ________________________________________________________________


# https://docs.streamlit.io/library/api-reference/chat/st.chat_message

# import streamlit as st
# import numpy as np

# message = st.chat_message("assistant")
# message.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))

# message1 = st.chat_message("user")
# message1.write("Thanks")


# ________________________________________________________________

# import time
# import streamlit as st

# with st.status("Downloading data...", expanded=True) as status:
#     st.write("Searching for data...")
#     time.sleep(2)
#     st.write("Found URL.")
#     time.sleep(1)
#     st.write("Downloading data...")
#     time.sleep(1)
#     status.update(label="Download complete!", state="complete", expanded=False)

# st.button('Rerun')

# ________________________________________________________________