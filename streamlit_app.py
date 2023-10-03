import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.header('st.write')

# example 1
"### Display Text"
st.write('Hello, *world!* :sunglasses:')

# example 2
"""
### Display Numbers
"""
st.write(1234)

# example 3
"""
### Display DataFrame
"""
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

st.write(df)

# example 4
"### Accept multiple arguments"
st.write('below is a DataFrame', df, 'Above is a DataFrame')

# example 5
"### Display Charts"
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c']
)

st.write(c)