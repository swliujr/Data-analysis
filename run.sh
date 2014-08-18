#!/bin/bash

cd /home/work/data_anlyzer/py

year=`date +%Y`
month=`date +%m`
day=`date -d '-1 days' +%d`
rm -f /home/work/baihe/fire/photo/clog/file/${year}/${month}/${day}/${year}-${month}-${day}_0.log
python dsclog.py $year $month $day channelid
python dfclog.py $year $month $day
python dmysqldata.py
python showtime.py $year $month $day
