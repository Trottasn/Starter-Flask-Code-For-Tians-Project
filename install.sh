tar -xzvf Python-3.7.7.tgz
cd Python-3.7.7/
./configure
make
sudo make install
cd ..
sudo pip3 install --upgrade pip
sudo pip3 install -r requirements.txt
python3 ./server.py
