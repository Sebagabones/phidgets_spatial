# # Copyright 2019 Open Source Robotics Foundation, Inc.
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
#
# """Launch a Phidgets spatial in a component container."""
#
# import launch
# from launch.actions import DeclareLaunchArgument
# from launch_ros.actions import ComposableNodeContainer
# from launch_ros.descriptions import ComposableNode
#
#
# def generate_launch_description():
#     """Generate launch description with multiple components."""
#     enableHeating = DeclareLaunchArgument("heating_enabled", default_value="False")
#     topicPrefix = DeclareLaunchArgument("topic_prefix", default_value="imu")
#     useOrientation = DeclareLaunchArgument("use_orientation", default_value="False")
#     spatialAlgorithm = DeclareLaunchArgument("spatial_algorithm", default_value="ahrs")
#
#     params = {
#         # optional ahrs parameters
#         "ahrs_angular_velocity_threshold": 1.0,
#         "ahrs_angular_velocity_delta_threshold": 0.1,
#         "ahrs_acceleration_threshold": 0.1,
#         "ahrs_mag_time": 10.0,
#         "ahrs_accel_time": 10.0,
#         "ahrs_bias_time": 1.25,
#     }
#
#     for option in [enableHeating, topicPrefix, useOrientation, spatialAlgorithm]:
#         params.add(option)
#
#     print(f"params are: {params}")
#     container = ComposableNodeContainer(
#         name="phidget_container",
#         namespace="",
#         package="rclcpp_components",
#         executable="component_container",
#         composable_node_descriptions=[
#             ComposableNode(
#                 package="phidgets_spatial",
#                 plugin="phidgets::SpatialRosI",
#                 name="phidgets_spatial",
#                 parameters=[params],
#             ),
#         ],
#         output="both",
#     )
#
#     return launch.LaunchDescription([container])
