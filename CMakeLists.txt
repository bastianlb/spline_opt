cmake_minimum_required(VERSION 3.13)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake/")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(spline_opt LANGUAGES C CXX)

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  conan_basic_setup(TARGETS)
else()
  message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()

include(GNUInstallDirs)

add_subdirectory(src)
