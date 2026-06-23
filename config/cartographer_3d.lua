-- Cartographer ROS configuration template for visual-inertial LiDAR SLAM.
-- This is a public-safe template based on the research pipeline.

include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,

  -- Frame setup. Adjust to match your TF tree.
  tracking_frame = "camera_imu_optical_frame",
  published_frame = "camera_pose_frame",
  odom_frame = "camera_odom_frame",
  provide_odom_frame = false,

  -- Sensor inputs.
  use_odometry = true,
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 0,
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 1,

  lookup_transform_timeout_sec = 0.2,
  submap_publish_period_sec = 0.3,
  pose_publish_period_sec = 5e-3,
  trajectory_publish_period_sec = 30e-3,
  rangefinder_sampling_ratio = 1.0,
  odometry_sampling_ratio = 1.0,
  fixed_frame_pose_sampling_ratio = 1.0,
  imu_sampling_ratio = 1.0,
  landmarks_sampling_ratio = 1.0,
}

MAP_BUILDER.use_trajectory_builder_3d = true
TRAJECTORY_BUILDER_3D.max_range = 40.0
TRAJECTORY_BUILDER_3D.voxel_filter_size = 0.01
TRAJECTORY_BUILDER_3D.use_online_correlative_scan_matching = true
POSE_GRAPH.optimize_every_n_nodes = 50
POSE_GRAPH.constraint_builder.min_score = 0.65

return options
