from launch import LaunchDescription
from ament_index_python import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import TimerAction


def generate_launch_description():
    use_sim_time=LaunchConfiguration('use_sim_time')
    slam_params_file=LaunchConfiguration("slam_params_file")

    dec_sim_time=DeclareLaunchArgument("use_sim_time",default_value="true")
    dec_params_file=DeclareLaunchArgument("slam_params_file",default_value=os.path.join(get_package_share_directory("custom_bot"),'config', "param.yaml"))

    nod=TimerAction(
        period=3.0,
        actions=[Node(
        package="slam_toolbox",
        executable="async_slam_toolbox_node",
        name="slam_toolbox",
        output="screen",
        parameters=[slam_params_file,{"use_sim_time":use_sim_time}]
    )])

    ld=LaunchDescription()

    ld.add_action(dec_sim_time)
    ld.add_action(dec_params_file)
    ld.add_action(nod)

    return ld
