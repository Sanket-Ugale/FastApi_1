# FastAPI API Repository

This repository contains a set of APIs created using FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

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

<strong>API Endpoints</strong>
Here are the API endpoints available in this project:
<strong>Authentication</strong>


<strong>POST</strong>
/login
Login

<strong>Blogs</strong>


<strong>GET</strong>
/blog/
All



<strong>POST</strong>
/blog/
Create



<strong>PUT</strong>
/blog/{id}
Update



<strong>GET</strong>
/blog/{id}
Show



<strong>DELETE</strong>
/blog/{id}
Destroy


<strong>Users</strong>


<strong>GET</strong>
/user/
All



<strong>POST</strong>
/user/
Create User



<strong>GET</strong>
/user/{id}
Show



<strong>DELETE</strong>
/user/{id}
Destroy