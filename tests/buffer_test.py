import os
import sys

import pytest

from trajectory import Trajectory

def test_trajectory():
    traj = Trajectory()
    assert traj.get_length() == 0