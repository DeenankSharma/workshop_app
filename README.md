# ShoutBoard

This is a simple messaging app built with Flask. The project is structured with separate directories for backend and frontend components, making it easier to manage and scale.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Navigate to the Project Directory](#2-navigate-to-the-project-directory)
  - [3. Create a Virtual Environment](#3-create-a-virtual-environment)
  - [4. Activate the Virtual Environment](#4-activate-the-virtual-environment)
  - [5. Install Required Packages](#5-install-required-packages)
  - [6. Run the Application](#6-run-the-application)

## Prerequisites

- Python 3.x installed on your system.
- Git installed on your system.
- VS Code or any other IDE.
- Live Server extension on VS Code.(not compulsory)

## Getting Started

Follow these steps to clone the repository, set up the environment, and run the application:

### 1. Clone the Repository

First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/DeenankSharma/workshop_app.git
```

### 2. Navigate to the Project directory

```bash
cd WORKSHOP_APP
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

Activate the virtual environment. The activation command varies depending on your operating system:

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Required Packages

Navigate to the backend directory and install Flask along with any other necessary packages:

```bash
cd backend
pip install flask
```

### 6. Run the backend

To start the Flask development server, use the following command within the backend directory:

```bash
python app.py
```

The backend will be accessible locally at http://127.0.0.1:5000. 
### 7. Run the frontend

```bash
cd ..
cd frontend
```

and Go Live on index.html or else you can just open the file directly in browser.
