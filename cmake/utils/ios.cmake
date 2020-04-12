macro(setup_framework_properties TARGET)
    set_target_properties(${TARGET} PROPERTIES FRAMEWORK TRUE
            FRAMEWORK_VERSION "1.0"
            MACOSX_FRAMEWORK_IDENTIFIER "vn.nganht.helloworld"
            MACOSX_FRAMEWORK_INFO_PLIST ${BUILD_DIR}/framework.plist.in
            VERSION "1.0"
            SOVERSION "1.0"
            PUBLIC_HEADER "${PUBLIC_HEADER}"
            XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1,2"
            XCODE_ATTRIBUTE_SKIP_INSTALL "YES")
endmacro()

macro(add_exampleapp TARGET)
    set(DEVELOPMENT_PROJECT_NAME "project")
    set(APP_NAME "exampleapp")

    set(PRODUCT_NAME ${APP_NAME})
    set(EXECUTABLE_NAME ${APP_NAME})
    set(APP_BUNDLE_IDENTIFIER "vn.nganht.helloworld.exampleapp")
    set(MACOSX_BUNDLE_EXECUTABLE_NAME ${APP_NAME})
    set(MACOSX_BUNDLE_INFO_STRING ${APP_BUNDLE_IDENTIFIER})
    set(MACOSX_BUNDLE_GUI_IDENTIFIER ${APP_BUNDLE_IDENTIFIER})
    set(MACOSX_BUNDLE_BUNDLE_NAME ${APP_BUNDLE_IDENTIFIER})
    set(MACOSX_BUNDLE_ICON_FILE "")
    set(MACOSX_BUNDLE_LONG_VERSION_STRING "1.0")
    set(MACOSX_BUNDLE_SHORT_VERSION_STRING "1.0")
    set(MACOSX_BUNDLE_BUNDLE_VERSION "1.0")
    set(MACOSX_BUNDLE_COPYRIGHT "nganht")

    set(CMAKE_EXE_LINKER_FLAGS
            "-framework AudioToolbox -framework CoreGraphics -framework QuartzCore -framework UIKit")

    set(EXAMPLE_APP_DIR ${BUILD_DIR}/exampleapp)
    set(APP_HEADER_FILES
            ${EXAMPLE_APP_DIR}/AppDelegate.h
            ${EXAMPLE_APP_DIR}/ViewController.h
            )

    set(APP_SOURCE_FILES
            ${EXAMPLE_APP_DIR}/AppDelegate.m
            ${EXAMPLE_APP_DIR}/ViewController.mm
            ${EXAMPLE_APP_DIR}/main.m
            )

    set(RESOURCES
            ${EXAMPLE_APP_DIR}/Main.storyboard
            ${EXAMPLE_APP_DIR}/LaunchScreen.storyboard
            )

    add_executable(
            ${APP_NAME}
            MACOSX_BUNDLE
            ${APP_HEADER_FILES}
            ${APP_SOURCE_FILES}
            ${RESOURCES}
    )

    # Locate system libraries on iOS
    find_library(UIKIT UIKit)
    find_library(FOUNDATION Foundation)
    find_library(MOBILECORESERVICES MobileCoreServices)
    find_library(CFNETWORK CFNetwork)
    find_library(SYSTEMCONFIGURATION SystemConfiguration)

    # link the frameworks located above
    target_link_libraries(${APP_NAME} ${UIKIT} ${FOUNDATION} ${MOBILECORESERVICES} ${CFNETWORK} ${SYSTEMCONFIGURATION})


    add_dependencies(${APP_NAME} ${TARGET})

    set_target_properties(${APP_NAME} PROPERTIES
            XCODE_ATTRIBUTE_OTHER_LDFLAGS "${XCODE_ATTRIBUTE_OTHER_LDFLAGS} -framework ${TARGET}"
            MACOSX_BUNDLE_INFO_PLIST ${EXAMPLE_APP_DIR}/plist.in
            XCODE_ATTRIBUTE_TARGETED_DEVICE_FAMILY "1,2"
            XCODE_ATTRIBUTE_LD_RUNPATH_SEARCH_PATHS "@executable_path/Frameworks"
            RESOURCE "${RESOURCES}"
            )

    # Copy the framework into the app bundle
    add_custom_command(
            TARGET
            ${APP_NAME}
            POST_BUILD COMMAND /bin/sh -c
            \"COMMAND_DONE=0 \;
            if ${CMAKE_COMMAND} -E copy_directory
                \${BUILT_PRODUCTS_DIR}/${TARGET}.framework
                \${BUILT_PRODUCTS_DIR}/${APP_NAME}.app/Frameworks/${TARGET}.framework
                \&\>/dev/null \; then
                COMMAND_DONE=1 \;
            fi \;
            if [ \\$$COMMAND_DONE -eq 0 ] \; then
                echo Failed to copy the framework into the app bundle \;
                exit 1 \;
            fi\"
    )

endmacro()
