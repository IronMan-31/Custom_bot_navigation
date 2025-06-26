
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_gazebo_ros=get_package_share_directory("gazebo_ros")
    urdf_path=os.path.join(get_package_share_directory("custom_bot"),'urdf','my_bot.urdf')
    world=os.path.join(get_package_share_directory("custom_bot"),"Custom_world","model.world")
    return LaunchDescription([
        IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
        os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
    ),
    launch_arguments={'world': world}.items()
),
     IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("custom_bot"), 'launch', 'display.launch.py')
        ),
    ),
        #  Node(
        #     package='robot_state_publisher',
        #     executable='robot_state_publisher',
        #     parameters=[{'robot_description': open(urdf_path).read()}],
        #     output='screen',
        # ),
        
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'simple_bot',
                '-file', urdf_path,
                '-x', '3.0', '-y', '0.5', '-z', '0.01'
            ],
            output='screen'
        )
    ])
