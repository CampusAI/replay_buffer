import torch

def to_tensor(elements):
    if len(elements) == 0:
        return None
    return torch.cat(elements)

def unpack_transition_list(transitions_list):
    states = to_tensor([t.s for t in transitions_list])
    actions = to_tensor([t.a for t in transitions_list])
    rewards = to_tensor([t.r for t in transitions_list])
    next_states = to_tensor([t.next_s for t in transitions_list if t.next_s is not None])
    mask = torch.tensor([not t.done for t in transitions_list])
    td_errors = to_tensor([t.td_error for t in transitions_list if t.td_error is not None])
    action_probs = to_tensor([t.action_prob for t in transitions_list if t.action_prob is not None])
    return states, actions, rewards, next_states, mask, td_errors, action_probs
