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
import urllib
import json
from versionInfo import version_year, version_major

addonHandler.initTranslation()
manifest = addonHandler.getCodeAddon().manifest

try:
	opener = urllib.request.urlopen
except AttributeError:
	opener = urllib.urlopen

updateInfo = {"text":"", "currentVersion":manifest["version"], "newVersion":"", "getAddonUrl":"", "downloadUrl":"", "size":"", "FileName":"", "isAvailable":False}

def loadUpdateInfo():
	global updateInfo
	checkUrl = "https://api.github.com/repos/jawhien/extendedTotalCmd/releases"
	try:
		data = json.load(opener(checkUrl))
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
		for asset in latest["assets"]:
			if asset["content_type"] == "application/x-nvda-addon":
				updateInfo["downloadUrl"] = asset["browser_download_url"]
				updateInfo["size"] = asset["size"]
				updateInfo["FileName"] = asset["name"]
				break

		updateInfo["isAvailable"] = True
	else:
		updateInfo["text"] = _("No update available.")

def getAddon():
	import tempfile, os
	addon = opener(updateInfo["downloadUrl"])
	content = addon.read()
	addon.close()
	if updateInfo["size"] != len(content):
		gui.messageBox(_("Data load error"), _("Error"), style=wx.OK|wx.ICON_ERROR)
		return
	fd,path = tempfile.mkstemp(".nvda-addon", "tcmd_addon_update-")
	with open(path, "wb") as file:
		file.write(content)
	import core
	bundle = addonHandler.AddonBundle(path)
	try:
		if not addonHandler.addonVersionCheck.isAddonCompatible(bundle):
			gui.messageBox(_("This version of NVDA is incompatible. To install the add-on, NVDA version {year}.{major} or higher is required. Please update NVDA or download an older version of the add-on here: \n{link}").format(year=bundle.minimumNVDAVersion[0], major=bundle.minimumNVDAVersion[1], link="https://github.com/jawhien/extendedTotalCmd/releases/tag/2.5"), _("Error"), style=wx.OK|wx.ICON_ERROR)
			os.close(fd)
			os.unlink(path)
			return
	except:
		pass
	gui.ExecAndPump(addonHandler.installAddonBundle, bundle)
	for addon in addonHandler.getAvailableAddons():
		if not addon.isPendingRemove and manifest["name"].lower() == addon.manifest["name"].lower():
			addon.requestRemove()
			break
	os.close(fd)
	os.unlink(path)
	if gui.messageBox(_("Changes were made to add-ons. You must restart NVDA for these changes to take effect. Would you like to restart now?"), _("Restart NVDA"), style=wx.YES|wx.NO|wx.ICON_WARNING) == wx.YES: core.restart()

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


