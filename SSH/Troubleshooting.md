# Troubleshooting


### Unprotected private key file
```bash
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'path/to/private/key' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "path/to/private/key": bad permissions
[user]@[ipaddress]: Permission denied (publickey).
```

#### Solution:
- Change the permission of the private key to read-only to the current user
    
    ```bash
    sudo chown 400 path/to/private/key  # 400 is read-only
    ```