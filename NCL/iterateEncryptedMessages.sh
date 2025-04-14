#!/bin/bash
rm log.txt
for i in $(seq 1 50); do
echo Verifying email_$i >> log.txt
gpg --verify email_$i.txt.sig email_$i.txt 2>> log.txt
done

for i in $(seq 1 50); do
cat email_$i.txt
read
done
