#!/bin/bash
# Ask the user for their name

#read instance

source /home/devstack/Desktop/login/auth.sh


nova boot --nic net-id=9eb7888c-13a3-4684-8ac5-8769a7884f19 --flavor 1 --image 90764208-f211-447b-95f0-f7c46e3d6772 --security-group default --key-name test2 new_instance | awk -F"|" 'gensub(/^[ \t]+|[ \t]+$/,"","g",$2)=="id"{print gensub(/^[ \t]+|[ \t]+$/,"","g",$3);}'


