def unpack_transition_list(transitions_list):
    states = [t.s for t in transitions_list]
    actions = [t.a for t in transitions_list]
    rewards = [t.r for t in transitions_list]
    next_states = [t.next_s for t in transitions_list if t.next_s is not None]
    mask = [not t.done for t in transitions_list]
    td_errors = [t.td_error for t in transitions_list]
    action_probs = [t.action_prob for t in transitions_list]
    return states, actions, rewards, next_states, mask, td_errors, action_probs
