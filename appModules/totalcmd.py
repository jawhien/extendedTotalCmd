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
import speech
import controlTypes
import winsound
import re
import ui
import winUser
import scriptHandler
from . import tcApi
import config
import eventHandler
import os

addonHandler.initTranslation()

manifest = addonHandler.getCodeAddon().manifest

oldActivePannel=0
activePannel=1
currentTab = 0

class getTCInfo():

	def convertSizeFromBytes(self, bytes):
		try:
			sizeBytes = int(bytes)
		except ValueError:
			return False
		sizeKB = int((sizeBytes / 1024) * 100) / 100
		sizeMB = int((sizeBytes / 1024 / 1024) * 100) / 100
		sizeGB = int((sizeBytes / 1024 / 1024 / 1024) * 100) / 100
		sizeTB = int((sizeBytes / 1024 / 1024 / 1024 / 1024) * 100) / 100
		if sizeTB >= 1:
			return _("{size} tB").format(size=sizeTB)
		elif sizeGB >= 1:
			return _("{size} gB").format(size=sizeGB)
		elif sizeMB >= 1:
			return _("{size} mB").format(size=sizeMB)
		elif sizeKB >= 1:
			return _("{size} kB").format(size=sizeKB)
		else:
			return _("{size} Bytes").format(size=sizeBytes)

	def getCurrentDirPath(self):
		hnd = tcApi.getCurDirPanelHandle()
		return NVDAObjects.IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0).name[:-1]

	def getSingleFileSize(self):
		currentDir = self.getCurrentDirPath()
		name = api.getFocusObject().name.split("\t")[0]
		path = '\\'.join([currentDir, name])
		statusbar = tcApi.getAvailableSize()
		if currentDir.startswith("\\\\") and statusbar and re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{2}', statusbar):
			return self.convertSizeFromBytes(self.getSingleFileSizeFromStatusbar(statusbar))
		elif currentDir.startswith("\\\\"):
			return _("This object is not supported.")
		elif re.match(r'[0-9]+:/', currentDir) and statusbar:
			return self.getSingleFileSizeFromStatusbar(statusbar)
		elif re.match(r'[0-9]+:/', currentDir) and statusbar == False:
			return _("No size information. Try select this item.")
		elif os.path.isfile(path):
			return self.convertSizeFromBytes(os.path.getsize(path))
		elif os.path.isdir(path):
			return _("This object is directory.")
		else:
			return _("No size information. Try select this item.")

	def getSingleFileSizeFromStatusbar(self, str):
		size = re.sub(r'[0-9]{2}\.[0-9]{2}\.[0-9]{2}.*', '', str).strip()
		if size[-1:].isdigit():
			return self.convertSizeFromBytes(re.sub(r'[^0-9]+', '', size[size.rfind(" "):]))
		else:
			return size[size.rfind(" ", 0, size.rfind(" ")):]

	def getSelectedFilesSize(self):
		sizeData = tcApi.getAvailableSize()
		if sizeData[0:1] == '?':
			ui.message(_("The size is calculated, wait a few seconds..."))
			return
		size=re.match(r'[\d,\s]+\s[\S]+\s', sizeData)
		return size.group().strip()

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
		return {"kb:upArrow","kb:leftArrow","KB:PageUp","KB:HOME"}

	def getNextItemGestures(self):
		return {"kb:downArrow","kb:rightArrow","KB:PageDown","KB:END"}

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

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		windowClass = obj.windowClassName
		if windowClass in ("TMyListBox","LCLListBox")  and self._getForegroundWindowClass(obj) == "TTOTAL_CMD":
			clsList.insert(0, TCFileList)
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

class TCFileList(IAccessible):
	scriptCategory = manifest['summary']
	__previousItemGestures = tcInfo.getPreviousItemGestures()
	__nextItemGestures = tcInfo.getNextItemGestures()

	def _get_positionInfo(self):
		if tcApi.isApiSupported() and self.role == controlTypes.ROLE_LISTITEM:
			index= tcApi.getCurrentElementNum()
			totalCount= tcApi.getCountElements()
			return dict(indexInGroup=index,similarItemsInGroup=totalCount) 
		else:
			return None

	def event_gainFocus(self):
		global activePannel
		if tcApi.isApiSupported():
			curPanel = tcApi.getActivePanelNum()
			if curPanel != activePannel:
				message = _("Left") if curPanel == 1 else _("Right")
				ui.message(message)
				activePannel = curPanel
		else:
			tcInfo.speakActivePannel(self)
		super(TCFileList,self).event_gainFocus()

	def event_selectionWithIn(self):
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
				if self.name != '..':
					speakList.append(' ' + template)
			if self.hasFocus:
				speech.speakMessage(" ".join(speakList))
		else:
			super(TCFileList,self).reportFocus()

	def script_nextElement(self, gesture):
		gesture.send()
		if not self.next:
			winsound.PlaySound("default", winsound.SND_ASYNC)

	def script_previousElement(self, gesture):
		gesture.send()
		if not self.previous:
			winsound.PlaySound("default", winsound.SND_ASYNC)

	def initOverlayClass(self):
		for gesture in self.__nextItemGestures:
			self.bindGesture(gesture, "nextElement")
		for gesture in self.__previousItemGestures:
			self.bindGesture(gesture, "previousElement")

	def script_selectedElementsInfo(self, gesture):
		tcInfo.speakSelectedItemsInfo()
	script_selectedElementsInfo.__doc__ = _("Reports information about the number of selected elements")

	def script_reportFileSize(self, gesture):
		if not tcApi.isApiSupported():
			ui.message(_("Not supported in this version of total commander"))
			return
		if tcApi.getSelectedElements() > 0:
			size = tcInfo.getSelectedFilesSize()
		else:
			size = tcInfo.getSingleFileSize()
		ui.message(size)
	script_reportFileSize.__doc__ = _("Reports the size of the file under the cursor. If multiple objects are selected, reports their total size.")

	def script_speakPath(self, gesture):
		if not tcApi.isApiSupported():
			ui.message(_('Not supported in this version of total commander'))
			return
		curPath = tcInfo.getCurrentDirPath()
		if scriptHandler.getLastScriptRepeatCount() != 0 and api.copyToClip(curPath):
			ui.message(_("Copied to clipboard"))
		ui.message(curPath)
	script_speakPath.__doc__ = _("Reports the current path to the folder. Pressing twice Copies it to the clipboard.")

	__gestures={
		"kb:control+shift+d":"speakPath",
		"KB:CONTROL+SHIFT+E":"selectedElementsInfo",
	"KB:CONTROL+SHIFT+R":"reportFileSize"
	}

class TCFTPList(IAccessible):
	__previousItemGestures = tcInfo.getPreviousItemGestures()
	__nextItemGestures = tcInfo.getNextItemGestures()

	def script_nextElement(self, gesture):
		gesture.send()
		if not self.next:
			winsound.PlaySound("default", winsound.SND_ASYNC)

	def script_previousElement(self, gesture):
		gesture.send()
		if not self.previous:
			winsound.PlaySound("default", winsound.SND_ASYNC)

	def initOverlayClass(self):
		for gesture in self.__nextItemGestures:
			self.bindGesture(gesture, "nextElement")
		for gesture in self.__previousItemGestures:
			self.bindGesture(gesture, "previousElement")

class TCDriveList(IAccessible):

	def event_gainFocus(self):
		description = self.displayText
		if description:
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
