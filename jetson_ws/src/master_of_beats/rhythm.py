#!/usr/bin/env python
import numpy as np



class Models:
    MODELS=[]
    # TODO: add Constans for method indexes and create an array of methods

    class BaseModel(object):
        def __init__(self, offset):
            self.observations=[offset] # beats, sohuld we move that out
            self.steps = [] # intervals between beats
            self.predictions=[offset]
            self.erros=[] # observations(t) - predictions(t)


            self.offset=0
            self.bpm=60 # Not used
            self.confidence=1

            #self.window (window of interest)
        def adjust(self, t):
            self.offset+=t

        def update(self,t_stmp):

            self.steps.append(t_stmp-self.observations[-1]) #this way first one is always 0
            self.observations.append(t_stmp)

        # gets n new predictions, appends them, and returns the new ones
        def predict(self,n):
            last=self.observations[-1]
            next_step=self.fit_fun(1)
            rospy.logdebug("next_step: ", next_step)
            rospy.logdebug("prev. steps: ", self.steps[-10:])
            current_predictions = [(self.fit_fun(i) + last) for i in range(1,n+1)]
            self.predictions.extend(current_predictions)
            return current_predictions

        # when we want to update n predictions starting from after existing index i
        def repredict(self, n, idx):
            current_predictions = []
            last=self.observations[-1]

            for i in range(1,n+1):
                pred=self.fit_fun(i) + self.observations[idx]
                current_predictions.append(pred)
                if idx+i < len(self.predictions):
                    self.predictions[i] = pred
                else:
                    self.predictions.append(pred)

            return current_predictions

        def calc_errors(self):
            pass # index aligning should happen first,
                 # and that needs more code shaped out


        # should be defined by the inheritng class
        def fit_fun(self,i): #lambda?
            pass

    class AvgFit(BaseModel):
    
        def __init__(self,offset):
            # f=mx+p
            super().__init__(offset)
            self.m=0

        def update(self,t_stmp):
            super().update(t_stmp)
            l=len(steps)
            #also ignore the first 0
            self.m = (self.m *(l-2)+ self.steps[-1])/(l-1) # should be faster than mean function

        def fit_fun(self,i):
            #constant part currently comes from the selected index of beats
            return self.m*(i) #+self.observations[self.i]

    class RunningAvgFit(BaseModel):
    
        def __init__(self,offset):
            # f=mx+p
            super().__init__(offset)
            self.m_n=0 #running average
            self.n=10 # window size for avg
            
        def update(self,t_stmp):
            super().update(t_stmp)
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
                super().__init__(offset)

    class MultiLinearFit(BaseModel):
    
        def __init__(self,offset):
            super().__init__(offset)

    # Like this one
    class WindowsOfN(BaseModel):
    
        def __init__(self,offset):
            super().__init__(offset)

    class SecondOrderFit(BaseModel):
    
        def __init__(self,offset):
            super().__init__(offset)

    class KalmanFilter(BaseModel):
    
        def __init__(self,offset):
            super().__init__(offset)
