@echo off
setlocal enabledelayedexpansion
:main
for /l %%i in (1,1,100) do (
    REM echo %%i
    :MIX2 eb606528 
    adb -s eb606528 shell input swipe 540 1300 540 900 220
    :Oppo 1bb5d02d 
    adb -s 1bb5d02d shell input swipe 540 1300 540 900 220
    choice /t 10 /d y /n >nul
    :adb -s 1bb5d02d shell input tap 90 160
    :adb -s 1bb5d02d shell input tap 980 910
)
goto main
REM pause