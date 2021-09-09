import socket # for udp communication
import time
import json

SLEEP_TIME=0.5 #[s]
RECEIVER_IP = 'localhost'
RECEIVER_PORT = 56483
MAX_BUFFER_SIZE = 1024

# TODO: Need function to get only latest msg, throwing away other old ones.

def main():
    address = (RECEIVER_IP, RECEIVER_PORT) # set receiver's IP and port.
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # generate socket named udp
    udp.bind(address) # bind ip address to the socket
    udp.setblocking(False) # set socket to be non-blocking	

    try:
        # loop forever
        while True:
            try:
                time.sleep(SLEEP_TIME) # sleep for a while
                rcv_byte = bytes() # define buffer to receive msg
                rcv_byte, addr = udp.recvfrom(MAX_BUFFER_SIZE) # get message
                msg = rcv_byte.decode() # convert bytedata to string type
                # if the socket receives "close", then close udp connection.
                if msg == 'close': 
                    print("Received command to close communication.")
                    udp.close()
                    break
                elif is_json(msg):
                    # if msg is json format
                    print("Received json object : ")
                    json_msg = json.loads(msg)
                    print(json.dumps(json_msg,indent=2))

                    print(f"json_msg['value0']={json_msg['value0']}")
                    print(f"json_msg['value0_1']={json_msg['value0']['value1']}")
                    print(f"json_msg['value0_1']={json_msg['value0']['value1']}")
                    print(f"json_msg['value0_2']={json_msg['value0']['value2'][2]}")
                else:
                    # simply output msg
                    print("Received simple text message : ")
                    print(msg)

            # not receiving message yet
            except Exception as e:
                if e.args[0]==10035: 
                    print("Not receive new msg yet.")
                    continue

    # close socket when the process is interrupted.
    except KeyboardInterrupt:
        udp.close()

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

if __name__ == '__main__':
    main()