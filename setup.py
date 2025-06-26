from setuptools import find_packages, setup

package_name = 'custom_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name+'/launch', ['launch/display.launch.py','launch/gazebolaunch.py','launch/mappinglaunch.py','launch/navig.py']),
         ('share/' + package_name+'/urdf', ['urdf/my_bot.urdf','urdf/tb3.sdf']),
         ('share/' + package_name+'/Custom_world', ['Custom_world/model.world','Custom_world/model.config']),
         ('share/' + package_name+'/config', ['config/param.yaml','config/botnav.yaml']),
          ('share/' + package_name+'/maps', ['maps/my_map.yaml','maps/my_map.pgm','maps/my_map1.yaml','maps/my_map1.pgm']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pranabpandey31',
    maintainer_email='pranabpandey31@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
