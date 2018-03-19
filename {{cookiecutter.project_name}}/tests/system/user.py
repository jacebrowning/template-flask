site = None
browser = None


def visit(path):
    browser.visit(site + path)


def goto_home():
    visit("/")
