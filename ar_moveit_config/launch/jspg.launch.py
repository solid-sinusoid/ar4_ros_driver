import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import (
    PathJoinSubstitution,
    LaunchConfiguration,
    Command,
    FindExecutable,
)


def generate_launch_description():
    # Определение аргументов командной строки
    ar_model_arg = DeclareLaunchArgument(
        "ar_model",
        default_value="mk1",
        choices=["mk1", "mk2", "mk3"],
        description="Model of AR4",
    )
    ar_model_config = LaunchConfiguration("ar_model")

    robot_description_content = Command([
        PathJoinSubstitution([FindExecutable(name="xacro")]),
        " ",
        PathJoinSubstitution([
            FindPackageShare("ar_moveit_config"), "urdf", "fake_ar.urdf.xacro"
        ]),
        " ",
        "ar_model:=",
        ar_model_config,
    ])
    robot_description = {"robot_description": robot_description_content}

    # Запуск joint_state_publisher_gui
    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        output="screen",
    )

    # Публикация состояния робота
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="both",
        parameters=[robot_description],
    )

    return LaunchDescription(
        [
            ar_model_arg,
            joint_state_publisher_gui_node,
            robot_state_publisher_node,
        ]
    )
