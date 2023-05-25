import os
from socket import *

def databaseMenu() :
    """
    Interface untuk buka database
    """
    try :
        loopMainMenu = True
        while loopMainMenu : 
            request ="""GET /listDatabase HTTP/1.1\nHost: localhost\n\nBody"""

            clientSocket.send(request.encode())
            listMenu = clientSocket.recv(5012).decode().splitlines()

            print("List Data : ")
            print("\n".join([str(i+1) + ". " + listMenu[i] for i in range(len(listMenu))]))
            print("99. Exit")

            inputUser = int(input("Pilih data yang akan di download : "))-1

            if inputUser >= 0 and inputUser < len(listMenu)-1 :
                return "/database/"+listMenu[inputUser], listMenu[inputUser]
            elif inputUser == 98 :
                return ("99", "")

            print("Input Tidak ada di Menu")

    except IOError :
        print("Input Invalid")


def clientRequestHandler(path) :
    """
    Format request sama path untuk get code
    """
    request = f"GET {path} HTTP/1.1\nHost: localhost\n\nBody"
    
    return request

def clientWriteHandler(response, fileName) :
    """
    Write data dari binary response server
    """
    try :
        # Menuliskan data yang sudah diterima dari server ke folder cilentFolder
        data = open("clientFolder/"+fileName, "wb") # Write Binary 
        data.write(response)
        data.close()
    
    # Jika folder clientFolder belum dibuat
    except FileNotFoundError :
        # Membuat folder clientFolder
        os.mkdir("clientFolder")

        # Menuliskan data yang sudah diterima dari server ke folder cilentFolder
        data = open("clientFolder/"+fileName, "wb") # Write Binary
        data.write(response)
        data.close()

if __name__ == "__main__" :
    serverName = 'localhost'
    serverPort = 80

    loopDatabase = True
    while loopDatabase :
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))


        path, fileName = databaseMenu()
        if path == "99" :
            loopDatabase = False
            break

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        request = clientRequestHandler(path)

        clientSocket.send(request.encode())

        # Max buffer 1MB
        response = clientSocket.recv(10000000000)

        if isinstance(response, bytes) :
            clientWriteHandler(response, fileName)
            print("Data telah didownload di folder download/"+fileName)
        else :
            print("Data Tidak Ditemukan")

    # Close Socket
    clientSocket.close()