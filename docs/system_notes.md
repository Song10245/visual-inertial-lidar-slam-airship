# System notes

## Hardware

- Platform: non-rigid lighter-than-air indoor inspection platform
- Compute: Raspberry Pi 4
- LiDAR: RPLiDAR S1 mounted vertically
- Visual-inertial tracking: Intel RealSense T265
- Optional multi-modal sensor: CZT gamma detector

## ROS data flow

- `/scan`: 2D LiDAR scans from RPLiDAR S1
- `/laserPointCloud`: projected PointCloud2 representation of vertical scans
- `/camera/odom/sample`: six-degree-of-freedom visual-inertial odometry
- `/camera/imu`: IMU stream from T265
- `/tf` and `/tf_static`: dynamic and static sensor transforms

## Engineering constraints

- Tight payload budget
- Embedded compute limitations
- Sensor timing and calibration sensitivity
- Indoor GPS-denied environment
- Real capture conditions rather than clean benchmark data
