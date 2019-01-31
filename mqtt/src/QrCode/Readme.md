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
| --filname     | file name of the qr code image (OPTIONAL)|



To run : 

```python qrCodeGen.py [CONFIG] [HOST] --filename [FILENAME]```

For Help :

```python qrCodeGen.py -h```