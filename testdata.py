import pickle
import numpy as np

with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

    data = np.asarray(data_dict['data'])
    labels = np.asarray(data_dict['labels'])


print(len(labels))


