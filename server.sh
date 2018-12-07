#!/bin/bash

#Run with virtualenv
source env/bin/activate

# Compile Bluetooth Server
gcc bluetooth-server/bluetooth_server.c -o bluetooth-server/bluetooth-server -lbluetooth

# Run HTTP Flask Server
python http-server/main.py &
python bluetooth-server/bluetooth_server.py

# On Exit
wait
echo server closed
deactivate
