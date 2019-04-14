import caffe
import cv2 as cv
import numpy as np


caffe.set_mode_cpu()

model_def =  '/ws/model/test.prototxt'
model_weights = '/ws/model/weights/cifar10_quick_iter_5000.caffemodel.h5'

net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)

mu = np.load('/opt/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy')
mu = mu.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values
# print 'mean-subtracted values:', zip('BGR', mu)      

print("Input shape = ",net.blobs['data'].data.shape)
# create transformer for the input called 'data'
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR

image = caffe.io.load_image('/opt/caffe/examples/images/cat.jpg')
transformed_image = transformer.preprocess('data', image)
print("Input shape = ",transformed_image.shape)
net.blobs['data'].data[...] = transformed_image

output = net.forward()
output_prob = output['prob'][0]  # the output probability vector for the first image in the batch

classes = {0: 'airplane', 
            1: 'automobile', 
            2: 'bird', 
            3: 'cat',  
            4: 'deer', 
            5: 'dog', 
            6:'frog', 
            7:'horse', 
            8:'ship', 
            9:'truck'}

print 'predicted class is:', classes[output_prob.argmax()]