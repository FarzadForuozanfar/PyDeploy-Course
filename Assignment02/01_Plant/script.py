import requests
import os
import dotenv


dotenv = dotenv.load_dotenv()

FAL_API_KEY = os.getenv("FAL_API_KEY")
PLANETNET_API_KEY = os.getenv("PLANETNET_API_KEY")

url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"

payload = {
    "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
    "prompt": "(masterpiece:1.4), (best quality), (detailed), A pretty red rose with a blue-green vase",
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
}

headers = {
    "Authorization": FAL_API_KEY,
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
img_link = response.json()['image']['url']
res      = requests.get(img_link, allow_redirects=True)

open('red_rose_image.png', 'wb').write(res.content)

url    = "https://my-api.plantnet.org/v2/identify/all"
payload = {
    "api-key": PLANETNET_API_KEY
}

files = {
    'images': open('red_rose_image.png','rb')
}

response = requests.post(url, params=payload, files=files)
print(response.json()['results'][0]['species']['commonNames'][0])
