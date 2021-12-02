FROM python:3.8
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN  pip install -r /app/requirements.txt
RUN  python -m spacy download en_core_web_sm
EXPOSE 8501

COPY . /app/
ENTRYPOINT ["streamlit", "run"]

CMD ["summarization_example.py"]
