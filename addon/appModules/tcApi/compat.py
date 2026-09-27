#appModules/tcApi/compat.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

from NVDAObjects import IAccessible
from . import common, core

def GetActivePanelNum() -> int | None:
	return core.GetActivePanel()

def getActivePanelNum() -> int | None:
	return core.GetActivePanel()

def isUpdir() -> bool:
	return common.IsUpdir()

def getHeaderHandle() -> int | None:
	return common.GetHeaderHandle()

def getCountElements() -> int | None:
	return common.GetCountItems()

def getSelectedElements() -> int | None:
	return common.GetSelectedItems()

def getCurrentElementNum() -> int | None:
	return common.GetCurrentItem()

def getStatusBarHandle() -> int | None:
	return common.GetStatusBarHandle()

def getStatusBarText() -> str:
	return common.GetStatusBarText()

def getStatusBarObject() -> IAccessible.IAccessible:
	return common.GetStatusBarObject()

def isApiSupported() -> bool:
	return common.IsApiSupported()

def getCurDirPanelHandle() -> int | None:
	return core.GetCurDirPanelHandle()

def getTabListHandle() -> int | None:
	return common.GetTabListHandle()

def getTabList() -> list[IAccessible.IAccessible] | None:
	return common.GetTabList()

def getTabListFromTab(obj: IAccessible.IAccessible) -> list[IAccessible.IAccessible]:
	items = obj.parent
	if items is None:
		return []
	tabList = items.children
	tabs = []
	for tab in tabList:
		if tab.windowHandle == obj.windowHandle and tab.name:
			tabs.append(tab)
	return tabs
