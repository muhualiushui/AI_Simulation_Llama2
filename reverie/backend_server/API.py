import json
import requests

def send(query):
    try:
        url = "https://llama.k8s-gosha.atlas.illinois.edu/completion" 
        myobj = {
            "prompt": "<s>[INST]"+query+"[/INST]",
            "n_predict": -1
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YXRsYXNhaXRlYW06anhAVTJXUzhCR1Nxd3U="
        }

        response = requests.post(url, data=json.dumps(myobj), headers=headers, 
                                auth=('atlasaiteam', 'jx@U2WS8BGSqwu'), timeout=1000)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return response.json()