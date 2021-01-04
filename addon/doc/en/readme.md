# Total Commander

This add-on improves the accessibility of the Total Commander file manager. It is compatible with all versions starting with TC 7.0, but some functions work only in versions 9.0 and higher.

[Donate the author of the add-on](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php)
[GitHub repository](https://github.com/jawhien/extendedTotalCmd)

# Table of contents

* [Compatibility](#user-content-compatibility)
* [Main features](#user-content-main-features)
* [Installation](#user-content-installation)
* [Key commands](#user-content-key-commands)
* [Acknowledgments](#user-content-acknowledgments)
* [Frequently Asked Questions](#user-content-faq)
* [Change log](#user-content-change-log)
* [Official page of the add-on](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/)

<a name="user-content-compatibility"></a>
# Compatibility

* NVDA 2017.3 or higher, including 2019.3.
Note: In versions older than 2017.3, the add-on was not tested, but, most likely, no problems will arise.
* Warning! The add-on may not be compatible with other add-ons for Total Commander, as well as the "sounds by navigation on files" add-on.

<a name="user-content-main-features"></a>
# Main features

* More precise definition of the right and left panel.
* Sound indication when reaching the borders of the list of elements.
* The pronunciation of labels for items in the drive selection window.
* Support work with tabs.
* The ability to quickly recognize the active panel. To do this, press the key command NVDA + Up Arrow, or NVDA + TAB.
* Full support for 64-bit versions of Total Commander.
* Report actions when selecting items or undoing them. (This function is only available in TC 9+).
* The ability to find out the number of selected items. (This function is only available in TC 9+).
* The ability to find out the size of the selected file, or all selected items. (This function is only available in TC 9+).
* Report of the correct item position information in the list. For this feature to work, enable the corresponding option in the NVDA settings dialog. (This function is only available in TC 9+).

<a name="user-content-installation"></a>
# Installation

1. Download the NVDA Add-on File [on this page](https://github.com/jawhien/extendedTotalCmd/releases/latest).
2. In any file manager, go to the directory where the file was downloaded, select it and press the "Enter" key.
3. Confirm the installation by clicking the "Yes" button in the dialog box that appears.
4. If you are updating the add-on, you will need to confirm the installation again.

You can install the add-on through the NVDA add-on manager, for this, do the following:
1. Download the NVDA Add-on File [on this page](https://github.com/jawhien/extendedTotalCmd/releases/latest).
2. Open the NVDA Add-ons Manager from the Tools menu in the main program menu.
3. Click the Install button.
4. Select the downloaded add-on file.
5. Confirm the installation by clicking the "Yes" button in the dialog box that appears.
6. If you are updating the add-on, you will need to confirm the installation again.

<a name="user-content-key-commands"></a>
# Key commands

* Control + Shift + E - Reports information about selected items.
* Control + Shift + R - Reports size information for selected items. If no items are selected, reports the size of the file in focus.
* Control + Shift + D - Reports the full path of the current directory. Pressing twice Copies it to the clipboard.

<a name="user-content-acknowledgments"></a>
# Acknowledgments

I would like to thank all those who send their suggestions, and also helps in testing and detecting errors. Your contribution is undoubtedly very important for the development of this add-on.

<a name="user-content-faq"></a>
# Frequently Asked Questions

Q: Does not the reporting of the size of the file under the cursor

A: In some cases (for example, when working via FTP), determining the size of the file under the cursor works only brief view.

Q: How can I help develop the add-on?

A: If you liked my add-on, you can donate any amount on the [special page](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php).

Q: I found a bug / I have suggestions for improving the add-on, how can I contact you?

A: In this case, you need to [create a new issue](https://github.com/jawhien/extendedTotalCmd/issues/new) in the GitHub repository. Describe as much as possible your problem / proposal.

Q: The add-on does not support my language, can I help with the translation?

A: Yes, please send me letter to the email address indicated in the add-on, and I will send you the necessary files and instructions. You can view the author’s email address in the NVDA Add-ons Manager.

<a name="user-content-change-log"></a>
# Change log

V2.4: 13.12.2020

* Added definition of the size of directories under the cursor. This is a slower process than determining the size of a single file and can take several seconds.
* Added automatic check for updates after starting NVDA. Note: the automatic check for updates will not be performed if the check for updates for NVDA is disabled in the settings.
* Fixed a bug due to which the size of files was not detected in some cases.
* Fixed a bug due to which the website page in English was always opened.
* Fixed some false positives for selection events.
* Other minor improvements.

V2.3: 05.10.2020

* Fixed incorrect detection of the active panel in some cases.
* Fixed tab support in some 32-bit version dialog boxes.
* Messages about selecting files or canceling it no longer depend on pressing certain keys.
* Fixed duplicate messages when selecting files.
* Fixed persistent messages about selected files when switching tabs in the main window of Total Commander.
* Improvements to dialogs with messages. Now, when these dialogs appear (for example, when deleting files) NVDA will read the information that is displayed on the screen.
* Improved file overwrite dialog. Now when the message about overwriting files appears, NVDA will report all the information that is displayed on the screen.
* The trailing ">" character is now missing in the path to the current directory.
* Fixed determination of the size of selected files. Now it is reported as displayed on the screen. You can set the display format in the Total Commander settings.
* Fixed determining the size of the file under the cursor. It is now reported correctly in both short and detailed view.
* Fixed determination of the size of files with UNC paths and when working via FTP. The size is now reported as displayed on the screen. you can change the display format in the settings of Total Commander. (Works correctly only in short form)
* Updated some messages.
* Updated Russian localization.
* Full code optimization.
* Other minor improvements and fixes.

V2.2.0: 20.04.2020

* When switching tabs, the name of the selected tab will now be reported, as well as its position, if enabled in the NVDA settings.
* Added the function of copying the path to the current folder to the clipboard by double-pressing CTRL + SHIFT + D
* Fixed a bug leading to problems when determining the version of TC.
* Fixed a bug when determining the file size under the cursor associated with using a large font.
* Code optimization.
* Other minor improvements and fixes.

V2.1.0: 21.03.2020

* Added a new function to reports the full path to the current directory.
* Added option to check updates. To check the update, open the tools menu in the main NVDA menu and select "Update Total Commander add-on..."
* Fixed a bug in Total Commander version 7 and 8 when you select file pronounced the message that the TC version is not supported.
* Now add-on can determine the size of any file, even if it is not selected.
* Fixed a bug where the size of the elements for which there is a symbol "." could not be determined.
* Now the size of the elements can be represented in bytes, kB, mB, gB, or tB. The value will be automatically converted to the correct format.
* When reports the size of the directory if it is not defined, the add-on will report it.
* Fully updated documentation. Made the layout of pages for readability.
* Removed unused variables.
* Full code optimization.

V2.0.1: 01.03.2020

* Documentation bugs fixed

V2.0: 22.02.2020

* Fixed a bug where the list borders were erroneously determined on some files.
* The problem was fixed in 32 bit versions of TC8 +, when, upon exiting to the previous directory, the first element of the list was declared first, and then the element in focus.
* Added announcement of item positions in the list, if this feature is enabled in the NVDA settings. (Only in TC9 +).
* Added the ability to report information about selected items by ctrl + shift + e. (Only in TC9 +).
* Added announcement of selected elements when pressing CTRL + A. (Only in TC9 +).
* Added announcement about deselecting when pressing CTRL + num-. (Only in TC9 +).
* Added announcement of the size of selected files by pressing CTRL + SHIFT + R. (Only in TC9 +).

V1.4: 19.07.2019

* The list border signal has been replaced with standard windows sound.
* Added a signal to the top of the list.
* Now not only arrows are processed, but also Home, End, PageUp and PageDown keys for signaling list boundaries.
* Added compatibility with new versions of NVDA.

V1.3

* The sound signal will now play only when navigating the list when the down arrow is pressed on the last element of the list, and not when the focus is on the last element.
* Fixed erroneous behavior outside the main window, settings, and other lists.
* Improved behavior in the FTP connection dialog.

V1.2

* The mechanism for determining the active panel in versions 8 and above has been changed.
* Optimized code to avoid problems with versions 7 and below.
* When the focus falls on the last element of the list, a sound signal will be played.
* Fixed incorrect pronunciation of the active panel outside the main window.

V1.1

* Now, in the disc selection window, disc labels are read.
* A description with the name of the active panel has been added to the elements, when you press the (NVDA + UpArrow) or (NVDA + TAB) keys, the element name and the name of the active panel are pronounced.
* Minor improvements.

V1.0

* First version.
