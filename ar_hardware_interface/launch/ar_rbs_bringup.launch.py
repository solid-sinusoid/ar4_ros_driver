from launch import LaunchDescription
from launch.actions import (
    IncludeLaunchDescription,
    OpaqueFunction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    PathJoinSubstitution,
)
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):
    main_script = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                PathJoinSubstitution(
                    [FindPackageShare("rbs_runtime"), "launch", "runtime.launch.py"]
                )
            ]
        ),
        launch_arguments={
            "with_gripper": "true",
            "robot_type": "ar4",
            "description_package": "ar_moveit_config",
            "description_file": "fake_ar.urdf.xacro",
            "robot_name": "ar4",
            "use_moveit": "false",
            "moveit_config_package": "ar_moveit_config",
            "moveit_config_file": "ar.srdf.xacro",
            "use_sim_time": "true",
            "use_controllers": "true",
            "scene_config_file": "",
            "base_link_name": "base_link",
            "ee_link_name": "ee_link",
            "control_space": "task",
            "control_strategy": "position",
            "interactive": "true",
            "use_rbs_utils": "true",
            "real_robot": "true",
            "assembly_config_name": "board_pick_and_place",
        }.items(),
    )

    nodes_to_start = [
        main_script,
    ]
    return nodes_to_start


def generate_launch_description():
    declared_arguments = []

    return LaunchDescription(
        declared_arguments + [OpaqueFunction(function=launch_setup)]
    )
