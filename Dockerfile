FROM python:3.8.3-alpine
    RUN apk --update add git py3-virtualenv postgresql-client postgresql-dev gcc python3-dev musl-dev
    ENV PYTHONUNBUFFERED 1
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
    USER ze-backend
