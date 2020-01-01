@echo off
setlocal enabledelayedexpansion
:main
for /l %%i in (1,1,100) do (
    REM echo %%i
    :adb shell input tap 81 1081
    :choice /t 3 /d y /n >nul
    :adb shell input tap 60 120
    :adb shell input tap 987 1223
    choice /t 10 /d y /n >nul
    adb shell input swipe 540 1300 540 900 220
)
goto main
REM pause