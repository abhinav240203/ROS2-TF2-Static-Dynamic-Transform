from setuptools import find_packages, setup

package_name = 'robot_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abhinav',
    maintainer_email='abhinavflora403@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'simple_parameters = robot_py.simple_parameters:main',
            'simple_turtlesim_kinematics = robot_py.simple_turtlesim_kinematics:main',
            'simple_tf_kinematics = robot_py.simple_tf_kinematics:main',
            'simple_service_server = robot_py.simple_service_server:main',
            'simple_service_client = robot_py.simple_service_client:main'
        ],
    },
)
