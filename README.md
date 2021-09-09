## Simple udp sender/receiver with python

### Environment
Python 3.*

### How to run
Launch two separate command lines, and run these commands :

```
$ python sender.py

...
[
  {
    "time": 13.0,
    "control_input": {
      "lateral": {
        "steer_angle": 2.0
      },
      "longitudinal": {
        "throttle": 1.0,
        "brake": 0.0
      }
    }
  }
]

```


```
$ python receiver.py

...
Got json object below : 
[
  {
    "time": 13.0,
    "control_input": {
      "lateral": {
        "steer_angle": 2.0
      },
      "longitudinal": {
        "throttle": 1.0,
        "brake": 0.0
      }
    }
  }
]

```