SET(APP_HEADERS
        # "${CMAKE_CURRENT_SOURCE_DIR}/test.h"
        )

SET(APP_SOURCES
        "${CMAKE_CURRENT_SOURCE_DIR}/main.cpp"
        )
set(PROJECT spline_opt)

add_executable(${PROJECT} ${APP_SOURCES} ${APP_HEADERS} )
set_property(TARGET ${PROJECT} PROPERTY CXX_STANDARD 11)
set_target_properties(${PROJECT} PROPERTIES LINKER_LANGUAGE CXX)

target_link_libraries(${PROJECT} PRIVATE
        CONAN_PKG::ceres-solver
        )

target_include_directories(${PROJECT} PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
        PRIVATE
        $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/src>
        )

install(TARGETS ${PROJECT} 
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
