#!/bin/bash

source /home/devstack/Desktop/login/auth.sh
echo $id
echo $ip
openstack server add floating ip '$id' '$ip'
