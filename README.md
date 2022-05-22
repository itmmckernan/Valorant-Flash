# Valorant-Flash
My Eyes have never hurt more

Detects Flashes by reduction in contract over text on the screen

Send serial message to arduino or similar to control flashlamp

TODO:
Detection system could use some work, code could be commented, things like that

# Usage
1. Capture stream with OBS, create a virtualcam, feed that into Opencv - note may need to use the plugin rather than the builtin due to compatability
2. Current capture areas are calibrated off of a 1080p 16:9 OBS feed
3. To set up a physical flasher, it just needs to react to a serial port message
4. There is an example under example_flasher.ino
