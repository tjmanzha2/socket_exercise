import socket

SERVER_IP_ADDRESS = "192.168.0.8"
SERVER_PORT_NUM = 56774
PI_IP_ADDRESS = "192.168.137.179"
PI_PORT_NUM = 43179

if __name__ == "__main__":
    server_socket = socket.socket(socket_AF_INET, socket.SOCK_STREAM)
    server_socket.connect(PI_IP_ADDRESS, PI_PORT_NUM)

    while True:
        recv_msg = input('What is the value u want?')
        data_format = struct.Struct("i")
        pwm_value = data_format.pack(*recv_msg)
        server_socket.send(pwm_value)
        server_socket.close()




