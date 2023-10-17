```markdown
# Amazon ASIN Image Scraper

## Overview
This Python script allows you to scrape product image URLs from Amazon based on ASIN (Amazon Standard Identification Number) values provided in an Excel file. It uses Selenium and BeautifulSoup for web scraping.

## Features
- Scrapes product image URLs from Amazon based on a list of ASIN values.
- Supports the input of ASIN values via an Excel file.
- Saves the ASIN and corresponding image URLs in a new Excel file.

## Requirements
- Python 3.x
- [Selenium](https://selenium-python.readthedocs.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (for Selenium)

## Usage
1. Clone or download this repository.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Download and configure the Chrome WebDriver. Make sure it's in your system's PATH.
4. Run the script by executing `python amazon_asin_scraper.py`.

## How to Input ASIN Values
1. Create an Excel file with a column named "ASIN" (case-insensitive).
2. Add ASIN values in this column.
3. Run the script, and it will extract image URLs and create a new Excel file with "ASIN" and "URL" columns.

## Example Excel File (input):
```plaintext
+-------------+
|    ASIN     |
+-------------+
| B07H8NS8W1  |
| B06XY7D3VT  |
| B01LZM5ML2  |
| ...         |
+-------------+
```

## Example Excel File (output):
```plaintext
+-------------+----------------------------------------+
|    ASIN     |               URL                      |
+-------------+----------------------------------------+
| B07H8NS8W1  | https://www.amazon.com/image1.jpg      |
| B06XY7D3VT  | https://www.amazon.com/image2.jpg      |
| B01LZM5ML2  | https://www.amazon.com/image3.jpg      |
| ...         | ...                                    |
+-------------+----------------------------------------+
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project uses the [Selenium](https://selenium-python.readthedocs.io/) library for web automation.
- It utilizes [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
- Data processing is performed using [Pandas](https://pandas.pydata.org/).

