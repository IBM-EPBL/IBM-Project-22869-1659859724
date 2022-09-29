import time
import Adafruit_DHT
from Adafruit_IO import Client, Feed
DHT_READ_TIMEOUT = 5
DHT_DATA_PIN = 26
ADAFRUIT_IO_KEY = 'YOUR_AIO_KEY'
ADAFRUIT_IO_USERNAME = 'YOUR_AIO_USERNAME'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidity')
dht22_sensor = Adafruit_DHT.DHT22
while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, DHT_DATA_PIN)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
        temperature = '%.2f'%(temperature)
        humidity = '%.2f'%(humidity)
        aio.send(temperature_feed.key, str(temperature))
        aio.send(humidity_feed.key, str(humidity))
    else:
        print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
    time.sleep(DHT_READ_TIMEOUT)
