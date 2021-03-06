#!/usr/bin/env python
import sys
import numpy as np



class Models:
    MODELS=[]
    # TODO: add Constans for method indexes and create an array of methods

    class BaseModel(object):
        def __init__(self, offset=0):
            self.observations=[offset] # beats, sohuld we move that out
            self.steps = [0] # intervals between beats
            self.predictions=[-1 ,-1]
            self.errors=[0] # observations(t) - predictions(t)
            self.idx=1

            self.offset=0
            self.bpm=60 # Not used
            self.confidence=1

            #self.window (window of interest)
        def current_pred(self):
            return self.predictions[self.idx]

        def adjust(self, t):
            self.offset+=t

        def update(self,t_stmp):
            print(self.idx)
            last_i=self.idx-1
            self.steps.append(t_stmp-self.observations[last_i]) #this way first one is always 0
            self.observations.append(t_stmp)
            self.calc_err(last_i)
            self.errors.append(self.calc_err(last_i))
            print(self.errors[-1])
            print(self.steps[-1])

        # gets n new predictions, appends them, and returns the new ones
        def predict(self,n):
            return self.repredict(n, self.idx)
       #     last=self.observations[self.idx-1]
       #     next_step=self.fit_fun(1)
       #     #print("next_step: ", next_step)
       #     #print("prev.steps: ", self.steps[-10:])
       #     current_predictions = [(self.fit_fun(i) + last) for i in range(1,n+1)]
       #     self.predictions.extend(current_predictions)
            #print(current_predictions)
       #     return current_predictions

        # when we want to update n predictions starting from after existing index i
        def repredict(self, n, idx):
            current_predictions = []
            last=self.observations[idx-1]

            for i in range(1,n+1):
                pred=self.fit_fun(i) + last
                current_predictions.append(pred)
                if idx+i < len(self.predictions):
                    self.predictions[i] = pred
                else:
                    self.predictions.append(pred)

            #print(self.predictions)

            return current_predictions

        def calc_err(self,i):
            #last=self.idx-1
            #self.errors.append(self.observations[last]-self.predictions[last])

            return self.observations[i]-self.predictions[i]

        # should be defined by the inheritng class
        def fit_fun(self,i): #lambda?
            pass

        def eval(self): #some statistics stuff
            pass

    class AvgFit(BaseModel):

        def __init__(self,offset):

            # f=mx+p
            super(AvgFit, self).__init__(offset)
            self.m=0

        def update(self,t_stmp):
            super(AvgFit, self).update(t_stmp)
            l=len(steps)
            #also ignore the first 0
            self.m = (self.m *(l-2)+ self.steps[-1])/(l-1) # should be faster than mean function

        def fit_fun(self,i):
            #constant part currently comes from the selected index of beats
            return self.m*(i) #+self.observations[self.i]

    class RunningAvgFit(BaseModel):

        def __init__(self,offset, window):
            # f=mx+p
            super(Models.RunningAvgFit, self).__init__(offset)
            self.m_n=0 #running average
            self.n=window # window size for avg

        def update(self,t_stmp):
            super(Models.RunningAvgFit, self).update(t_stmp)
            #also ignore the first 0
            # last -n elements stops at first element if it's out of bounds

            self.m_n = np.sum(self.steps[-self.n:])/self.n # should be faster than mean function

        def fit_fun(self,i):
            #constant part currently comes from the selected index of beats
            return self.m_n*(i)  #+self.observations[self.i

        def set_window(self,n):
            self.n=n

    class BinaryLinearFit(BaseModel):

        def __init__(self,offset):
                super(BinaryLinearFit, self).__init__(offset)

    class MultiLinearFit(BaseModel):

        def __init__(self,offset):
            super(MultiLinearFit, self).__init__(offset)

    # Like this one
    class WindowsOfN(BaseModel):

        def __init__(self,offset):
            super(WindowsOfN, self).__init__(offset)
            self.l=1 # windows size
            self.T = 0 #time
            self.N=[0]
            self.hist=10 #history of beats
            #rearrange


        def update(self,t_stmp):
            super(Models.WindowsOfN, self).update(t_stmp)
            T=self.index - self.index%i #time
            folded=np.array(self.beats[T-self.winsize*self.hist:T+1]).reshape(self.winsize, self.hist)
            self.N=np.mean(folded , axis=1) # should i jsut pop and push? TODO: fill with -1's until we got enpough data
            
            #TODO: increase/decrease window. Error method
            
            #also ignore the first 0
            # last -n elements stops at first element if it's out of bounds

            
        def fit_fun(self,i):
            #constant part currently comes from the selected index of beats

            return self.N[i%l]*(i//N+1)  #+self.observations[self.i

        def eval_window(self):
            pass

        def adjust_window(self):
            pass

        def set_window(self,n):
            self.N=n

    class SecondOrderFit(BaseModel):

        def __init__(self,offset):
            super(SecondOrderFit, self).__init__(offset)

    class KalmanFilter(BaseModel):

        def __init__(self,offset):
            super(KalmanFilter, self).__init__(offset)
