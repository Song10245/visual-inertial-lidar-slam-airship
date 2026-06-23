#!/usr/bin/env python3
"""Check that expected ROS topics are available before running mapping.

This script is intentionally lightweight and portfolio-safe. Run it inside a ROS 1 environment.
"""

import subprocess
import sys

EXPECTED_TOPICS = [
    "/scan",
    "/laserPointCloud",
    "/camera/odom/sample",
    "/camera/imu",
    "/tf",
    "/tf_static",
]


def get_topics():
    try:
        result = subprocess.run(["rostopic", "list"], check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print("rostopic not found. Source your ROS environment first.")
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print("Failed to call rostopic list:", exc.stderr)
        sys.exit(1)
    return set(result.stdout.splitlines())


def main():
    topics = get_topics()
    missing = [topic for topic in EXPECTED_TOPICS if topic not in topics]
    if missing:
        print("Missing expected topics:")
        for topic in missing:
            print(f"  - {topic}")
        sys.exit(2)
    print("All expected topics are available.")


if __name__ == "__main__":
    main()
