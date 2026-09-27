#appModules/tcApi/common.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

from NVDAObjects import IAccessible
import winUser
from . import core

def IsUpdir() -> bool:
	match core.GetActivePanel():
		case core.TC_PANEL_LEFT:
			return core.IsLeftUpdir()
		case core.TC_PANEL_RIGHT:
			return core.IsRightUpdir()
		case _:
			return False

def GetHeaderHandle() -> int | None:
	match core.GetActivePanel():
		case core.TC_PANEL_LEFT:
			return core.GetLeftHeaderHandle()
		case core.TC_PANEL_RIGHT:
			return core.GetRightHeaderHandle()
		case _:
			return None

def GetCountItems() -> int | None:
	match core.GetActivePanel():
		case core.TC_PANEL_LEFT:
			return core.GetLeftCountItems()
		case core.TC_PANEL_RIGHT:
			return core.GetRightCountItems()
		case _:
			return None

def GetSelectedItems() -> int | None:
	match core.GetActivePanel():
		case core.TC_PANEL_LEFT:
			return core.GetLeftSelectedItems()
		case core.TC_PANEL_RIGHT:
			return core.GetRightSelectedItems()
		case _:
			return None

def GetCurrentItem() -> int | None:
	match core.GetActivePanel():
		case core.TC_PANEL_LEFT:
			return core.GetLeftCurrentItem()
		case core.TC_PANEL_RIGHT:
			return core.GetRightCurrentItem()
		case _:
			return None

def GetStatusBarHandle() -> int | None:
	match core.GetActivePanel():
		case core.TC_PANEL_LEFT:
			return core.GetLeftSizeHandle()
		case core.TC_PANEL_RIGHT:
			return core.GetRightSizeHandle()
		case _:
			return None

def GetStatusBarText() -> str:
	return GetStatusBarObject().displayText

def GetStatusBarObject() -> IAccessible.IAccessible:
	return IAccessible.getNVDAObjectFromEvent(GetStatusBarHandle(), winUser.OBJID_CLIENT, 0)

def GetTabListHandle() -> int | None:
	match core.GetActivePanel():
		case core.TC_PANEL_LEFT:
			return core.GetLeftTabsHandle()
		case core.TC_PANEL_RIGHT:
			return core.GetRightTabsHandle()
		case _:
			return None

def GetTabList() -> list[IAccessible.IAccessible] | None:
	hnd = GetTabListHandle()
	if hnd is None:
		return None
	items = IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
	if items is None:
		return None
	tabList = items.children
	tabs = []
	for tab in tabList:
		if tab.windowHandle == hnd and tab.name:
			tabs.append(tab)
	return tabs

def GetTabPosition(obj: IAccessible.IAccessible) -> dict[str, int] | None:
	items = obj.parent
	if items is None:
		return None

	tabs = []
	for tab in items.children:
		if tab.windowHandle == obj.windowHandle and tab.name:
			tabs.append(tab)

	index = obj.IAccessibleChildID
	for position, tab in enumerate(tabs, start=1):
		if tab.IAccessibleChildID == obj.IAccessibleChildID:
			index = position
			break

	return dict(indexInGroup=index, similarItemsInGroup=len(tabs))

def IsApiSupported() -> bool:
	return core.IsApiSupported()
