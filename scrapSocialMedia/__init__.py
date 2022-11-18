import logging

import azure.functions as func

import json

from . import scrapSocialMedia as scrapper

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ig_name = req.params.get('ig_name')
    if not ig_name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ig_name = req_body.get('ig_name')

    if ig_name:
        ig_profile = scrapper.InstagramProfile(ig_name)
        return func.HttpResponse(
            json.dumps(ig_profile.scrap()),
            mimetype="application/json",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
