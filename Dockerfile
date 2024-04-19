FROM python:3.12.3-alpine
WORKDIR /app
COPY . /app/

RUN apk add --no-cache gcc python3-dev musl-dev linux-headers networkmanager
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
EXPOSE 4000

CMD ["python", "main.py"]
