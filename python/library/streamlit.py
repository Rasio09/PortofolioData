import streamlit as st 
import pandas as pd

st.title('Belajar Analisis Data')

st.write(pd.DataFrame({ #untuk tampilan jenis data
    'c1': [1,2,3,4],
    'c2': [10,20,30,40], 
}))

st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')

st.markdown( #menampilklan format teks
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

# untuk menampilkan teks dengan ukuran kecil
st.caption('Copyright (c) 2023')

# penggunaan function code() untuk menampilkan potongan code
code = """def hello(): 
    print("Hello, Streamlit!")"""
st.code(code, language='python')

# menampilkan teks normal
st.text('ini adalah ukuran teks normal')

# untuk menampilkan rumus dengan function latex()
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")



# DATA DISPLAY

# dataframe()
df = pd.DataFrame({
    'c1': [1,2,3,4],
    'c2': [10,20,30,40],
})
st.dataframe(data=df, width=500, height=150)

# table()
st.table(data=df)

# metric()
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# data json
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# membuat chart 
# function pyplot()
import matplotlib.pyplot as plt
import numpy as np

x= np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

# basic widget dalam streamlit

# input widget
# text input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

# text area
text = st.text_area('Feedback')
st.write('Feedback: ', text)

# number input
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

# date input
import datetime
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

# file uploader
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# camera input
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)


# button widgets
# button
if st.button('Say hello'):
    st.write('Hello there')

# checkbox
agree = st.checkbox("pilih ya")
if agree:
    st.write("Pilihan sudah dipilih")

# radio button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)
if genre:
    st.write("Pilihan Anda : ", genre)

# select box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

# multiselect
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

if genre:
    st.write("Pilihan anda ini ", genre)

# slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
