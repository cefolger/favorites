import wx
from view.mainview import MainView
from controller.mainviewcontroller import start

app = wx.App(False)
frame = MainView(None, 'Small editor')
start(frame)
app.MainLoop()