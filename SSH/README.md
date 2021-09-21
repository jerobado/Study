# SSH (Secure Shell Protocol)
- the Secure Shell Protocol is a cryptographic network protocol for operating network services securely over an unsecured network.
- typical applications include remote command-line, login, and remote command execution, but any network service can be secured with SSH.

# Usage

1. Use the `ssh-keygen` command to generate public-private keys in your client machine
    ```
    $ ssh-keygen -f ~/my-super-secret-key -t ecdsa -b 521
    ```
2. Copy the Public key to the server using the `ssh-copy-id` command
    ```
    $ ssh-copy-id -i ~/my-super-secret-key user@domain.com
    ```
3. Login to your remote server
    ```
    $ ssh user@domain.com
    ```

# Commands
`ssh-keygen`
-
- to create a SSH key pair

`ssh-copy-id`
-
- to copy/install the authorized key on the server

`ssh-agent`
- 
- is a program that can hold a user's private key, so that the private key passphrase only needs to be supplied once

# Definition of Terms/Concepts

**Private keys**
- also known as _identity keys_ that must be properly secured
- must **NOT** be kept on the public server

**Public keys**
- also known as _authorized keys_ stored in your server

**authorized_keys**
- default location is `.ssh/authorized_keys` in the user's home directory
- list of keys that your SSH server will allow to login

