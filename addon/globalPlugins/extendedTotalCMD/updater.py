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
from languageHandler import getLanguage
try:
	import urllib2
except:
	import urllib
import json
from versionInfo import version_year, version_major

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
	try:
		data = json.load(opener.open(checkUrl))
	except:
		updateInfo["text"] = _("An error occurred while checking for updates! Check your internet connection.")
		return
	latest = data[0]
	newVersion = latest["tag_name"]
	if newVersion >= "3.0" and (version_year, version_major) < (2018, 3):
		updateInfo["text"] = _("To install the new version of the add-on, you need NVDA 2018.3 or higher.")
		return
# check which release is currently available. If we have a version with the "dev" index, we must make sure that the same or a newer release is available, otherwise the versions with the "dev" index will not be updated.
	if (newVersion > updateInfo["currentVersion"]) or (updateInfo["currentVersion"].find("-dev") and updateInfo["currentVersion"].rstrip("-dev") <= newVersion):
		updateInfo["text"] = _("New version {version} is available. Do you want to download it?").format(version=newVersion)
		updateInfo["newVersion"] = newVersion
		lang = getLanguage().split("_")[0]
		if lang != "en" and lang != "ru": lang = "en"
		updateInfo["getAddonUrl"] = "https://jnsoft.ru/{locale}/articles/nvda/extendedTotalCmd/".format(locale=lang)
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
	t = threading.Timer(3.0, autoUpdate)
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


