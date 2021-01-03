#installTasks.py
#A part of Total Commander add-on
#Copyright (C) 2020 Eugene Poplavsky <jawhien@gmail.com>
#This file is covered by the GNU General Public License.
#See the file LICENSE.txt for more details.

import webbrowser
import wx
import gui
import addonHandler
from languageHandler import getLanguage

addonHandler.initTranslation()

lang = getLanguage().split("_")[0]
if lang != "en" and lang != "ru": lang = "en"

donations_url = "https://jnsoft.ru/{lang}/articles/nvda/extendedTotalCmd/donation.php".format(lang=lang)

def onInstall():
	manifest = addonHandler.getCodeAddon().manifest
	# Translators: The text of the dialog shown during add-on installation.
	message = _(""" {name} - this free add-on for NVDA.
You can make a donation to the author to help further development of this add-on and other free software.
You want to make a donation now? For transaction you will be redirected to the website of the developer.""").format(name=manifest['summary'])

	if gui.messageBox(message, caption=_("Request donations for {name}").format(name=manifest['summary']), style=wx.YES_NO|wx.ICON_QUESTION) == wx.YES:
		webbrowser.open(donations_url)
