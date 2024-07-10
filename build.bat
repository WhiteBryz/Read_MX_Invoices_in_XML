@echo off
del /s /q build
del /s /q dist
del /q XMLScrapping.spec

pyinstaller --onefile ^
			--add-data "info.json;." ^
			--name XMLScrapping ^
			--icon xmlScrapping.ico ^
			main.py