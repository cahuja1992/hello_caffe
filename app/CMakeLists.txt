set(name hello_caffe)

add_executable(${name} "${PROJECT_SOURCE_DIR}/app/cpp/main.cpp")
target_link_libraries(${name} ${Caffe_LINK})

set_target_properties(${name} PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/app/")
install(TARGETS ${name} DESTINATION ${CMAKE_INSTALL_BINDIR})