from flask import Flask, jsonify
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
@app.route("/api/home", methods=['GET'])
def return_home():
    global sitemap_links
    return jsonify({
        'sitemap_links': sitemap_links,
    })

# Example usage with example.com
website_name = "website.com"
sitemap_url = "https://" + website_name + "/sitemap.xml"
sitemap_links = extract_links_from_sitemap(sitemap_url)

# Check if sitemap_links is not None and is a list
if sitemap_links and isinstance(sitemap_links, list):
    # Now sitemap_links contains the extracted links from the sitemap
    print("Extracted links from the sitemap:", sitemap_links)

if __name__ == "__main__":
    app.run(debug=True, port=8080)


# the extracted links from the sitemap is stored in the list called sitemap_links
# change the value of website_name to the website you want to extract the links from