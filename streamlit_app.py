import streamlit as st
import pandas as pd
import random
import base64
with open( "font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
with open( "colour.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)      
st.markdown("""
<style>
   h1 {
      font-size: 12px;
      text-transform: uppercase;
   }
</style>
""", unsafe_allow_html=True)              
colnames=['cards','meanings','reverse_meanings']
cards=pd.read_csv("tarot.csv",names=colnames)
options = ["One card", "Three cards"]
selection = st.pills("Type of reading", options, selection_mode="single")

num=random.randint(0,21)
if num==0:
    file_ = open("the fool.gif", "rb")
elif num==1:
    file_ = open("the magician .gif", "rb")
elif num==2:
    file_ = open("the high priestess .gif", "rb")
elif num==3:
    file_ = open("the empress.gif", "rb")
elif num==4:
    file_ = open("the emperor.gif", "rb")
elif num==5:
    file_ = open("the hierophant.gif", "rb")
elif num==6:
    file_ = open("the lovers.gif", "rb")
elif num==7:
    file_ = open("the chariot.gif", "rb")
elif num==8:
    file_ = open("strength.gif", "rb")
elif num==9:
    file_ = open("the hermit.gif", "rb")
elif num==10:
    file_ = open("the wheel of fate.gif", "rb")
elif num==11:
    file_ = open("justice.gif", "rb")       
elif num==12:
    file_ = open("the hanged man.gif", "rb")
elif num==13:
    file_ = open("death.gif", "rb")
elif num==14:
    file_ = open("temperance .gif", "rb")
elif num==15:
    file_ = open("the devil.gif", "rb")
elif num==16:
    file_ = open("the tower.gif", "rb")
elif num==17:
    file_ = open("the star.gif", "rb")
elif num==18:
    file_ = open("the moon.gif", "rb")
elif num==19:
    file_ = open("the sun.gif", "rb")
elif num==20:
    file_ = open("judgment .gif", "rb")
elif num==21:
    file_ = open("the world.gif", "rb")

if selection=="One card":
    if st.button("Get tarot reading"):
        rev=random.randint(0,1)
        card=cards.at[num,'cards']
        mean=cards.at[num,'meanings']
        rev_mean=cards.at[num,'reverse_meanings']
        st.title(card)
        if rev==1:
            st.write("This card indicates",mean,"in your life.")
        else:
            st.write("This card in reverse indictates",rev_mean,"in your life.")
        
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )
        
if selection=="Three cards":
    if st.button("Get tarot reading"):
        num2=random.randint(0,21)
        num3=random.randint(0,21)
        while num==num2 or num2==num3:
            num2=random.randint(0,21)
        while num==num3 or num2==num3:
            num3=random.randint(0,21)
        st.write(num,num2,num3)
        rev=random.randint(0,1)
        card=cards.at[num,'cards']
        mean=cards.at[num,'meanings']
        rev_mean=cards.at[num,'reverse_meanings']
        st.title("Your past")
        if rev==1:
            st.write(card)
            st.write("this card indicates",mean,"in your past.")
        else:
            st.write(card,"reversed")
            st.write("this card in reverse indictates",rev_mean,"in your past.")
        
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )

        rev=rev=random.randint(0,1)
        card2=cards.at[num2,'cards']
        mean2=cards.at[num2,'meanings']
        rev_mean2=cards.at[num2,'reverse_meanings']
        st.title("Your Present")
        if rev==1:
            st.write(card2)
            st.write("this card indicates",mean2,"in your present.")
        else:
            st.write(card2,"reversed")
            st.write("this card in reverse indictates",rev_mean2,"in your present.")
        
        if num2==0:
            file_ = open("the fool.gif", "rb")
        elif num2==1:
            file_ = open("the magician .gif", "rb")
        elif num2==2:
            file_ = open("the high priestess .gif", "rb")
        elif num2==3:
            file_ = open("the empress.gif", "rb")
        elif num2==4:
            file_ = open("the emperor.gif", "rb")
        elif num2==5:
            file_ = open("the hierophant.gif", "rb")
        elif num2==6:
            file_ = open("the lovers.gif", "rb")
        elif num2==7:
            file_ = open("the chariot.gif", "rb")
        elif num2==8:
            file_ = open("strength.gif", "rb")
        elif num2==9:
            file_ = open("the hermit.gif", "rb")
        elif num2==10:
            file_ = open("the wheel of fate.gif", "rb")
        elif num2==11:
            file_ = open("justice.gif", "rb")       
        elif num2==12:
            file_ = open("the hanged man.gif", "rb")
        elif num2==13:
            file_ = open("death.gif", "rb")
        elif num2==14:
            file_ = open("temperance .gif", "rb")
        elif num2==15:
            file_ = open("the devil.gif", "rb")
        elif num2==16:
            file_ = open("the tower.gif", "rb")
        elif num2==17:
            file_ = open("the star.gif", "rb")
        elif num2==18:
            file_ = open("the moon.gif", "rb")
        elif num2==19:
            file_ = open("the sun.gif", "rb")
        elif num2==20:
            file_ = open("judgment .gif", "rb")
        elif num2==21:
            file_ = open("the world.gif", "rb")

        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )

        rev=random.randint(0,1)
        card3=cards.at[num3,'cards']
        mean3=cards.at[num3,'meanings']
        rev_mean3=cards.at[num3,'reverse_meanings']
        st.title("Your future")
        if rev==1:
            st.write(card3.capitalize())
            st.write("this card indicates",mean3,"in your future.")
        else:
            st.write(card3,"reversed")
            st.write("this card in reverse indictates",rev_mean3,"in your future.")

        if num3==0:
            file_ = open("the fool.gif", "rb")
        elif num3==1:
            file_ = open("the magician .gif", "rb")
        elif num3==2:
            file_ = open("the high priestess .gif", "rb")
        elif num3==3:
            file_ = open("the empress.gif", "rb")
        elif num3==4:
            file_ = open("the emperor.gif", "rb")
        elif num3==5:
            file_ = open("the hierophant.gif", "rb")
        elif num3==6:
            file_ = open("the lovers.gif", "rb")
        elif num3==7:
            file_ = open("the chariot.gif", "rb")
        elif num3==8:
            file_ = open("strength.gif", "rb")
        elif num3==9:
            file_ = open("the hermit.gif", "rb")
        elif num3==10:
            file_ = open("the wheel of fate.gif", "rb")
        elif num3==11:
            file_ = open("justice.gif", "rb")       
        elif num3==12:
            file_ = open("the hanged man.gif", "rb")
        elif num3==13:
            file_ = open("death.gif", "rb")
        elif num3==14:
            file_ = open("temperance .gif", "rb")
        elif num3==15:
            file_ = open("the devil.gif", "rb")
        elif num3==16:
            file_ = open("the tower.gif", "rb")
        elif num3==17:
            file_ = open("the star.gif", "rb")
        elif num3==18:
            file_ = open("the moon.gif", "rb")
        elif num3==19:
            file_ = open("the sun.gif", "rb")
        elif num3==20:
            file_ = open("judgment .gif", "rb")
        elif num3==21:
            file_ = open("the world.gif", "rb")

        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True,
        )