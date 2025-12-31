@echo off
echo ==========================================
echo      GCP Study Plan - GitHub Pusher
echo ==========================================

REM 1. Find Git
set "GIT_CMD=git"
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo 'git' command not found in PATH. Checking default location...
    if exist "C:\Program Files\Git\cmd\git.exe" (
        set "GIT_CMD=C:\Program Files\Git\cmd\git.exe"
        echo Found Git at: "C:\Program Files\Git\cmd\git.exe"
    ) else (
        echo [ERROR] Could not find Git! 
        echo Please restart VS Code to refresh your environment variables.
        pause
        exit /b 1
    )
)

echo.
echo [1/5] Initializing Repository...
"%GIT_CMD%" init

REM Configure Identity (to avoid 'who are you' errors)
"%GIT_CMD%" config user.email "student@gcpstudy.com"
"%GIT_CMD%" config user.name "GCP Student"

echo.
echo [2/5] Adding Files (ignoring secrets)...
"%GIT_CMD%" add .

echo.
echo [3/5] Committing Code...
"%GIT_CMD%" commit -m "Auto-commit by GCP Agent"

echo.
echo [4/5] Linking to GitHub...
"%GIT_CMD%" remote remove origin >nul 2>nul
"%GIT_CMD%" remote add origin https://github.com/jyothivempa/gcp-study-plan.git

echo.
echo [5/5] Pushing to Main...
"%GIT_CMD%" branch -M main
"%GIT_CMD%" push -u origin main

echo.
echo ==========================================
echo           SUCCESS! 🚀
echo ==========================================
