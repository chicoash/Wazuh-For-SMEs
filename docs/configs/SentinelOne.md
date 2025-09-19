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
1. Create API Polling Script
    - Place the script in /var/ossec/integrations/sentinel_one.py
        + [S1 Script](docs/sentinel_one.py)
    - 


