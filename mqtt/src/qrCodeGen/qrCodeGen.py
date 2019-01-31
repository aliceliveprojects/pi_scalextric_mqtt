import qrcode
import qrcode.image.svg
import json
import urllib

host = "https://aliceliveprojects.github.io/pi_scalextric_mqtt/spwa/src/index.html#!/index"


config = None


# Read config details from config.json file
with open('../config.json') as json_data:
    config = json.load(json_data)
    
# Check config contains the correct details
if('uuid' not in config):
    raise KeyError('uuid was not found in config')

if('host' not in config['broker']):
    raise KeyError('broker host was not found in config')

if('port' not in config['broker']):
    raise KeyError('boker port was not found in config')


urlParams = config['broker']
urlParams['uuid'] = config['uuid']

# Rename keys for url paramaters
urlParams['brokerHost'] = urlParams.pop('host')
urlParams['brokerPort'] = urlParams.pop('port')

encodedUrlParams = urllib.urlencode(urlParams)

url = "{}?{}".format(host,encodedUrlParams)

factory = qrcode.image.svg.SvgImage

qr = qrcode.QRCode(
    version= 5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size= 10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black",back_colour="white")
img.save("image.jpg")

