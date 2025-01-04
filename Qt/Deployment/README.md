# Deployment

## Windows Deployment using `windeployqt`

1. **Build Project in Release Mode**
    - Open Qt Creator and build your project in **Release** mode.
    - This will create a new `release` directory containing the build files.

2. **Copy and Rename Release Folder**
    - Copy the entire `release` build directory and rename it to `deploy`:
    
      ```cmd
      xcopy /E /I release deploy
      ```

3. **Add `windeployqt` to PATH**
    - Locate the `windeployqt.exe` command, typically found in `C:\Qt\<version>\<compiler>\bin`.
    - Add this directory to your user environment PATH variable.

4. **Run `windeployqt`**
    - Change the current directory to the `deploy` directory:
    
      ```cmd
      cd deploy
      ```
    - Execute the `windeployqt` command to deploy your application:

      ```cmd
      windeployqt test-app.exe
      ```

5. **Run Your Application**
    - Execute your application to ensure it runs correctly:

      ```cmd
      test-app.exe
      ```

## References
- [How to Deploy Your Qt Cross-Platform Applications to Windows Operating System Using windeployqt](https://medium.com/swlh/how-to-deploy-your-qt-cross-platform-applications-to-windows-operating-system-by-using-windeployqt-a7cd5663d46e)
- [Qt for Windows - Deployment](https://doc.qt.io/qt-5/windows-deployment.html)