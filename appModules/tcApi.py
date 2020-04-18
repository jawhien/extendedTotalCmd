#appModules/tcApi.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

from ctypes import windll
from NVDAObjects import IAccessible
import winUser
import api

class tcApi():

	def sendMessage(self, param1, param2):
		user32 = windll.user32
		hnd = user32.GetForegroundWindow()
		value = user32.SendMessageW(hnd, 1074, param1, param2)
		return value

	def getLeftListHandle(self):
		left = self.sendMessage(1, 0)
		return left

	def getRightListHandle(self):
		right = self.sendMessage(2, 0)
		return right

	def getActiveListHandle(self):
		active = self.sendMessage(3, 0)
		return active

	def getActivePanelNum(self):
		panel = self.sendMessage(1000, 0)
		return panel

	def isUpdir(self):
		activePanel = self.getActivePanelNum()
		param1 = 1009 if activePanel == 1 else 1010
		updir = self.sendMessage(param1, 0)
		isUpdir = False if updir == 0 else True
		return isUpdir

	def getCountElements(self):
		activePanel = self.getActivePanelNum()
		param1 = 1001 if activePanel == 1 else 1002
		count = self.sendMessage(param1, 0)
		if self.isUpdir():
			count -= 1
		return count

	def getSelectedElements(self):
		activePanel = self.getActivePanelNum()
		param1 = 1005 if activePanel == 1 else 1006
		count = self.sendMessage(param1, 0)
		return count

	def getCurrentElementNum(self):
		activePanel = self.getActivePanelNum()
		param1 = 1007 if activePanel == 1 else 1008
		count = self.sendMessage(param1, 0)
		if self.isUpdir() == False:
			count += 1
		return count

	def getSizeHandle(self):
		activePanel = self.getActivePanelNum()
		param1 = 7 if activePanel == 1 else 8
		hnd = self.sendMessage(param1, 0)
		return hnd

	def getAvailableSize(self):
		hnd = self.getSizeHandle()
		obj = IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
		text = obj.displayText
		if text.find('<') >= 0 or text.find('>') >= 0:
			return False
		else:
			return text

	def isApiSupported(self):
		if self.getActivePanelNum() == 0:
			return False
		else:
			return True

	def getCurDirPanelHandle(self):
		return self.sendMessage(21, 0)

	def getTabListHandle(self):
		activePanel = self.getActivePanelNum()
		param1 = 26 if activePanel == 1 else 27
		hnd = self.sendMessage(param1, 0)
		return hnd

	def getTabList(self):
		hnd = self.getTabListHandle()
		items = IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
		if items == None:
			return False
		tabList = items.children
		output = []
		for tab in tabList:
			if tab.windowHandle == hnd:
				output.append(tab)
		return output

	def getTabListFromTab(self, obj):
		items = obj.parent
		if items == None:
			return False
		tabList = items.children
		output = []
		for tab in tabList:
			if tab.windowHandle == obj.windowHandle:
				output.append(tab)
		return output
