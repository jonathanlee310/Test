@echo off
title 00 Claude - run the worker once (real time)
cd /d "%~dp0"
echo Starting Claude Code in this folder and running the 00 Claude worker once on whatever is labelled.
echo The window stays open afterwards so you can ask follow-up questions. Close it when you are done.
echo The hourly cloud routine keeps running by itself regardless of this window.
echo.
claude "Follow docs/03-routine-prompt-cloud.md exactly and process the 00 Claude labels now. When finished, print the run summary and tell me, in plain language, what you did and what I should check."
pause
