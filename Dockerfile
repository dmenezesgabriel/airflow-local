# pull official base image
FROM python:3.8.2-slim-buster

# Set envrionment variables
ENV AIRFLOW_HOME=/opt/airflow
# Python version
ENV PYTHON_VERSION=3.8
# Airflow Version
ENV AIRFLOW_VERSION=2.0.1
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONBUFFERED 1
# Define python Language
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install system dependencies
RUN apt-get install -y --no-install-recommends \
        freetds-bin \
        krb5-user \
        ldap-utils \
        libffi6 \
        libsasl2-2 \
        libsasl2-modules \
        libssl1.1 \
        locales  \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc

# Install Airflow with the correct version of it's dependencies
RUN pip install apache-airflow --constraint https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt
