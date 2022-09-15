How to setup Apache HTTP Server with Let's Encrypt on Ubuntu
---

1. Install Certbot
    ```bash
    sudo apt install certbot python3-certbot-apache
    ```

2. [Setup](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04#step-5-%E2%80%94-setting-up-virtual-hosts-(recommended)) your Apache Virtual Host configuration file. Make sure that the `ServerName` and `ServerAlias` are properly configured.
    ```bash
    # sudo nano /etc/apache2/sites-available/your_domain.conf
    ...
    ServerName your_domain
    ServerAlias www.your_domain
    ...
    ```

3. Obtain an SSL Certificate
    ```bash
    sudo certbot --apache
    ```
    This command will prompt your to answer a series of questions in order to configure your SSL certificate.
    

Resources
--- 
- [How To Secure Apache with Let's Encrypt on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04)
