import streamlit as st
import spacy
from spacy import displacy

import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article
st.title("Named Entity Recognition")
links=st.text_input("Enter URL :")
compose=st.text_area("else, compose a paragraph :")
if st.button("check"):
   if (links):
      article=Article(links)
      article.download()
      article.parse()
      doc=nlp(article.text)
      ent_html=displacy.render(doc,jupyter=False,style='ent')
      st.markdown(ent_html, unsafe_allow_html=True)
   elif (compose):
      doc=nlp(compose)
      ent_html=displacy.render(doc,jupyter=False,style='ent')
      st.markdown(ent_html, unsafe_allow_html=True)
   
