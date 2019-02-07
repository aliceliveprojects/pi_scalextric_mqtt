# Qr Code Generation
Generates a qr code containing single page web app and broker details.

## Qr Code Details

### Command Line Arguments

Positional Arguments

| Arguments     | Description  |
| ------------- |:-------------:|
| config        | path to the config.json file |
| host          | host of the single page web app|

Optional Arguments

| Arguments     | Description |
| ------------- |:---------------:|
| --filename     | file name of the qr code image (OPTIONAL)|
| --websocket    | flag to use the websocket port (OPTIONAL)|
| --ssl    | flag to use the ssl on websocket port (OPTIONAL)|



To run : 

```python qrCodeGen.py [CONFIG] [HOST]```

For Help :

```python qrCodeGen.py -h```



