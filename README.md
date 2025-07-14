## 1.   A screenshot or export of your workflow flowchart.

This is my first workflow of the Logic App
```
Teams (When a new channel message is added)
    |
    v
Azure Function (Check message content—inappropriate?)
    │
    v
Condition
 ┌──┴───┐
No      Yes
│        │
End   Send Email (Outlook365 send an Email)
```
![I got an error while I just open function app](https://raw.githubusercontent.com/lian0138/25S_CST8917_Lab_3/refs/heads/main/img/8917lab3error.png)
But unfortunately, because of a Microsoft error, while I open an even empty function App, I get an error in the portal. So, finally, I made it simple
![This is my workflow](https://raw.githubusercontent.com/lian0138/25S_CST8917_Lab_3/refs/heads/main/img/workflow.png)


## 2.  Description of your Logic App setup.
I built a Logic App
When a new channel message is added (connect to my team as the YouTube video), next the condition will check if the message context body contains some "Bad words"; if yes, send an alarm email.

## 3.   Optional: details about Azure Functions or Cognitive Services used.
Even though I got an error in the function APP running in Azure, I still can share my code
```
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
```
## 4. Explanation of how you tested the workflow.
As I show up in the YouTube video, I built a team in the Microsoft team, and post information that contains the violation of inappropriate information, and am waiting for the email alert.

## 5. Challenges you encountered and how you resolved them.
My Microsoft Azure account's issue, while I run the function app, I get errors even when I just have a view in the portal. So I just make it simple.

## 6. Recommendations for future improvement.
Like I said in the class, I'm not very recommended using function app, even though it's a serverless architecture, because we can not effectively estimate the cost with an official cost calculator, it makes while we build up this kind of solution, our cost estimation without a strong evidence due to lack to references.

YouTube link:
https://youtu.be/mrwVc5sr848