# Product catalog API.

This repository contains all the code needed for running the Product catalog API.


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#installation">Installation</a></li>
          <li><a href="#usage">Usage</a></li>
         <ul>
           <li><a href="#usage">Run Locally</a></li>
         </ul>
      <li><a href="#pycharm-configurations">Pycharm Configurations</a></li>
    <li><a href="#useful-links">Useful Links</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Micro Service created with FastAPI and Python.
This project includes a Docker Compose file ready to build and run.

### Built With
   - Python 3.10
   - Django and DRF
   - PostgreSQL
   - Docker
   - Docker Compose
   - PyCharm
   - Git
   - GitHub
   - Swagger
   - AWS

<!-- INSTALLATION -->
# Installation

To get a local copy up and running follow these simple steps.

* Make sure you add a new SSH key to your GitHub account. [GitHub Documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
* Install [Docker Desktop](https://www.docker.com/products/docker-desktop)


Instructions to set up the project on Linux & macOS. 


1. Clone the repo
   ```sh
    git clone git@github.com:sebadp/catalog.git   
   ```
2. To create a virtualenv use the following command. Always remember to activate it manually
   ```sh
   python3 -m venv catalog
   ```
   Once it is activated you should see a prompt similar to this (zsh)
   >(catalog) ➜   catalog git:(main)
   
   If having an issue with venv:

   $ sudo apt install python3.9-venv > $  python3.9 -m venv catalog

3. Change directory to catalog
   ```sh
   cd catalog
   ```
4. Install python dependencies with pip.
   ```sh
   pip install -r requirements.txt
   ```
5. Build containers with docker-compose.
   ```sh
   docker-compose build
   ```
6. Start containers.
   ```sh
   docker-compose up -d
   ```

Congrats!

You should be able to open the site in your browser now 
> http://localhost:8000/


<!-- PYCHARM CONFIGURATIONS -->
## PyCharm Configurations

### Configure the Python Interpreter
1. In a terminal, place your prompt at the project root directory.
2. Activate your venv environment
   ```sh
   source ../catalog/bin/activate
   ```
3. Copy the path to your Python interpreter
   ```sh
   which python
   ```
4. Open your Pycharm-Professional
   ```sh
   pycharm-professional
   ```
5. Go to Settings > Project: catalog > Python Interpreter.
6. Add python interpreter > Add local interpreter > Existing environment.
7. Paste the path that you copy at step 3.
8. Go to Settings > Project: catalog > Project Structure
9. Add as source the app directory.(must be blue colored once selected)


### Configure Docker Runner

10. Go to Settings > Plugins > Docker and install the plugin.
11. Go to "Run" > "Edit Configurations..." 
12. Add a new Docker-Compose Configuration(Press the "+" button).
13. Select the Server field at the three dots("..."). 
14. Connect with Docker Daemon with Socket Unix Default
15. Select the Docker Compose file: ./docker-compose.yml
16. Press: Apply > OK > Run

<!-- USEFUL LINKS -->
## Useful links

- [Product Definitions](/docs/DEFINITIONS.md)
- [How I will Scale](/docs/SCALE_UP.md)
- [API Documentation](http://localhost:8000/SWAGGER)