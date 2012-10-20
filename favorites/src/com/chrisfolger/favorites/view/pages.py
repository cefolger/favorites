import wx

class HtmlFavoritePage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        wx.StaticText(self, -1, "This is a PageThree object", (60, 60))
