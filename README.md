# amazondata

[![PyPI version](https://badge.fury.io/py/amazondata.svg)](https://badge.fury.io/py/amazondata)

A python package to get amazon product and search data in json form. The package does not require any API keys as it works by scraping the amazon page.

Reference: [How To Scrape Amazon Product Details and Pricing using Python](https://medium.com/scrapehero/tutorial-how-to-scrape-amazon-product-details-using-python-56d40e7503b7)

## Install

```
pip install amazondata
```

## Usage

To get Amazon product details from the url, use the following function.

### get_product_from_url(url)

```python
from amazondata.product_details_extractor import ProductDetailsExtractor

product_details_extractor = ProductDetailsExtractor()

data = product_details_extractor.get_product_from_url('https://www.amazon.in/dp/B09JSYVNZ2')

print(data)
```

To get Amazon product details from the ASIN (Amazon Standard Identification Number) code, use the following function.

### get_product_from_asin_code(asin_code)

```python
from amazondata.product_details_extractor import ProductDetailsExtractor

product_details_extractor = ProductDetailsExtractor()

data = product_details_extractor.get_product_from_asin_code('B09JSYVNZ2')

print(data)
```

To get the list of products from search query use the following function

### search(query, page)

```python
from amazondata.search_result_extractor import SearchResultExtractor

search_result_extractor = SearchResultExtractor()

data = search_result_extractor.search('perfume for men', 3)

print(data)

```

NOTE: Optionally, you can pass custom `headers` to all these functions. The default headers value is:

```python
headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Sec-Fetch-Site": "none",
            "Host": "www.amazon.in",
            "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
            "Sec-Fetch-Mode": "navigate",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Priority": "u=0, i",
        }
```

In case the the scraper gets blocked from Amazon, you can fetch the html code using selenium and pass the html code to the following function

```python
data = search_result_extractor.extract_search_results(html_code)
```

```python
data = product_details_extractor.extract_product_details(html_code)
```
