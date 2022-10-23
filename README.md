# amazondata

A python package to get amazon product and search data in json form. The package does not require any API keys as it works by scraping the amazon page.

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


