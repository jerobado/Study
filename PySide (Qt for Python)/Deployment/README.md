# Deployment
- `pyside6-deploy` is an easy to use tool for deploying PySide6 applications to different platforms. 
- It is a wrapper around Nuitka, a Python compiler that compiles your Python code to C code, and links with libpython to produce the final executable.
- The final executable produced has a .exe suffix on Windows, .bin on Linux and .app on macOS.

### Usage
```cmd
pyside6-deploy /path/to/main_file.py
```

### References
- [pyside6-deploy: the deployment tool for Qt for Python](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html)