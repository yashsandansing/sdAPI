FROM python:3.10.6

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# RUN python -c "from bark import preload_models; import os; os.environ[' SUNO_USE_SMALL_MODELS'] = 'True'; preload_models()"

COPY ./app /code/app

EXPOSE 80

CMD ["uvicorn", "app.run:app", "--host", "0.0.0.0", "--port", "80"]