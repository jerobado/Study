# Apache HTTP Server


## Usage

The following command requires sudo.

### List enabled sites
```
sudo apache2ctl -S
```


### Enable a site
```
sudo a2ensite <site-name>.conf
sudo systemctl reload apache2
```

### Disable a site
```
sudo a2dissite <site-name>.conf
sudo systemctl reload apache2
```