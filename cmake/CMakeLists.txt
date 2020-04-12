set(CMAKE_UTILITIES
        utils/common.cmake
        utils/ios.cmake)

foreach (UTILITY ${CMAKE_UTILITIES})
    include(${UTILITY})
endforeach ()

add_custom_target(hello_cmake SOURCES ${CMAKE_UTILITIES})
