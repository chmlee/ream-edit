#!/bin/bash

while true; do 
    CPU=$(top -b -n1 | grep "flask" | head -1 | awk '{print $9}')
    MEM=$(top -b -n1 | grep "flask" | head -1 | awk '{print $10}')
    echo -n -e "\r CPU: $CPU | MEM: $MEM"
    sleep 5
done
