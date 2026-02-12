from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('poppu@gmail.com')

    user_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_input.fill('poppy')

    pass_input = page.get_by_test_id('registration-form-password-input').locator('input')
    pass_input.fill('poppy')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    context.storage_state(path='brwsr-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='brwsr-state.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    page.wait_for_timeout(5000)
