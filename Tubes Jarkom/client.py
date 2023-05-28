from socket import *
import os

def databaseMenu() :
    try :
        # Looping Mainmenu
        loopMainMenu = True
        while loopMainMenu : 
            # Format request untuk mendapatkan list nama data yang ada di database
            request ="""GET /listDatabase HTTP/1.1\nHost: localhost\n\nBody"""

            # Mengirim GET request ke server
            clientSocket.send(request.encode())

            # Menerima response dari server
            listMenu = clientSocket.recv(10000).decode().splitlines()

            # Print list data yang ada di database
            print("List Data : ")
            print("\n".join([str(i+1) + ". " + listMenu[i] for i in range(len(listMenu))]))
            print("99. Exit")

            # Meminta input user
            inputUser = int(input("Pilih data yang akan di download : "))-1

            # Mereturn path yang diminta user dan nama file yang diminta
            if inputUser >= 0 and inputUser < len(listMenu) :
                return "/database/"+listMenu[inputUser], listMenu[inputUser]
            # Stopping condition untuk looping menu
            elif inputUser == 99-1 :
                return ("99", "")
    
            print("Input Tidak ada di Menu")

    # Error handling jika input bukan integer
    except IOError :
        print("Input Invalid")


def clientRequestHandler(path) :
    # Format request agar dapat diparsing, dan ditambahkan dengan PATH yang akan di GET
    request = f"GET {path} HTTP/1.1\nHost: localhost\n\nBody"
    return request

def clientWriteHandler(fileName) :
    # Folder untuk menyimpan hasil download dari server
    folderName = "download/"
    filePath = folderName + fileName

    # Pembuatan folder untuk hasil downlaod (jika belum ada)
    try :
        os.mkdir(folderName)
    except FileExistsError :
        pass

    # Penulisan data dalam chunk

    # Buka data
    with open(filePath, "wb") as data :
        receivedBytes = 0
        # Maksimal data yang diterima adalah 10MB
        while receivedBytes < 10 * 1024 * 1024 :
            # Penerimaan data dalam chunk 1kb per transfer
            response = clientSocket.recv(1024)

            # Looping berhenti jika isi response bukan byte atau kosong
            if not isinstance(response, bytes) :
                print("Data tidak ditemukan")
                break

            if not response :
                break
            
            # Penulisan data kepada file dan pencatatan jumlah byte yang diterima
            data.write(response)
            receivedBytes += len(response)
    
    print("Data telah didownload di folder download/"+fileName)
    

if __name__ == "__main__" :
    # Target IP dan Port server
    serverName = 'localhost' # 127.0.0.1
    serverPort = 80

    # Looping menu utama client
    loopDatabase = True
    while loopDatabase :
        # Membuat socket dan membuat connection ke server
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))

        # Path dan fileName yang dipilih user dari menu
        path, fileName = databaseMenu()

        # Stopping condition untuk looping menu
        if path == "99" :
            loopDatabase = False
            break

        # Parsing request berdasarkan path yang sudah diplih
        request = clientRequestHandler(path)

        # Membuat socket dan membuat connection ke server
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        # Mengirim request kepada server
        clientSocket.send(request.encode())

        # Menuliskan data yang diterima kepada komputer client
        clientWriteHandler(fileName)


    # Close Socket
    clientSocket.close()