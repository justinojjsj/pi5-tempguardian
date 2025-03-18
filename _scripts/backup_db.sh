#!/bin/bash

#Variables
YearMonth=$(date '+%Y-%m')
YearMonthDay=$(date '+%Y-%m-%d')

#Performs backup with date of day
cd /home/silvajunior/desenvolvimento/pi5-tempguardian/_db
mkdir -p  $YearMonth
docker exec -i tempguardian_db bash -c 'mariadb-dump -u root -p"tX84c=7OljSX"  db_tempguardian' > /home/silvajunior/desenvolvimento/pi5-tempguardian/_db/$YearMonth/bkp_$YearMonthDay.sql
