import base64

def convertBase64ImageToImageBinary(data: str):

    mime = data.split(",")[0].split(":")[1].split(";")[0]
    data = base64.b64decode(data.split(",")[1])

    return data, mime