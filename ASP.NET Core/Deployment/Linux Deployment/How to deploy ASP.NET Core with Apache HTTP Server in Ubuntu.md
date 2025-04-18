# How to deploy ASP.NET Core with Apache HTTP Server in Ubuntu
- This is a high level overview about deploying ASP.NET Core project in Ubuntu with Apache HTTP Server as a reverse proxy.

**Assumptions**

- You have already an existing working website in your production server.
- Apache HTTP Server is already installed in your production server.
- Apache HTTP Server headers and mods are already enabled.
- .NET Runtime or SDK is already installed in your production server, see installation tutorial [here]((https://learn.microsoft.com/en-us/dotnet/core/install/linux-ubuntu)).


### Project setup

1. Configure a proxy server in `Program.cs` file

2. Create/update your `appsettings.json` file for production

3. Run [migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying?tabs=vs) to have a snapshot of your development database in an `.sql` file

4. Publish your project in **Release** mode

### Database setup (production)

1. Create a user/owner for the database

2. Create a database

3. Run the migration script to restore your database

### Server setup (production)

1. Download a copy of your publish project to the server, use `sftp` or `scp` tool

2. Transfer your donwloaded project to `/var/www/project/`

3. Create and configure **Apache HTTP Server** virtual host file in `/etc/apache2/sites-available/{project}.conf`

4. Create and configure **systemd** service file in `/etc/systemd/system/{project}.service`

5. [Configure](https://github.com/jerobado/Study/blob/main/Let's%20Encrypt/How%20to%20setup%20Apache%20with%20Let's%20Encrypt%20on%20Ubuntu.md) an SSL Certificate with Let's Encrypt using `certbot` tool

### Hosting setup

1. Create and configure a domain or sub-domain in your hosting provider

## Troubleshooting

#### Certain headers or modules must be enabled
```
sudo a2enmod headers
sudo a2enmod proxy
sudo a2enmod proxy_http
```

## Resources
- [Host ASP.NET Core on Linux with Apache](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-apache?view=aspnetcore-6.0)
- [Applying Migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying?tabs=vs)