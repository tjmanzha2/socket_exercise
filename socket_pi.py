import socket
import struct
import threading

SERVER_IP_ADDRESS = "192.168.0.8"
SERVER_PORT_NUM = 56774
PI_IP_ADDRESS = "192.168.0.2"
PI_PORT_NUM = 43179

def detected_sign_from_server(self):
    while True:
        clnt_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clnt_socket.bind((PI_IP_ADDRESS, PI_PORT_NUM))
        clnt_socket.listen()    
        conn, addr = clnt_socket.accept()
        temp_msg = conn.recv(1024)
        data_format = struct.Struct("i")
        recv_value = data_format.unpack(temp_msg)
        recv_int = recv_value[0]

        print("received msg: ", recv_int)

        ''' Implement some codes for recv sign '''

        conn.close()


if __name__ == "__main__": 
    sign_detection_thread = threading.Thread(target=detected_sign_from_server)
    sign_detection_thread.start()



