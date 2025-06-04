import os
import json
import pickle
from numba import njit


def filter_data(data, key, value):
    # Filter the list of dictionaries based on a specific key-value pair
    return [entry for entry in data if entry.get(key) == value]

def get_number_ave_thres(distribution, bottom_threshold, top_threshold):
    """
    Generate the average threshold between the range of threshold 
    arguments:
        distribution:histogram  
        bottom_threshold: bottom threshold
    returns:
       ave_valu: average intensity
    """  
    new_dis = []
    count_new_dis=[]
    xrange = np.arange(0,256,1)
    for i in range(len(xrange)):
        if i < bottom_threshold:
            new_dis.append(0)
        else:
            if i > top_threshold:
                new_dis.append(0)
            else:
                count_new_dis.append(1)
                new_dis.append(distribution[i])
    ave_valu = np.dot(new_dis, xrange)/(np.sum(new_dis))   
    return ave_valu
    
@njit(fastmath=True)
def fast_cal(mask, stacks):
    """
    Generate the list of voxels from the staining stack where intensity is greater than zero for the given region 
    arguments:
        mask: region stack  
        stacks: gene expression stack
    returns:
        mask_list: list of voxels with value
    """  
    mask_list = []
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            for k in range(len(mask[i][j])):
                if mask[i][j][k] == 0:
                    pass
                else:
                    mask_list.append(stacks[i][j][k])
    return mask_list

def calculate_histogram(mask, stacks, name):
    """
    Compute the histogram of staining stack in the region
    arguments:
        mask: region stack  
        stacks: gene expression stack
        name: name of the region
    returns:
        densitys: histogram density
    """  
    mask = mask.astype('float') 
    mask_list = fast_cal(mask, stacks)             
    densitys, bin_edges = np.histogram(mask_list, bins=256, range=(0,255), density=False )
    return densitys
    
def write_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def read_pickle(filename):
    with open(filename, 'rb') as file:
        distribution_data = pickle.load(file)
        return distribution_data
        
        
def write_json(json_data, out_json):
    json_file= open(out_json, 'w')
    json.dump(json_data,json_file) 
        

def read_json(filename):
    with open(filename) as f:
        return json.load(f)