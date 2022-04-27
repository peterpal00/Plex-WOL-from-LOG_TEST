# For more information, please refer to https://aka.ms/vscode-docker-python

FROM python:3.9.12-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

ENV PLEX_PATH=${PLEX_PATH}
ENV PART_OF_LOG_PATH=${PART_OF_LOG_PATH}
ENV LOG_FILE_NAME=${LOG_FILE_NAME}
ENV MAC_ADDRESS=${MAC_ADDRES}
ENV IP_ADDRESS=${IP_ADDRES}

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

VOLUME /logfile

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT [ "python", "Plex-WOL-from-LOG/Plex_WOL_from_LOG.py" ]
# CMD ["python", "Plex-WOL-from-LOG/Plex_WOL_from_LOG.py"]
