from playwright.sync_api import sync_playwright, expect, Request, Response


def log_request(request: Request):
    print(f'Request: {request.url}')

def log_response(response: Response):
    print(f'Response: {response.url} status: {response.status}')



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request', log_request)
    # page.remove_listener('request', log_request)
    page.on('response', log_response)

    page.wait_for_timeout(5000)





















# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://insurance.delivery.tst.yandex.ru/account?storefrontId=interco_market&insuranceContractId=insuranceContract_3286bb1ecd6e4b9d87cebd6bc2111eed')
#
#     add_user_button = page.get_by_test_id('split-add-user-more-button')
#     add_user_button.click()
#
#     to_login_button = page.get_by_test_id('menu-option-switchToLogin')
#     to_login_button.click()
#
#     email_input = page.get_by_test_id('text-field-input')
#     email_input.fill('yndx-insurance-caretool')
#
#     add_user_next_button = page.get_by_test_id('split-add-user-next-login')
#     add_user_next_button.click()
#
#     password_input = page.get_by_test_id('password-input').locator('input')
#     password_input.fill('QNKa.7mbj')
#
#     password_next_button = page.get_by_test_id('password-next')
#     password_next_button.click()
#
#     page.on('request', log_request)
#     page.on('response', log_response)
#
#     page.wait_for_timeout(5000)