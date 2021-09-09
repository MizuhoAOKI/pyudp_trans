import socket # for udp communication
import time

SLEEP_TIME=1.0 #[s]
RECEIVER_IP = 'localhost'
RECEIVER_PORT = 56483
MAX_BUFFER_SIZE = 1024

address = (RECEIVER_IP, RECEIVER_PORT) # set receiver's IP and port.
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # generate socket named udp
udp.bind(address) # bind ip address to the socket
udp.setblocking(False) # set socket to be non-blocking	

# loop forever
while True:
    time.sleep(SLEEP_TIME) # sleep for a while
    try:
        rcv_byte = bytes() # define buffer to receive msg
        rcv_byte, addr = udp.recvfrom(MAX_BUFFER_SIZE) # get message
        msg = rcv_byte.decode() # convert bytedata to string type
        print(msg) # show the received message
        # if the socket receives "close", then close udp connection.
        if msg == 'close': 
            udp.close()
            break

    # not receiving message yet
    except Exception as e:
        if e.args[0]==10035: 
            print("Not receive new msg yet.")
            continue

    # close socket when the process is interrupted.
    except KeyboardInterrupt:
        udp.close()