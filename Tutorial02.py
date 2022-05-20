from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# content manager - Aim: open & close page
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    # headless creation of a browser object we can reference
    # note by default PW will always be headless, so we need to = to false to change

    # creating page objects  - for interrogation

    # 1.  GO TO URL
    page = browser.new_page()
    page.goto('https://demo.opencart.com/admin')

    # 2. ENTER AUTHENTICATION
    # CSS: input#input-username           (sendkeys)
    page.fill('input#input-username', 'demo')
    # CSS: input#input-password           (sendkeys)
    page.fill('input#input-password', 'demo')

    # 3. CLICK LOGIN
    # CSS: <button type="submit" class="btn btn-primary"><i class="fa fa-key"></i> Login</button>
    # Using the input type as our css selector
    page.click('button[type=submit]')

    # WEB SCRAPING USING "BEAUTIFUL SOUP" (HTML PARSER)

    # >>>>> Additional: only show when a certain element is visible/found
    page.is_visible('div.tile-body')

    # Pull in data
    html = page.inner_html('#content')  # from the url elements
    # PRINT pulled data
    print(html)

    # Creation of a SOUP Object that we can work & parse with

    html = page.inner_html('#content')
    soup = BeautifulSoup(html, 'html.parser')

    # test cases - pull total orders
    total_orders = soup.find(('h2', {'class': 'pull-right'})).text
