FROM python:3.7
COPY . /app
WORKDIR /app
EXPOSE 8050
RUN pip install -r requirements.txt
CMD ["python","server.py"]