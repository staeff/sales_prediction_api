FROM python:3-slim
# set a directory for the app
WORKDIR /app
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy all the files to the container
COPY . .
# tell the port number the container should expose
EXPOSE 8080
# replace APP_NAME with module name
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "app:app"]
