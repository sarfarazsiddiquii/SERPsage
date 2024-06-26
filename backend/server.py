from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import xml.etree.ElementTree as ET
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.getenv('API_KEY')

# app instance
app = Flask(__name__)
CORS(app)

#ai code
genai.configure(api_key= apikey)
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])



# new function
def extract_links_from_sitemap(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            sitemap_xml = response.text
            root = ET.fromstring(sitemap_xml)
            links = []
            for elem in root.iter():
                if '}' in elem.tag:
                    elem.tag = elem.tag.split('}', 1)[1]
                if elem.tag.lower() == 'loc':
                    links.append(elem.text)
            return links
        else:
            return None
    except Exception as e:
        return None

Aimesssage = "represent these links in readable format for better understanding, list them so i can read their titles. Also exclude all the links with extension of that of photos or any oother media. im just interested in the titles. make sure you print all the titles from these links in numbered list, if the entities are more than 25, just print the first 25 and write + more at the end"
# /api/home
@app.route("/api/home", methods=['POST'])
def return_home():
    global sitemap_links
    data = request.json
    website_name = data.get('website_name')
    sitemap_url = "https://" + website_name + "/post-sitemap.xml"
    sitemap_links = extract_links_from_sitemap(sitemap_url)
    convo.send_message(Aimesssage + str(sitemap_links))
    return convo.last.text

if __name__ == "__main__":
    app.run(debug=True, port=8080)
