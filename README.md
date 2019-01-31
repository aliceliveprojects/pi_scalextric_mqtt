# pi_scalextric_mqtt

### Project Structure
- Check out the [mqtt](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt) folder if you want to setup a mqtt broker, python scripts or configuration files

- Check out the [node_red_flow](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/node_red_flow) folder for the node red flow



# Topic Structure

## {UUID}/control/game_state
Sets or gets the game state

### Subscribe
To retrieve game state

### Publish
To set game state

| Option      | Value  |
| ------------- |:-------------:|
| Retain   | True |


## {UUID}/control/pi_state
Sets or gets the pi state

### Subscribe
To retrieve pi state

**Format**

New state has been requested
```
{
  requested : [target_state]
}
```

State is in the process of execution
```
{
  requested : [state]
}
```


State is ready for a new request
```
{
  requested : [state]
}
```

### Publish
To set pi state

| Option      | Value  |
| ------------- |:-------------:|
| Retain   | True |

**Format**

```
{
  requested : [target_state]
}
```

## {UUID}/control/{channe}/throttle
Sets or gets the channel throttle

### Subscribe
To retrieve channel throttle

**Format**

```
[throttle]
```

### Publish
To Set channel throttle

**Format**

```
{
  set : [throttle]
}
```

## {UUID}/control/{channe}/event
In Progress...

## {UUID}/control/{channe}/{resourceId}/state
Sets or gets the resource state

### Subscribe 
To retrieve resource state

**Format**

Resource is deploying
```
{
  requested : [state]
}
```


Resource is ready for deployment
```
{
  requested : [state]
}
```

### Publishing
To deploy resource

**Format**

```
state : "Requested"
target : [CHANNEL_ID]
}
```


## {UUID}/control/{channe}/{resourceId}/count
Sets or gets the number of deployments left for a resource

### Subscribe
To retireve resource count

**Format**

```
count
```

### Publishing
To set resource count

| Option      | Value  |
| ------------- |:-------------:|
| Retain   | True |


**Format**

```
count
````

## {UUID}/sensors
To get sensor details

### Subscribe
To retireve all sensor details

**Format**

see https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Config#sensors

## {UUID}/resources
To get resource details

### Subscribe
To retrieve all resource details

**Format**

see https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Config#resources


## {UUID}/sensors/{sensorId}
Gets sensor events

### Subscribed
Notified when a sensor is triggered

## {UUID}/sensors/{sensorId}/trigger_percent
Set a trigger percent

### Publish
Set a new trigger percent, this does not update the [config](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Config) file

| Option      | Value  |
| ------------- |:-------------:|
| Retain   | True |


**Format**

```
trigger_percent
```
