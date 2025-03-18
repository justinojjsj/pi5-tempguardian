#!/bin/bash

cd /home/silvajunior/desenvolvimento/pi5-tempguardian/

git checkout db_e_log-atualizados
git add --all
git commit -a -m 'Atualização do banco de dados e dos logs'
git push