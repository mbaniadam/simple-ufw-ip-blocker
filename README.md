# Simple IP blocker in UFW firewall 


This repository contains a simple Python script that integrates with a Postgres database and schedules firewall rules based on IP addresses and expiration dates. The script retrieves IP addresses and expiry dates from user input, inserts them into a Postgres database running in a Docker container, and calculates the expiry dates. If an IP address with an expired date is found, the script sends a command to the UFW firewall to block that IP.

You can schedule wg_expiration.py to run periodically (e.g., using a cron job) to automatically update firewall rules and block expired IP addresses.

### Prerequisites
To run this script, you need to have the following dependencies installed:

Python 3.x
Docker


### Getting Started
Follow the steps below to get started with this script:

#### Clone the repository to your local machine:
git clone https://github.com/mbaniadam/simple-blocker-linux.git

#### Install the required Python dependencies:
pip install psycopg2

#### Start the Postgres database container using Docker:
docker-compose up -d

### Run the script:
python3 add_user_in_db.py

