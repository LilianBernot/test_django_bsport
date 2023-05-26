FROM python:3.11-slim AS base

EXPOSE 8000 8000

RUN export PIPENV_VENV_IN_PROJECT=1
RUN mkdir /var/tmp/django-cache

ADD ./Pipfile /app/
ADD ./Pipfile.lock /app/

WORKDIR /app

RUN apt -qq update
ARG BUILDPLATFORM

# install gdal and uwsgi deps
RUN apt -qq install -y  \
		libc6-dev \
		gdal-bin\
		build-essential \
		python3-setuptools \
		python3-wheel \
		python3-cffi \
		libffi-dev \
		libpq-dev \
		shared-mime-info \
		gettext \
		python3-dev \
		git \
		postgresql-client \
		postgis && \
	pip install -q pipenv

RUN pipenv install --ignore-pipfile --system --deploy --dev

RUN pip install psycopg2

RUN rm -rf /var/lib/apt/lists/* && \
	rm -rf $PIPENV_CACHE_DIR && \
	apt-get remove -y gcc libc6-dev python3-dev && \
	apt-get autoremove -y && \
	pip uninstall pipenv -y

COPY . /app

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
