from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import xml.etree.ElementTree as ET

# app instance
app = Flask(__name__)
CORS(app)

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

# /api/home
@app.route("/api/home", methods=['POST'])
def return_home():
    global sitemap_links
    data = request.json
    website_name = data.get('website_name')
    sitemap_url = "https://" + website_name + "/sitemap.xml"
    sitemap_links = extract_links_from_sitemap(sitemap_url)
    return jsonify({
        'message': 'Website name received and data extracted from sitemap.',
        'sitemap_links': sitemap_links,
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)
