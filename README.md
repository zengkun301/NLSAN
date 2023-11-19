# NLSAN

### Non-Local Self-Attention Network for Image Super-Resolution

## Environment
- [PyTorch >= 1.7](https://pytorch.org/)
- [BasicSR == 1.3.4.9](https://github.com/XPixelGroup/BasicSR/blob/master/INSTALL.md) 

### Installation
```
pip install -r requirements.txt
python setup.py develop
```

## How To Test
```
- Refer to `./options/test` for the configuration file of the model to be tested, and prepare the testing data and pretrained model.  
- he pretrained models are available at [Baidu Netdisk](https://pan.baidu.com/s/15_zTnP_fNSZPGhnnlymRug) (access code: gykc).  
sh demo.sh
```
The testing results will be saved in the `./results` folder.


## Acknowledgements
This code is built on [BasicSR](https://github.com/XPixelGroup/BasicSR) and [HAT](https://github.com/XPixelGroup/HAT). We thank the authors for sharing their codes.
