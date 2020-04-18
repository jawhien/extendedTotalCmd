#appModules/totalcmd.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#Some parts of the code copied from the original module that is included with NVDA
#Copyright (C) 2006-2012 NVDA Contributors
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

addonHandler.initTranslation()
tcApi = tcApi.tcApi()
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

	def convertSizeFromKB(self, kb):
		sizeKB = int(kb)
		sizeMB = int((sizeKB / 1024) * 100) / 100
		sizeGB = int((sizeKB / 1024 / 1024) * 100) / 100
		sizeTB = int((sizeKB / 1024 / 1024 / 1024) * 100) / 100
		if sizeTB >= 1:
			return _("{size} tB").format(size=sizeTB)
		elif sizeGB >= 1:
			return _("{size} gB").format(size=sizeGB)
		elif sizeMB >= 1:
			return _("{size} mB").format(size=sizeMB)
		else:
			return _("{size} kB").format(size=sizeKB)

	def getSingleFileSize(self, str):
		str = str[:str.rfind(":")]
		size = str[str.rfind(" ", 0, len(str[:-13].rstrip())):-13]
		size = re.sub(r'[^0-9]+', r'', size)
		return size

	def speakSize(self):
		if tcApi.isApiSupported():
			selected = tcApi.getSelectedElements()
			sizeData = tcApi.getAvailableSize()
			if selected > 0:
				waitIndicator = sizeData[0:1]
				if waitIndicator == '?':
					ui.message(_("The size is calculated, wait a few seconds..."))
					return
				size = ''
				for s in sizeData:
					if s.isspace() == False and s.isdigit() == False:
						break
					if s.isdigit():
						size += s
				convertedSize = self.convertSizeFromKB(size)
				ui.message(convertedSize)
			elif selected == 0 and sizeData != False:
				size = self.getSingleFileSize(sizeData)
				convertedSize = self.convertSizeFromBytes(size)
				if convertedSize == False:
					ui.message(_("No size information. Try select this item."))
				else:
					ui.message(convertedSize)
			else:
				ui.message(_("No size information. Try select this item."))
		else:
			ui.message(_("Not supported in this version of total commander"))

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

	def getSelectedCommandGestures(self):
		return {"KB:CONTROL+A","KB:CONTROL+numpadMinus"}

	def speakCurrentPath(self):
		if not tcApi.isApiSupported():
			ui.message(_('Not supported in this version of total commander'))
			return

		hnd = tcApi.getCurDirPanelHandle()
		obj = NVDAObjects.IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
		ui.message(obj.name)

	def copyCurrentPath(self):
		if not tcApi.isApiSupported():
			ui.message(_('Not supported in this version of total commander'))
			return

		hnd = tcApi.getCurDirPanelHandle()
		obj = NVDAObjects.IAccessible.getNVDAObjectFromEvent(hnd, winUser.OBJID_CLIENT, 0)
		if api.copyToClip(obj.name):
			ui.message(_("Copied to clipboard"))

tcInfo = getTCInfo()

class AppModule(appModuleHandler.AppModule):
	scriptCategory = manifest['summary']

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName in ("TMyListBox", "TMyListBox.UnicodeClass")  and obj.parent.parent.parent.windowClassName == "TTOTAL_CMD":
			clsList.insert(0, TCList)
		if obj.windowClassName in ("ComboLBox", "ComboLBox.UnicodeClass"):
			clsList.insert(0, TCCombo)
		if obj.windowClassName in ("LCLListBox", "LCLListBox.UnicodeClass")  and obj.parent.parent.parent.windowClassName == "TTOTAL_CMD":
			clsList.insert(0, TCList64)
		if obj.windowClassName in ("LCLListBox", "LCLListBox.UnicodeClass")  and obj.parent.parent.parent.windowClassName == "TCONNECT":
			clsList.insert(0, TCListConnect)
		if obj.windowClassName in ("TMyListBox", "TMyListBox.UnicodeClass") and obj.parent.parent.parent.windowClassName == "TCONNECT":
			clsList.insert(0, TCListConnect)
		if obj.windowClassName in ("SysTabControl32", "SysTabControl32.UnicodeClass"):
			clsList.insert(0, tcTabPanel)
		if obj.windowClassName in ("TMyTabControl", "TMyTabControl.UnicodeClass") and obj.parent.parent.parent.parent.parent.windowClassName == "TTOTAL_CMD":
			clsList.insert(0, tcTabPanel)

class TCList(IAccessible):
	scriptCategory = manifest['summary']
	__previousItemGestures = tcInfo.getPreviousItemGestures()
	__nextItemGestures = tcInfo.getNextItemGestures()
	__selectedCommandsGestures = tcInfo.getSelectedCommandGestures()

	def event_gainFocus(self):
		global oldActivePannel, activePannel
		if oldActivePannel !=self.windowControlID:
			oldActivePannel=self.windowControlID
			obj=self
			while obj and obj.parent and obj.parent.windowClassName!="TTOTAL_CMD":
				obj=obj.parent
			counter=0
			while obj and obj.previous and obj.windowClassName!="TPanel":
				obj=obj.previous
				if obj.windowClassName!="TDrivePanel":
					counter+=1
			if self.parent.parent.parent.windowClassName=="TTOTAL_CMD":
				if counter==2:
					speech.speakMessage(_("Left"))
					activePannel = 1
				else:
					speech.speakMessage(_("Right"))
					activePannel = 2
		super(TCList,self).event_gainFocus()

	def _get_positionInfo(self):
		if tcApi.isApiSupported() and self.role == controlTypes.ROLE_LISTITEM:
			index= tcApi.getCurrentElementNum()
			totalCount= tcApi.getCountElements()
			return dict(indexInGroup=index,similarItemsInGroup=totalCount) 
		else:
			return None

	def reportFocus(self):
		global activePannel
		obj = self
		if obj.parent.parent.parent.windowClassName=="TTOTAL_CMD":
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
			super(TCList,self).reportFocus()

	def script_nextElement(self, gesture):
		gesture.send()
		if not self.next:
			winsound.PlaySound("default",1)

	def script_previousElement(self, gesture):
		gesture.send()
		if not self.previous:
			winsound.PlaySound("default",1)

	def initOverlayClass(self):
		for gesture in self.__nextItemGestures:
			self.bindGesture(gesture, "nextElement")
		for gesture in self.__previousItemGestures:
			self.bindGesture(gesture, "previousElement")
		for gesture in self.__selectedCommandsGestures:
			self.bindGesture(gesture, "selectedCommands")

	def script_selectedElementsInfo(self, gesture):
		tcInfo.speakSelectedItemsInfo()
	script_selectedElementsInfo.__doc__ = _("Reports information about the number of selected elements")

	def script_selectedCommands(self, gesture):
		gesture.send()
		tcInfo.speakSelectedCommand()

	def script_reportFileSize(self, gesture):
		tcInfo.speakSize()
	script_reportFileSize.__doc__ = _("Reports to the size off selected files and folders")

	def script_speakPath(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() != 0:
			tcInfo.copyCurrentPath()
		tcInfo.speakCurrentPath()
	script_speakPath.__doc__ = _("Reports the current path to the folder. Pressing twice Copies it to the clipboard.")

	__gestures={
		"kb:control+shift+d":"speakPath",
		"KB:CONTROL+SHIFT+E":"selectedElementsInfo",
	"KB:CONTROL+SHIFT+R":"reportFileSize"
	}

class TCCombo(IAccessible):

	def event_gainFocus(self):
		description = self.displayText
		if description:
			self.name = description[0:1] + " (" + description[2:] + ")"
		super(TCCombo,self).event_gainFocus()

class TCList64(IAccessible):
	scriptCategory = manifest['summary']
	__previousItemGestures = tcInfo.getPreviousItemGestures()
	__nextItemGestures = tcInfo.getNextItemGestures()
	__selectedCommandsGestures = tcInfo.getSelectedCommandGestures()

	def event_gainFocus(self):
		global oldActivePannel, activePannel
		if oldActivePannel !=self.windowControlID:
			oldActivePannel=self.windowControlID
			obj=self
			while obj and obj.parent and obj.parent.windowClassName!="TTOTAL_CMD":
				obj=obj.parent
			if self.parent.parent.parent.windowClassName == "TTOTAL_CMD":
				if obj.previous and obj.next and obj.previous.windowClassName == "LCLListBox" and obj.next.windowClassName == "Window":
					speech.speakMessage(_("Left"))
					activePannel = 1
				elif obj.previous and obj.next and obj.previous.windowClassName == "Window" and obj.next.windowClassName == "LCLListBox":
					speech.speakMessage(_("Right"))
					activePannel = 2
		super(TCList64,self).event_gainFocus()

	def _get_positionInfo(self):
		if tcApi.isApiSupported() and self.role == controlTypes.ROLE_LISTITEM:
			index= tcApi.getCurrentElementNum()
			totalCount= tcApi.getCountElements()
			return dict(indexInGroup=index,similarItemsInGroup=totalCount) 
		else:
			return None

	def reportFocus(self):
		global activePannel
		obj = self
		if obj.parent.parent.parent.windowClassName=="TTOTAL_CMD":
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
			super(TCList64,self).reportFocus()

	def script_nextElement(self, gesture):
		gesture.send()
		if not self.next:
			winsound.PlaySound("default",1)

	def script_previousElement(self, gesture):
		gesture.send()
		if not self.previous:
			winsound.PlaySound("default",1)

	def initOverlayClass(self):
		for gesture in self.__nextItemGestures:
			self.bindGesture(gesture, "nextElement")
		for gesture in self.__previousItemGestures:
			self.bindGesture(gesture, "previousElement")
		for gesture in self.__selectedCommandsGestures:
			self.bindGesture(gesture, "selectedCommands")

	def script_selectedElementsInfo(self, gesture):
		tcInfo.speakSelectedItemsInfo()
	script_selectedElementsInfo.__doc__ = _("Reports information about the number of selected elements")

	def script_selectedCommands(self, gesture):
		gesture.send()
		tcInfo.speakSelectedCommand()

	def script_reportFileSize(self, gesture):
		tcInfo.speakSize()
	script_reportFileSize.__doc__ = _("Reports to the size off selected files and folders")

	def script_speakPath(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() != 0:
			tcInfo.copyCurrentPath()
		tcInfo.speakCurrentPath()
	script_speakPath.__doc__ = _("Reports the current path to the folder. Pressing twice Copies it to the clipboard.")

	__gestures={
		"kb:control+shift+d":"speakPath",
		"KB:CONTROL+SHIFT+E":"selectedElementsInfo",
	"KB:CONTROL+SHIFT+R":"reportFileSize"
	}

class TCListConnect(IAccessible):
	__previousItemGestures = tcInfo.getPreviousItemGestures()
	__nextItemGestures = tcInfo.getNextItemGestures()

	def script_nextElement(self, gesture):
		gesture.send()
		if not self.next:
			winsound.PlaySound("default",1)

	def script_previousElement(self, gesture):
		gesture.send()
		if not self.previous:
			winsound.PlaySound("default",1)

	def initOverlayClass(self):
		for gesture in self.__nextItemGestures:
			self.bindGesture(gesture, "nextElement")
		for gesture in self.__previousItemGestures:
			self.bindGesture(gesture, "previousElement")

class tcTabPanel(IAccessible):

	def _get_positionInfo(self):
		index= self.IAccessibleChildID
		totalCount= len(tcApi.getTabListFromTab(self))
		return dict(indexInGroup=index,similarItemsInGroup=totalCount) 

	def isDuplicateIAccessibleEvent(self, obj):
		global currentTab
		if obj.windowClassName != "SysTabControl32" and obj.windowClassName != "TMyTabControl":
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
		super(tcTabPanel,self).event_selection()
