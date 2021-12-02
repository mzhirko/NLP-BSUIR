# Streamlit NMT + POS

*!!is not fully done yet!!*

NMT using large BART model + POS tagging using NLTK.

Download pre-treined model locally to accelerate processing.

*Links to the useful info:*

- [NLTK;](https://www.nltk.org/)
- [mBART;](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)

## Run w/o Docker

```bash
streamlit run app.py 
```

## Run w Docker

```bash
docker build -t imstupidassbastard .
docker run -p 8501:8501 imstupidassbastard:latest
```
## Demo image

![NMT and POS demo](images/demo.png)