# Python Installation Manager

Python Installation Manager is a Windows application for managing installed Python version in Windows.

## Usage

### List installed Python versions

```
> py list
Tag           Name            Managed By  Version  Alias                                
3.14[-64]  *  Python 3.14.3   PythonCore  3.14.3   python3[-64].exe, python3.14[-64].exe
3.12[-64]     Python 3.12.10  PythonCore  3.12.10  python3.12[-64].exe  
```

### Install Python version
```
> py install 3.14
```

### Upgrade installed Python version

```
> py install 3.14 --update
```

## References
- [Get started with the new Python Installation Manager](https://www.infoworld.com/article/4001983/get-started-with-the-new-python-installation-manager.html)