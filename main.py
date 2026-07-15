# testing skills, sending POST request to llama server

import httpx

def request():
    model = "llama3.2"
    prompt = "If you get this message, respond with a greeting (playing a wizard)"
    stream = False
    
    params = {
        "model" : model,
        "prompt" : prompt,
        "stream" : stream,
    }

    url = "http://localhost:11434/api/generate"
    # the url: http://localhost:11434/api/generate, not sure where it goes
    # the json= thing is confusing, elaborate please.
    response = httpx.post(url, json=params, timeout=60)
    print("Request Sent")
    print(response.json())

# I recall python needs some kind of __main__ or something to actually
# run, lets see how rusty I am. Going to try running it like this.


if __name__ == "__main__":
    request()