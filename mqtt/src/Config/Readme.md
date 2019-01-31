# Configuration Files

There are three configuration files: 

    - config.json holds the start up configuration details
    - resources.json holds the deployable resources details
    - sensor.json holds sensor details


### Config

#### Details

| Details     | Description  |
| ----------- |:-------------:|
| uuid        | Id to unqiuely identify each pi |
| host        | broker host |

| Broker Details     | Description  |
| ----------- |:-------------:|
| port        | broker port |
| username    | broker username (OPTIONAL) |
| password    | broker password (OPTIONAL) |

| Sensor Details     | Description  |
| ----------- |:-------------:|
| resources   | absolute path to resources folder |
| sensors     | absolute path to sensor startup script |

#### Format

```
{
    "uuid" :
    "broker" : {
        "host"
        "port"
        "username"
        "password"
    },
    "paths":{
        "resources"
        "sesnors
    }

}
```


