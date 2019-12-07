# Currently Running Code:

## Joe:
```
t_epochs = [25]
t_batches = [800]
t_val = 0.2
best_acc = 0
best_results = []

while 0==0:
    for i in t_epochs:
        for j in t_batches:
            layers = [random.randint(100,3001),random.randint(100,3001),random.randint(100,3001),random.randint(100,3001),random.randint(100,3001)]
            print('\nLoss Function: NLLLoss \tNumber of Epochs: {} \tBatch Size: {} \tValidation Percent: {}'.format(i,j,t_val))
            print('Images resized to 30x40px.')
            print("Layers: \t{}".format(layers))
            acc = train_network(epochs=i, val_percent=t_val, train_batch_size=j, test_batch_size=j, eval_freq=1, layer_widths=layers)
            if acc > best_acc:
                best_acc = acc
                print("******************************************************** NEW BEST ACCURACY: {:.6f}".format(best_acc))
                print("******************************************************** LAYER WIDTHS:      {}".format(layers))
```
---

# Results:

Run 17

* Loss Function: NLLLoss 	Number of Epochs: 10 	Batch Size: 50 	Validation Percent: 0.2
* Images resized to 30x40px.
* Beginning setup...
* Setting up train, test, and validation sets...
* Full train set size:  9957
* Train set size:  7966
* Validation set size:  1991
* Test set size:  2487
* Beginning training...
* Epoch: 1 	Accuracy: 0.600415 	Training Loss: 1.097977 	Validation Loss: 1.160111 
* Epoch: 2 	Accuracy: 0.615024 	Training Loss: 0.916336 	Validation Loss: 1.170981 
* Epoch: 3 	Accuracy: 0.659744 	Training Loss: 0.853748 	Validation Loss: 1.069735 
* Epoch: 4 	Accuracy: 0.612244 	Training Loss: 0.811477 	Validation Loss: 1.334290 
* Epoch: 5 	Accuracy: 0.677024 	Training Loss: 0.761510 	Validation Loss: 0.830155 
* Epoch: 6 	Accuracy: 0.678963 	Training Loss: 0.710578 	Validation Loss: 0.892294 
* Epoch: 7 	Accuracy: 0.675573 	Training Loss: 0.671650 	Validation Loss: 0.891510 
* Epoch: 8 	Accuracy: 0.683963 	Training Loss: 0.611281 	Validation Loss: 0.838476 
* Epoch: 9 	Accuracy: 0.679354 	Training Loss: 0.581496 	Validation Loss: 0.808214 
* Epoch: 10 	Accuracy: 0.690573 	Training Loss: 0.547951 	Validation Loss: 1.292905 
* Final Results:	Accuracy: 0.488930 	Training Loss: 0.588135 	Testing Loss: 1.627002 


Run 18

* Loss Function: NLLLoss 	Number of Epochs: 10 	Batch Size: 100 	Validation Percent: 0.2
* Images resized to 30x40px.
* Beginning setup...
* Setting up train, test, and validation sets...
* Full train set size:  9957
* Train set size:  7966
* Validation set size:  1991
* Test set size:  2487
* Beginning training...
* Epoch: 1 	Accuracy: 0.555176 	Training Loss: 1.124714 	Validation Loss: 1.049849 
* Epoch: 2 	Accuracy: 0.645368 	Training Loss: 0.877542 	Validation Loss: 0.900281 
* Epoch: 3 	Accuracy: 0.631522 	Training Loss: 0.824654 	Validation Loss: 0.868768 
* Epoch: 4 	Accuracy: 0.667016 	Training Loss: 0.748276 	Validation Loss: 0.851706 
* Epoch: 5 	Accuracy: 0.682368 	Training Loss: 0.693535 	Validation Loss: 0.783253 
* Epoch: 6 	Accuracy: 0.681868 	Training Loss: 0.632877 	Validation Loss: 0.782845 
* Epoch: 7 	Accuracy: 0.683863 	Training Loss: 0.577922 	Validation Loss: 0.807150 
* Epoch: 8 	Accuracy: 0.711665 	Training Loss: 0.521608 	Validation Loss: 0.736940 
* Epoch: 9 	Accuracy: 0.707764 	Training Loss: 0.454957 	Validation Loss: 0.785636 
* Epoch: 10 	Accuracy: 0.719610 	Training Loss: 0.407335 	Validation Loss: 0.788728 
* Final Results:	Accuracy: 0.479269 	Training Loss: 0.450259 	Testing Loss: 1.560974 


Run 19

* Loss Function: NLLLoss 	Number of Epochs: 10 	Batch Size: 200 	Validation Percent: 0.2
* Images resized to 30x40px.
* Beginning setup...
* Setting up train, test, and validation sets...
* Full train set size:  9957
* Train set size:  7966
* Validation set size:  1991
* Test set size:  2487
* Beginning training...
* Epoch: 1 	Accuracy: 0.599804 	Training Loss: 1.171397 	Validation Loss: 0.973513 
* Epoch: 2 	Accuracy: 0.588874 	Training Loss: 0.937229 	Validation Loss: 1.015982 
* Epoch: 3 	Accuracy: 0.612280 	Training Loss: 0.814486 	Validation Loss: 0.986740 
* Epoch: 4 	Accuracy: 0.636063 	Training Loss: 0.740062 	Validation Loss: 0.893427 
* Epoch: 5 	Accuracy: 0.672327 	Training Loss: 0.669452 	Validation Loss: 0.819181 
* Epoch: 6 	Accuracy: 0.674398 	Training Loss: 0.575852 	Validation Loss: 0.836685 
* Epoch: 7 	Accuracy: 0.697681 	Training Loss: 0.508199 	Validation Loss: 0.825571 
* Epoch: 8 	Accuracy: 0.668016 	Training Loss: 0.431571 	Validation Loss: 0.863401 
* Epoch: 9 	Accuracy: 0.695110 	Training Loss: 0.375060 	Validation Loss: 0.817083 
* Epoch: 10 	Accuracy: 0.676657 	Training Loss: 0.315847 	Validation Loss: 0.896484 
* Final Results:	Accuracy: 0.483174 	Training Loss: 0.388844 	Testing Loss: 1.670899 


Run 20

* Loss Function: NLLLoss 	Number of Epochs: 10 	Batch Size: 400 	Validation Percent: 0.2
* Images resized to 30x40px.
* Beginning setup...
* Setting up train, test, and validation sets...
* Full train set size:  9957
* Train set size:  7966
* Validation set size:  1991
* Test set size:  2487
* Beginning training...
* Epoch: 1 	Accuracy: 0.587986 	Training Loss: 1.236846 	Validation Loss: 1.055822 
* Epoch: 2 	Accuracy: 0.623366 	Training Loss: 0.961489 	Validation Loss: 0.905803 
* Epoch: 3 	Accuracy: 0.622854 	Training Loss: 0.848723 	Validation Loss: 0.916030 
* Epoch: 4 	Accuracy: 0.663153 	Training Loss: 0.810521 	Validation Loss: 0.839140 
* Epoch: 5 	Accuracy: 0.678538 	Training Loss: 0.719327 	Validation Loss: 0.799447 
* Epoch: 6 	Accuracy: 0.666027 	Training Loss: 0.662806 	Validation Loss: 0.839970 
* Epoch: 7 	Accuracy: 0.673515 	Training Loss: 0.614681 	Validation Loss: 0.834663 
* Epoch: 8 	Accuracy: 0.686119 	Training Loss: 0.533959 	Validation Loss: 0.794181 
* Epoch: 9 	Accuracy: 0.696665 	Training Loss: 0.458621 	Validation Loss: 0.787878 
* Epoch: 10 	Accuracy: 0.700619 	Training Loss: 0.413524 	Validation Loss: 0.756762 
* Final Results:	Accuracy: 0.492397 	Training Loss: 0.442663 	Testing Loss: 1.396512 


Run 21

* Loss Function: NLLLoss 	Number of Epochs: 10 	Batch Size: 800 	Validation Percent: 0.2
* Images resized to 30x40px.
* Beginning setup...
* Setting up train, test, and validation sets...
* Full train set size:  9957
* Train set size:  7966
* Validation set size:  1991
* Test set size:  2487
* Beginning training...
* Epoch: 1 	Accuracy: 0.475972 	Training Loss: 1.314685 	Validation Loss: 1.238930 
* Epoch: 2 	Accuracy: 0.574277 	Training Loss: 1.098886 	Validation Loss: 1.051863 
* Epoch: 3 	Accuracy: 0.589053 	Training Loss: 0.974349 	Validation Loss: 0.978190 
* Epoch: 4 	Accuracy: 0.635212 	Training Loss: 0.904811 	Validation Loss: 0.916149 
* Epoch: 5 	Accuracy: 0.646122 	Training Loss: 0.843347 	Validation Loss: 0.872921 
* Epoch: 6 	Accuracy: 0.644417 	Training Loss: 0.789788 	Validation Loss: 0.870462 
* Epoch: 7 	Accuracy: 0.650500 	Training Loss: 0.748503 	Validation Loss: 0.880995 
* Epoch: 8 	Accuracy: 0.655006 	Training Loss: 0.694173 	Validation Loss: 0.856772 
* Epoch: 9 	Accuracy: 0.650610 	Training Loss: 0.655904 	Validation Loss: 0.895626 
* Epoch: 10 	Accuracy: 0.670179 	Training Loss: 0.624158 	Validation Loss: 0.838727 
* Final Results:	Accuracy: 0.539670 	Training Loss: 0.630354 	Testing Loss: 1.293276 



