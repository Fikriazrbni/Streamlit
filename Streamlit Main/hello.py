import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
c = pd.read_csv(url)

st.title("Streamlit Project")
st.write("### Data Head")
st.dataframe(c.head(), use_container_width=True)

region_counts = c["Region"].value_counts()
st.write("### Counts of Region")
st.dataframe(region_counts, use_container_width=True)

st.write("### Showing Detail Region")
x = st.text_input("Input Region ...")
st.write(f"#### Showing detail of region  _{x}_")

detail_region = c[c['Region'] == x]

st.dataframe(detail_region, use_container_width=True)

#creating plot pie chart
st.write("### Region Distribution Chart")
explode = [0.1 if detail_region == x else 0 for detail_region in region_counts.index]

fig = plt.figure(figsize=(15, 7))
plt.pie(region_counts, labels=region_counts.index, autopct='1%.1f%%', startangle=140, colors=plt.cm.Paired.colors, explode= explode, shadow= True)
plt.title("Region Distribution")
st.pyplot(fig)
