from handler.getHandler import handleGET
from handler.postHandler import handlePOST
from handler.parsingHandler import requestParsing
from handler.datahandler import handleData
import mimetypes

def handleRequest(request):
    # Respon OK dan tipe konten respon
    response_line = "HTTP/1.1 200 OK\r\n"
    path = requestParsing(request)["uri"]

    # Menentukan content type respon
    content_type = f"Content-Type: {mimetypes.guess_type(path)[0]}\r\n\r\n"
    # isi respon dari request
    message_body = handleMethod(request)
    
    # Jika balasan request berupa file dalam format biner langsung return balasan
    if isinstance(message_body, bytes) :
        return message_body
    
    # Jika balasan request berupa file string beri spasi satu baris dan return balasan
    elif isinstance(message_body, list) :
        return '\n'.join(message_body)
    
     # Ok Response, Content, dan Isi di concat menjadi satu
    response = response_line+content_type+message_body
    return response

def handleMethod(request):
    # Parsing Pesan
    request = requestParsing(request)

    if "database/" in request["uri"] :
        # Response for Get Raw Data
        return handleData(request["uri"])
    elif request["method"] == "GET":
        # Get Response
        return handleGET(request["uri"])
    elif request["method"] == "POST":
        # Post Response
        return handlePOST(request["body"])

    return "Method Not Allowed"