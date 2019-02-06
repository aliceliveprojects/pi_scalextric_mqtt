# Configuration Files

There are three configuration files: 

- config.json holds the start up configuration details
- resources.json holds the deployable resources details
- sensor.json holds sensor details


## Config


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


```
{
    "uuid",
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

## Resources

| Details     | Description  |
| ----------- |:-------------:|
| id          | Id to uniquely identify each resource |
| name        | Resource name |
| imageUrl    | Url to resource image |
| systemResource | Which system resource, if any, does the resource use (OPTIONAL)|


*If the resource uses a system resource the resource name MUST match the resource script file, for example oil_slick ==> oil_slick.py*  


| Supported System Resources     | Description  |
| ----------- |:-------------:|
| throttle         | Effects the throttle |


```
[
    {
        "id",
        "name",
        "imageUrl",
        "systemResource"
    }
]
```

## Sensors
| Details     | Description  |
| ----------- |:-------------:|
| id          | Id to uniquely identify each sensor |
| name        | Sensor name |
| default_trigger    | Percentage to trigger a sensor event|


*The sensor name MUST match the sensor script file, for example light ==> light.py*  

```
[
    {
        "id",
        "name",
        "default_trigger"
    }
]
```


