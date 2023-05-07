def requestParsing(decodedRequest) :
    request_line = ''.join((line + '\n') for line in decodedRequest.splitlines())
    request_head, request_body = request_line.split('\n\n', 1)

    request_head = request_head.splitlines()
    request_headline = request_head[0]
    request_headers = dict(x.split(': ', 1) for x in request_head[1:])
    request_method, request_uri, request_proto = request_headline.split(' ', 3)

    request = {
        "method": request_method,
        "uri": request_uri,
        "proto": request_proto,
        "body": request_body,
        "headers": request_headers
    }

    return request
