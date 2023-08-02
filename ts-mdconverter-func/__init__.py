import logging
import markdown2
import json

import azure.functions as func

def convert2html(dtoin):
    return markdown2.markdown(dtoin)

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
    


    if req.files.values():
        for file in req.files.values():
            dToOut = convert2html(file.stream.read())
            return func.HttpResponse(json.dumps(dToOut) , mimetype="application/json", status_code=200)
    if req.headers.get('Content-Type') == "application/json":
        req_body = req.get_json()
        if req_body:
            data = req_body.get('data')
            if data:
                converted = convert2html(data)
                dToOut = {
                    "data": converted,
                    "status": "success"
                }
                return func.HttpResponse(json.dumps(dToOut) , mimetype="application/json", status_code=200)
        else:
            return func.HttpResponse('no daa found')
    if len(req.files.values()) == 0:
        return func.HttpResponse("No content", status_code=400)
    else:
        return func.HttpResponse("here")
    
    