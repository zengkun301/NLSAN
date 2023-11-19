# flake8: noqa
import os.path as osp
import pdb

import nlsan.archs
import nlsan.data
import nlsan.models
from basicsr.test import test_pipeline

import os
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ['CUDA_VISIBLE_DEVICES'] = "0"
# os.environ['CUDA_CACHE_PATH'] = '~/.cudacache'
# os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"
if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    test_pipeline(root_path)
