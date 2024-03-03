@echo off
set "script_dir=%~dp0"
python "%script_dir%crop-video.py" %*
