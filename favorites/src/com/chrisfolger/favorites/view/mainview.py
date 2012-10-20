import wx

class MainView(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))

        
        self.firstButton = wx.TreeCtrl(self, wx.ID_ANY)
        id = self.firstButton.AddRoot('hello')
        self.firstButton.AppendItem(id, 'foo')
        self.secondButton = wx.Button(self, -1, 'foo two')
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.firstButton, 1, wx.EXPAND)
        self.sizer.Add(self.secondButton, 3, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        #self.sizer.Fit(self)        
        self.Show(True)