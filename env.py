import erutils

cfg = erutils.read_yaml('config/graceful-face-normal.yaml')['cfg']

if __name__ == "__main__":
    # print(*(f'{v}\n' for v in cfg))
    f = erutils.pars_model_v2(cfg=cfg, c_req=['Conv'], imports='from modules.commons import *')
    print(f)
