@echo off
title HiQ Robocon Quiz 2D (c) HiQ/Keltsu 2019
MODE 190,50
color 06
robot -d web_pipotest/ --outputdir \hiq_pipo\temp\reports --variablefile \hiq_pipo\web_competition\99_common_data\common_data.py .
pause
