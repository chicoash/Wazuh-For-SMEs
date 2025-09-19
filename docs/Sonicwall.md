# This file contains SentinelOne, O365 and Sonciwall Configurations

## SonicWall
### Append the following configuration snippet inside the <ossec_config> </ossec_config> section of the /var/ossec/etc/ossec.conf file
``` bash
  <!--  SYSLOG Firewall -->
  <remote>
    <connection>syslog</connection>
    <port>514</port>
    <protocol>udp</protocol>
    <allowed-ips>this is your sonicwall IP</allowed-ips>
  </remote>
```

