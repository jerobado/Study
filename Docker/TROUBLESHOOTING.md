# Troubleshooting

### Build error?
- disconnect to VPN
- add `--network host` flag when building

### Can't start Docker Desktop on Windows?
- if you are in a standard account, make sure your account is added in the `docker-user` group
- run **Computer Management** as administrator 
- open **Local Users and Groups** node > **Groups** 
- find and right-click `docker-users`, select **Add to Group**... in the context menu
- in the _docker-users Properties_ dialog, add the user you want to add as member of that group