import socket
import struct

SERVER_IP_ADDRESS = "192.168.0.8"
SERVER_PORT_NUM = 56774
PI_IP_ADDRESS = "192.168.137.179"
PI_PORT_NUM = 43179

def send_detected_sign_to_pi(self):
    while True:
        recv_msg = input('What is the value u want?')
        recv_int = int(recv_msg)
        data = [recv_int]
        data_format = struct.Struct("i")
        pwm_value = data_format.pack(*data)
        server_socket.send(pwm_value)
        server_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(PI_IP_ADDRESS, PI_PORT_NUM)
    
    send_detected_sign_to_pi()
    



