# How to create an installer

1. Create a `package` directory

2. Create `config.xml` configuration file in **config** directory
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <Installer>
        <Name>Eddy</Name>
        <Version>0.3.0</Version>
        <Title>Eddy v0.3 Installer</Title>
        <Publisher>Microsoft</Publisher>
        <StartMenuDir>Eddy</StartMenuDir>
        <TargetDir>@HomeDir@/Eddy</TargetDir>
    </Installer>
    ```

3. Create `package.xml` package information file in **meta** directory
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <Package>
        <DisplayName>The root component</DisplayName>
        <Description>Install this example.</Description>
        <Version>0.3.0</Version>
        <ReleaseDate>2024-01-01</ReleaseDate>
        <Licenses>
            <License name="GNU Lesser General Public License (LGPL) v3.0 Agreement" file="license.txt" />
        </Licenses>
        <Default>script</Default>
        <Script>installscript.qs</Script>
        <UserInterfaces>
            <UserInterface>page.ui</UserInterface>
        </UserInterfaces>
    </Package>
    ```

4. Create and package your application in `.zip` file in `data` directory

5. Run `binarycreator` tool

    On Windows
    ```
    binarycreator --offline-only -c config\config.xml -p packages EddyInstaller.exe
    ```

    This will create `EddyInstaller.exe` installer.

    Note: binarycreator must be in your PATH environment variable to run this command

# Resources
- [Tutorial: Creating an Installer](https://doc.qt.io/qtinstallerframework/ifw-tutorial.html)