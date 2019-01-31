# pi_scalextric_mqtt

### Project Structure
- Check out the [mqtt](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/mqtt) folder if you want to setup a mqtt broker, python scripts or configuration files

- Check out the [node_red_flow](https://github.com/aliceliveprojects/pi_scalextric_mqtt/tree/master/node_red_flow) folder for the node red flow



# Topic Structure

## {UUID}
Unqiue Id to identify which device

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
