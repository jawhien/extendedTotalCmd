# Total Commander

This add-on improves the accessibility of the Total Commander file manager. It is compatible with all versions starting with TC 7.0, but some functions work only in versions 9.0 and higher.

## Compatibility

* NVDA 2017.3 or higher, including 2019.3.
Note: In versions older than 2017.3, the add-on was not tested, but, most likely, no problems will arise.

# Main features

* More precise definition of the right and left panel.
* Sound indication when reaching the borders of the list of elements.
* The pronunciation of labels for items in the drive selection window.
* The ability to quickly recognize the active panel. To do this, press the key command NVDA + Up Arrow, or NVDA + TAB.
* Full support for 64-bit versions of Total Commander.
* Report actions when selecting items or undoing them. (This function is only available in TC 9+).
* The ability to find out the number of selected items. (This function is only available in TC 9+).
* The ability to find out the size of the selected file, or all selected items. (This function is only available in TC 9+).
* Report of the correct item position information in the list. For this feature to work, enable the corresponding option in the NVDA settings dialog. (This function is only available in TC 9+).

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

# Key commands

* Control + Shift + E - Reports information about selected items.
* Control + Shift + R - Reports size information for selected items. If no items are selected, reports the size of the file in focus.

# Frequently Asked Questions

## How can I help develop the add-on?
If you liked my add-on, you can donate any amount on the [special page](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php).

## I found a bug / I have suggestions for improving the add-on, how can I contact you?
In this case, you need to [create a new issue](https://github.com/jawhien/extendedTotalCmd/issues/new) in the GitHub repository. Describe as much as possible your problem / proposal.

## The add-on does not support my language, can I help with the translation?
Yes, please send me letter to the email address indicated in the add-on, and I will send you the necessary files and instructions. You can view the author’s email address in the NVDA Add-ons Manager.

# Change log

## V2.0.1: 01.03.2020
* Documentation bugs fixed

## V2.0: 22.02.2020
* Fixed a bug where the list borders were erroneously determined on some files.
* The problem was fixed in 32 bit versions of TC8 +, when, upon exiting to the previous directory, the first element of the list was declared first, and then the element in focus.
* Added announcement of item positions in the list, if this feature is enabled in the NVDA settings. (Only in TC9 +).
* Added the ability to report information about selected items by ctrl + shift + e. (Only in TC9 +).
* Added announcement of selected elements when pressing CTRL + A. (Only in TC9 +).
* Added announcement about deselecting when pressing CTRL + num-. (Only in TC9 +).
* Added announcement of the size of selected files by pressing CTRL + SHIFT + R. (Only in TC9 +).

## V1.4: 19.07.2019
* The list border signal has been replaced with standard windows sound.
* Added a signal to the top of the list.
* Now not only arrows are processed, but also Home, End, PageUp and PageDown keys for signaling list boundaries.
* Added compatibility with new versions of NVDA.

## V1.3
* The sound signal will now play only when navigating the list when the down arrow is pressed on the last element of the list, and not when the focus is on the last element.
* Fixed erroneous behavior outside the main window, settings, and other lists.
* Improved behavior in the FTP connection dialog.

## V1.2
* The mechanism for determining the active panel in versions 8 and above has been changed.
* Optimized code to avoid problems with versions 7 and below.
* When the focus falls on the last element of the list, a sound signal will be played.
* Fixed incorrect pronunciation of the active panel outside the main window.

## V1.1
* Now, in the disc selection window, disc labels are read.
* A description with the name of the active panel has been added to the elements, when you press the (NVDA + UpArrow) or (NVDA + TAB) keys, the element name and the name of the active panel are pronounced.
* Minor improvements.

## V1.0
* First version.
