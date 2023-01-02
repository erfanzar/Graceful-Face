import erutils.utils as eu
import torch.optim
from erutils.lightning import *


class GraceFulFace(TorchBaseModule):
    def __init__(self, config: Union[str, os.PathLike] = 'config/graceful-face-normal.yaml'):
        super(GraceFulFace, self).__init__()

        self.cfg = eu.read_yaml(config)
        self.model, self.saves = pars_model_v2(cfg=self.cfg['cfg'], c_req=self.cfg['c_rec'], sc=self.cfg['s_channel'],
                                               imports='from modules.commons import *',
                                               print_status=True)
        self.optimizer = self.optim()

    def forward_once(self, x):

        route = []
        for i, m in enumerate(self.model):
            if m.f != -1:
                x = route[m.f] if isinstance(m.f, int) else [x if j == -1 else route[j] for j in m.f]
            x = m(x)
            route.append(x if i in self.saves else None)
        return x

    def optim(self):
        return torch.optim.SGD(self.model.parameters(), 1e-4)

