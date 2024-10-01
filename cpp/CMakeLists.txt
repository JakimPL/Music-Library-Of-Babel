cmake_minimum_required(VERSION 3.5)

project(babel LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(babel main.cpp babel.cpp)
target_link_libraries(babel gmp gmpxx)

install(TARGETS babel
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
