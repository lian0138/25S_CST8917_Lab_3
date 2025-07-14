import azure.functions as func
import json

# Define inappropriate keywords
BAD_WORDS = ["XXOO", "XXII", "XXUU", "XXYY"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        message = req_body.get('content', '').lower()

        is_inappropriate = any(bad_word in message for bad_word in BAD_WORDS)

        response = {
            "is_inappropriate": is_inappropriate,
            "original_message": message
        }

        # Return response
        return func.HttpResponse(
            json.dumps(response),
            status_code=200,
            mimetype='application/json'
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype='application/json'
        )