@echo off
title HiQ Robocon Quiz 2D (c) HiQ/Keltsu 2019
MODE 178,56
color 06
robot -d web_pipotest/ --outputdir \hiq_quiz\temp\reports --variablefile \hiq_quiz\web_competition\99_common_data\common_data.py .
pause