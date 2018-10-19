#!/bin/bash
while true
do
   if [ -z $(curl http://169.254.169.254/latest/meta-data/spot/termination-time | head -1 | grep 404 | cut -d \ -f 2) ]
   then
      # 2 minute warning received. Do all your cleanup work.
      break
   else
      # Still running fine, sleep and then check again
      sleep 3
   fi
done