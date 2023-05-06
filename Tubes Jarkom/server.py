import threading
from socket import *
from handler.getHandler import *
from handler.postHandler import *
from handler.requestHandler import *

def threadingSocket(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode() #decode request
        response = handleRequest(request) #handle request
        connectionSocket.send(response.encode()) #kirimkan respon
        connectionSocket.close() #tutup koneksi
    except IOError:
        connectionSocket.send("File Not Found".encode()) #file not found error
        connectionSocket.close() #tutup koneksi

if __name__ == "__main__":
    serverSocket = socket(AF_INET, SOCK_STREAM) #inisiasi bahwa socket menggunakan IPv4, TCP
    serverAddress = "localhost" #inisiasi nama server
    serverPort = 80 #menentukan port server

    #mengizinkan server untuk menggunakan socket dan alamat yang sama
    #setelah koneksi sebelumnya berakhir 
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    serverSocket.bind((serverAddress, serverPort)) #menyiapkan alamat server dan port pada socket
    serverSocket.listen(5) #socket akan menunggu koneksi dan maksimal adalah 5 koneksi

    #menampilkan server adress ke terminal
    print(f"\n\nYou can Acces Your Website in http://{serverAddress}:{serverPort}\n\n")
    while True:
        connectionSocket, addr = serverSocket.accept() #menerima permintaan koneksi
        threading.Thread(target=threadingSocket, args=(connectionSocket,)).start() #memulai koneksi