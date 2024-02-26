# File Extension Identification via WebSocket in Django

This project implements a WebSocket service using Django that allows clients to send a file to the server. The server then identifies the file's extension and returns this information to the client.

## Key Features

- WebSocket Setup: Implements the WebSocket connection using Django Channels.
- File Processing: Accepts a file over the WebSocket, determines its extension, and communicates this back to the client.
- Security Measures: Addresses common security concerns to ensure safe file handling.
- Documentation: Thoroughly documents the setup, usage, dependencies, and interaction with the WebSocket service.

## Getting Started

### Prerequisites

- Python 3.12


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/KarimTayie/file-extension-websocket.git
    cd file-extension-websocket
    ```
2. **Create a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # Linux/Mac
    # OR
    .\env\Scripts\activate   # Windows
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This project relies on `python-magic`. Ensure that `libmagic` is installed on your system:

    - **Debian/Ubuntu:** 
        ```bash
        sudo apt-get install libmagic1
        ```

    - **Windows:** 
        You'll need DLLs for libmagic. You can fetch them with:
        ```bash
        pip install python-magic-bin
        ```

    - **macOS:**
        - When using Homebrew: 
            ```bash
            brew install libmagic
            ```
        - When using MacPorts: 
            ```bash
            port install file
            ```

3. **Set up environment variables:**
   
    Create a `.env` file in the project root directory and define the following variables:
   
    ```plaintext
    SECRET_KEY=<your_secret_key>
    DEBUG=True
    MAX_ALLOWED_SIZE=<max_allowed_size_in_megabytes>
    ```

## Usage

1. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

2. **Navigate to `http://localhost:8000/fe/upload/`** in your web browser to access the file upload form.

3. **Choose a file** and click the "Send File" button. The file extension will be identified and displayed on the page.

## WebSocket Configuration

- The WebSocket endpoint for file extension identification is located at **`ws://localhost:8000/ws/file_extension/`**.

## Notes

- The maximum allowed size for uploaded files is defined by the `MAX_ALLOWED_SIZE` environment variable in the `.env` file.
- Files exceeding the maximum allowed size will result in a validation error.
- File extensions are identified using the `python-magic` library along with MIME type detection.
