FROM python:3.7

COPY ./api /api

WORKDIR /api

RUN pip install -r requirements.txt

ENV MODEL_PATH=models/model.joblib

EXPOSE 80

ENTRYPOINT ["uvicorn"]

CMD ["main:app", "--host", "0.0.0.0", "--port", "80"]
