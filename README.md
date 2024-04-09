# Address Book
Build an address book application with a RESTful API using FastAPI to facilitate address creation, updating, retrieval, and deletion, all stored in an SQLite database with coordinates. Incorporate spatial search functionality for users to access addresses within a specified distance from given location coordinates, utilizing FastAPI's built-in Swagger documentation for API reference and testing.

## For Running Locally

### Prerequisites

To run the source files locally, you may require the below tools/frameworks

- Visual Studio
- Python

### Installation
- Run this command to install virtual environment
  ```python
  python3 -m venv venv
  ```
- Activate your environment
    ```bash
    # Windows command prompt
    venv\Scripts\activate.bat

    # Windows PowerShell
    venv\Scripts\Activate.ps1

    # macOS and Linux
    source venv/bin/activate
    ```
- Install requirements to the virtual environment
    ```python
    pip install -r requirements.txt

-Run this command inside the root folder

```uvicorn main:app --reload