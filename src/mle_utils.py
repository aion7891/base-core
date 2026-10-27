import numpy as np

class Rescale:

    def scale_live(self, train, live):
        max_val = np.max(train)
        min_val = np.min(train)
        print(f" the maxval :{max_val} \n the min value : {min_val}" )
        live_scale = [self._mix_max_scale(min_val,max_val,x) for x in live]
        return live_scale

    def _mix_max_scale(self,min, max, value):
        if max - min == 0:
            return value
        svalue = (value - min) / (max - min)
        return svalue

