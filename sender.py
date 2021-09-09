import socket # for udp communication
import time
import json

SLEEP_TIME=0.5 #[s]
TARGET_IP = '127.0.0.1'
TARGET_PORT = 56483

## JSON message template (example) : 
#   {
#     "control_input":{
#         "lateral":{
#         "steer_angle": steer_angle_value[rad]
#         },
#         "longitudinal":{
#         "throttle" : throttle_pedal_value [-],
#         "brake" : brake_pedal_value [-]
#         }
#   }

def main():
    address = (TARGET_IP, TARGET_PORT) # set target IP and port number.
    # make json structure with python object
    sim_time = 0.0
    steer_angle = 2.0
    throttle = 1.0
    brake = 0.0


    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # generate socket named udp
    udp.setblocking(False) # set socket to be non-blocking	

    try:
        # loop forever
        while True:
            # prepare message to send
            json_msg = [{"time": sim_time,
                        "control_input": {\
                        "lateral" : {\
                            "steer_angle" : steer_angle
                        },\
                        "longitudinal" : {\
                            "throttle" : throttle,\
                            "brake"    : brake \
                        }  }\
                    }]
            msg = json.dumps(json_msg, indent=2) # convert python object to string
            # send the binarized string message
            udp.sendto(msg.encode(), address) 
            print("Sent following message")
            print(msg)
            time.sleep(SLEEP_TIME) # sleep for a while
            sim_time += SLEEP_TIME # increment

    # close socket when the process is interrupted.
    except KeyboardInterrupt:
        udp.close()

if __name__ == '__main__':
    main()