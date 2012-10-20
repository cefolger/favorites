import wx

class MainView(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))

        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY)
        self.secondButton = wx.Button(self, -1, 'foo two')
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.treeCtrl, 1, wx.EXPAND)
        self.sizer.Add(self.secondButton, 3, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        #self.sizer.Fit(self)        
        self.Show(True)
    
    def setFavorites(self, favoritesRoot):
        self.rootId = self.treeCtrl.AddRoot(favoritesRoot.label)
        self.addChildren(favoritesRoot, self.rootId)
    
    def addChildren(self, node, parentId):
        for child in node.children:
            childId = self.treeCtrl.AppendItem(parentId, child.label)
            self.addChildren(child, childId)
        