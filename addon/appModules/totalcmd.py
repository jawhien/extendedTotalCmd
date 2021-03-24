#appModules/totalcmd.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

import appModuleHandler
import addonHandler
import api
import NVDAObjects
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.IAccessible import sysListView32
import speech
import controlTypes
import winsound
import re
import ui
import winUser
import scriptHandler
from scriptHandler import script
import threading
from . import tcApi
import config
import eventHandler
import os
from tones import beep
from time import sleep

addonHandler.initTranslation()

manifest = addonHandler.getCodeAddon().manifest

oldActivePannel=0
activePannel=1
currentTab = 0
isMultiColumn = False

class getTCInfo():

	def formatSize(self, size):
		formats = [_("Bytes"), _("kB"), _("mB"), _("gB"), _("tB")]
		i = 0
		while size >= 1024:
			if not formats[i + 1]: break
			size = size / 1024;
			i += 1
		if isinstance(size, float): size = int(size * 100) / 100
		return "{size} {format}".format(size=size, format=formats[i])

	def threadMonitor(self, thread):
		i = 0
		while thread.isAlive():
			sleep(0.1)
			i += 1
			if i == 10:
				beep(250, 90)
				i = 0

	def getCurrentDirPath(self):
		return NVDAObjects.IAccessible.getNVDAObjectFromEvent(tcApi.getCurDirPanelHandle(), winUser.OBJID_CLIENT, 0).name[:-1]

	def getSingleFileSize(self):
		currentDir = self.getCurrentDirPath()
		name = api.getFocusObject().name.split("\t")[0]
		path = os.path.join(currentDir, name)
		statusbar = tcApi.getStatusBarText()
		if currentDir.startswith("\\\\") and not re.findall(r'<\S*[\s>]', statusbar) and re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{2}', statusbar):
			return self.getSingleFileSizeFromStatusbar(statusbar)
		elif currentDir.startswith("\\\\"):
			return _("This object is not supported.")
		elif re.match(r'[0-9]+:/', currentDir) and not re.findall(r'<\S*[\s>]', statusbar):
			return self.getSingleFileSizeFromStatusbar(statusbar)
		elif re.match(r'[0-9]+:/', currentDir) and re.findall(r'<\S*[\s>]', statusbar):
			return _("No size information. Try select this item.")
		elif os.path.isfile(path):
			return self.formatSize(os.path.getsize(path))
		elif os.path.isdir(path):
			threads = threading.enumerate()
			for thr in threads:
				if thr.getName() == path: return _("The size is calculated, wait a few seconds...")
			t1 = threading.Thread(name=path, target=self.speakSingleDirectorySize, args=(path,))
			t1.start()
			monitor = threading.Thread(name="monitor", target=self.threadMonitor, args=(t1,))
			monitor.start()
			return None
		else:
			return _("No size information. Try select this item.")

	def speakSingleDirectorySize(self, path):
		totalSize = 0
		for dirpath, dirnames, filenames in os.walk(path):
			for f in filenames:
				fp = os.path.join(dirpath, f)
				try:
					totalSize += os.path.getsize(fp)
				except:
					pass
		ui.message(self.formatSize(totalSize))

	def getSingleFileSizeFromStatusbar(self, str):
		size = re.sub(r'[0-9]{2}\.[0-9]{2}\.[0-9]{2}.*', '', str).strip()
		if size[-1:].isdigit():
			return self.convertSizeFromBytes(re.sub(r'[^0-9]+', '', size[size.rfind(" "):]))
		else:
			return size[size.rfind(" ", 0, size.rfind(" ")):]

	def getSelectedFilesSize(self):
		statusBar = tcApi.getStatusBarText()
		if statusBar.startswith("?"):
			return _("The size is calculated, wait a few seconds...")
		size=re.match(r'[\d,\s]+\s[\S]+\s', statusBar)
		return size.group().strip()

	def getDateTime(self):
		if tcApi.getSelectedElements() > 0:
			return _("There is no information about the time of the change.")
		str = tcApi.getStatusBarText()
		datetime = re.search(r'[0-9]{2}\.[0-9]{2}\.[0-9]{2,4}\s[0-9]{1,2}:[0-9]{1,2}', str)
		if not datetime:
			return _("There is no information about the time of the change.")
		return datetime.group(0)

	def speakSelectedCommand(self):
		if tcApi.isApiSupported():
			selected = tcApi.getSelectedElements()
			if selected > 0:
				template = _("Selected {count} items").format(count=selected)
				ui.message(template)
			elif selected == 0:
				ui.message(_("Nothing selected"))

	def speakSelectedItemsInfo(self):
		if tcApi.isApiSupported():
			total = tcApi.getCountElements()
			selected = tcApi.getSelectedElements()
			if selected > total:
				selected = total
			template = _("Selected {selected} of {total} items").format(selected=selected, total=total)
			ui.message(template)
		else:
			ui.message(_('Not supported in this version of total commander'))

	def getPreviousItemGestures(self):
		return ["kb:upArrow","kb:leftArrow","KB:PageUp","KB:HOME"]

	def getNextItemGestures(self):
		return ["kb:downArrow","kb:rightArrow","KB:PageDown","KB:END"]

	def speakActivePannel(self, obj):
		global oldActivePannel, activePannel
		if obj.windowClassName == "TMyListBox":
			if oldActivePannel !=obj.windowControlID:
				oldActivePannel=obj.windowControlID
				obj2 = obj
				while obj2 and obj2.parent and obj2.parent.windowClassName!="TTOTAL_CMD":
					obj2 = obj2.parent
				counter=0
				while obj2 and obj2.previous and obj2.windowClassName!="TPanel":
					obj2 = obj2.previous
					if obj2.windowClassName!="TDrivePanel":
						counter+=1
				if obj.parent.parent.parent.windowClassName=="TTOTAL_CMD":
					if counter==2:
						speech.speakMessage(_("Left"))
						activePannel = 1
					else:
						speech.speakMessage(_("Right"))
						activePannel = 2
		elif obj.windowClassName == "LCLListBox":
			if oldActivePannel != obj.windowControlID:
				oldActivePannel = obj.windowControlID
				obj2 = obj
				while obj2 and obj2.parent and obj2.parent.windowClassName!="TTOTAL_CMD":
					obj2 = obj2.parent
				if obj.parent.parent.parent.windowClassName == "TTOTAL_CMD":
					if obj2.previous and obj2.next and obj2.previous.windowClassName == "LCLListBox" and obj.next.windowClassName == "Window":
						speech.speakMessage(_("Left"))
						activePannel = 1
					elif obj2.previous and obj2.next and obj2.previous.windowClassName == "Window" and obj.next.windowClassName == "LCLListBox":
						speech.speakMessage(_("Right"))
						activePannel = 2

tcInfo = getTCInfo()

class AppModule(appModuleHandler.AppModule):

	def _getForegroundWindowClass(self, obj):
		try:
			return obj.parent.parent.parent.windowClassName
		except AttributeError:
			return None

	def _get_statusBar(self):
		if api.getForegroundObject().windowClassName == "TTOTAL_CMD":
			obj = tcApi.getStatusBarObject()
			obj.name = obj.displayText
			return obj

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		windowClass = obj.windowClassName
#		ui.message(str(obj.name))
		if windowClass in ("TMyListBox","LCLListBox") and obj.role == controlTypes.ROLE_LIST:
			clsList.insert(0, tcFileListObject)
		if windowClass in ("TMyListBox","LCLListBox")  and self._getForegroundWindowClass(obj) == "TTOTAL_CMD" and obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0, tcFileListItem)
		if windowClass in ("TMyListBox","LCLListBox") and self._getForegroundWindowClass(obj) == "TCONNECT":
			clsList.insert(0, TCFTPList)
		if windowClass in ("ComboLBox"):
			clsList.insert(0, TCDriveList)
		if windowClass in ("SysTabControl32", "TMyTabControl", "TMyTabbedNotebook"):
			clsList.insert(0, TCTabControl)
		if windowClass in ("TExtMsgForm"):
			clsList.insert(0, tcMessageBox)
		if windowClass in ("TOverWriteForm"):
			clsList.insert(0, tcOverWriteBox)

class tcFileListObject(sysListView32.List):

	def _getAccessibleName(self):
		child = api.getFocusObject()
		name = child.IAccessibleObject.accName(child.IAccessibleChildID)
		return name

	def _get_isMultiColumn(self):
		return isMultiColumn

	def _get_columnCount(self):
		return len(self._getAccessibleName().split("\t"))

class tcFileListItem(sysListView32.ListItem):
	scriptCategory = manifest['summary']

	def _getAccessibleName(self):
		return self.IAccessibleObject.accName(self.IAccessibleChildID)

	def _getColumnHeader(self, column):
		obj = NVDAObjects.IAccessible.getNVDAObjectFromEvent(tcApi.getHeaderHandle(), winUser.OBJID_CLIENT, 0)
		if obj == None:
			return "none"
		text = obj.displayText
		headers = "".join(";" + x if x.isupper() else x for x in text).strip(";").split(";")
		if len(headers) > 1:
			headers.pop()
			headers.append(_("Attributes"))
			return headers[column -1]
		else:
			return _("Unknown column")

	def _getColumnContent(self, column):
		name = self._getAccessibleName().split("\t")
		return name[column-1]

	def _get_positionInfo(self):
		if tcApi.isApiSupported() and self.role == controlTypes.ROLE_LISTITEM:
			index= tcApi.getCurrentElementNum()
			totalCount= tcApi.getCountElements()
			return dict(indexInGroup=index,similarItemsInGroup=totalCount) 
		else:
			return None

	def event_gainFocus(self):
		global activePannel, isMultiColumn
		isMultiColumn = True if self.location.width > 1000 else False
		if tcApi.isApiSupported():
			curPanel = tcApi.getActivePanelNum()
			if curPanel != activePannel:
				message = _("Left") if curPanel == 1 else _("Right")
				ui.message(message)
				activePannel = curPanel
		else:
			tcInfo.speakActivePannel(self)
		super(tcFileListItem,self).event_gainFocus()

	def event_selectionWithIn(self):
		events = eventHandler._pendingEventCountsByName
		if len(events) == 0: return

		if not eventHandler.isPendingEvents("gainFocus") and not eventHandler.isPendingEvents("valueChange"):
			tcInfo.speakSelectedCommand()

	def event_selection(self):
		pass

	def reportFocus(self):
		global activePannel
		if activePannel == 1:
			self.description = _("Left pannel")
		else:
			self.description = _("Right pannel")

		if self.name:
			speakList=[]
			if controlTypes.STATE_SELECTED in self.states:
				speakList.append(controlTypes.stateLabels[controlTypes.STATE_SELECTED])
			speakList.append(self.name.split("\\")[-1])
			if config.conf['presentation']['reportObjectPositionInformation'] == True and tcApi.isApiSupported():
				positionInfo = self.positionInfo
				template = _('{current} of {all}').format(current=positionInfo['indexInGroup'], all=positionInfo['similarItemsInGroup'])
				if self.name.split("\t")[0] != '..':
					speakList.append(' ' + template)
			if self.hasFocus:
				speech.speakMessage(" ".join(speakList))
		else:
			super(TCFileList,self).reportFocus()

	@script(gestures=tcInfo.getPreviousItemGestures())
	def script_previousElement(self, gesture):
		gesture.send()
		if not self.previous:
			winsound.PlaySound("default", winsound.SND_ASYNC)

	@script(gestures=tcInfo.getNextItemGestures())
	def script_nextElement(self, gesture):
		gesture.send()
		if not self.next:
			winsound.PlaySound("default", winsound.SND_ASYNC)

	@script(gesture="kb:Control+Shift+e", description=_("Reports information about the number of selected elements"))
	def script_selectedElementsInfo(self, gesture):
		tcInfo.speakSelectedItemsInfo()

	@script(gesture="kb:Control+Shift+r", description=_("Reports the size of the file under the cursor. If multiple objects are selected, reports their total size."))
	def script_reportFileSize(self, gesture):
		if not tcApi.isApiSupported():
			ui.message(_("Not supported in this version of total commander"))
			return
		if tcApi.getSelectedElements() > 0:
			size = tcInfo.getSelectedFilesSize()
		else:
			size = tcInfo.getSingleFileSize()
		ui.message(size)

	@script(gesture="kb:Control+Shift+d", description=_("Reports the current path to the folder. Pressing twice Copies it to the clipboard."))
	def script_speakPath(self, gesture):
		if not tcApi.isApiSupported():
			ui.message(_('Not supported in this version of total commander'))
			return
		curPath = tcInfo.getCurrentDirPath()
		if scriptHandler.getLastScriptRepeatCount() != 0 and api.copyToClip(curPath):
			ui.message(_("Copied to clipboard"))
		ui.message(curPath)

	@script(gesture="kb:Control+Shift+t", description=_("Reports the modification time of the file under the cursor."))
	def script_speakDateTime(self, gesture):
		if not tcApi.isApiSupported():
			ui.message(_('Not supported in this version of total commander'))
			return
		datetime = tcInfo.getDateTime()
		ui.message(datetime)

class TCFTPList(IAccessible):

	@script(gestures=tcInfo.getPreviousItemGestures())
	def script_previousElement(self, gesture):
		gesture.send()
		if not self.previous:
			winsound.PlaySound("default", winsound.SND_ASYNC)

	@script(gestures=tcInfo.getNextItemGestures())
	def script_nextElement(self, gesture):
		gesture.send()
		if not self.next:
			winsound.PlaySound("default", winsound.SND_ASYNC)

class TCDriveList(IAccessible):

	def event_gainFocus(self):
		name = self.name
		description = self.displayText
		if description and name[:2] == "[-" and name[-2:] == "-]":
			self.name = description[0:1] + " (" + description[2:] + ")"
		super(TCDriveList,self).event_gainFocus()

class TCTabControl(IAccessible):

	def _get_positionInfo(self):
		index= self.IAccessibleChildID
		totalCount= len(tcApi.getTabListFromTab(self))
		return dict(indexInGroup=index,similarItemsInGroup=totalCount) 

	def isDuplicateIAccessibleEvent(self, obj):
		global currentTab
		if obj.windowClassName != "SysTabControl32" and obj.windowClassName != "TMyTabControl" and obj.windowClassName != "TMyTabbedNotebook":
			return False
		tab = {"handle":obj.windowHandle,"childID":obj.IAccessibleChildID,"items":obj.positionInfo["similarItemsInGroup"]}
		if tab == currentTab:
			return True
		else:
			currentTab = tab
			return False

	def event_selection(self):
		if controlTypes.STATE_SELECTED in self.states and not self.isDuplicateIAccessibleEvent(self):
			self.reportFocus()
		super(TCTabControl,self).event_selection()

class tcMessageBox(IAccessible):

	def initOverlayClass(self):
		self.role = controlTypes.ROLE_STATICTEXT
		text = self.displayText
		if text.find("?") >= 0:
			self.name = text[:text.rfind("?") + 1]
		elif text.find("!") >= 0:
			self.name = text[:text.rfind("!") + 1]
		else:
			self.name = text

class tcOverWriteBox(IAccessible):

	def initOverlayClass(self):
		text = self.displayText
		self.name = text[:text.rfind("+")]
