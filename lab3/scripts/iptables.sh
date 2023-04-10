#!/bin/bash

echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -A FORWARD -p icmp --icmp-type echo-reply -m limit --limit 1/sec -j ACCEPT
iptables -A FORWARD -p icmp --icmp-type echo-request -m limit --limit 1/sec -j ACCEPT
iptables -S