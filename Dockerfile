ARG INTERNAL_GATEWAY_ARG
ARG EXTERNAL_GATEWAY_ARG
ARG PING_COUNT_ARG
ARG INTERFACE_LAN_ARG
ARG INTERFACE_WIFI_ARG
ARG WIFI_SSID_ARG
ARG WIFI_BAND_ARG
ARG WIFI_PASSWORD_ARG

FROM python:3.12.3-alpine
WORKDIR /app
COPY . /app/
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create .env file
RUN echo "INTERNAL_GATEWAY=$INTERNAL_GATEWAY_ARG" >> .env
RUN echo "EXTERNAL_GATEWAY=$EXTERNAL_GATEWAY_ARG" >> .env
RUN echo "PING_COUNT=$PING_COUNT_ARG" >> .env
RUN echo "INTERFACE_LAN=$INTERFACE_LAN_ARG" >> .env
RUN echo "INTERFACE_WIFI=$INTERFACE_WIFI_ARG" >> .env
RUN echo "WIFI_SSID=$WIFI_SSID_ARG" >> .env
RUN echo "WIFI_BAND=$WIFI_BAND_ARG" >> .env
RUN echo "WIFI_PASSWORD=$WIFI_PASSWORD_ARG" >> .env

EXPOSE 4000
CMD ["python", "main.py"]
