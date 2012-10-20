import wx
from view.mainview import MainView

app = wx.App(False)
frame = MainView(None, 'Small editor')
app.MainLoop()