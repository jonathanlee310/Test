@echo off
title 00 Claude - Claude Code in this folder
cd /d "%~dp0"
echo Opening Claude Code in this folder. If it asks you to log in, type /login and press Enter.
echo.
claude "Read CONTINUE.md and SETUP-STATUS.md. Tell me in a few lines where this project stands and what I can ask you to do next, then wait for my instruction."
pause
