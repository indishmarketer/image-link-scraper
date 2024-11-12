# Image Link Scraper

## Project Overview
The **Image Link Scraper** is a Flask-based web application that extracts and displays all `.png` image links from a specified web page. Users can input a URL, and the app will fetch the page, parse it, and list all `.png` image links, formatted and clickable for convenience.

## Features
- **Easy Input**: Users can submit any URL via web form.
- **Image Parsing**: Extracts and modifies image links to ensure the highest resolution (`s1920` size).
- **Dynamic List**: Outputs all image links in an ordered list with proper numbering.
- **User-Friendly Interface**: Clean and intuitive UI design.

## Technologies Used
- **Python**: Core language for building the app.
- **Flask**: Lightweight web framework.
- **BeautifulSoup**: Library for web scraping.
- **HTML/CSS**: Frontend design and layout.
- **Jinja2**: Templating engine used in Flask.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/image-link-scraper.git
   cd image-link-scraper
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open a web browser and navigate to `http://127.0.0.1:5000/`.

## How to Use
1. Enter the URL of the webpage you want to scrape in the provided input box.
2. Click on **Scrape Image Links**.
3. The app will display an ordered list of all extracted `.png` image links.
4. Click on any link to open the image in a new tab.

## File Structure
```
image-link-scraper/
│
├── app.py                 # Main Flask application script
├── requirements.txt       # Dependencies for the project
└── templates/
    └── index.html         # HTML template for rendering the page
```

## Example Output
A sample list generated by the app would look like this:
```
1. https://example.com/images/image1.png
2. https://example.com/images/image2.png
3. https://example.com/images/image3.png
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For questions or feedback, feel free to reach out:
- **Email**: [info@indishmarketer.com](mailto:info@indishmarketer.com)
- **Twitter**: [@indishmarketer](https://twitter.com/indishmarketer)
