# Trial 1
## Network:
### Convolution:
* 32 filters with 3 by 3 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Network:
* 64 nodes with ReLU activation function
### Output:
* Softmax activation function
## Results:
Epoch 10 Accuracy: 0.6923
Accuracy: 0.7021
Loss = 1.0635
## Notes:
Doesn't seem to be overfitting. Will try adding more nodes to the hidden layer.
 
# Trial 2
## Network:
### Convolution:
* 32 filters with 3 by 3 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Network:
* 128 nodes with ReLU activation function
### Output:
* Softmax activation function
## Results:
Epoch 10 Accuracy: 0.9674
Accuracy: 0.9185
Loss = 0.5033
## Notes:
Seems to be overfitted. After epoch 5 or 6 no real improvement. Will try adding Dropout.
 
# Trial 3
## Network:
### Convolution:
* 32 filters with 3 by 3 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Network:
* 128 nodes with ReLU activation function, dropout: 0.5
### Output:
* Softmax activation function
## Results:
Epoch 10 Accuracy: 0.0562
Accuracy: 0.0554
Loss = 3.5052
## Notes:
Less overfitting but may have set dropout value too high. Will try again with a lesser dropout rate value.
 
# Trial 4
## Network:
Convolution:
* 32 filters with 3 by 3 kernels and ReLU activation function
Pooling:
* 2 by 2 pool size
### Network:
* 128 nodes with ReLU activation function, dropout: 0.1
Output: Softmax activation function
## Results:
Epoch 10 Accuracy: 0.8706
Accuracy: 0.9150
Loss = 0.3316
## Notes:
Definitely no apparent overfitting. Relatively accurate but can be better. Will try creating two layers each with half of the nodes currently in the one layer.
 
# Trial 5
## Network:
### Convolution:
* 32 filters with 3 by 3 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 64 nodes with ReLU activation function. Dropout: 0.1
* 64 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.3674
* Accuracy: 0.4715
* Loss = 1.6558
## Notes:
* Low accuracy.
* No overfitting.
* Will try increasing the number of nodes in both layers.
 
# Trial 6
## Network:
### Convolution:
* 32 filters with 3 by 3 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 128 nodes with ReLU activation function. Dropout: 0.1
* 128 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.6832
* Accuracy: 0.7763
* Loss = 0.7528
## Notes:
* Slightly better accuracy.
* No overfitting.
* Will again try to increase the number of nodes in the first layer only.
* Will try to reduce kernel size of convolution layer.
 
# Trial 7
## Network:
### Convolution:
* 32 filters with 2 by 2 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 256 nodes with ReLU activation function. Dropout: 0.1
* 128 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.8403
* Accuracy: 0.8753
* Loss = 0.4600
## Notes:
* Better accuracy.
* No overfitting.
* Will try a larger convolution kernel to see if the node count or kernel size resulted in improved accuracy.
 
# Trial 8
## Network:
### Convolution:
* 32 filters with 4 by 4 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 256 nodes with ReLU activation function. Dropout: 0.1
* 128 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9471
* Accuracy: 0.9412
* Loss = 0.2752
## Notes:
* Much better accuracy.
* Larger kernel size seems to improve accuracy.
* Will increase kernel size again to see if it will further improve accuracy.
 
# Trial 9
## Network:
### Convolution:
* 32 filters with 5 by 5 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 256 nodes with ReLU activation function. Dropout: 0.1
* 128 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9441
* Accuracy: 0.9382
* Loss = 0.3358
## Notes:
* Not much more accuracy.
* Will try tweaking the pool size and decreasing node counts.
 
# Trial 10
## Network:
### Convolution:
* 32 filters with 5 by 5 kernels and ReLU activation function
### Pooling:
* 3 by 3 pool size
### Hidden Layers:
* 128 nodes with ReLU activation function. Dropout: 0.1
* 128 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9398
* Accuracy: 0.9045
* Loss = 0.4770
## Notes:
* Similar accuracy.
* Will return to pool size of 2 by 2 as there seems to be no benefit in increasing it.
* Will also increase node counts on both layers.
* Will try to decrease the amount of filters used.
 
# Trial 11
## Network:
### Convolution:
* 16 filters with 5 by 5 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 200 nodes with ReLU activation function. Dropout: 0.1
* 200 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9441
* Accuracy: 0.9154
* Loss = 0.4120
## Notes:
* Similar accuracy.
* Will try to decrease the amount of filters used again.
 
# Trial 12
## Network:
### Convolution:
* 8 filters with 5 by 5 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 200 nodes with ReLU activation function. Dropout: 0.1
* 200 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9195
* Accuracy: 0.8899
* Loss = 0.5847
## Notes:
* Decrease in filters seems to result in less accuracy.
* Will try increasing them over the original level.
 
# Trial 13
## Network:
### Convolution:
* 64 filters with 5 by 5 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 200 nodes with ReLU activation function. Dropout: 0.1
* 200 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9370
* Accuracy: 0.9392
* Loss = 0.2998
## Notes:
* Seems a bit more accurate, but overall about the same.
* Will try to increase the number of layers.
 
# Trial 14
## Network:
### Convolution:
* 32 filters with 5 by 5 kernels and ReLU activation function
### Pooling:
* 2 by 2 pool size
### Hidden Layers:
* 256 nodes with ReLU activation function. Dropout: 0.1
* 256 nodes with ReLU activation function. Dropout: 0.1
* 256 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9429
* Accuracy: 0.9490
* Loss = 0.2441
## Notes:
* Accuracy seems pretty good.
* Still not over 0.95 though.
* Increasing nodes or layers don't seem to improve accuracy that much... Rather just seems to make overfitting more likely.
* Trying to remove one hidden layer and try adding another convolution and pooling layer.
 
# Trial 15
## Network:
### Convolution:
* 32 filters, 5 by 5 kernels, ReLU activation function
* 32 filters, 5 by 5 kernels, ReLU activation function
### Pooling:
* 2 by 2 pool size
* 2 by 2 pool size
### Hidden Layers:
* 256 nodes with ReLU activation function. Dropout: 0.1
* 256 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9429
* Accuracy: 0.9490
* Loss = 0.2441
## Notes:
* Extra convolution greatly increases accuracy, breaking the 0.95 line.
* Overfitting also seems to reduce after removing the third layer.
* Will try changing the filter number on the second convolution layer.
 
# Trial 16
## Network:
### Convolution:
* 32 filters, 5 by 5 kernels, ReLU activation function
* 64 filters, 5 by 5 kernels, ReLU activation function
### Pooling:
* 2 by 2 pool size
* 2 by 2 pool size
### Hidden Layers:
* 256 nodes with ReLU activation function. Dropout: 0.1
* 256 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9720
* Accuracy: 0.9688
* Loss = 0.1683
## Notes:
* Broke the 0.95 mark, but not always consistently over. Different runs have different results but all are pretty good.
* Slight sign of overfitting.
* Will try experimenting with kernel sizes.
 
# Trial 17
## Network:
### Convolution:
* 32 filters, 3 by 3 kernels, ReLU activation function
* 64 filters, 3 by 3 kernels, ReLU activation function
### Pooling:
* 2 by 2 pool size
* 2 by 2 pool size
### Hidden Layers:
* 256 nodes with ReLU activation function. Dropout: 0.2
* 256 nodes with ReLU activation function. Dropout: 0.1
### Output:
* Softmax activation function
## Results:
* Epoch 10 Accuracy: 0.9813
* Accuracy: 0.9789
* Loss = 0.1171
## Notes:
* Great accuracy without any apparent overfitting.
* Over multiple trials consistently above or around 0.95 mark.
