


This repository contains a simple Python script that integrates with a Postgres database and schedules firewall rules based on IP addresses and expiration dates. The script retrieves IP addresses and expiry dates from user input, inserts them into a Postgres database running in a Docker container, and calculates the expiry dates. If an IP address with an expired date is found, the script sends a command to the UFW firewall to block that IP.


### Prerequisites
To run this script, you need to have the following dependencies installed:

Python 3.x
Docker
