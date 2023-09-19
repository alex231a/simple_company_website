import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.header("The Best Company")
content = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rhoncus turpis augue, ac maximus odio vulputate et. 
    Nulla facilisi. Vestibulum eu tincidunt sapien. Duis leo nulla, feugiat a tortor auctor, aliquam aliquet arcu. 
    Curabitur auctor est id nisl mattis, eu maximus lacus porttitor. Proin eleifend at magna nec suscipit. 
    Nullam eleifend malesuada ex. Ut pharetra, nibh et tristique hendrerit, purus tortor gravida quam, 
    eu aliquam felis dui eget neque. Vestibulum mollis porttitor justo a feugiat. Phasellus quam turpis, condimentum 
    sit amet elit eu, vehicula porta nisi. Aenean tempor feugiat massa non sodales. Pellentesque porttitor, massa 
    in ullamcorper tristique, diam justo posuere nibh, id tincidunt odio felis sed augue. Proin dapibus pulvinar erat 
    vel dignissim. Aliquam semper, lectus a dapibus accumsan, mauris nulla molestie orci, sit amet ullamcorper quam 
    tellus sit amet purus. Aenean fermentum, sem quis sodales tristique, elit nibh convallis mauris, id sollicitudin 
    est lacus et elit.
"""
st.write(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv", ",")

with col1:
    for index, row in df[:4].iterrows():
        full_name = str(f"{row['first name']} {row['last name']}").title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        full_name = str(f"{row['first name']} {row['last name']}").title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        full_name = str(f"{row['first name']} {row['last name']}").title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image(f"images/{row['image']}")
