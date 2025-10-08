# VirusTotal Integration


1.  Append the following configuration snippet inside the <ossec_config> </ossec_config> section of the /var/ossec/etc/ossec.conf file
``` xml
  <!--  VT Integration -->
  <integration>
    <name>virustotal</name>
    <api_key>your key</api_key>
    <group>syscheck</group>
    <alert_format>json</alert_format>
  </integration>
```
2. Restart the Wazuh Manager
``` bash
sudo systemctl restart wazuh-manager
```
