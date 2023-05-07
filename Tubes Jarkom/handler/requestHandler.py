from handler.getHandler import handleGET
from handler.postHandler import handlePOST
from handler.parsingHandler import requestParsing

def handleRequest(request):
    # Respon OK dan tipe konten respon
    response_line = "HTTP/1.1 200 OK\r\n"
    content_type = "Content-Type: text/html ; charset=utf-8\r\n\r\n"
    message_body = handleMethod(request)
    
    # Info Header dan Memberikan Respon kepada klien
    response = response_line+content_type+message_body
    return response

def handleMethod(request):
    # Parse the Request
    request = requestParsing(request)

    if request["method"] == "GET":
        # Get Response
        return handleGET(request["uri"])
    elif request["method"] == "POST":
        # Post Response
        return handlePOST(request["body"])

    return "Method Not Allowed"