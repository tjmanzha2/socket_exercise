import socket

SERVER_IP_ADDRESS = "192.168.0.8"
SERVER_PORT_NUM = 56774
PI_IP_ADDRESS = "192.168.137.179"
PI_PORT_NUM = 43179

if __name__ == "__main__": 
    clnt_socket = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
    clnt_socket.bind((PI_IP_ADDRESS, PI_PIRT_NUM))
    clnt_socket.listen()

    while True:
        conn, addr = clnt_socket.accept()
        temp_msg = conn.recv(1024)
        data_format = struct.Struct("i")
        recv_value = data_format.unpack(temp_msg)

        print("received msg: ", temp_msg)
        conn.close()



