FROM python:3-slim
# set a directory for the app
WORKDIR /usr/src/app
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy all the files to the container
COPY . .
# tell the port number the container should expose
EXPOSE 5000
# run the command
CMD ["python", "./app.py"]
