#Update module
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

import addonHandler
import wx
import gui
from gui import guiHelper
import threading
import webbrowser
try:
	import urllib2
except:
	import urllib
import json

addonHandler.initTranslation()
manifest = addonHandler.getCodeAddon().manifest
try:
	opener = urllib2.build_opener()
except NameError:
	opener = urllib.request.build_opener()

updateInfo = {"text":"", "currentVersion":manifest["version"], "newVersion":"", "getAddonUrl":"", "isAvailable":False}

def loadUpdateInfo():
	global updateInfo
	checkUrl = "https://api.github.com/repos/jawhien/extendedTotalCmd/releases"
	data = json.load(opener.open(checkUrl))
	latest = data[0]
	newVersion = latest["tag_name"]
	if newVersion > updateInfo["currentVersion"]:
		updateInfo["text"] = _("New version {version} is available. Do you want to download it?").format(version=newVersion)
		updateInfo["newVersion"] = newVersion
		updateInfo["getAddonUrl"] = "https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/"
		updateInfo["isAvailable"] = True
	else:
		updateInfo["text"] = _("No update available.")

def getAddon():
	webbrowser.open(updateInfo["getAddonUrl"])

def onCheckForUpdates(event):
	t = threading.Thread(target=update)
	t.daemon = True
	t.start()

def autoCheckForUpdates():
	t = threading.Timer(5.0, autoUpdate)
	t.daemon = True
	t.start()

def update():
	loadUpdateInfo()
	wx.CallAfter(tcAddonUpdateDialog, gui.mainFrame)

def autoUpdate():
	loadUpdateInfo()
	if updateInfo["isAvailable"]:
		dlg = wx.MessageDialog(gui.mainFrame, updateInfo["text"], _("Update Total Commander add-on"), wx.YES_NO | wx.ICON_QUESTION)
		if dlg.ShowModal() == wx.ID_YES:
			getAddon()
		dlg.Destroy()

class tcAddonUpdateDialog(wx.Dialog):

	def __init__(self,parent):
		super(tcAddonUpdateDialog,self).__init__(parent, title= _("Update Total Commander add-on"), size = (500, 700))
		self.sizerLayout = guiHelper.BoxSizerHelper(self, wx.VERTICAL)
		self.sizerLayout.addItem (wx.StaticText(self, label=updateInfo["text"]))
		self.buttons = guiHelper.ButtonHelper(wx.HORIZONTAL)
		if updateInfo["isAvailable"]:
			self.updateButton = self.buttons.addButton(self, wx.ID_OK, label=_("Get new version"))
			self.updateButton.Bind(wx.EVT_BUTTON, self.onUpdate)
		self.closeButton = self.buttons.addButton(self, wx.ID_CANCEL, label=_("Close"))
		self.buttonBar = self.sizerLayout.addDialogDismissButtons(self.buttons)
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.mainSizer.Add(self.sizerLayout.sizer, border=5, flag=wx.ALL)
		self.SetSizer(self.mainSizer)
		wx.CallAfter(self.Show)

	def onUpdate(self, event):
		getAddon()
		self.Destroy()


