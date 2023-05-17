import os
from handler.messageHandler import *

def handlePOST(request_body: str):
    # Split Request Body untuk menemukan Search Key
    search = request_body.split("\n")[3].replace("\r", "")

    # List file yang sesuai dengan search key
    result = [name for name in os.listdir('./database') if search.lower() in name.lower()]
    result.sort()
    # Render HTML Page sesuai dengan Search Key dan Result
    return htmlRenderer(search, result)