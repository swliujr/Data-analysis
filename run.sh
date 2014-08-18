#!/bin/bash

cd /home/work/data_anlyzer/py

year=`date +%Y`
month=`date +%m`
day=`date -d '-1 days' +%d`

python dsclog.py $year $month $day channelid
python dfclog.py $year $month $day
python dmysqldata.py
python showtime.py $year $month $day
