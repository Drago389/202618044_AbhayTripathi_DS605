import scrapy

class BooksSpider(scrapy.Spider):
    name = "books_scraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://toscrape.com"]
    
    def __init__(self, *args, **kwargs):
        super(BooksSpider, self).__init__(*args, **kwargs)
        self.page_count = 0
        self.max_pages = 5  # Limits crawl to a minimum of 5 catalog pages

    def parse(self, response):
        self.page_count += 1
        
        # Locate all book item cards on the current catalog listing page
        books = response.css("article.product_pod")
        for book in books:
            # Extract the partial relative URL and the category name
            book_url = book.css("h3 a::attr(href)").get()
            
            # Follow link into the individual detail page
            if book_url:
                yield response.follow(
                    book_url, 
                    callback=self.parse_book_details
                )
        
        # Follow pagination link up to the target catalog boundary limit
        if self.page_count < self.max_pages:
            next_page = response.css("li.next a::attr(href)").get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

    def parse_book_details(self, response):
        # Extract fields from the breadcrumbs loop and specific HTML nodes
        category = response.css(".breadcrumb li:nth-child(3) a::text").get()
        title = response.css(".product_main h1::text").get()
        price = response.css(".product_main .price_color::text").get()
        availability = response.css(".product_main .availability::text").get()
        
        # Parse the star rating from the class attributes (e.g., "star-rating Three")
        rating_classes = response.css(".product_main .star-rating::attr(class)").get()
        rating = rating_classes.replace("star-rating ", "") if rating_classes else None
        
        # Extract the description string
        description = response.css("#product_description ~ p::text").get()
        
        # Map values from the structured technical product specifications table
        table_rows = response.css("table.table-striped tr")
        product_info = {}
        for row in table_rows:
            key = row.css("th::text").get()
            val = row.css("td::text").get()
            if key and val:
                product_info[key.strip()] = val.strip()
                
        # Consolidate and strip whitespace data
        yield {
            "title": title.strip() if title else None,
            "category": category.strip() if category else None,
            "price": price.strip() if price else None,
            "rating": rating,
            "availability": "".join(availability.split()) if availability else None,
            "product_description": description.strip() if description else None,
            "UPC": product_info.get("UPC"),
            "number_of_reviews": product_info.get("Number of reviews"),
            "product_url": response.url,
        }
