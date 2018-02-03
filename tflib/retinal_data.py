# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:25:22 2017

@author: manuel
"""

import sys
sys.path.append('/home/manuel/improved_wgan_training/')
import numpy as np
import scipy.io as sio
from tflib import sim_pop_activity


def get_samples(num_bins=27, num_neurons=10, instance='1'):                        
    
    mat_contents = sio.loadmat('/home/manuel/generative-neural-models-master/k_pairwise/results/data_num_neurons_' + str(num_neurons) + '_' + instance + '.mat')   
    data = mat_contents['data']
    
    if num_bins!=1:
        X = np.zeros((num_bins*data.shape[1],data.shape[0]-num_bins))
        for ind_s in range(data.shape[0]-num_bins):
            sample = data[ind_s:ind_s+num_bins,:].T
            X[:,ind_s] = sample.reshape((num_neurons*num_bins,-1))[:,0] 
    else:
        X = data.T
    sim_pop_activity.plot_samples(X, num_neurons=num_neurons, folder='/home/manuel/improved_wgan_training/', name='retinal_samples')
    return X
        
        
def load_samples_from_k_pairwise_model(num_samples=2**13, num_bins=27, num_neurons=10, instance='1', folder='/home/manuel/generative-neural-models-master/k_pairwise/results'):
    #get samples produced by k-pairwise model
    mat_contents = sio.loadmat(folder + '/simulated_samples_num_neurons_' + str(num_neurons) + '_' + instance + '.mat')    
    data = mat_contents['samples_batch_all']
    if num_bins!=1:
        data = data[0:data.shape[0]-data.shape[0]%num_bins,:]
        X = np.zeros((num_bins*data.shape[1],int(np.min([num_samples,data.shape[0]/num_bins]))))
        for ind_s in range(int(np.min([num_samples,data.shape[0]/num_bins]))):
            sample = data[ind_s*num_bins:(ind_s+1)*num_bins,:].T
            X[:,ind_s] = sample.reshape((num_neurons*num_bins,-1))[:,0] 
    
    else:
        X = data.T

    return X
   

def load_samples_from_DDG_model(num_samples=2**13, num_bins=27, num_neurons=10, instance='1', name='DDGfit_of_retinal_data'):
    #get samples produced by DG model
    #assert num_neurons==50
    assert instance=='1'
    mat_contents = sio.loadmat('/home/manuel/DDG/results/' + name + '.mat')   
    data = mat_contents['data']
    if num_bins!=1:
        data = data[0:data.shape[0]-data.shape[0]%num_bins,:]
        X = np.zeros((num_bins*data.shape[1],int(np.min([num_samples,data.shape[0]/num_bins]))))
        for ind_s in range(int(np.min([num_samples,data.shape[0]/num_bins]))):
            sample = data[ind_s*num_bins:(ind_s+1)*num_bins,:].T
            X[:,ind_s] = sample.reshape((num_neurons*num_bins,-1))[:,0] 
    
    else:
        X = data.T


    return X
   


    
if __name__ == '__main__':
    load_samples_from_k_pairwise_model(num_samples=2**13, num_bins=128, num_neurons=32, instance='1', folder='/home/manuel/generative-neural-models-master/k_pairwise/results_neg_corrs')
    X = get_samples(num_bins=32, num_neurons=50, instance='1')
    sim_pop_activity.plot_samples(X, num_neurons=50, folder='/home/manuel/improved_wgan_training/', name='test')
    
