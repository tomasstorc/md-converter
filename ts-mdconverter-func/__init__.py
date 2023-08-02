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
            logging.info(f"received file ${file.filename}")
            converted_f = convert2html(file.stream.read())
            dToOut = {
                "data": converted_f,
                "status": "success"
            }
            logging.info("successfully converted file")
            return func.HttpResponse(json.dumps(dToOut) , mimetype="application/json", status_code=200)
    if req.headers.get('Content-Type') == "application/json":
        logging.info("received json body")
        req_body = req.get_json()
        if req_body:
            data = req_body.get('data')
            if data:
                converted = convert2html(data)
                logging.info("successfully converted json data")
                dToOut = {
                    "data": converted,
                    "status": "success"
                }
                return func.HttpResponse(json.dumps(dToOut) , mimetype="application/json", status_code=200)
        else:
            return func.HttpResponse(json.dumps({"status": "error", "data": "no input found"}), status_code=400)
    if len(req.files.values()) == 0:
        return func.HttpResponse(json.dumps({"status": "error", "data": "no file found"}), status_code=400)
    else:
        return func.HttpResponse("here")
    
    