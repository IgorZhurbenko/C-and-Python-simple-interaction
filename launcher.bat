echo off
chcp 855
cls
gcc main.c
if %errorlevel% == 0 (
a.exe 1 2 3 4 5)
pause
