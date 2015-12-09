# Pulse Reader

This is a simple setup to read an I2C sensor from GrovePi+ using any version of Raspberry Pi running Raspbian. This was last updated to work with version 1.2.2 of the GrovePi firmware. If your sensor "disappears" with the GrovePi (can't find it using i2cdetect -y 1 or i2cdetect -y 0), unplug it and plug it back in. From my experience, the pi will reset once or twice when you plug in the sensor as it handles the sudden power draw. 

If you need to test any other I2C sensors, just change the address to match the address you find using i2cdetect. 

This has been tested to work with the finger strap pulse reader offered by Dexter Ind. There is a standing, intermittent issue with the GrovePi and sensor suddenly disappearing.
