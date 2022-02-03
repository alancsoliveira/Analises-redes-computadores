#!/bin/bash

DIR="../../simulation/$pktSize/"

# Simulation Time
SIMULATION_TIME=120

# Packet Size
packetSize=(512 1024 1500)

# Nodes Wifi
nWifi=(2 4 8 16 32 64 100)


for pktSize in "${packetSize[@]}"; do
    
    # Create Packet Size dir 
    if [ ! -d $DIR ];
    then
        mkdir $DIR ;
    fi

    for nodeWifi in "${nWifi[@]}"; do
        echo -e "packetSize: $pktSize, nWifi: $nodeWifi\n" ;
        sudo ../waf --run "networkCristian --packetSize=$pktSize --nWifi=$nodeWifi --simulationTime=$SIMULATION_TIME --verbose=0"; 2>> $DIR/log-netWorkOne-packetSize-$pktSize-nWifi-$nodeWifi.txt ;
        echo -e "\n" ;
    done    
done
