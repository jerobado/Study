# How to install `mod_wsgi` in Python and Apache

1. Configure and build Python with `--enable-shared` option
    ```bash
    ./configure --enable-shared
    make
    sudo make install
    ```

2. Install `mod_wsgi` using pip
    ```bash
    pip install mod-wsgi
    ```

    This will install `mod_wsgi` in your current Python installation. You can also install it in a virtual environment.

3. Run `mod_wsgi-express module-config` and copy its output.
    ```bash
    LoadModule wsgi_module "/home/jerobado/.local/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so"
    WSGIPythonHome "/usr/local"
    ```

    This output will be different if you install `mod_wsgi` in a virtual environement.

4. Go to `/etc/apache2/mods-available` directory
    ```bash
    cd /etc/apache2/mods-available
    ```

5. Create `wsgi.load` file and paste the output from **Step 3** into this file
    ```bash
    sudo vim wsgi.load
    ```

6. Enable this module and restart Apache
    ```bash
    sudo a2enmod wsgi
    sudo systemctl restart apache2
    ```

# Resources
- [Connecting into Apache installation](https://github.com/GrahamDumpleton/mod_wsgi#connecting-into-apache-installation)