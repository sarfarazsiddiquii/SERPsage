import requests
import xml.etree.ElementTree as ET

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
            print("Failed to fetch sitemap. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage:
website_name = input("Enter the website name: ")
sitemap_url = "https://" + website_name + "/sitemap.xml"
sitemap_links = extract_links_from_sitemap(sitemap_url)
if sitemap_links:
    print("Links in sitemap:")
    for link in sitemap_links:
        print(link)
