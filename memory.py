from abc import ABC, abstractmethod
import collections
import random

class ReplayBuffer(ABC):

    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = collections.deque(maxlen=max_size)
    
    def sample(self, batch_size):
        assert len(self.buffer) >= batch_size, \
            f'Cannot sample {batch_size} elements from buffer of size {self.cur_len}'
        indices = random.sample(range(len(self.buffer)), batch_size)
        return [self.buffer[i] for i in indices]

    def insert(self, element):
        self.buffer.append(element)
