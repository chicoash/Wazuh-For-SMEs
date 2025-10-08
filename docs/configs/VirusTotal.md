# VirusTotal Integration
Prerequisites
1. Virustotal account (to get the api key)


On Wazuh Server
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
3. Add Agent Config
- Go to Agents management → Groups
- Select the group where you want VT to integrate
- Click Edit group configuration under the Actions
- Add the following configurations (this will push the config to all Linux machines under the group)
    ``` bash
    <agent_config os="Linux">
      <syscheck>
        <directories realtime="yes" check_all="yes"> /tmp</directories>
        <directories realtime="yes" check_all="yes"> /var/www/html</directories>
      </syscheck>
    </agent_config>
    ```
