FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install --upgrade pip && pip3 install -r ./requirements.txt --no-cache-dir
COPY test_task/ /app
ENV STRIPE_PUBLISHABLE_KEY pk_test_51LiiJdDhJMg7BOrbVwloJs1sPKRs7gBd31Gi102oR4xtHzWzjH2st17cQIi33roCGd8YUcOQ2135Fjqx4HytPsn800Nyztne3d
ENV STRIPE_SECRET_KEY sk_test_51LiiJdDhJMg7BOrbmqofmL2ksTmWlarnkVBwbGjnfytFCiFiV9uKTIEvz0cdCM35zVAMEuoYSVRil0cILjGA6kKP00zpcEQvN5
ENV STRIPE_PUBLIC_API_KEY pk_test_51LiiJdDhJMg7BOrbVwloJs1sPKRs7gBd31Gi102oR4xtHzWzjH2st17cQIi33roCGd8YUcOQ2135Fjqx4HytPsn800Nyztne3d
ENV STRIPE_SECRET_API_KEY sk_test_51LiiJdDhJMg7BOrbmqofmL2ksTmWlarnkVBwbGjnfytFCiFiV9uKTIEvz0cdCM35zVAMEuoYSVRil0cILjGA6kKP00zpcEQvN5
CMD ["python3", "manage.py", "runserver", "0:8000"]