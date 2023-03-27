# Total Commander

Este complemento melhora a acessibilidade do gerenciador de arquivos Total Commander. É compatível com todas as versões a partir do TC 7.0, mas algumas funções rodam apenas nas versões 9.0 e superiores.

[Fazer um donativo.](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php)
[Repositório no GitHub](https://github.com/jawhien/extendedTotalCmd)

<!-- border -->

# Índice
- [Compatibilidade](#user-content-compatibility)
- [Características principais](#user-content-main-features)
- [Instalação](#user-content-installation)
- [Teclas de comando](#user-content-key-commands)
- [Agradecimentos](#user-content-acknowledgments)
- [perguntas frequentes](#user-content-faq)
- [Change log](#user-content-change-log)
- [página oficial do add-on](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/)

<!-- border -->

<a name="user-content-compatibility"></a>
# Compatibilidade

- -       NVDA 2018.3 ou superior, incluindo 2022.1.
Atenção! O complemento pode não ser compatível com outros complementos para o Total Commander, bem como o complemento "sons por navegação em arquivos".

<a name="user-content-main-features"></a>
# Principais características

- Definição mais precisa do painel direito e esquerdo.
- Indicação sonora ao atingir as bordas da lista de elementos.
- Pronúncia dos rótulos dos itens na janela de seleção da unidade.
- Suporte ao trabalho com abas.
- Suporte para o modo multi colunas. (Esta função só está disponível na versão 9 ou superior).
- Capacidade de reconhecer rapidamente o painel ativo. Para fazer isso, pressione a tecla de comando NVDA + Seta para cima ou NVDA + TAB.
- Suporte completo para versões de 64 bits do Total Commander.
- Anúncio de ações ao selecionar itens ou desfazêr. (Esta função está disponível na versão 9 ou superior).
- Capacidade de descobrir o número de itens selecionados. (Esta função está disponível na versão 9 ou superior).
- Capacidade de descobrir o tamanho do arquivo selecionado ou todos os itens selecionados.(Esta função está disponível na versão 9 ou superior).
- Anúncio das informações corretas da posição de um item na lista. Para que este recurso funcione, ative a opção correspondente nas configurações do NVDA. (Esta função está disponível na versão 9 ou superior).

<a name="user-content-installation"></a>
# Instalação

1. Baixe o add-on do NVDA [nesta página](https://github.com/jawhien/extendedTotalCmd/releases/latest).
2. No seu explorador de arquivo, navegue até a pasta onde baixou o complemento e precione enter sobre ele.
3. Confirme a instalação clicando no botão " Sim " na caixa de diálogo que aparecer.
4. Se você estiver atualizando o complemento, precisará confirmar a instalação Outra vez.

Você pode instalar o add-on através do gerenciador de add-ons do NVDA, para isso faça o seguinte:
1. Baixe o add-on [nesta página](https://github.com/jawhien/extendedTotalCmd/releases/latest).
2. Abra o Gerenciador de complementos do NVDA no submenu Ferramentas no menu principal do NVDA.
3. Clique no botão "Instalar".
4. Selecione o add-on baixado.
5. Clique em "sim" na caixa de diálogo que aparecer.
6. Se você estiver atualizando o complemento, precisará confirmar a instalação novamente.

<a name="user-content-key-commands"></a>
# Teclas de comando

- CTRL+ Shift + E: diz as informações sobre os ítens selecionados.
- CTRL+ Shift + R: diz as informações de tamanho dos ítens selecionados. Caso não haja nenhum, informa o tamanho do arquivo focado.
- CTRL+ Shift + D: Informa o camino para o diretório atual. Se preciona duas vezes, copia para a área de transferência.
- CTRL+ Shift + T: Diz a data e hora da última modificiação.
- NVDA + A: Informa o painel ativo.
- Alt + W: Informa o nome da guia atual. Precionar duas vezes abre seu menu de contexto.

<a name="user-content-acknowledgments"></a>
# Agradecimentos

Gostaria de agradecer a todos que mandam suas sugestões e também ajudam nos testes e detecção dos erros. A sua contribuição é sem dúvida muito importante para o desenvolvimento deste add-on.

<a name="user-content-faq"></a>
# perguntas frequentes

Não informa o tamanho do arquivo sob o cursor

Em alguns casos (por exemplo, ao trabalhar via FTP), ele não consegue determinar o tamanho do arquivo no cursorpor mais de alguns instantes.

Como posso ajudar a desenvolver o complemento?

Se você gostou do meu add-on, você pode doar qualquer quantia nesta [página especial](https://jnsoft.ru/en/articles/nvda/extendedTotalCmd/donation.php).

Encontrei um bug / tenho sugestões para melhorar o add-on, como posso entrar em contato com você?

Neste caso, você precisa [criar uma nova issue](https://github.com/jawhien/extendedTotalCmd/issues/new) no repositório GitHub. Descreva o máximo possível o seu problema / proposta.

O add-on não suporta meu idioma, posso ajudar com a tradução?

Sim, por favor, envie-me uma mensagem para o endereço de e-mail indicado no add-on e eu lhe enviarei os arquivos e instruções necessários. Você pode visualizar o endereço de e-mail do autor gerenciador de complementos do NVDA. Bem, se você estiver usando o GitHub, basta me enviar um pull request com a tradução, será muito mais conveniente e rápido.

<a name="user-content-change-log"></a>
# Change log

Importante: A baixo daqui, tudo está em inglês!

V3.3.3: 27.03.2023

* Added new localization languages: Portuguese, Portuguese-Brazilian

V3.3.2: 05.12.2022

- Fixed compatibility with BluetoothAudio add-on.
- Additional fix for multi-column view in TC10.52
- Updated localization files.

V3.3.1: 02.12.2022

- Fixed multi-column view in TC10.52

V3.3: 27.11.2022

- Added Ukrainian localization.
- Fixed issue with multicolumn mode on some versions of NVDA.
- Fixed import error in NVDA 2019.2 and below.
- Updated documentation.
- Fixed other minor bugs.

V3.2.3: 25.05.2022

- Fixed multi-column mode in NVDA 2022.1 or higher.

V3.2.2: 24.05.2022

- This patch disables multi-column mode in NVDA 2022 as it does not work properly and should be fixed soon.

V3.2.1: 09.01.2022

- Fixed accidentally broken compatibility with earlier versions of NVDA.

V3.2: 08.01.2022

- Added information about the disk to the window for selecting disks in the format Used space / total space.
- fixed compatibility with nvda 2022+
- Fixed determination of the file modification time.
- Made minor localization improvements.

V3.1: 08.09.2021

- Added a function to reports the active panel. Press "NVDA + A" to find out the active panel.
- Added a function to reports the current tab on the active panel. When you press "ALT + W", the name of the current tab will be reported; Pressing twice it, its context menu will open.
- Added Spanish localization.
- Other minor improvements and fixes.

V3.0: 01.06.2021

- Introduced support for detailed display mode. Attention: this function is experimental and sometimes may not work correctly. If you find a bug, please report it.
- The update module has been completely redesigned. Now it downloads and installs the new version himself, and there is no need to do it manually.
- Added Czech and Slovak localization. Thanks to Radek Žalud and Peter Vágner for the translations provided.
- Compatibility requirements have been changed. Now you need NVDA version 2018.3 or higher to install the add-on.
- The bug that led to the fact that some drop-down lists were displayed incorrectly, for example, such as those opened by pressing the "F2" key in the group rename tool, has been fixed.
- Fixed some compatibility issues with NVDA 2018.3.
- Fixed compatibility with NVDA 2021.1.

V2.5: 19.01.2021

- Fix in the updater: from version 3.0 the compatibility requirements will be updated. Since newer versions will support NVDA 2018.3 or higher, users of earlier versions of the program will receive a message about this when checking for updates.
- Improvement: When reading the status bar, information about the selected item will now be reported, such as size, creation date, attributes, local disk information, etc. depending on TC settings.
- Improvement: added the ability to quickly find out the time and date of the change of the selected item, for this press the combination CTRL+ Shift + t. In NVDA settings, you can change the gestures for this action.
- Improvement: now if callculation of size takes more than 1 second, tones will sound until the process is complete.
- Improvement: the add-on now uses the standard template and SCons for building.
- Fix: the position of the object is no longer reported on the ".." element.
- Fix: in some cases sizing ended with an error.
- Other minor fixes and optimizations.

V2.4: 13.12.2020

- Added definition of the size of directories under the cursor. This is a slower process than determining the size of a single file and can take several seconds.
- Added automatic check for updates after starting NVDA. Note: the automatic check for updates will not be performed if the check for updates for NVDA is disabled in the settings.
- Fixed a bug due to which the size of files was not detected in some cases.
- Fixed a bug due to which the website page in English was always opened.
- Fixed some false positives for selection events.
- Other minor improvements.

V2.3: 05.10.2020

- Fixed incorrect detection of the active panel in some cases.
- Fixed tab support in some 32-bit version dialog boxes.
- Messages about selecting files or canceling it no longer depend on pressing certain keys.
- Fixed duplicate messages when selecting files.
- Fixed persistent messages about selected files when switching tabs in the main window of Total Commander.
- Improvements to dialogs with messages. Now, when these dialogs appear (for example, when deleting files) NVDA will read the information that is displayed on the screen.
- Improved file overwrite dialog. Now when the message about overwriting files appears, NVDA will report all the information that is displayed on the screen.
- The trailing ">" character is now missing in the path to the current directory.
- Fixed determination of the size of selected files. Now it is reported as displayed on the screen. You can set the display format in the Total Commander settings.
- Fixed determining the size of the file under the cursor. It is now reported correctly in both short and detailed view.
- Fixed determination of the size of files with UNC paths and when working via FTP. The size is now reported as displayed on the screen. you can change the display format in the settings of Total Commander. (Works correctly only in short form)
- Updated some messages.
- Updated Russian localization.
- Full code optimization.
- Other minor improvements and fixes.

V2.2.0: 20.04.2020

- When switching tabs, the name of the selected tab will now be reported, as well as its position, if enabled in the NVDA settings.
- Added the function of copying the path to the current folder to the clipboard by double-pressing CTRL + SHIFT + D
- Fixed a bug leading to problems when determining the version of TC.
- Fixed a bug when determining the file size under the cursor associated with using a large font.
- Code optimization.
- Other minor improvements and fixes.

V2.1.0: 21.03.2020

- Added a new function to reports the full path to the current directory.
- Added option to check updates. To check the update, open the tools menu in the main NVDA menu and select "Update Total Commander add-on..."
- Fixed a bug in Total Commander version 7 and 8 when you select file pronounced the message that the TC version is not supported.
- Now add-on can determine the size of any file, even if it is not selected.
- Fixed a bug where the size of the elements for which there is a symbol "." could not be determined.
- Now the size of the elements can be represented in bytes, kB, mB, gB, or tB. The value will be automatically converted to the correct format.
- When reports the size of the directory if it is not defined, the add-on will report it.
- Fully updated documentation. Made the layout of pages for readability.
- Removed unused variables.
- Full code optimization.

V2.0.1: 01.03.2020

- Documentation bugs fixed

V2.0: 22.02.2020

- Fixed a bug where the list borders were erroneously determined on some files.
- The problem was fixed in 32 bit versions of TC8 +, when, upon exiting to the previous directory, the first element of the list was declared first, and then the element in focus.
- Added announcement of item positions in the list, if this feature is enabled in the NVDA settings. (Only in TC9 +).
- Added the ability to report information about selected items by ctrl + shift + e. (Only in TC9 +).
- Added announcement of selected elements when pressing CTRL + A. (Only in TC9 +).
- Added announcement about deselecting when pressing CTRL + num-. (Only in TC9 +).
- Added announcement of the size of selected files by pressing CTRL + SHIFT + R. (Only in TC9 +).

V1.4: 19.07.2019

- The list border signal has been replaced with standard windows sound.
- Added a signal to the top of the list.
- Now not only arrows are processed, but also Home, End, PageUp and PageDown keys for signaling list boundaries.
- Added compatibility with new versions of NVDA.

V1.3

- The sound signal will now play only when navigating the list when the down arrow is pressed on the last element of the list, and not when the focus is on the last element.
- Fixed erroneous behavior outside the main window, settings, and other lists.
- Improved behavior in the FTP connection dialog.

V1.2

- The mechanism for determining the active panel in versions 8 and above has been changed.
- Optimized code to avoid problems with versions 7 and below.
- When the focus falls on the last element of the list, a sound signal will be played.
- Fixed incorrect pronunciation of the active panel outside the main window.

V1.1

- Now, in the disc selection window, disc labels are read.
- A description with the name of the active panel has been added to the elements, when you press the (NVDA + UpArrow) or (NVDA + TAB) keys, the element name and the name of the active panel are pronounced.
- Minor improvements.

V1.0

- First version.