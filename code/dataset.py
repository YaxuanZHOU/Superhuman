from __future__ import print_function
import numpy as np
import torch
from torch.utils.data import Dataset


def worker_init_fn(worker_id):
    # Each work already has its own random state (Torch).
    seed = torch.IntTensor(1).random_()[0]
    print("id = {}, seed = {}".format(worker_id, seed))
    np.random.seed(seed)


class SNEMI3D_Dataset(Dataset):
    """
    SNEMI3D dataset.
    """
    def __init__(self, sampler, size):
        super(SNEMI3D_Dataset, self).__init__()
        self.sampler = sampler
        self.size = size

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.sampler(imgs=['input'])
