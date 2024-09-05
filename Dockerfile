FROM python:3.12.3-alpine
WORKDIR /app
COPY . /app/
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN apt-get install iperf3

EXPOSE 4000

CMD ["python", "main.py"]