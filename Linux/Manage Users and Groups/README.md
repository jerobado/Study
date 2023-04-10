# Manage Users and Groups

Remember:
- avoid using the root account
- create unique accounts for each user
- assign only necessary authority to each user

## Monitoring users

### Files

`/etc/shadow` - a text file that contains information about the system's users password

`/etc/passwd` - is a text file that stores user account information

`/etc/group` - is a text file which defines the groups to which users belong under Linux and UNIX operating system

### Commands

`id [USER]` - print user and group information for each specified USER

`who` - print information about users who are currently logged in

`w` - show who is logged on and what they are doing

`last` - show a listing of last loggged in users

## Managing Users

### Create a user
```bash
sudo useradd -m john
```
This will create a new user **john** and create a new directory in `/home/john`.

### Set a password
```bash
sudo passwd john
```
This will set a password for **john** so that he can login.

## Managing Groups

### Create a group
```bash
sudo groupadd [group-name]
```

### Add user to a group
```bash
sudo usermod -a -G [group-name] john
```

# Resources
- [Getting Started with Linux System Administration](https://app.pluralsight.com/course-player?clipId=85f60b0b-7330-4647-9f46-809f0623ceea)