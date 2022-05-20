from playwright.sync_api import sync_playwright #module
dashboard = "https://reporting.egress.dev/home"
# content manager - Aim: open & close page
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3*1000) #600
    # headless creation of a browser object we can reference
    # note by default PW will always be headless, so we need to = to false to change

    # creating page objects  - for interrogation

    # GO TO URL
    page = browser.new_page()  # creation of a browser option
    # page.goto("https://sdx.egress.com/ui/signin.aspx?rt=https%3A%2F%2Fsso.esi.egress.dev%2Fauth%2Fticket&svc=samlsso&nonce=F0tCToVz-1QGbJO_r1OrFQ&post=1")
    page.goto('https://reporting.egress.dev/')

    # SIGN IN element by text
    page.click("text=Sign in")

    # ENTER USER EMAIL:
    # input id then data
    page.fill('input#tbEmail', 'reportingautomation@egress.com')
    page.fill('input#tbPassword', 'Egress.2020!')

    # Sign In button:
    page.click('a#btnLogin')

# verIfy success login via change in URL
    page.wait_for_url(dashboard)

    # Verify we can select from dropdown org
    # <div class="v-list-item__title">Egress Software Technologies</div>



  #  class ="v-list-item v-list-item--link theme--dark" > < div class ="v-list-item__content" > < div class ="v-list-item__title" > 021BA3A6-5522-4C8F-8012-946816480736 < / div > < / div > < / div >
     # locator - # value
    page.select_option('#v-list-item__title','Egress Software Technologies')