# Configuration Files

There are three configuration files: 

- config.json holds the start up configuration details
- resources.json holds the deployable resources details
- sensor.json holds sensor details


### Config

#### Details

| Details     | Description  |
| ----------- |:-------------:|
| uuid        | Id to uniquely identify each pi |


| Broker Details     | Description  |
| ----------- |:-------------:|
| host        | broker host |
| port        | broker port |
| username    | broker username (OPTIONAL) |
| password    | broker password (OPTIONAL) |

| Path Details     | Description  |
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


