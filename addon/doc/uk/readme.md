# Total Commander

Цей додаток поліпшує доступність файлового менеджера Total Commander. Він сумісний з усіма версіями TC, починаючи з 7.0, але деякі функції працюють лише у версії 9.0 і новіших.

[Підтримати автора додатка](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php)
[Репозиторій на GitHub ](https://github.com/jawhien/extendedTotalCmd)

<!-- border -->

# Зміст

* [Сумісність](#user-content-compatibility)
* [Основні можливості](#user-content-main-features)
* [Встановлення](#user-content-installation)
* [Комбінації клавіш](#user-content-key-commands)
* [Подяки](#user-content-acknowledgments)
* [Найчастіші запитання](#user-content-faq)
* [Журнал змін](#user-content-change-log)
* [Офіційна сторінка додатка](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/)

<!-- border -->

<a name="user-content-compatibility"></a>
# Сумісність

* NVDA 2018.3 чи новіша, включаючи 2022.1.
* Попередження! Додаток може бути несумісним з іншими додатками для Total Commander, такими як «sounds by navigation on files».

<a name="user-content-main-features"></a>
# Основні можливості

* Точніше визначення правої й лівої панелей.
* Звукова індикація, коли ви досягаєте межі списку елементів.
* Промовляння міток для елементів у вікні вибору диска.
* Підтримка роботи із вкладками.
* Підтримка відображення мультиколонкового режиму. (Ця функція доступна лише в TC 9+).
* Можливість швидко розпізнати активну панель. Щоб це зробити, натисніть комбінацію клавіш NVDA + стрілка вгору чи NVDA + TAB.
* Повна підтримка 64-розрядних версій Total Commander.
* Повідомлення про дії під час виділення або скасування виділення елементів. (Ця функція доступна лише в TC 9+).
* Можливість дізнатися кількість виділених елементів. (Ця функція доступна лише в TC 9+).
* Можливість дізнатися розмір виділеного файла чи всіх виділених елементів. (Ця функція доступна лише в TC 9+).
* Повідомлення інформації про коректну позицію елемента в списку. Щоб ця функція працювала, увімкніть відповідний параметр у діалозі налаштувань NVDA. (Ця функція доступна лише в TC 9+).

<a name="user-content-installation"></a>
# Встановлення

1. Завантажте файл додатка для NVDA [на цій сторінці](https://github.com/jawhien/extendedTotalCmd/releases/latest).
2. За допомогою будь-якого файлового менеджера увійдіть до папки, в яку цей файл було завантажено, оберіть його й натисніть клавішу «Enter».
3. Підтвердіть встановлення натисканням кнопки «Так» у діалозі, який з’явиться.
4. Якщо ви оновлюєте додаток, вам знадобиться підтвердити встановлення ще раз.

Ви можете встановити додаток через менеджер додатків NVDA, виконавши вказане нижче:
1. Завантажте файл додатка для NVDA [на цій сторінці](https://github.com/jawhien/extendedTotalCmd/releases/latest).
2. Відкрийте керування додатками з підменю «Інструменти» у головному меню NVDA.
3. Натисніть кнопку «Встановити».
4. Оберіть завантажений файл додатка.
5. Підтвердіть встановлення натисканням кнопки «Так» у діалозі, який з’явиться.
6. Якщо ви оновлюєте додаток, вам знадобиться підтвердити встановлення ще раз.

<a name="user-content-key-commands"></a>
# Комбінації клавіш

* Control + Shift + E — Повідомляє інформацію про виділені елементи.
* Control + Shift + R — Повідомляє інформацію про розмір виділених елементів. Якщо виділених елементів немає, повідомляє розмір файлу у фокусі.
* Control + Shift + D — Повідомляє повний шлях до поточної папки. Подвійне натискання копіює його в буфер обміну.
* Control + Shift + T — Повідомляє час і дату змінення.
* NVDA + A — Повідомляє активну панель.
* Alt + W — Повідомляє назву поточної вкладки. Подвійне натискання відкриває її контекстне меню.

<a name="user-content-acknowledgments"></a>
# Подяки

Я дякую всім, хто надсилає свої пропозиції, а також допомагає у тестуванні й виявленні помилок. Ваш внесок, безсумнівно, дуже важливий для розробки цього додатка.

<a name="user-content-faq"></a>
# Найчастіші запитання

Запитання: Не повідомляється розмір файлу під курсором

Відповідь: У деяких випадках (наприклад, під час роботи з FTP) визначення розміру файлу під курсором працює лише в скороченому вигляді.

Запитання: Як я можу допомогти в розробці цього додатка?

Відповідь: Якщо вам подобається мій додаток, ви можете пожертвувати будь-яку суму на [спеціальній сторінці](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php).

Запитання: Я виявив проблему / я маю пропозиції для поліпшення додатка, як можна з вами зв’язатись?

Відповідь: У цьому випадку вам потрібно [створити нову проблему](https://github.com/jawhien/extendedTotalCmd/issues/new) у репозиторії на GitHub. Опишіть якнайточніше вашу проблему / пропозицію.

Запитання: Додаток не підтримує мою мову, чи можу я допомогти з перекладом?

Відповідь: Так, будь ласка, надішліть мені лист на електронну пошту, зазначену в додатку, і я надішлю вам необхідні файли й інструкції. Ви можете дізнатися електронну адресу автора у менеджері додатків NVDA. Або ж, якщо ви використовуєте GitHub, ви можете надіслати мені Pull request із перекладом, це буде значно зручніше і швидше.

<a name="user-content-change-log"></a>
# Журнал змін

V3.2: 08.01.2022

* Added information about the disk to the window for selecting disks in the format Used space / total space.
* fixed compatibility with nvda 2022+
* Fixed determination of the file modification time.
* Made minor localization improvements.

V3.1: 08.09.2021

* Added a function to reports the active panel. Press "NVDA + A" to find out the active panel.
* Added a function to reports the current tab on the active panel. When you press "ALT + W", the name of the current tab will be reported; Pressing twice  it, its context menu will open.
* Added Spanish localization.
* Other minor improvements and fixes.

V3.0: 01.06.2021

* Introduced support for detailed display mode. Attention: this function is experimental and sometimes may not work correctly. If you find a bug, please report it.
* The update module has been completely redesigned. Now it downloads and installs the new version himself, and there is no need to do it manually.
* Added Czech and Slovak localization. Thanks to Radek Žalud and Peter Vágner for the translations provided.
* Compatibility requirements have been changed. Now you need NVDA version 2018.3 or higher to install the add-on.
* The bug that led to the fact that some drop-down lists were displayed incorrectly, for example, such as those opened by pressing the "F2" key in the group rename tool, has been fixed.
* Fixed some compatibility issues with NVDA 2018.3.
* Fixed compatibility with NVDA 2021.1.

V2.5: 19.01.2021

* Fix in the updater: from version 3.0 the compatibility requirements will be updated. Since newer versions will support NVDA 2018.3 or higher, users of earlier versions of the program will receive a message about this when checking for updates.
* Improvement: When reading the status bar, information about the selected item will now be reported, such as size, creation date, attributes, local disk information, etc. depending on TC settings.
* Improvement: added the ability to quickly find out the time and date of the change of the selected item, for this press the combination Control + Shift + t. In NVDA settings, you can change the gestures for this action.
* Improvement: now if callculation of size takes more than 1 second, tones will sound until the process is complete.
* Improvement: the add-on now uses the standard template and SCons for building.
* Fix: the position of the object is no longer reported on the ".." element.
* Fix: in some cases sizing ended with an error.
* Other minor fixes and optimizations.

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
