import os
from handler.messageHandler import *

def handlePOST(request_body: str):
    # Melakukan Split pada request_body untuk mendapatkan search key
    search = request_body.split("\n")[3].replace("\r", "")

    # List file yang sesuai dengan search key
    result = [name for name in os.listdir('./database') if search in name]
    # Render HTML Page sesuai dengan Search Key dan Result
    return htmlRenderer(search, result)