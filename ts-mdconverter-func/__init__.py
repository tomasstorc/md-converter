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
    if not data:
        return func.HttpResponse("No data in body found", status_code=400)

    if data:
        converted = convert2html(data)
        dToOut = {
            "data": converted,
            "status": "success"
        }
        return func.HttpResponse(json.dumps(dToOut) , mimetype="application/json", status_code=200)
