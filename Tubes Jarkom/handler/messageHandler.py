def htmlRenderer(search, data):
    # Map Corresponding File Extension
    extensions = {
        "pdf": ["pdf"],
        "txt": ["txt"],
        "mp3": ["mp3"],
        "mp4": ["mp4"],
        "image": ["jpg", "png", "jpeg"],
        "document": ["docx", "pptx", "xlsx", "doc", "ppt", "xls"],
        "archive": ["zip", "rar"],
        "code": ["html", "css", "js", "py"]
    }

    # Map File Name to Corresponding File Extension
    database_file = {k: [name for name in data if name.split(".")[-1] in v] for k, v in extensions.items()}

    # Map File Types to the Corresponding Icon Name
    database_icon = {
        "pdf" : "pdf",
        "txt" : "alt",
        "mp3" : "audio",
        "mp4" : "video",
        "image" : "image",
        "document" : "word",
        "archive" : "archive",
    }

    file_icon = """
    <div>
        <i
            class="fa-solid fa-file-{}" 
            style="color: #c7c9cc;" >
        </i>
        <h5
            style="font-family: 'Comic Sans MS';"
            class="text-white pt-2 text-center"
        > {} </h5>
    </div>
    """
    # List of Each Element that Represent a File Icon and File Name
    file_icons = [file_icon.format(database_icon[key], value) for key in database_file for value in database_file[key]]
    print(''.join(file_icons))

    html_body = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">
            <script src="https://cdn.tailwindcss.com"></script>
            <title>Local Server</title>
            <style>
                input[type="text"],
                textarea {{
                    border: none;
                    outline: none;
                    border-bottom: 2px solid white;
            }}
            </style>
        </head>
        <body style="background-color: #1a1a1a">
            <div class="flex flex-col items-center text-white">
                <div style="font-family: 'Comic Sans MS';" class="pt-20 text-4xl">
                    Kessoku Database
                </div>
                <div class="pt-10 px-10">
                    <form action="" method="POST" enctype="multipart/form-data">
                        <input type="text" id="searchFile" name="searchFile" style="background-color: #1a1a1a;" class="border-b-4" size="50">
                        <button type="Submit" class="ml-2 h-8 text-justify rounded-md p-1 bg-neutral-100 text-black">Search</button>
                    </form>
                </div>
                <div class="p-3 text-2xl" style="font-family: 'Comic Sans MS';">
                    Result Search for {}
                </div>
                <div class="p-5 grid grid-cols-4 gap-4">
                    {}
                </div>
                <div class="p-1 h-96 w-96">
                    <img src="https://i.ibb.co/gt4PXS7/member.jpg" alt="Member Kessoku">
                </div>
            </div>
        </body>
        </html>
    """

    html_body = html_body.format(search, file_icon)
    return html_body