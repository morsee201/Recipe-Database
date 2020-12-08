# Project Information
This is Team 4K's autograder project for CIS-405 Software Engineering.

# Installation Instructions
To get the site working you will need both django and docker installed onto your machine. Then you will need to
clone from the master branch of this repository. Once you have all the files cloned you should build the images
needed to run the website with the build command from our run script. See 'Run Script Commands' below on how to do
this. After that you should migrate the files through the migrate command and you can either use the provided
fixture for a pre-built database. Or you can build a new database from scratch. If you have issues with
connecting to the database see 'Database Troubleshooting' below.

# Run Script Commands
The script is run by entering "python3 run.py 'command' " with 'command' being:  
up: do docker-compose up  
down: do docker-compose down  
build: does docker build  
migrate: runs makemigrations and migrate  
admin: create a new superuser  
test: run all of the tests made  
load-data: Loads the fixture stored in the 'fixtures' directory.  
dump-data: Stores your current database setup into the 'fixtures' directory.  

# Fixture Database Info
If you are loading the pre-built database this is the information you will need:  
The admin username is: Team4K  
The password for every user is: TBEJ@potsdam

# Database Troubleshooting
If you get an error saying that you can't connect to the mariadb server, find the id of the container running
the mariadb service and enter the following:

````
sudo docker exec -it <container ID> bash
root@<container ID>:/ mysql -u root -p
````

It will ask you for a password, it is either:" This_is_a_bad_password" or you just press enter. Once you're in
do this:

````  
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'django'@'%' IDENTIFIED BY 'django' WITH GRANT OPTION;FLUSH PRIVILEGES;
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'django'@'localhost' IDENTIFIED BY 'django' WITH GRANT OPTION;FLUSH PRIVILEGES;
MariaDB [(none)]> CREATE DATABASE autograder;
````

By this point it should work.

