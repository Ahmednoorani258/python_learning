# import streamlit as st

# st.title('Counter Example')
# count = 0

# increment = st.button('Increment')
# if increment:
#     count += 1

# st.write('Count = ', count)

# ----------------------------------------------------

# import streamlit as st

# st.title('Counter Example')

# st.write(st.session_state)

# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment = st.button('Increment')
# if increment:
#     st.session_state.count += 1

# st.write('Count = ', st.session_state.count)
# # del st.session_state.count
# "Text" , st.session_state.count

# ----------------------------------------------------

# import streamlit as st

# st.title('Counter Example using Callbacks')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter():
#     st.session_state.count += 1

# st.button('Increment', on_click=increment_counter)

# st.button('Increment logic1', on_click=increment_counter)

# st.button('Increment logic2', on_click=increment_counter)

# st.write('Count = ', st.session_state.count)

# ----------------------------------------------------

import streamlit as st

st.title('Counter Example using Callbacks with args')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('Enter a value', value=1, step=5)

def increment_counter(increment_value):
    st.session_state.count += increment_value

increment = st.button('Increment', on_click=increment_counter,
    args=(increment_value, ))

st.write('Count = ', st.session_state.count)