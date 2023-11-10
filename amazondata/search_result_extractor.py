from selectorlib import Extractor
import requests

YAML_STRING = """
products:
    css: 'div[data-component-type="s-search-result"]'
    xpath: null
    multiple: true
    type: Text
    children:
        title:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Text
        url:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Link
        rating:
            css: 'div.a-row.a-size-small span:nth-of-type(1)'
            xpath: null
            type: Attribute
            attribute: aria-label
        number_of_ratings:
            css: 'div.a-row.a-size-small span:nth-of-type(2)'
            xpath: null
            type: Attribute
            attribute: aria-label
        price:
            css: 'span.a-price:nth-of-type(1) span.a-offscreen'
            xpath: null
            type: Text
        is_sponsored:
            css: span.s-label-popover-default
            xpath: null
            type: Text
"""


class SearchResultExtractor:
    def __init__(self):
        self._amazon_product_extractor = Extractor.from_yaml_string(YAML_STRING)

    def __scrape(self, url, headers):
        if not headers:
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

        r = requests.get(url, headers=headers)

        if r.status_code > 500:
            raise Exception(
                "Page %s was blocked by Amazon. Please try using better proxies." % url
            )
        else:
            return self._amazon_product_extractor.extract(r.text)

    def __extract_search_results(self, html_code):
        return self._amazon_product_extractor.extract(html_code)

    def __process_rating(self, data):
        if "rating" in data:
            rating = data["rating"]

            if rating:
                rating = rating.replace("out of 5 stars", "").strip()

            return rating
        return None

    def __process_number_of_ratings(self, data):
        if "number_of_ratings" in data:
            number_of_ratings = data["number_of_ratings"]

            if number_of_ratings:
                number_of_ratings = int(number_of_ratings.replace(",", "").strip())

            return number_of_ratings
        return None

    def __process_is_sponsored(self, data):
        if "is_sponsored" in data:
            is_sponsored = data["is_sponsored"]
            if is_sponsored == "Sponsored":
                return True

        return False

    def __process_url(self, data):
        if "url" in data:
            url = data["url"]

            if url:
                url = "https://www.amazon.in" + url

            return url
        return None

    def __process_data(self, data):
        for product in data["products"]:
            product["rating"] = self.__process_rating(product)
            product["number_of_ratings"] = self.__process_number_of_ratings(product)
            product["is_sponsored"] = self.__process_is_sponsored(product)
            product["url"] = self.__process_url(product)

        return data

    def search(self, query, page=1, headers=None):
        url = "https://www.amazon.in/s?k=" + query + "&page=" + str(page)
        data = self.__scrape(url, headers)
        processed_data = self.__process_data(data)
        return processed_data

    def extract_search_results(self, html_code):
        data = self.__extract_search_results(html_code)
        processed_data = self.__process_data(data)
        return processed_data
