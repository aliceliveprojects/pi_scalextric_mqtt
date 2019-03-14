# pi_scalextric_mqtt
STOP PRESS - we have now seen 2 occasions where the Grove Pi sensor board refuses to read sensor values. This is accompanied by the LEF on the board, marked 'RST' turning RED.
To reset the board and clear this error, execute the following from the command line:

```bash
avrdude -c gpio -p m328p
```

## Project Structure
- [Mqtt](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt): setup a mqtt broker, python scripts or configuration files

- [Node Red Flow](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/node_red_flow): node red flows

---

## Topic Structure
I recommend viewing the topic structure on mind-mup

## {UUID}/control/game_state
Sets or gets the game state

**Subscribe**: To retrieve game state


**Publish**: To set game state

Options:

| Option      | Value  |
| ------------- |:-------------:|
| Retain        | True |

---

## {UUID}/control/pi_state
Sets or gets the pi state

**Subscribe**: To retrieve pi state

Format:

New state has been requested
```
{
  requested : [target_state]
}
```

State is in the process of execution
```
{
  busy : [state]
}
```


State is ready for a new request
```
{
  done : [state]
}
```


**Publish**: To set pi state

Format:

```
{
  requested : [target_state]
}
```

Options:

| Option      | Value  |
| ------------- |:-------------:|
| Retain   | True |


---

## {UUID}/control/{channel}/throttle
Sets or gets the channel throttle

**Subscribe**:To retrieve channel throttle

Format:

```
[throttle]
```


**Publish**: To Set channel throttle

Format

```
{
  set : [throttle]
}
```

---

## {UUID}/control/{channel}/event
In Progress...

---

## {UUID}/control/{channel}/{resourceId}/state
Sets or gets the resource state

**Subscribe**:To retrieve resource state

Format:

Resource is deploying
```
{
  state : "busy"
}
```


Resource is ready for deployment
```
{
  state : "ready"
}
```


**Publishing**: To deploy resource

Format:

```
state : "requested"
target : [CHANNEL_ID]
}
```

---

## {UUID}/control/{channe}/{resourceId}/count
Sets or gets the number of deployments left for a resource

**Subscribe**: To retireve resource count

Format:

```
count
```


**Publishing**: To set resource count

Format:

```
count
````

Options:

| Option      | Value  |
| ------------- |:-------------:|
| Retain   | True |


---

## {UUID}/sensors
To get sensor details

**Subscribe**: To retireve all sensor details

Format:

see https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Config#sensors

---

## {UUID}/resources
To get resource details

**Subscribe**: To retrieve all resource details

Format:

see https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Config#resources

---

## {UUID}/sensors/{sensorId}
Gets sensor events

**Subscribe**: Notified when a sensor is triggered

Currently, we support the following sensors:

|channel|Sensor|
|-|-|
|1| Grove Light Sensor |
|2| Grove Sound Sensor |
|3| [Grove IR Reflective Sensor](https://www.seeedstudio.com/Grove-Infrared-Reflective-Sensor-v1-2-p-2791.html) |
|4| [Grove IR Reflective Sensor](https://www.seeedstudio.com/Grove-Infrared-Reflective-Sensor-v1-2-p-2791.html) |

The IR reflective sensors  can be mounted trackside and publish an output when the car goes past. They can be used as lap counters, or to sense when both cars are at the start line.

---

## {UUID}/sensors/{sensorId}/trigger_percent
Set a trigger percent

**Publish**: Sets a new trigger percent, this does not update the [config](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt/src/Config) file

Format:

```
trigger_percent
```

Options:

| Option      | Value  |
| ------------- |:-------------:|
| Retain   | True |


---



This is the work of [Yusof Bandar](https://github.com/YusofBandar) for [DigitalLabs@MMU](https://digitallabs.mmu.ac.uk/).

<p align="center">
<img align="middle" src="https://trello-attachments.s3.amazonaws.com/5b2caa657bcf194b4d089d48/5b98c7ec64145155e09b5083/d2e189709d3b79aa1222ef6e9b1f3735/DigitalLabsLogo_512x512.png"  />
 </p>
 
 
<p align="center">
<img align="middle" src="https://trello-attachments.s3.amazonaws.com/5b2caa657bcf194b4d089d48/5b98c7ec64145155e09b5083/e5f47675f420face27488d4e5330a48c/logo_mmu.png" />
 </p>

