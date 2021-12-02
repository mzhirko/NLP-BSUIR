import streamlit as st
from htbuilder import div, styles
from htbuilder.units import px
from sentence_transformers import SentenceTransformer
from summarizer.sbert import SBertSummarizer
# from keybert import KeyBERT
from wordwise import Extractor
import pandas as pd
import base64

from annotation_helper import annotate

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
COLORS = ["#8ef", "#faa", "#afa", "#fea"]

def download_link(object_to_download, download_filename, download_link_text):
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

st.set_page_config(layout="wide")
st.title("Interactive Summarization")
st.markdown(
"""
Text processing
"""
)

uploaded_file = st.file_uploader('Article to process',type=['txt'])
if uploaded_file is not None:
    if uploaded_file.name[-3:] == 'txt':
        ARTICLE = uploaded_file.read().decode('utf-8')
else:
    with open("summarization_sample.txt", "r") as f:
        ARTICLE = f.read()

st.sidebar.title("Configuration")
st.sidebar.subheader(
"""
Summarization Options
"""
)

process_keywords = st.sidebar.checkbox("Process Keywords", value=False)

input_col, result_col = st.columns(2)

input_col.header("Enter text to analyze")
text = input_col.text_area("", ARTICLE, height=400)
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
summary = model(text)

result_col.header("Summary")
result_col.subheader("")
if st.button(label='Submit'):
    result_col.write(HTML_WRAPPER.format(summary), unsafe_allow_html=True)

if result_col.button('Download output as a text file'):
    tmp_download_link = download_link(summary, 'SUMMARY.txt', 'Click here to download your summary!')
    st.markdown(tmp_download_link, unsafe_allow_html=True)


if process_keywords:
    st.sidebar.subheader(
        """
        Keyword Options
        """
    )

    keywords_amount = st.sidebar.slider('Keywords Amount', min_value=1, max_value=20, value=3)

    extractor = Extractor()
    kw = extractor.generate(text, keywords_amount)

#    That one model takes lesser space :)
#    kw_model = KeyBERT()
#    kw = kw_model.extract_keywords(text, diversity=diversity)

    if kw:
        result_col.header("Keywords")
        kw_expander = result_col.expander("Expand keywords!")
        if kw_expander:
            kw_expander.write(HTML_WRAPPER.format(kw), unsafe_allow_html=True)
