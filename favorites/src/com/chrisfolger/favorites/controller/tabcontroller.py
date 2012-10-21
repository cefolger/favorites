import mainviewcontroller

tabView = None
logger = None

def start(tabview):
    global tabView
    global logger
    tabView = tabview
    logger = tabView.logger

def show_page(page):
    tabView.show_page(page)

def save_page(page):
    mainviewcontroller.save(page.item, page=page)
