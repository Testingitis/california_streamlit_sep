import numpy as np
import joblib
import streamlit as st
obj = joblib.load ('california.joblib')
model= obj['model']
cols=obj['columns']

st.title ('California app')
In=[]
for i in cols:
    v=st.number_input(f'Enter{i}values:')
    In.append(v)
if st.button('click'):
  
    out = model.predict([In])
    st.success(f'The median is {out}')
