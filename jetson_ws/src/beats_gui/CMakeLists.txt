cmake_minimum_required(VERSION 2.8.3)
project(beats_gui)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

SET(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${PROJECT_SOURCE_DIR}/CMakeModules/")
set(CMAKE_CXX_FLAGS "-std=c++11 ${CMAKE_CXX_FLAGS}")

find_package(catkin REQUIRED COMPONENTS
  roscpp
  beat_msgs
)

FIND_PACKAGE(OpenGL REQUIRED)
FIND_PACKAGE(GLUT REQUIRED)
FIND_PACKAGE(Freetype REQUIRED)
FIND_PACKAGE(GLEW REQUIRED)
FIND_PACKAGE(PkgConfig REQUIRED)
pkg_check_modules(GLFW REQUIRED glfw3)

## Uncomment this if the package has a setup.py.
# catkin_python_setup()

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OPENGL_INCLUDE_DIR}
  ${GLUT_INCLUDE_DIR}
  ${GLEW_INCLUDE_DIRS}
  ${FREETYPE_INCLUDE_DIRS}
  ${GLFW_INCLUDE_DIRS}
#  ${EIGEN3_INCLUDE_DIR}
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
  INCLUDE_DIRS include
#  LIBRARIES beat_msgs
  CATKIN_DEPENDS roscpp beat_msgs
#  DEPENDS system_lib
)

#SET(FTGL_LIBRARY /usr/lib/x86_64-linux-gnu/libftgl.so)

 add_executable(glviewer 
                  src/gui.cpp
#                  src/include/transformation2.cpp
)
 
 target_link_libraries(glviewer 
  ${catkin_LIBRARIES}
  ${OPENGL_LIBRARIES}
  ${GLUT_glut_LIBRARY}
  ${FREETYPE_LIBRARIES}
  ${GLEW_LIBRARIES}
  ${GLFW_LIBRARIES}
#  ${FTGL_LIBRARY}
)