#!/usr/bin/env bash

/etc/init.d/cron start
#chmod u+x /app/crontab_scheduler.sh
#chmod u+x /app/script_executor.sh
#/app/crontab_scheduler.sh

exec "$@"