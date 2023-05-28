import threading
from socket import IPPROTO_TCP
from socket import TCP_NODELAY
from socket import *
from handler.requestHandler import handleRequest

def threadingSocket(connectionSocket):
    try:
        # Koneksi yang diterima kemudian di decode
        request = connectionSocket.recv(5012).decode()

        # Memanggil function handleRequest untuk mendapatkan response yang sesuai
        response = handleRequest(request)

        # Jika jenis response byte, tidak usah diencode
        if isinstance(response, bytes) :
            # Mengirim Response ke Client
            connectionSocket.send(response)
        else :
            # Encode dan Mengirim response ke client
            connectionSocket.send(response.encode())
            
        connectionSocket.close()
    except IOError:
        # Return HTML 'Error 404' jika terdapat IOErr
        errorPage = open("views/404.html", "r").read()
        connectionSocket.send(errorPage.encode())
        connectionSocket.close()

if __name__ == "__main__":
    # AF_INET = IP address, SOCK_STREAM = Socket Type: TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 127.0.0.1:80 / localhost:80
    serverAddress = "localhost"
    serverPort = 80

    # Buat Address dan Port reusable
    serverSocket.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)

    # Bind Address dengan Port. Max Connection : 5
    serverSocket.bind((serverAddress, serverPort))
    serverSocket.listen(5)

    # Print Address dan Port di Terminal
    print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")
    while True:
        # Menerima request dari client
        connectionSocket, addr = serverSocket.accept()
        # Pemrosesan request secara threading
        threading.Thread(target=threadingSocket, args=(connectionSocket,)).start()

