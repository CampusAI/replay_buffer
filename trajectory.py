from transition import Transition

from utilities import unpack as unpack_transition_list
class Trajectory(list):
    """Container class for a trajectory.

    A trajectory is a sequence (s_0, a_0, p_a_0, r_0, s_1, ...). A trajectory ends with a next
    state s_n if the episode is not over.
    """
    def done(self):
        """Return True if the this trajectory ended because of an episode termination,
        false otherwise.
        """
        return self[-1].done

    def truncate(self, start, end):
        """Return a copy of this trajectory, truncated from the given start and end indices.

        Args:
            start (int): Index from which to keep transitions.
            end (int): Last index (exclusive) of the kept transitions.
        """
        return self[start:end]

    def unpack(self):
        return unpack_transition_list(self)