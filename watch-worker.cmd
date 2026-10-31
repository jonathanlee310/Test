@echo off
title 00 Claude - watch and run every hour (close this window to stop)
cd /d "%~dp0"
echo Claude Code will run the 00 Claude worker now and then again every hour while this window stays open.
echo Close the window (or press Ctrl+C) to stop. The hourly cloud routine keeps running by itself regardless.
echo If it does not start looping, type this line and press Enter:
echo   /loop 1h Follow docs/03-routine-prompt-cloud.md exactly and process the 00 Claude labels now.
echo.
claude "/loop 1h Follow docs/03-routine-prompt-cloud.md exactly and process the 00 Claude labels now."
pause
