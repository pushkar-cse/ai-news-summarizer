@echo off
title AI News Bot
cd /d C:\news-bot
echo Starting AI News Bot...
echo.
python digest_gemini.py
echo.
echo News digest completed!
pause