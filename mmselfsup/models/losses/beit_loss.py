# Copyright (c) OpenMMLab. All rights reserved.
from typing import Tuple

import torch
from mmengine.model import BaseModule
from torch import nn

from mmselfsup.registry import MODELS


@MODELS.register_module()
class BEiTLoss(BaseModule):
    """Loss function for BEiT.

    Compute the main loss.
    """

    def __init__(self) -> None:
        super().__init__()
        self.loss_cross_entropy = nn.CrossEntropyLoss()

    def forward(self, logits: torch.Tensor,
                target: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Forward function of BEiT Loss.

        Args:
            logits (torch.Tensor): The outputs from the decoder.
            target (torch.Tensor): The targets generated by dalle.

        Returns:
            Tuple[torch.Tensor, torch.Tensor]: The main loss.
        """
        loss_main = self.loss_cross_entropy(logits, target)

        return loss_main