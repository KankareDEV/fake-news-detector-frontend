FROM python:3.10-slim

WORKDIR /opt/program

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --default-timeout=100 --no-cache-dir -r requirements.txt

COPY inference.py .
COPY news_model.pkl .
COPY tfidf_vectorizer.pkl .

# Copy the serve script and make it executable
COPY serve /usr/local/bin/serve
RUN chmod +x /usr/local/bin/serve

EXPOSE 8080

ENTRYPOINT ["serve"]
CMD ["serve"]
