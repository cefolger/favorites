import wx
from pages import HtmlFavoritePage

class MainView(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
        self.treeCtrl = wx.TreeCtrl(self, wx.ID_ANY)
        self.tabCtrl = wx.Notebook(self)
        
        page1 = HtmlFavoritePage(self.tabCtrl)
        self.tabCtrl.AddPage(page1, 'test page')
        
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.treeCtrl, 1, wx.EXPAND)
        self.sizer.Add(self.tabCtrl, 3, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)
        self.Show(True)
    
    def set_favorites(self, favoritesRoot):
        self.rootId = self.treeCtrl.AddRoot(favoritesRoot.label)
        self.add_children(favoritesRoot, self.rootId)
    
    def add_children(self, node, parentId):
        for child in node.children:
            childId = self.treeCtrl.AppendItem(parentId, child.label)
            self.add_children(child, childId)
        