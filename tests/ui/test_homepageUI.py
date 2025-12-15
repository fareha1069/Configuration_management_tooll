def test_homepage_loads(browser):
    browser.get("http://localhost:3000")
    assert "Helm" in browser.page_source
