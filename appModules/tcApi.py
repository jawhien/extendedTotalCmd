
from ctypes import windll
from NVDAObjects.IAccessible import IAccessible
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

	def isCurrentFolder(self):
		hnd = self.getSizeHandle()
		obj = IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
		text = obj.displayText
		if textInfo.find('<') >= 0 or textInfo.find('>') >= 0:
			return True
		else:
			return False

	def isApiSupported(self):
		obj = api.getFocusObject()
		version = int(obj.appModule.productVersion.split(".")[0])
		if version >= 9:
			return True
		else:
			return False
