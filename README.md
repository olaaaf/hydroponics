# hydroponics - a better way to grow food

A **raspberry pi** (Zero W) based project for growing plants with a hydroponic system.

The heart of it is the water pump, which is turned on or off with a SSR, as the pump works with *12V @ 3.6W*.   The main goal of the project is to be able to monitor and change parameters of the aquaponic system such as water flow and the schedule of the pump turning on. Changes are to be made on a locally hosted website that runs on pi.

The physical model - a literal PVC pipe connected by two 32 to 6 mm adapters (that were modeled and 3D printed) to connect them to the pump with industrial plastic tubing. Then small (37 mm in diameter) holes are drilled on one axis, which are to be used for "baskets" that will hold the plants with bentonite balls.

Please take a look at the wiki, as it contains most of the documentation

##### Dependencies
**pigpio
**
To install use:
```
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```
