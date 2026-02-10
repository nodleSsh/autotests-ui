from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login', wait_until='networkidle')

    # unknow = page.locator('#unknow')
    # expect(unknow).to_be_visible()

    # btn = page.get_by_test_id('login-form-password-input')
    # btn.fill('text')

    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'text erea'
        """
    )