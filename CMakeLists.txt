cmake_minimum_required(VERSION 3.10)
project(phidgets_spatial)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

find_package(ament_cmake_ros REQUIRED)
find_package(phidgets_api REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)

# include_directories(include)
#
# add_library(phidgets_spatial SHARED src/spatial_ros_i.cpp)
#
# target_compile_features(phidgets_spatial PUBLIC cxx_std_17)
#
# target_link_libraries(phidgets_spatial PUBLIC
#   ${sensor_msgs_TARGETS}
#   ${std_msgs_TARGETS}
#   ${std_srvs_TARGETS}
#   phidgets_api::phidgets_api
#   rclcpp::rclcpp
#   rclcpp_components::component
#   sensor_msgs::sensor_msgs_library
# )

# install(TARGETS phidgets_spatial
#   ARCHIVE DESTINATION lib
#   LIBRARY DESTINATION lib
#   RUNTIME DESTINATION bin
# )

# install(DIRECTORY include/
#   DESTINATION include
# )

# install(DIRECTORY launch
#   DESTINATION share/${PROJECT_NAME}
# )


add_executable(run_phidgets src/spatial_ros_i.cpp)
target_link_libraries(run_phidgets PUBLIC
  ${sensor_msgs_TARGETS}
  ${std_msgs_TARGETS}
  ${std_srvs_TARGETS}
  phidgets_api::phidgets_api
  rclcpp::rclcpp
  rclcpp_components::component
  sensor_msgs::sensor_msgs_library)

install(TARGETS
  run_phidgets
  DESTINATION lib/${PROJECT_NAME})

ament_package()
