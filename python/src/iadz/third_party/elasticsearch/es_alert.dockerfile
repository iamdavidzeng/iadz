FROM platform-base:latest

WORKDIR /var/osl/

RUN . /appenv/bin/activate; \
    pip install requests

COPY search_and_alert.py /var/osl/search_and_alert.py

CMD . /appenv/bin/activate; python search_and_alert.py
