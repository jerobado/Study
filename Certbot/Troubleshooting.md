# Troubleshooting

### Invalid response from acme-challenge
Make sure that you put the port number in your `<VirtualHost>` configuration.
```bash
<VirtualHost *:80>  # <-- explicitly add port 80
    ServerName www.jerobado.com
    ...
</VirtualHost>
```