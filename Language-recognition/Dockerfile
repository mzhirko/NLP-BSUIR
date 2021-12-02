FROM tensorflow/tensorflow:2.1.0-py3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update 
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y
RUN apt-get install -y x11-apps
RUN apt-get install -y libqt5gui5 && \
    rm -rf /var/lib/apt/lists/*
ENV QT_DEBUG_PLUGINS=1
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip
RUN pip3 install --user pyqt5
RUN [ "python3", "-c", "import nltk; nltk.download('stopwords')" ]
RUN [ "python3", "-c", "import nltk; nltk.download('punkt')" ]
RUN cp -r /root/nltk_data /usr/local/share/nltk_data

COPY . /app/

CMD [ "python", "./language_recognition.py" ] 
