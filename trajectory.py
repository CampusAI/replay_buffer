class Trajectory:
    """Container class for a trajectory.

    A trajectory is a sequence (s_0, a_0, p_a_0, r_0, s_1, ...). A trajectory ends with a next
    state s_n if the episode is not over. The episode_ended() method can be used to check whether
    the last state in states corresponds to a terminal state or not.
    """

    def __init__(self):
        self.states = []  # Note that states[1:] corresponds to the next states
        self.actions = []
        self.p_actions = []  # Policy for the state-action pair at the time the action was taken.
        self.rewards = []

    def episode_ended(self):
        """Return True if the this trajectory ended because of an episode termination,
        false otherwise.

        If True, then states has the same length as the other attributes, as there is no next state.
        If False, states has an additional state corresponding to the state at which the
        trajectory was cut.
        """
        return len(self.states) == len(self.actions)

    def get_length(self):
        """Returns the length of the trajectory, without counting the possible additional final
        state.
        """
        return len(self.actions)

    def truncate(self, start, end):
        """Return a copy of this trajectory, truncated from the given start and end indices.

        The states list will contain the additional next state unless the trajectory ends at
        index end due to episode termination.

        Args:
            start (int): Index from which to keep transitions.
            end (int): Last index (inclusive) of the kept transitions.
        """
        new_t = Trajectory()
        last_state_idx = end if end == self.get_length() - 1 and self.episode_ended() else end + 1
        new_t.states = self.states[:last_state_idx]
        new_t.actions = self.actions[start: end + 1]
        new_t.p_actions = self.p_actions[start: end + 1]
        new_t.rewards = self.rewards[start: end + 1]
        return new_t