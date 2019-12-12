import torch
from .base import IndependentTransformation


# TODO would be nice to auto-generate this
class Sigmoid(IndependentTransformation):
    """ Sigmoid activation
    """
    def __init__(self, apply_to):
        super().__init__(apply_to=apply_to)

    def apply_to_one(self, tensor):
        return torch.sigmoid(tensor)
