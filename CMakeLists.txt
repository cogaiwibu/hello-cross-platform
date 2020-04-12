cmake_minimum_required(VERSION 3.6)
set(PROJECT_NAME helloworld)
project(${PROJECT_NAME})

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_ANDROID_STL_TYPE "c++_static")

add_subdirectory(cmake)

set_diagnostic_flags()
hide_symbol()

set(PUBLIC_HEADER src/time_repository.h)
set(SOURCES src/time_repository.cpp)

if ("${PLATFORM}" STREQUAL "IOS")
    set(SOURCES ${SOURCES} ${PUBLIC_HEADER})

elseif ("${PLATFORM}" STREQUAL "ANDROID")
    set(SOURCES ${SOURCES} src/android_wrapper.cpp)

else ()
    set(SOURCES ${SOURCES} src/main.cpp)

endif ()

add_main_executable(${PROJECT_NAME} PLATFORM ${PLATFORM} PUBLIC_HEADER ${PUBLIC_HEADER} SOURCES ${SOURCES})

target_link_libraries(${PROJECT_NAME})
