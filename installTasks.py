# -*- coding: UTF-8 -*-

import webbrowser
import wx
import addonHandler
addonHandler.initTranslation()
import gui
import languageHandler

curLang = languageHandler.curLang

if curLang == "ru_RU":
	DONATIONS_URL = "https://jnsoft.ru/ru/articles/nvda/extendedTotalCmd/donation.php"
else:
	DONATIONS_URL = "https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php"

def onInstall():
	manifest = addonHandler.getCodeAddon().manifest
	# Translators: The text of the dialog shown during add-on installation.
	message = _(""" {name} - this free add-on for NVDA.
You can make a donation to the author to help further development of this add-on and other free software.
You want to make a donation now? For transaction you will be redirected to the website of the developer.""").format(name=manifest['summary'])
	# Translators: The title of the dialog shown during add-on installation.
	if gui.messageBox(message, caption=_("Request donations for {name}").format(name=manifest['summary']),
		style=wx.YES_NO|wx.ICON_QUESTION) == wx.YES:
		webbrowser.open(DONATIONS_URL)
