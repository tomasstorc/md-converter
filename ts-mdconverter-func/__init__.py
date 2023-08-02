import logging
import markdown2
import json

import azure.functions as func

def convert2html(dtoin):
    return markdown2.markdown(dtoin)

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    data = req_body.get('data')
    if not data and len(req.files.values()) == 0:
        return func.HttpResponse("No content", status_code=400)

    if data:
        converted = convert2html(data)
        dToOut = {
            "data": converted,
            "status": "success"
        }
        return func.HttpResponse(json.dumps(dToOut) , mimetype="application/json", status_code=200)
    if req.files.values():
        for file in req.files.values():
            dToOut = convert2html(file.stream.read())
            return func.HttpResponse(json.dumps(dToOut) , mimetype="application/json", status_code=200)