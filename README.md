# Project4
Carla and Ros integration with hardware system


# Useful commands
## Building
Get into catkin workspace
```
cd
cd catkin_ws/
```
Build
```
catkin_make
```
After building the workspace you have to source the setup file
```
source /home/pi/catkin_ws/devel/setup.bash
```

## Ros commands
```
rostopic pub/echo/list - ros topic commands
rocd <package-name> - change directory to package
roscore -launch core of the system
rosrun <package-name> <script-name> - launch specific node
rosnode list
```
