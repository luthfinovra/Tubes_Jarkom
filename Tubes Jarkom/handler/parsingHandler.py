def requestParsing(decodedRequest) :
    # Memecah request menjadi baris
    request_line = ''.join((line + '\n') for line in decodedRequest.splitlines())
    # Memecah Head dan Body
    request_head, request_body = request_line.split('\n\n', 1)

    request_head = request_head.splitlines()
    # Headline dari HTML
    request_headline = request_head[0].split(' ')

    # Header dari HTML
    request_headers = dict(x.split(': ', 1) for x in request_head[1:])

    # Method, Uri, dan Proto dari HTML
    request_method = request_headline[0]
    request_uri = ' '.join(request_headline[1:len(request_headline)-1])
    request_proto = request_headline[-1]

    # Informasi dari Request dimasukkan ke dalam Dictionary
    request = {
        "method": request_method,
        "uri": request_uri,
        "proto": request_proto,
        "body": request_body,
        "headers": request_headers
    }

    return request
