FROM python:3.10-slim-buster

RUN groupadd -r nobody
WORKDIR /app    
COPY ./app /app
RUN pip3 install  --ignore-installed -r requirements.txt

COPY flag /
RUN chmod -R 747 /app
RUN chown -R root:nobody /flag
RUN chmod 444 /flag

USER nobody
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]