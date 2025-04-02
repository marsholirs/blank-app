import streamlit as st
import pandas as pd
import random
import base64
colnames=['cards','meanings','reverse_meanings']
cards=pd.read_csv("tarot.csv",names=colnames)
options = ["One card", "Three cards"]
selection = st.pills("Type of reading", options, selection_mode="single")

file_ = open("Untitled_Artwork.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)


if selection=="One card":
    if st.button("Get tarot reading"):
        num=random.randint(0,21)
        rev=random.randint(0,1)
        card=cards.at[num,'cards']
        mean=cards.at[num,'meanings']
        rev_mean=cards.at[num,'reverse_meanings']
        st.title(card)
        if rev==1:
            st.write("This card indicates",mean,"in your life.")
        else:
            st.write("This card in reverse indictates",rev_mean,"in your life.")

if selection=="Three cards":
    if st.button("Get tarot reading"):
        num1=random.randint(0,21)
        num2=random.randint(0,21)
        num3=random.randint(0,21)
        while num1==num2 or num2==num3:
            num2=random.randint(0,21)
        while num1==num3 or num2==num3:
            num3=random.randint(0,21)
        st.write(num1,num2,num3)
        rev=random.randint(0,1)
        card=cards.at[num1,'cards']
        mean=cards.at[num1,'meanings']
        rev_mean=cards.at[num1,'reverse_meanings']
        st.title(card)
        if rev==1:
            st.write("This card indicates",mean,"in your past.")
        else:
            st.write("This card in reverse indictates",rev_mean,"in your past.")
        
        rev=rev=random.randint(0,1)
        card2=cards.at[num2,'cards']
        mean2=cards.at[num2,'meanings']
        rev_mean2=cards.at[num2,'reverse_meanings']
        st.title(card2)
        if rev==1:
            st.write("This card indicates",mean2,"in your present.")
        else:
            st.write("This card in reverse indictates",rev_mean2,"in your present.")

        rev=random.randint(0,1)
        card3=cards.at[num3,'cards']
        mean3=cards.at[num3,'meanings']
        rev_mean3=cards.at[num3,'reverse_meanings']
        st.title(card3)
        if rev==1:
            st.write("This card indicates",mean3,"in your future.")
        else:
            st.write("This card in reverse indictates",rev_mean3,"in your future.")