import streamlit as st
import pandas as pd
import base64


archivo = st.file_uploader('Csv Mañoso')

if archivo:
    df = pd.read_csv(archivo, sep = '\t', encoding = 'latin1')
    df['visible'] = df['visible'].apply(lambda x: str(x).upper())
    csv = df.to_csv(index=False, sep=',', encoding = 'latin1')
    b64 = base64.b64encode(csv.encode('latin1')).decode()
    st.markdown(f'<a href="data:file/csv;base64,{b64}" download="out.csv">Download csv file</a>', unsafe_allow_html=True)
