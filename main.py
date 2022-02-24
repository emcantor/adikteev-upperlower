from ast import IsNot, Str
import streamlit as st
import pandas as pd

#title
st.title('Case Fix')

#selection
os = st.selectbox('iOS or Android', ('iOS', 'Android'))

#File Uploader
upload_file = st.file_uploader('Upload File', '.csv')

global df
if upload_file is not None:
    try:
        df = pd.read_csv(upload_file)
        if os == 'iOS':
            df_new = df.iloc[:,0].str.upper()
        elif os == 'Android':
            df_new = df.iloc[:,0].str.lower()
    except:
        pass

try:
    st.write(df_new)
except:
    st.write('No File')

@st.cache
def download(df):
    return df.to_csv()

try:
    csv = download(df_new)
except:
    csv = 0

try:
    st.download_button(
        label='Download',
        data=csv,
        file_name=format(upload_file.name.replace('.csv', '_fixed.csv'))
    )
except:
    st.button('Download')
