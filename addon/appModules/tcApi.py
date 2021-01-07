#appModules/tcApi.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

from ctypes import windll
from NVDAObjects import IAccessible
import winUser
import api

def sendMessage(param1, param2):
	user32 = windll.user32
	hnd = user32.GetForegroundWindow()
	return user32.SendMessageW(hnd, 1074, param1, param2)

def getLeftListHandle():
	return sendMessage(1, 0)

def getRightListHandle():
	return sendMessage(2, 0)

def getActiveListHandle():
	return sendMessage(3, 0)

def getActivePanelNum():
	return sendMessage(1000, 0)

def isUpdir():
	activePanel = getActivePanelNum()
	param1 = 1009 if activePanel == 1 else 1010
	updir = sendMessage(param1, 0)
	isUpdir = False if updir == 0 else True
	return isUpdir

def getCountElements():
	activePanel = getActivePanelNum()
	param1 = 1001 if activePanel == 1 else 1002
	count = sendMessage(param1, 0)
	if isUpdir():
		count -= 1
	return count

def getSelectedElements():
	activePanel = getActivePanelNum()
	param1 = 1005 if activePanel == 1 else 1006
	return sendMessage(param1, 0)

def getCurrentElementNum():
	activePanel = getActivePanelNum()
	param1 = 1007 if activePanel == 1 else 1008
	count = sendMessage(param1, 0)
	if isUpdir() == False:
		count += 1
	return count

def getStatusBarHandle():
	activePanel = getActivePanelNum()
	param1 = 7 if activePanel == 1 else 8
	return sendMessage(param1, 0)

def getAvailableSize():
	hnd = getStatusBarHandle()
	obj = IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
	text = obj.displayText
	if text.find('<') >= 0 or text.find('>') >= 0:
		return False
	else:
		return text

def getStatusBarText():
	return getStatusBarObject().displayText

def getStatusBarObject():
	return IAccessible.getNVDAObjectFromEvent(getStatusBarHandle(), winUser.OBJID_CLIENT, 0)

def isApiSupported():
	if getActivePanelNum() == 0:
		return False
	else:
		return True

def getCurDirPanelHandle():
	return sendMessage(21, 0)

def getTabListHandle():
	activePanel = getActivePanelNum()
	param1 = 26 if activePanel == 1 else 27
	return sendMessage(param1, 0)

def getTabList():
	hnd = getTabListHandle()
	items = IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
	if items == None:
		return False
	tabList = items.children
	output = []
	for tab in tabList:
		if tab.windowHandle == hnd:
			output.append(tab)
	return output

def getTabListFromTab(obj):
	items = obj.parent
	if items == None:
		return False
	tabList = items.children
	output = []
	for tab in tabList:
		if tab.windowHandle == obj.windowHandle:
			output.append(tab)
	return output
