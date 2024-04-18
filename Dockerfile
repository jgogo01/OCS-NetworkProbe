ARG INTERNAL_GATEWAY
ARG EXTERNAL_GATEWAY
ARG PING_COUNT
ARG INTERFACE_LAN
ARG INTERFACE_WIFI
ARG WIFI_SSID
ARG WIFI_BAND
ARG WIFI_PASSWORD

FROM python:3.12.3-alpine
WORKDIR /app
COPY . /app/
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create .env file
RUN echo "INTERNAL_GATEWAY=$INTERNAL_GATEWAY" >> .env
RUN echo "EXTERNAL_GATEWAY=$EXTERNAL_GATEWAY" >> .env
RUN echo "PING_COUNT=$PING_COUNT" >> .env
RUN echo "INTERFACE_LAN=$INTERFACE_LAN" >> .env
RUN echo "INTERFACE_WIFI=$INTERFACE_WIFI" >> .env
RUN echo "WIFI_SSID=$WIFI_SSID" >> .env
RUN echo "WIFI_BAND=$WIFI_BAND" >> .env
RUN echo "WIFI_PASSWORD=$WIFI_PASSWORD" >> .env

EXPOSE 4000
CMD ["python", "main.py"]
