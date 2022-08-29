import logging
import azure.functions as func


def main(req: func.HttpRequest, articlesrecommended: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not articlesrecommended or len(articlesrecommended) == 0:
        return func.HttpResponse(
             "Recommendation not found",
             status_code=404
        )
    else:
        return func.HttpResponse(
            articlesrecommended[0].to_json(),
            mimetype="application/json",
            status_code=200
        )
