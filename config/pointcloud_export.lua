-- Cartographer assets writer pipeline for exporting high-detail point clouds.
-- Replace filenames and ranges according to your dataset.

VOXEL_SIZE = 0.001

include "transform.lua"

options = {
  tracking_frame = "camera_pose_frame",
  pipeline = {
    {
      action = "min_max_range_filter",
      min_range = 0.1,
      max_range = 40.0,
    },
    {
      action = "write_ply",
      filename = "high_fidelity_points.ply",
    },
  }
}

return options
