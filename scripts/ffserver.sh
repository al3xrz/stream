echo 'Попытка остановки FFSERVER'
killall ffserver
sleep 5
echo 'Запуск FFSERVER'
ffserver -f ./ffserver.conf

