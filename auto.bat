:pythonファイルをドラック&ドロップ
:python %1
:pause

:pythonファイルを同じディレクトリに置いてダブルクリック
@echo off
cd /d %~dp0
py sshauto.py
pause

