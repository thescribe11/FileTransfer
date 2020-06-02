!include MUI2.nsh

Unicode true
BrandingText "Thescribe Inc."

Name "File Transfer Tools"

OutFile "Install File Transfer Tools.exe"

InstallDir "$APPDATA\File Transfer Tools"
InstallDirRegKey HKCU "Software\File Transfer Tools" ""
RequestExecutionLevel admin

!define MUI_ICON "icon.ico"
!define MUI_UNICON "icon.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "background.bmp"
!define MUI_ABORTWARNING


!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "License.txt"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\File Transfer Tools"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"

!insertmacro MUI_PAGE_INSTFILES

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "Install" SecInstall
    CreateDirectory "$INSTDIR\bin"
    SetOutPath "$INSTDIR\bin"
    WriteRegStr HKCU "Software\File Transfer Tools" "" $INSTDIR
    WriteUninstaller "$INSTDIR\Uninstall.exe"
    CreateDirectory "$SMPROGRAMS\File Transfer Tools"
    CreateShortcut "$SMPROGRAMS\File Transfer Tools\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
    CreateShortCut "$SENDTO\File Transfer Tools.lnk" "$INSTDIR\bin\send.exe"
    File send.exe
    File receive.exe
    EnVar::Check "NULL" "NULL"
    Pop $0
    DetailPrint "EnVar::Check write access HKCU returned=|$0|"

    EnVar::SetHKLM
    EnVar::AddValue "Path" "$INSTDIR\bin"
SectionEnd

LangString DESC_SecInstall ${LANG_ENGLISH} "Installing File Transfer Tools..."
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecInstall} ${DESC_SecInstall}
!insertmacro MUI_FUNCTION_DESCRIPTION_END

Section "Uninstall"
    Delete "$INSTDIR\Uninstall.exe"
    Delete "$INSTDIR\bin\send.exe"
    Delete "$INSTDIR\bin\receive.exe"
    RMDIR "$INSTDIR\bin"
    RMDIR $INSTDIR
    RMDIR "$INSTDIR"
    Delete "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk"
    Delete "$SENDTO\File Transfer Tools.lnk"
    RMDIR "$SMPROGRAMS\$StartMenuFolder"

    DeleteRegKey /ifempty HKCU "Software\File Transfer Tools"
SectionEnd