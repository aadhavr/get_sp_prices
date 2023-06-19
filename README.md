# S&P 500 Stock Information Web Scraper

This web scraper is designed to retrieve stock information for companies listed in the S&P 500 index. It extracts the price, change, and change in percentage for each stock and returns the data in a JSON format.

## Prerequisites

To use this web scraper, you will need the following:

- Python 3.x installed on your machine.
- Python libraries: `beautifulsoup4` and `requests`. You can install them using ```python3 -m pip install beautifulsoup4 requests```.
- Know your user agent.

## Usage

1. Clone or download the repository to your local machine.

2. Install the required Python libraries mentioned in the prerequisites section.

3. Open the sp500_scraper.py file in a text editor.

4. Modify the output_file_path variable in the script to specify the desired file path for the output JSON file.

5. Modify the user agent.

6. Run the sp500_scraper.py script using the following command:
    
```
python3 sp500_scraper.py
```

6. The script will scrape the S&P 500 stock information from the website and save it to the specified JSON file.

## Output

The output JSON file will contain an array of objects, where each object represents a stock and includes the following fields:

- stock: The stock symbol.
- price: The price of the stock at the time of running the script. Closing price if script is run after market hours.
- change: The change in price from the previous day's closing price.
- percent change: The percentage change in price from the previous day's closing price.

Here is an example of the JSON file structure:
```json
[
  {"stock": "ABC", 
  "price": "123.45", 
  "change": "+1.23", 
  "percent change": "+4.56%"
  }, 
  {"stock": "XYZ", 
  "price": "78.90", 
  "change": "+6.78", 
  "percent change": "+8.90%"
  }
]
```

## Notes

The web scraper fetches the data from a reliable source, but it's important to note that the accuracy and availability of the data depend on the website being scraped. If the website structure or layout changes, the scraper may need to be updated accordingly. Make sure to comply with the terms of service and usage policies of the website you are scraping. Always be respectful and responsible when scraping web data. This web scraper is provided for informational purposes only. It does not constitute financial advice or any recommendation to buy or sell securities. The stock information retrieved by this web scraper should not be considered as a basis for making investment decisions. Always perform your own research and consult with a qualified financial advisor before making any investment decisions. The accuracy and availability of the data obtained by this web scraper depend on the website being scraped, and there is no guarantee of its completeness or accuracy. By using this web scraper, you acknowledge and agree that the author and contributors are not responsible for any losses or damages incurred as a result of using the scraped data or relying on it for investment purposes.
