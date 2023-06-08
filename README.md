# Simple IP Blocker and Unblocker Based on Valid Days

### Blocking and Unblocking IP addresses in the UFW firewall based on the valid days entered in the script.

![image](https://github.com/mbaniadam/simple-ufw-ip-blocker/assets/75830370/3080c9c4-4213-4787-b383-5847feeb33a0)
![image](https://github.com/mbaniadam/simple-ufw-ip-blocker/assets/75830370/d48fd8d8-9505-4b8d-8e05-a7dc40fe25dc)
![image](https://github.com/mbaniadam/simple-ufw-ip-blocker/assets/75830370/5cca7e62-e02f-42ae-807e-86d8d9623dfc)
#### This repository contains a simple Python script that integrates with a Postgres database and firewall rules based on IP addresses and expiration dates.

#### The script retrieves IP addresses and expiry dates from user input, inserts them into a Postgres database running in a Docker container, and calculates the expiration dates based on the current date. If an IP address in database with an expired date is found, the script sends a command to the UFW firewall to block that IP.

#### You can schedule wg_expiration.py to run periodically (e.g., using a cron job) to automatically update firewall rules and block expired IP addresses.

### Prerequisites
To run this script, you need to have the following dependencies installed:

Python 3.x

Docker

psycopg2


## Getting Started
Follow the steps below to get started with this script:

#### Clone the repository to your local machine:
git clone https://github.com/mbaniadam/simple-blocker-linux.git

#### Install the required Python dependencies:
pip install psycopg2

#### Start the Postgres database container using Docker:
docker-compose up -d

#### Run the script:
python3 add_user_in_db.py


## Usage

The script can be adapted for accounting purposes by associating IP addresses with accounting-related data, such as users in softwares like Wireguard etc. You can modify the script to store additional information in the database, such as account numbers, transaction types, or financial values. This allows you to leverage the script's scheduling capabilities and integrate it into your accounting processes.


## Contributing

Contributions to this project are welcome. If you find any issues or have ideas for improvements, please submit a pull request or open an issue on the GitHub repository.
