def test_google_search(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title

def test_bing_search(browser):
    browser.get("https://www.bing.com")
    assert "Bing" in browser.title
