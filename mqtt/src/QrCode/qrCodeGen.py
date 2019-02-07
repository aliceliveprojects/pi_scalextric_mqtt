import qrcode
import qrcode.image.svg
import json
import urllib
import argparse


# Define Command Line Arguments
parser = argparse.ArgumentParser(description='Generates url qr code containing single page web app domain and broker details')
parser.add_argument('config',help='path to the config.json file')
parser.add_argument('host',help='host of the single page web app')
parser.add_argument('--filename',nargs=1,help='file name of the qr code image')
parser.add_argument('--websocket', action='store_true',  help='uses the websocket port instead')
parser.add_argument('--ssl',action='store_true',help='uses ssl for websocket port')


args = parser.parse_args()



def main():
    DEFAULTFILENAME = 'QrCode'
    host = args.host
    config = None


    # Read config details from config.json file
    with open(args.config) as json_data:
        config = json.load(json_data)
        
    # Check config contains the correct details
    if('uuid' not in config):
        raise KeyError('uuid was not found in config')

    if('host' not in config['broker']):
        raise KeyError('broker host was not found in config')

    if(args.websocket):
        if('websocketPort' not in config['broker']):
            raise KeyError('broker websocketPort for was not found in config')
    elif('port' not in config['broker']):
        raise KeyError('boker port was not found in config')

    


    urlParams = config['broker']
    urlParams['uuid'] = config['uuid']

    # pick which port to use
    portKey = 'port'
    if(args.websocket):
        portKey = 'websocketPort'

    # remove ssl argument if not chosen
    if not (args.ssl):
        urlParams.pop('ssl',None)

    # Rename keys for url paramaters
    urlParams['brokerHost'] = urlParams.pop('host')
    urlParams['brokerPort'] = urlParams.pop(portKey)

    # Params url encoded
    encodedUrlParams = urllib.urlencode(urlParams)

    # Final Url 
    url = "{}?{}".format(host,encodedUrlParams)



    # Generate Qr Code
    qr = qrcode.QRCode(
        version= 5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_colour="white")

    # Save Qr Code Image
    fileName = "{}.{}".format(DEFAULTFILENAME,'png')
    if(args.filename != None):
        fileName = args.filename

    img.save(fileName)


if __name__=='__main__':
    main()


