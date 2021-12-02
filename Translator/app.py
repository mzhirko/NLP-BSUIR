from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import streamlit as st

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def download_model():
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50Tokenizer.from_pretrained(model_name)
    return model, tokenizer

uploaded_file = st.file_uploader('Article to process',type=['txt'])
if uploaded_file is not None:
    if uploaded_file.name[-3:] == 'txt':
        text = uploaded_file.read().decode('utf-8')
else:
    with open("sample.txt", "r") as f:
        text = f.read()

st.title('Russian to English Translator')
text = st.text_area("Enter Text:", value=text, height=None, max_chars=None, key=None)
model, tokenizer = download_model()


if st.button('Translate to English'):
    if text == '':
        st.write('Please enter Russian text for translation') 
    else: 
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "ru_RU"
        encoded_russian_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_russian_text, forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        translation = ' '.join(out)
        st.write(translation)
        

        tokens = nltk.word_tokenize(translation)
        cleaned_tokens= [token for token in tokens if token.isalnum()]
        tagged_sentence = nltk.pos_tag(cleaned_tokens)
        output = ''
        for tag in tagged_sentence:
            out = tag[0] + ' ---> ' + tag[1] + '<br>'
            output += out
        st.markdown(output, unsafe_allow_html=True)
        
else: pass