# Installation Instructions (For New PC)

To install this software on another computer, follow these steps:

## 1. Install prerequisites
-   Download and Install **Python** (version 3.10 or higher) from [python.org](https://www.python.org/).
-   **Important**: During installation, check the box that says **"Add Python to PATH"**.

## 2. Copy Files
-   Copy the entire `talvex` folder to the new computer.

## 3. One-Click Setup (Recommended)
Simply double-click the `setup.bat` file in the folder.
This will automatically:
1.  Create the environment.
2.  Install libraries.
3.  Create the admin (`Vrushabhsakhiya`)
4.  Start the application.

---
**Advanced / Manual Setup:**
If the above doesn't work, follow these steps:
1.  Open the folder in VS Code or Terminal.
2.  Open Terminal (`Ctrl + ~`) and run:
    ```powershell
    python -m venv .venv
    ```
3.  Activate the environment:
    ```powershell
    .venv\Scripts\activate
    ```

## 4. Install Dependencies
Run the following command to install required libraries:
```powershell
pip install -r requirements.txt
```

## 5. Setup Database & Admin
Initialize the database and create the default admin user by running:
```powershell
python setup_app.py
```
*This creates the admin user `Vrushabhsakhiya` with password `@VrU(846)`.*

## 6. Run the Application
Start the software by running:
```powershell
python app.py
```
Open your browser and search for `http://127.0.0.1:5000`
