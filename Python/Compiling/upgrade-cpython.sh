cd ~/Downloads
wget $1
tar -xf *.tar.gz
cd cpython-*
./configure --enable-optimizations --with-lto
make -j4
sudo make install
