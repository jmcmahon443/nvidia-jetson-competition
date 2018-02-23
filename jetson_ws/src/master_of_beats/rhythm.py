#!/usr/bin/env python
import sys
import numpy as np
from collections import deque # performance improvement! everything is a dequeue


class models: # namespace models
    #MODELS=[self.RunningAvgFit, self.WindowsOfN, self.KalmanFilter]
    # TODO: add Constans for method indexes and create an array of methods

    class BaseModel(object):
        def __init__(self, offset=0, window=5):
            self.observations=[offset] # beats, sohuld we move that out
            self.steps = [0] # intervals between beats
            self.predictions=[-1 ,-1]
            self.errors=[0] # observations(t) - predictions(t)
            self.idx=0

            self.W=window
            self.offset=0
            self.bpm=60 # Not used
            self.confidence=1

            #self.window (window of interest)
        def current_pred(self):
            #print("i:", self.idx)
            #print("p:",len(self.predictions))
            # print("o:",len(self.observations))
            # print("will get", self.idx+1)
            return self.predictions[self.idx]

        def adjust(self, t):
            self.offset+=t

        def update(self,t_stmp):

            last_i=self.idx
            self.steps.append(t_stmp-self.observations[last_i]) #this way first one is always 0
            self.observations.append(t_stmp)
            self.calc_err(last_i)
            self.errors.append(self.calc_err(last_i))
            self.idx+=1
            # print(self.idx)
            # print(len(self.observations))
            # print(len(self.predictions))

            print("e:", self.errors[-1])
            print("dt:", self.steps[-1])

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
            last=self.observations[idx]
            for i in range(1,n+1):
                pred=self.fit_fun(i) + last
                current_predictions.append(pred)
                if idx+i < len(self.predictions):
                    self.predictions[i] = pred
                    print("repl")

                else:
                    print("added")
                    self.predictions.append(pred)

            print("i:", self.idx)
            print("p:",len(self.predictions))
            print("o:",len(self.observations))
            print("should get", self.idx+1)

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

        def __init__(self,offset, window):

            # f=mx+p
            super(AvgFit, self).__init__(offset, window)
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
            super(models.RunningAvgFit, self).__init__(offset, window)
            self.m_n=0 #running average
            #self.W=window # window size for avg
            self.ROI=deque([],window)


        def update(self,t_stmp):
            super(models.RunningAvgFit, self).update(t_stmp)
            self.ROI.append(self.steps[-1])

            #also ignore the first 0
            # last -n elements stops at first element if it's out of bounds

            self.m_n = np.mean(self.ROI) # should be faster than mean function

        def fit_fun(self,i):
            #constant part currently comes from the selected index of beats
            return self.m_n*(i)  #+self.observations[self.i

        def set_window(self,n):
            self.n=n

    class BinaryLinearFit(BaseModel):

        def __init__(self,offset):
                super(BinaryLinearFit, self).__init__(offset, window)

    class MultiLinearFit(BaseModel):

        def __init__(self,offset):
            super(MultiLinearFit, self).__init__(offset, window)

    # Like this one
    class WindowsOfN(BaseModel):
        treshold=0.025
        def __init__(self, offset):

            super(WindowsOfN, self).__init__(offset, window=10)
            self.L=1 # length of pattern
            self.T = 0 #time
            self.N=[0]
            self.Sigma=np.array([0])
            self.shape_roi()
            #W # hist.window size
            #rearrange
            self.last_fit=0 #cheeky for loops
            #self.ROI[index%i].append(t_stmp)


        def update(self, t_stmp):

            super(models.WindowsOfN, self).update(t_stmp)

            mod=self.idx%self.L #time
            #self.N=np.mean(folded , axis=1) # should i jsut pop and push? TODO: fill with -1's until we got enpough data

            self.ROI[mod].append(self.steps[-1])
            self.N[mod]=np.mean(self.ROI[mod])
            self.Sigma[mod]=np.std(self.ROI[mod])/self.N[mod]
            #TODO: increase/decrease window. Error method

            #also ignore the first 0
            # last -n elements stops at first element if it's out of bounds


        def fit_fun(self,i):
            #constant part currently comes from the selected index of beats
            #cheeky workaround with for loops
            if i == 1:
                self.last_fit=self.N[(self.idx+1)%self.L]  #+self.observations[self.i
                #so, we reset everytime prediction is invoked anew
            else:
                self.last_fit= self.last_fit + self.N[(self.idx+i)%self.L]

            return self.last_fit



        def shape_roi(self):
            self.ROI=[deque([],self.W) for i in range(self.N)]

        def fill_roi(self): #when we rehsape, we refill the ROI except for the first time
            N=self.N
            (self.ROI[i%N].append(self.steps[i]) for  i in range(self.idx-N*self.W,self.idx))


        def eval_window(self):
            if np.std(self.N)/np.mean(self.N)<0.015 and  self.L == 1:
                self.adjust_window(self.index-1)
            elif false: # this is a placefolder for
                pass#folding the pattern in hallf

            # compare normalized deviations
            elif  self.Sigma.any() > WindowsOfN.treshold :
                self.adjust_window(self.index+1)

        def adjust_window(self,new_l):
            self.L=new_l
            self.N=np.zeros(new_l)
            self.Sigma=np.zeros(new_l)
            self.shape_roi()
            self.fill_roi()




    class SecondOrderFit(BaseModel):

        def __init__(self,offset):
            super(SecondOrderFit, self).__init__(offset, window)

    class KalmanFilter(BaseModel):

        def __init__(self,offset):
            super(KalmanFilter, self).__init__(offset, window)

    class MarkovChain(BaseModel):

        def __init__(self,offset):
            super(MarkovChain, self).__init__(offset, window)
