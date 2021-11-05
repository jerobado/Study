# Deployment

## Windows Deployment

1. In Qt Creator, build your project in _**Release**_ mode
2. Create a new folder in your current working directory, e.g., _deployment_
3. Copy all the files from the _Release_ build directory to your newly created _**deployment**_ directory
4. Find and add the `windeployqt.exe` command to your user environment PATH variable. The path can be found in `C:\Qt\6.2.1\mingw81_64\bin`.

    Just note that your path will vary depending on available Qt compilers in your system
    
5. Open your favorite CLI like `cmd` or `Windows Terminal` and change the path to the newly created _deployment_ directory
6. Run `windeployqt test-app.exe` command. This will create folders and files as dependencies.
7. Run `test-app.exe`.
8. If all goes well, your shiny new application will now run! Enjoy!


# Resources
- [How to Deploy Your Qt Cross-Platform Applications to Windows Operating System Using windeployqt](https://medium.com/swlh/how-to-deploy-your-qt-cross-platform-applications-to-windows-operating-system-by-using-windeployqt-a7cd5663d46e)
- [Qt for Windows - Deployment](https://doc.qt.io/qt-5/windows-deployment.html)