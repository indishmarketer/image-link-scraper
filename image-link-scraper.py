from flask import Flask, request, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to scrape image links from a given URL
def get_image_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        image_links = []

        # Extract all image links ending with .png
        for img_tag in soup.find_all('img'):
            img_url = img_tag.get('src')
            if img_url and img_url.endswith('.png'):
                # Modify the image URL to include the 's1920' size
                if 's320' in img_url:
                    img_url = img_url.replace('s320', 's1920')
                image_links.append(img_url)

        return image_links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

# HTML template for rendering the web page
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Link Scraper</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }
        h1, h2 {
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
            max-width: 600px;
            margin: auto;
        }
        input[type="text"] {
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .links-list {
            list-style-type: decimal;
            margin-top: 20px;
            padding-left: 40px;
        }
        li {
            margin-bottom: 10px;
            word-break: break-all;
        }
    </style>
</head>
<body>
    <h1>Image Link Scraper</h1>
    <form method="POST">
        <input type="text" name="url" placeholder="Enter the URL of the page" required>
        <button type="submit">Scrape Image Links</button>
    </form>
    
    {% if image_links %}
        <h2>Scraped Image Links</h2>
        <ol class="links-list">
            {% for num, link in image_links %}
                <li><a href="{{ link }}" target="_blank">{{ link }}</a></li>
            {% endfor %}
        </ol>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    image_links = []
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            image_links = get_image_links(url)
            # Enumerate the image links in Python
            image_links = list(enumerate(image_links, start=1))
    return render_template_string(html_template, image_links=image_links)

if __name__ == '__main__':
    app.run(debug=True)
