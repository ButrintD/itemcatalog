### Project Overview
> The aim of this project was to develop a web application that has CRUD support and uses third party user authentication and authorization. The application is an online Catalog with different categories, a list of items within each of those categories with the ability to add, edit or delete items.

### Technologies used
>Python
>Flask
>SQLAlchemy 

#### Project Setup:
  1. Install [Vagrant](https://www.vagrantup.com/) 
  2. Install [VirtualBox](https://www.virtualbox.org/)
  2. Clone or Download [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Navigate to the catalog folder and put the project inside the catalog folder.
  
#### Starting the Virtual Machine:
  1. **vagrant up** to start up the VM.
  2. **vagrant ssh** to login into the VM.
 
#### Run the Catalog Application:
  1. After you have logged into the VM, change to this directory **cd /vagrant/catalog**.
  2. Run the following python script **python db_populator.py** to populate the database with some data.
  3. Start the Catalog Application by running this python script **python project.py**.
  4. Use this URL **http://localhost:8000** to play around with the application.
