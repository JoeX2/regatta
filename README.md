# regatta
Regatta is an app dedicated to the yearly regatta arranged by Odense Roklub. 

It is implemented in Kivy and should be runable on most Android hardware as well as PCs. 

## Setup
Setup the installation environment:
```
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt update
sudo apt install python-kivy git
cd workspace
git clone git@github.com:JoeX2/regatta.git
```

## Run
When the above setup is done, you can run it with
```
cd regatta
python main.py
```

## Build for Android
This should create a apk file that can be installed on an Andoid phone or tablet
```
sudo apt install python-setuptools zlib1g-dev cython openjdk-8-jdk python-pip aidl:i386 zlib1g:i386
pip install python-for-android
cd ..
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
cd ..
cd regatta
buildozer --verbose android debug deploy run
```
