FROM python:3.7-alpine

#Creation of director
RUN mkdir /app

#set the working directory
WORKDIR /app

EXPOSE 80
#copy the dependencies file to the working directory
COPY requirements.txt .

#install dependencies
RUN pip3 install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/src"

EXPOSE 27017

#copy the content of the local src directory to the working directory
COPY src/ ./src

#command to run on container start
CMD ["python", "./src/cli.py"]
