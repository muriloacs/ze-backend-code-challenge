FROM python:3.8.3-alpine
    RUN apk --update add git postgresql-client py3-virtualenv
    ENV PYTHONUNBUFFERED 1
    ENV CLEAR_CACHE 0
    ENV VIRTUAL_ENV=/venv
    ENV PATH="$VIRTUAL_ENV/bin:$PATH"

    # Install dependencies in a virtualenv
    # Should you use virtual env in docker: https://vsupalov.com/virtualenv-in-docker/
    # Elegantly activating a virtualenv in a Dockerfile: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
    COPY requirements.txt code/
    RUN pip install --no-cache-dir --upgrade pip
    RUN pip install --no-cache-dir setuptools --upgrade
    RUN pip install --no-cache-dir -r code/requirements.txt

    # Create user and group
    RUN addgroup --gid 1000 ze-backend
    RUN adduser --uid 1000 --ingroup ze-backend --shell /bin/bash --home "$(pwd)" --disabled-password ze-backend
    COPY --chown=ze-backend:ze-backend . /code/
    WORKDIR /code
    USER ze-backend

    # Run application (remove it later)
    CMD ["python", "manage.py", "runserver", "0:8000"]
