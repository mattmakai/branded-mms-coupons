#!/bin/sh
ansible-playbook coupons.yml -vvvv --private-key=./ssh_conf/id_rsa -K -u deployer -i ./hosts
