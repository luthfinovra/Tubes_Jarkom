def htmlRenderer(search, data):
     # Kategori file berdasarkan extension filenya
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

    # Map File berdasarkan kategorinya
    database_file = {k: [name for name in data if name.split(".")[-1] in v] for k, v in extensions.items()}

    # Nama icon berdasarkan kategori file
    database_icon ={
        "pdf": "pdf",
        "txt": "lines",
        "mp3": "audio",
        "mp4": "video",
        "image": "image",
        "document": "word",
        "archive": "archive",
        "code" : "code"
    }

    # HTML untuk Box Icon dan Filename
    file_icon = """
        <div class="flex flex-col items-center gap-2 my-1 pt-5 hover:bg-cyan-500 hover:rounded-lg">
            <a href="database/{}" target="blank">
                <i class="fa fa-solid fa-file-{} fa-2xl items-center justify-center flex mb-3" style="color: #FFFFFF;"></i>
                <h5 style="font-family: 'Lexend'; font-weight: 200" class="text-white pt-2 text-center">{}</h5>
            </a>
        </div>
    """

    # List setiap file yang di cari kedalam Box Icon dan Filename
    list_file = ''.join([file_icon.format(value, database_icon[key], value) for key in database_file for value in database_file[key] if len(database_file[key]) > 0])

    # Response HTML jika tidak ada file yang ditemukan
    if not list_file :
        list_file = """
            <div class="justify-center items-center pt-2 text-white text-center" style="font-family: Lexend;">No Data Found</div>
        """

    # HTML Page yang direturn
    html_body = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Lexend:wght@200;400;600;800&display=swap" rel="stylesheet">
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <title>Local Server</title>
            <style>
                input[type="text"],
                input[type="password"],
                textarea {{
                    border: none;
                    outline: none;
                    border-bottom: 2px solid white;
            }}
            </style>
        </head>
        <body style="background-color: #0D467F">
            <div class="flex flex-col items-center justify-center text-white">
                <div style="font-weight: 800; font-family: Lexend;" class="pt-20 text-4xl">
                    DATABASE
                </div>
                <div style="height: 0.4px; width: 300px; background-color: #898989;"></div>
                <div style="font-weight: 200; font-family: Lexend;"class="text-sm">Kelompok 7 | IF-45-12</div>
                <div class="pt-10 px-10">
                    <form action="" method="POST" enctype="multipart/form-data" class="flex justify-center items-center">
                        <input type="text" id="searchFile" name="searchFile" style="background-color: #E1EEFD; font-family: Lexend;" class="border-b-0 px-4 py-2 text-black rounded-full" size="50" required>
                        <button type="Submit" class="ml-3 p-2.5 rounded-full" style="background-color: #E1EEFD;">
                            <i class="fa fa-solid fa-magnifying-glass hover:fa-beat fa-xl" style="color: #0D467F;"></i>
                        </button>
                    </form>
                </div>
                <div class="p-3 pt-3 mt-2">
                    <a href="./index.html" class="p-3 rounded-full" style="color: #0D467F ;background-color: #E1EEFD; font-style: Lexend; font-weight: 600;">Back</a>
                </div>
                <div class="p-3 text-xl pb-2 mt-3" style="font-family: 'Lexend'; font-weight:400; ">
                    Result Search for {}
                </div>
                <div class="p-5 grid grid-cols-4 gap-3 gap-y-6">
                    {}
                </div>
            </div>
        </body>
        </html>
    """

    # Isi HTML dengan searchkey dan Box Icon
    if search == "" :
        html_body = html_body.format("All Files", list_file)
    else :
        html_body = html_body.format("Result Search For "+ search, list_file)
    return html_body