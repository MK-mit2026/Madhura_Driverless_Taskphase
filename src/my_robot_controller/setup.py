from setuptools import find_packages, setup

package_name = 'my_robot_controller'

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
    maintainer='madhura',
    maintainer_email='madhura.mitmpl2026@learner.manipal.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "test_node = my_robot_controller.node1:main",
            "draw_circle = my_robot_controller.draw_circle:main",
            "pose_sub = my_robot_controller.pose_sub:main",
            "turtle_control = my_robot_controller.turtle_control:main",
            "task1_pub = my_robot_controller.q1_pub:main",
            "task1_sub = my_robot_controller.q1_sub:main",
            'q2_node1 = my_robot_controller.q2_node1:main',
            'q2_node2 = my_robot_controller.q2_node2:main',
            'q2_node3 = my_robot_controller.q2_node3:main'
        ],
    },
)
