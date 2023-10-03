# FastAPI API Repository

This repository contains a set of APIs created using FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#Api-Endpoints)

## Getting Started

### Prerequisites

Before you start, make sure you have the following installed:

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

### Installation

1. Clone this repository:

   ```shell
   git clone https://github.com/Sanket-Ugale/fastapi_1.git

2. Navigate to the project directory:

    ```shell
    cd fastapi-api-repo

3. Install the dependencies:

    ```shell
    pip install -r requirements.txt

4. Usage
   To run the FastAPI application, use the following command:

    ```shell
    uvicorn main:app --reload
Replace main with the name of your FastAPI app file.

## Api-Endpoints
<!-- <h1>API Endpoints</h1> -->
Here are the API endpoints available in this project:
<br><h2>Authentication</h2>


<strong>POST</strong><br>
Use: Login<br>
Route: /login<br><br>

<h2>Blogs</h2><br>


<strong>GET</strong>
Use: Get All Blogs<br>
Route: /blog/<br><br>



<strong>POST</strong><br>
Use: Create Blog<br>
Route: /blog/<br><br>



<strong>PUT</strong><br>
Use: Update Blog<br>
Route: /blog/{id}<br><br>



<strong>GET</strong><br>
Use: Show Blog By id<br>
Route: /blog/{id}<br><br>



<strong>DELETE</strong><br>
Use: Destroy Blog<br>
Route: /blog/{id}<br><br>


<h2>Users</h2><br>


<strong>GET</strong><br>
Use: Show all Users<br>
Route: /user/<br><br>



<strong>POST</strong><br>
Use: Create User<br>
Route: /user/<br><br>



<strong>GET</strong><br>
Use: Show User By id<br>
Route: /user/{id}<br><br>



<strong>DELETE</strong><br>
Use: Delete User<br>
Route: /user/{id}<br><br>