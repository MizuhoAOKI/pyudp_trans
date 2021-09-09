import socket # for udp communication
import time

SLEEP_TIME=1.0 #[s]
RECEIVER_IP = 'localhost'
RECEIVER_PORT = 56483

address = (RECEIVER_IP, RECEIVER_PORT) # set receiver's IP and port.
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # generate socket named udp
udp.bind(address) # bind ip address to the socket
udp.setblocking(False) # set socket to be non-blocking	

while True: #受信ループ
    time.sleep(SLEEP_TIME) # sleep for a while
    try:
        rcv_byte = bytes() #バイトデータ受信用変数
        rcv_byte, addr = udp.recvfrom(1024) #括弧内は最大バイト数設定
        msg = rcv_byte.decode() #バイトデータを文字列に変換
        print(msg) #文字列表示
        if msg == 'close': #受信した文字列がcloseならUDPソケットを閉じて終了
            udp.close()
            break

    # not receiving message yet
    except Exception as e:
        if e.args[0]==10035: 
            print("Not receive new msg yet.")
            continue

    # close socket when the process is interrupted.
    except KeyboardInterrupt:#強制終了を検知したらUDPソケットを閉じて終了
        udp.close()