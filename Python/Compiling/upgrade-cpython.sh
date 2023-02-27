# Usage
# $ ./upgrade-cpython.sh <URL to python version>

# For example:
# $ ./upgrade-cpython.sh https://www.python.org/ftp/python/3.8.16/Python-3.8.16.tar.xz

cd ~/Downloads
wget $1
tar -xf *.tar.xz
rm *.tar.xz
cd Python-*
./configure --enable-optimizations --with-lto
make -j4
sudo make install
