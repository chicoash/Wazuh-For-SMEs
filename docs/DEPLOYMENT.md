# Deployment Guide – Wazuh 4.12.0

## 1. Deployment Steps
### Install Wazuh (Single Node)
```bash
curl -sO https://packages.wazuh.com/4.12/wazuh-install.sh && sudo bash ./wazuh-install.sh -a
```
### Once the installation is done, you will see the url and the credentials at the end
![screenshot](images/Installation.png)

### Disable Wazuh Updates (Recommended)
```bash
sed -i "s/^deb /#deb /" /etc/apt/sources.list.d/wazuh.list
apt update
```

### Installing Agents on Windows
```bash
# replace xxx.xxx.xxx.xxx with the Wazuh manager's IP
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.12.0-1.msi -OutFile $env:tmp\wazuh-agent; msiexec.exe /i $env:tmp\wazuh-agent /q WAZUH_MANAGER='xxx.xxx.xxx.xxx' 
```

### Installing Agents on Linux (Debian amd64)
```
# replace xxx.xxx.xxx.xxx with Wazuh manager's IP
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.12.0-1_amd64.deb && sudo WAZUH_MANAGER='xxx.xxx.xxx.xxx' dpkg -i ./wazuh-agent_4.12.0-1_amd64.deb
```

