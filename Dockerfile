FROM python:3.12.3
RUN apt-get update && apt-get install -y libgl1-mesa-glx
WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*
EXPOSE 4000

CMD ["python", "main.py"]