import logging
import markdown2

import azure.functions as func

def convert2html(dtoin):
    return markdown2.markdown(dtoin)

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
    data = req.body.get('data')
    name = req.params.get('name')
    if not data:
        return func.HttpResponse("No data in body found", status_code=400)

    if data:
        converted = convert2html(data)
        dToOut = {
            "data": converted,
            "status": "success"
        }
        return func.HttpResponse(dToOut, mimetype="application/json", status_code=200)
