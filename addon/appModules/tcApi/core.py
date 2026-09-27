#appModules/tcApi/core.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

import ctypes
from ctypes import windll
import winUser
import api

user32 = windll.user32

# constants
TC_API_MSG = winUser.WM_USER + 50

# Query handles
# TC 9.0+
TC_QUERY_LEFT_LIST_HND = 1
TC_QUERY_RIGHT_LIST_HND = 2
TC_QUERY_ACTIVE_LIST_HND = 3
TC_QUERY_INACTIVE_LIST_HND = 4
TC_QUERY_LEFT_HEADER_HND = 5
TC_QUERY_RIGHT_HEADER_HND = 6
TC_QUERY_LEFT_SIZE_HND = 7
TC_QUERY_RIGHT_SIZE_HND = 8
TC_QUERY_LEFT_PATH_HND = 9
TC_QUERY_RIGHT_PATH_HND = 10
TC_QUERY_LEFT_INFO_HND = 11
TC_QUERY_RIGHT_INFO_HND = 12
TC_QUERY_LEFT_DRIVES_HND = 13
TC_QUERY_RIGHT_DRIVES_HND = 14
TC_QUERY_LEFT_PANEL_HND = 15
TC_QUERY_RIGHT_PANEL_HND = 16
TC_QUERY_BOTTOM_PANEL_HND = 17
TC_QUERY_LEFT_TREE_HND = 18
TC_QUERY_RIGHT_TREE_HND = 19
TC_QUERY_CMD_LINE_HND = 20
TC_QUERY_CUR_DIR_PANEL_HND = 21
TC_QUERY_INPLACE_EDIT_HND = 22
TC_QUERY_SPLIT_PANEL_HND = 23
TC_QUERY_LEFT_DRIVE_PANEL_HND = 24
TC_QUERY_RIGHT_DRIVE_PANEL_HND = 25
TC_QUERY_LEFT_TABS_HND = 26
TC_QUERY_RIGHT_TABS_HND = 27
TC_QUERY_BUTTON_BAR_HND = 28
TC_QUERY_BUTTON_BAR_VERT_HND = 29
# TC 11.57+
TC_QUERY_QUICK_VIEW_HND = 1028

# Panel queries
# TC 9.0+
TC_ACTIVE_PANEL = 1000
TC_LEFT_COUNT = 1001
TC_RIGHT_COUNT = 1002
TC_LEFT_TOTAL_COUNT = 1003
TC_RIGHT_TOTAL_COUNT = 1004
TC_LEFT_SEL_COUNT = 1005
TC_RIGHT_SEL_COUNT = 1006
TC_LEFT_CUR_IDX = 1007
TC_RIGHT_CUR_IDX = 1008
TC_LEFT_UPDIR = 1009
TC_RIGHT_UPDIR = 1010
TC_LEFT_FIRST_FILE_IDX = 1011
TC_RIGHT_FIRST_FILE_IDX = 1012
# TC 11.56+
TC_LEFT_SORT_ORDER = 1013
TC_RIGHT_SORT_ORDER = 1014
TC_LEFT_VIEW_MODE = 1015
TC_RIGHT_VIEW_MODE = 1016
# TC 11.57+
TC_LEFT_SEL_DIRS = 1017
TC_RIGHT_SEL_DIRS = 1018
TC_LEFT_SEL_FILES = 1019
TC_RIGHT_SEL_FILES = 1020
TC_LEFT_LIST_TYPE = 1021
TC_RIGHT_LIST_TYPE = 1022
TC_LEFT_ARCHIVE_LEN = 1023
TC_RIGHT_ARCHIVE_LEN = 1024
TC_LEFT_FS_TYPE = 1025
TC_RIGHT_FS_TYPE = 1026
TC_QUICK_VIEW_STATUS = 1027

# Return codes
# TC 11.56+: view mode codes (1015/1016)
TC_VIEW_BRIEF = 0
TC_VIEW_FULL = 1
TC_VIEW_TREE = 2
TC_VIEW_COMMENTS = 4
TC_VIEW_THUMBNAILS = 5
# TC 11.57+: list type codes (1021/1022)
TC_LIST_NORMAL = 0
TC_LIST_SEARCH = 1
TC_LIST_DUPLICATES = 2
# TC 11.57+: archive type codes (1025/1026)
TC_ARCHIVE_NONE = 0
TC_ARCHIVE_ZIP = 1
TC_ARCHIVE_ARJ = 2
TC_ARCHIVE_LHA = 3
TC_ARCHIVE_RAR = 4
TC_ARCHIVE_UC2 = 5
TC_ARCHIVE_GZIP = 8
TC_ARCHIVE_TAR = 9
TC_ARCHIVE_CAB = 10
TC_ARCHIVE_ACE = 11
TC_ARCHIVE_7ZIP = 13
TC_ARCHIVE_ZSTD = 14
TC_ARCHIVE_BROTLI = 15
# TC 11.57+: file system type codes (1025/1026)
TC_FS_REGULAR = 0
TC_FS_FTP = 100
TC_FS_PLUGIN = 101
TC_FS_VIRTUAL = 102
TC_FS_DESKTOP = 103
TC_FS_NETWORK = 104
TC_FS_COMPUTER = 105
TC_FS_RECYCLE_BIN = 106
# TC 11.57+: Quick View status codes (1027)
TC_QUICK_VIEW_NONE = 0
TC_QUICK_VIEW_LEFT = 1
TC_QUICK_VIEW_RIGHT = 2
TC_QUICK_VIEW_SEPARATE = 3

# flags
SMTO_ABORTIFHUNG = 2
TIMEOUT = 100 # ms

# API layers
TC_API_UNSUPPORTED = 0
TC_API_9_0 = 1
TC_API_11_56 = 2
TC_API_11_57 = 3

# Panel codes
TC_PANEL_LEFT = 1
TC_PANEL_RIGHT = 2

def SendMessage(wParam: int, lParam: int = 0, timeout: int = TIMEOUT) -> int | None:
	hnd = user32.GetForegroundWindow()
	result = ctypes.c_ulong()
	success = user32.SendMessageTimeoutW(hnd, TC_API_MSG, wParam, lParam, SMTO_ABORTIFHUNG, timeout, ctypes.byref(result))

	if success == 0:
		return None

	return result.value

def GetLeftListHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_LIST_HND)

def GetRightListHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_LIST_HND)

def GetActiveListHandle() -> int | None:
	return SendMessage(TC_QUERY_ACTIVE_LIST_HND)

def GetInactiveListHandle() -> int | None:
	return SendMessage(TC_QUERY_INACTIVE_LIST_HND)

def GetLeftHeaderHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_HEADER_HND)

def GetRightHeaderHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_HEADER_HND)

def GetLeftSizeHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_SIZE_HND)

def GetRightSizeHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_SIZE_HND)

def GetLeftPathHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_PATH_HND)

def GetRightPathHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_PATH_HND)

def GetLeftInfoHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_INFO_HND)

def GetRightInfoHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_INFO_HND)

def GetLeftDrivesHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_DRIVES_HND)

def GetRightDrivesHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_DRIVES_HND)

def GetLeftPanelHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_PANEL_HND)

def GetRightPanelHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_PANEL_HND)

def GetLeftTreeHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_TREE_HND)

def GetRightTreeHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_TREE_HND)

def GetLeftDrivePanelHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_DRIVE_PANEL_HND)

def GetRightDrivePanelHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_DRIVE_PANEL_HND)

def GetLeftTabsHandle() -> int | None:
	return SendMessage(TC_QUERY_LEFT_TABS_HND)

def GetRightTabsHandle() -> int | None:
	return SendMessage(TC_QUERY_RIGHT_TABS_HND)

def GetBottomPanelHandle() -> int | None:
	return SendMessage(TC_QUERY_BOTTOM_PANEL_HND)

def GetCmdLineHandle() -> int | None:
	return SendMessage(TC_QUERY_CMD_LINE_HND)

def GetCurDirPanelHandle() -> int | None:
	return SendMessage(TC_QUERY_CUR_DIR_PANEL_HND)

def GetInplaceEditHandle() -> int | None:
	return SendMessage(TC_QUERY_INPLACE_EDIT_HND)

def GetSplitPanelHandle() -> int | None:
	return SendMessage(TC_QUERY_SPLIT_PANEL_HND)

def GetButtonBarHandle() -> int | None:
	return SendMessage(TC_QUERY_BUTTON_BAR_HND)

def GetButtonBarVerticalHandle() -> int | None:
	return SendMessage(TC_QUERY_BUTTON_BAR_VERT_HND)

def GetActivePanel() -> int | None:
	return SendMessage(TC_ACTIVE_PANEL)

def IsLeftUpdir() -> bool:
	return bool(SendMessage(TC_LEFT_UPDIR))

def IsRightUpdir() -> bool:
	return bool(SendMessage(TC_RIGHT_UPDIR))

def GetLeftCountItems() -> int | None:
	count = SendMessage(TC_LEFT_COUNT)
	if count is not None and IsLeftUpdir():
		count -= 1
	return count

def GetRightCountItems() -> int | None:
	count = SendMessage(TC_RIGHT_COUNT)
	if count is not None and IsRightUpdir():
		count -= 1
	return count

def GetLeftTotalCountElements() -> int | None:
	return SendMessage(TC_LEFT_TOTAL_COUNT)

def GetRightTotalCountElements() -> int | None:
	return SendMessage(TC_RIGHT_TOTAL_COUNT)

def GetLeftSelectedItems() -> int | None:
	return SendMessage(TC_LEFT_SEL_COUNT)

def GetRightSelectedItems() -> int | None:
	return SendMessage(TC_RIGHT_SEL_COUNT)

def GetLeftCurrentItem() -> int | None:
	count = SendMessage(TC_LEFT_CUR_IDX)
	if count is not None and not IsLeftUpdir():
		count += 1
	return count

def GetRightCurrentItem() -> int | None:
	count = SendMessage(TC_RIGHT_CUR_IDX)
	if count is not None and not IsRightUpdir():
		count += 1
	return count

def GetLeftFirstFileIndex() -> int | None:
	return SendMessage(TC_LEFT_FIRST_FILE_IDX)

def GetRightFirstFileIndex() -> int | None:
	return SendMessage(TC_RIGHT_FIRST_FILE_IDX)

def GetLeftFsType() -> int | None:
	return SendMessage(TC_LEFT_FS_TYPE)

def GetRightFsType() -> int | None:
	return SendMessage(TC_RIGHT_FS_TYPE)

def GetLeftArchiveNameLength() -> int | None:
	return SendMessage(TC_LEFT_ARCHIVE_LEN)

def GetRightArchiveNameLength() -> int | None:
	return SendMessage(TC_RIGHT_ARCHIVE_LEN)

def GetQuickViewHandle() -> int | None:
	return SendMessage(TC_QUERY_QUICK_VIEW_HND)

def GetQuickViewStatus() -> int | None:
	return SendMessage(TC_QUICK_VIEW_STATUS)

def GetLeftSortOrder() -> int | None:
	return SendMessage(TC_LEFT_SORT_ORDER)

def GetRightSortOrder() -> int | None:
	return SendMessage(TC_RIGHT_SORT_ORDER)

def GetLeftViewMode() -> int | None:
	return SendMessage(TC_LEFT_VIEW_MODE)

def GetRightViewMode() -> int | None:
	return SendMessage(TC_RIGHT_VIEW_MODE)

def GetLeftSelectedDirs() -> int | None:
	return SendMessage(TC_LEFT_SEL_DIRS)

def GetRightSelectedDirs() -> int | None:
	return SendMessage(TC_RIGHT_SEL_DIRS)

def GetLeftSelectedFiles() -> int | None:
	return SendMessage(TC_LEFT_SEL_FILES)

def GetRightSelectedFiles() -> int | None:
	return SendMessage(TC_RIGHT_SEL_FILES)

def GetLeftListType() -> int | None:
	return SendMessage(TC_LEFT_LIST_TYPE)

def GetRightListType() -> int | None:
	return SendMessage(TC_RIGHT_LIST_TYPE)

def IsApiSupported() -> bool:
	activePanel = GetActivePanel()
	return activePanel in (TC_PANEL_LEFT, TC_PANEL_RIGHT)

def _ParseVersion(versionString: str) -> tuple[int, ...] | None:
	parts = []
	for part in versionString.replace(",", ".").split("."):
		if not part.isdigit():
			break
		parts.append(int(part))

	if not parts:
		return None

	return tuple(parts)

def _GetTotalCommanderVersion() -> tuple[int, ...] | None:
	try:
		return _ParseVersion(api.getForegroundObject().appModule.productVersion)
	except (AttributeError, TypeError):
		return None

def GetApiLayer() -> int:
	if not IsApiSupported():
		return TC_API_UNSUPPORTED

	tcVersion = _GetTotalCommanderVersion()
	if tcVersion is not None:
		if tcVersion >= (11, 57):
			return TC_API_11_57
		if tcVersion >= (11, 56):
			return TC_API_11_56

	sortOrder = GetLeftSortOrder()
	if sortOrder is not None and sortOrder != 0:
		return TC_API_11_56

	return TC_API_9_0
