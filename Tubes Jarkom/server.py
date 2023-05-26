import threading
from socket import *
from handler.requestHandler import handleRequest

def threadingSocket(connectionSocket):
    try:
        # Request yang diterima kemudian di decode
        request = connectionSocket.recv(1024).decode()
        # Panggil handleRequest untuk mendapatkan respon yang sesuai
        response = handleRequest(request)

        # Jika jenis response byte, tidak diperlukan proses encode
        if isinstance(response, bytes) :
            # Mengirim Resoponse Kepada Client
            connectionSocket.send(response)
        else :
            # Encode dan kirim response ke client
            connectionSocket.send(response.encode())
        
        connectionSocket.close()
    except IOError:
        errorPage = open("views/404.html", "r")
        connectionSocket.send(errorPage.encode())
        connectionSocket.close()

if __name__ == "__main__":
    # AF_INET : IPv4, SOCK_STREAM : TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Inisialisasi server 127.0.0.1:80 / localhost:80
    serverAddress = "localhost"
    serverPort = 80

    # Menjadikan alamat dan Port Reusable
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Bind Alamat dan Port dengan koneksi maksimal sebanyak 5
    serverSocket.bind((serverAddress, serverPort))
    serverSocket.listen(5)

    # Menampilkan server adress dan port ke terminal
    print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")
    while True:
        # Menerima permintaan koneksi
        connectionSocket, addr = serverSocket.accept()
        threading.Thread(target=threadingSocket, args=(connectionSocket,)).start()