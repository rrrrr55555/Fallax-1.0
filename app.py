import streamlit as st
import matplotlib.pyplot as plt
import spacy
from spacy.lang.el.stop_words import STOP_WORDS
from wordcloud import WordCloud
from utils import get_page_text

st.set_page_config(page_title = "Fallax 1.0")

@st.cache(allow_output_mutation=True)
def get_nlp_model(path):
    return spacy.load(path)

def generate_output(text):
     cats = nlp(text).cats
     if cats['FAKE'] > cats['REAL']:
         st.markdown("<h1 style='text-align: center; color: black;font-family :Brush Script MT '>I Hereby declare thy news as:</h1>",unsafe_allow_html=True)
         st.markdown("<h2 style='text-align: center; color: red;font-family :Engravers MT'>Fake news :(</h2>",unsafe_allow_html=True)            
     else:
         st.markdown("<h1 style='text-align: center; color: black;font-family :Brush Script MT'> I Hereby declare thy news as:</h1>",unsafe_allow_html=True) 
         st.markdown("<h2 style='text-align: center; color: green;font-family :Engravers MT'>Real News :)</h2>",unsafe_allow_html=True)             

     q_text = '> '.join(text.splitlines(True))
     q_text = '> ' + q_text
     st.markdown(q_text)

     wc = WordCloud(width = 1000, height = 600,
                    random_state = 1, background_color = 'white',
                    stopwords = STOP_WORDS).generate(text)

     fig, ax = plt.subplots()
     ax.imshow(wc)
     ax.axis('off')
     st.pyplot(fig)
     print(cats)

nlp = get_nlp_model('model')



st.markdown("<h1 style='text-align: center; color: Black;font-family : Tw Cen MT Condensed'>🛡 FALLAX 1.0 🛡</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Green;font-family: Bahnschrift Condensed'>| A Covid-19 Fake News Detector |</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: Black; font-family : magneto'> Enter the news in the Box of Judgement\
                   .....and prepare for thy verdict : </h4>", unsafe_allow_html=True) 
st.markdown("")
st.markdown("")
text = st.text_area("Box of Judgement:", height=100)
if st.button("Run"):
     generate_output(text)

st.markdown("<br><br><hr><center>Made with ❤️ by <a href='https://rutvikk5.github.io/'><strong>Rutvikk kakde & Team</strong></a></center><hr>", unsafe_allow_html=True)
