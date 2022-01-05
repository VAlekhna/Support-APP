FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/support_app

COPY requirements.txt /usr/src/support_app
RUN pip install -r /usr/src/support_app/requirements.txt

COPY .. /usr/src/support_app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
