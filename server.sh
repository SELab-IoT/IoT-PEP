#!/bin/sh

# Compile Bluetooth Server
gcc bluetooth-server/bluetooth_server.c -o bluetooth-server/bluetooth-server -lbluetooth

# Run HTTP Flask Server
python http-server/main.py &
python bluetooth-server/bluetooth_server.py

wait
echo server closed
