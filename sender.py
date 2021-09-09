import socket # for udp communication
import time

SLEEP_TIME=1.0 #[s]
TARGET_IP = '127.0.0.1'
TARGET_PORT = 56483

address = (TARGET_IP, TARGET_PORT) # set target IP and port number.
msg = '{"value0": {"value0": 1631182529,"value1": "test","value2": [0.0,0.0,0.0,0.0,0.0]} }\n ' # message to send

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # generate socket named udp
udp.setblocking(False) # set socket to be non-blocking	

# loop forever
while True:
    try:
        # send the binarized string message
        udp.sendto(msg.encode(), address) 
        time.sleep(SLEEP_TIME) # sleep for a while

    # close socket when the process is interrupted.
    except KeyboardInterrupt:
        udp.close()