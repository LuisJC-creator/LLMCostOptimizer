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
    # Post request format is url, the json converted dict, and a manual setting of the timeout to allow ample time for LLM responses.
    response = httpx.post(url, json=params, timeout=60)
    print("Request Sent")
    print(response.json())


# Python's entry-point idiom, distinguishes "ran directly" from "imported by another file" (doesn't exist in Rust/C++)

if __name__ == "__main__":
    request()
