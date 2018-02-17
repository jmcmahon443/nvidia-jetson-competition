cmake_minimum_required(VERSION 2.8.3)
project(beat_makers)

## Find catkin macros and libraries

find_package(catkin REQUIRED rospy beat_msgs)


## Generate added messages and services with any dependencies listed here
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES beat_msgs
  CATKIN_DEPENDS rospy  beat_msgs
#  DEPENDS system_lib
)
###########
## Build ##
###########

## Specify additional locations of header files
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
