macro(hide_symbol)
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -fvisibility=hidden -fvisibility-inlines-hidden")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} -fvisibility=hidden -fvisibility-inlines-hidden")

    if ("${PLATFORM}" STREQUAL "ANDROID")
        set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--version-script=${CMAKE_CURRENT_LIST_DIR}/version-script.txt")
    endif ()
endmacro()

macro(set_diagnostic_flags)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} \
    -Werror \
    -Wall \
    -Wextra \
    -W \
    -Wwrite-strings \
    -Wno-unused-parameter \
    -Wno-long-long \
    -Werror=return-type \
    -Wno-c++98-compat \
    -Wno-c++98-compat-pedantic \
    -Wno-c++11-compat \
    -Wno-undef \
    -Wno-reserved-id-macro \
    -Wno-gnu-include-next \
    -Wno-gcc-compat \
    -Wno-zero-as-null-pointer-constant \
    -Wno-deprecated-dynamic-exception-spec \
    -Wno-sign-conversion \
    -Wno-old-style-cast \
    -Wno-deprecated")
endmacro()

macro(add_main_executable TARGET)
    set(oneValueArgs PLATFORM PUBLIC_HEADER)
    set(multiValueArgs SOURCES)
    cmake_parse_arguments(APP "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})

    if ("${APP_PLATFORM}" STREQUAL "IOS")
        add_library(${TARGET} SHARED ${SOURCES})
        setup_framework_properties(${TARGET})
        add_exampleapp(${TARGET})

    elseif ("${APP_PLATFORM}" STREQUAL "ANDROID")
        add_library(${TARGET} SHARED ${SOURCES})

    else ()
        add_executable(${TARGET} ${SOURCES})
    endif ()
endmacro()
