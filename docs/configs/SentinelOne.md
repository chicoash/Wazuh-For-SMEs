# SentinelOne (S1) Configuration

## Integrating S1 with Wazuh using API
### Prerequisites
1. SentinelOne account with rights to create service users.
2. Windows endpoint (or any device) with the SentinelOne agent installed for testing.

### SentinelOne Portal:
1. Generate API Token in SentinelOne
    - Go to Settings → Users → Service Users
    - Create a new service user: give name, description, expiration.
    - Choose access scope: entire account or just specific sites.
    - Assign Viewer role.
    - Copy the generated API token.

### On Wazuh Server: 
1. Install dependencies for the script
    ``` bash
    # allow script to read the environment variable file
    sudo apt install python3-dotenv
    ```
2. Create .env file to store the token
    - Create the env file in /var/ossec/integrations/ by changing to the mentioned directory
        ``` bash
        cd /var/ossec/integrations/
        ```
    - Create the file and paste the API token in this file
        ```bash
        nano .env #copy the api key into this file
        ```
    - Set the ownership and permissions to root and wazuh user
        ```bash
        chmod 600 .env
        chown root:wazuh .env
3. Create API Polling Script
    - Place the script in /var/ossec/integrations/sentinel_one.py
        + [S1 Script](../sentinel_one.py)
    - Set the ownership and permissions to root and wazuh user
        ``` bash
        chown root:wazuh /var/ossec/integrations/sentinel_one.py
        chmod 750 /var/ossec/integrations/sentinel_one.py
        ```
    - Automate the execution of the script to retrieve the logs using crontab
        ```bash
        # run the job in realtime
        * * * * * /usr/bin/python3 /var/ossec/integrations/sentinel_one.py
        ```
4. Configure Wazuh to monitor the S1 log file for new logs
    - Append the following configuration snippet inside the <ossec_config> </ossec_config> section of the /var/ossec/etc/ossec.conf file
        ``` xml
        <localfile>
          <log_format>json</log_format>
          <location>/var/log/sentinelone.json</location>
        </localfile>
        ```
    - Make the log file accessible to wazuh user
        ``` bash
        chown root:wazuh /var/log/sentinelone.json
        chmod 640 /var/log/sentinelone.json
        ```
5. Create the S1 rules
    -   Place this file [sentinelone.xml](../Rules/sentinelone.xml) in /var/ossec/etc/rules/

6. Restart the Wazuh Manager
    ```bash 
    sudo systemctl restart wazuh-manager
    ```



