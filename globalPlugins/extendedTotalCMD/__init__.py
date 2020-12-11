#Update module
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

import globalPluginHandler
import gui
import wx
import addonHandler
from . import updater
import config

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.tools = gui.mainFrame.sysTrayIcon.toolsMenu
		self.tcUpdater = self.tools.Append(wx.ID_ANY, _("Update Total Commander add-on..."), _("Update Total Commander add-on..."))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, updater.onCheckForUpdates, self.tcUpdater)
		if config.conf['update']['autoCheck'] == True:
			updater.autoCheckForUpdates()

	def terminate(self):
		self.tools.Remove(self.tcUpdater)
