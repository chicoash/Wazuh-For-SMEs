# SonicWall Integration


1.  Append the following configuration snippet inside the <ossec_config> </ossec_config> section of the /var/ossec/etc/ossec.conf file
``` xml
  <!--  SYSLOG Firewall -->
  <remote>
    <connection>syslog</connection>
    <port>514</port>
    <protocol>udp</protocol>
    <allowed-ips>this is your sonicwall IP</allowed-ips>
  </remote>
```
2. Restart the Wazuh Manager
``` bash
sudo systemctl restart wazuh-manager
```
