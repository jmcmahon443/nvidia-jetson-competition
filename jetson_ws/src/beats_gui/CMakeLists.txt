cmake_minimum_required(VERSION 2.8.3)
project(beat_gui)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
find_package(catkin REQUIRED rospy beat_msgs)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py.
# catkin_python_setup()

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES beat_msgs
  CATKIN_DEPENDS rospy beat_msgs
#  DEPENDS system_lib
)
