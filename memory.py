from abc import ABC, abstractmethod
import collections
import random

class ReplayBuffer(collections.deque):

    def __init__(self, max_size):
        super().__init__([], maxlen=int(max_size))
    
    def sample(self, batch_size):
        assert len(self) >= batch_size, \
            f'Cannot sample {batch_size} elements from buffer of size {len(self)}'
        indices = random.sample(range(len(self)), batch_size)
        return [self[i] for i in indices]
