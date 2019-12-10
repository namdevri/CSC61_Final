# CSC461 Final
Training an artificial neural network to identify different blood cell types present within an in image of blood cells.

### Utilizing Google Colab
It appears that you need a Nvidia Graphics card in order to use PyTorch's cuda package.  You can check my running the following code snippet.
```
import torch

if torch.cuda.is_available():
  print("GPU available for training")
else:
  print("Only CPU available")
```
A simple workaround is utilizing Google Colab's free cuda enabled GPU to drastically speed up the training process.

#### initial setup
* Zip all training and test files
* Navigate to https://drive.google.com/drive and upload the zip file
* Navigate to https://colab.research.google.com and create a new notebook
* Press runtime at the top, click change runtime, then select GPU
* Re-run the above code snippet to ensure cuda is enabled

##### mount dataset

Run the following code and complete the OAuth process prompted by running this code
```
from google.colab import drive
#mount your drive.  Complete Oauth to authenticate
drive.mount('/content/gdrive')
```
Unzip the image folder using the following command.  Note: This assumes you uploaded a file named "jpegs.zip" into your google drive home directory.  You may need to change the path/file name.
```
#unzip image folder
!unzip -uq "/content/gdrive/My Drive/jpegs.zip" -d "/content/gdrive/My Drive/"
```

You should now be able to load your data from google drive.  Here's a sample using PyTorch dataset loader

```
train_set = datasets.ImageFolder("/content/gdrive/My Drive/jpegs/jpegs/train", transform=transformations)
validate_set = datasets.ImageFolder("/content/gdrive/My Drive/jpegs/jpegs/validate", transform=transformations)
```
### Visualizing boundary boxes

Download/clone GitHub project at: https://github.com/Shenggan/BCCD_Dataset

Visualization script at BCCD_Dataset/scripts/visualize.py

You may need to change path to jpeg/annotation files in order to visualize

## To Do
* Plot hyper parameters vs epochs during training/validation
* Test various loss functions
* Plot test and validation errors vs. epoch count
* Use cloud platform to improve training
* Plot train and validation vs epochs
* add regularization parameter to Adam optimizer(.001)
* Investigate larger numbers of epochs
* Stratified CV
* Explore unused optional parameters 

### Poster Content
This is what our poster content is going to be graded on. 
* Context and importance of research demonstrated / 10 
* Research problem clearly stated / 10
* Methodology clearly defined and related to Neural Networks and Deep Learning / 10 
* Results easily interpreted /10

Research Problem & Context: 
For our project, we decied to train an artificial neural network to identify different blood cell types present within images of blood cells. Our main goal for our project was to be able to classify different blood cell subtypes based on images of blood cells while using PyTorch. Diagnosing blood-based diseases typically involves identifying and characterizing the patients blood samples. An automated method being able to detect and classify blood cell subtypes are important applications in the medical field. This dataset contains 12,500 augmented images of blood cells (JPEG) with accompanying cell type labels (CSV). There are approximately 3,000 images for each of 4 different cell types grouped into 4 different folders (according to cell type). The cell types are Eosinophil, Lymphocyte, Monocyte, and Neutrophil. 

Methodology - Training an artificial neural network to identify different blood cell types present within an in image of blood cells. Once we found the dataset that we wanted to use, we wanted to find good accuracy as quickly as possible. We went with a DenseNet implementation and attempted to fine tune its layer widths using a genetic algorithm. Most of our process was tuning hyperparamters. We all would separately test different numbers of epochs, batch sizes, and random layer widths to try and find a good set of hyperparamters to use. Testing different loss functions with our paramaters was something we also did until We found the Negative Log-Likelihood Loss to use with our classifcation. 
 
Results - 

* Poster Display. Short text segments / 10
* Legible pictures, tables and legends (size, font, contrast) / 10
* Organization and logic appropriate for a broad audience / 10
* General style, liveliness, & stage presence / 10
* Effectiveness in answering questions / 10
* Overall impression of the poster and its presentation / 10

https://www.makesigns.com/SciPosters_Templates.aspx

---

## Outline

### Title
* Blood Cell Type Classification Using DenseNet and Genetic Algorithms
* [NAMES]
* University of Rhode Island
* CSC/DSP 461 - Fall 2019

### Research Problem and Context
* Medical science is a fast-growing field servicing an ever-growing population.
* Reducing time for sample processing can be crucial to effective treatment.
* Automation in the lab can decrease delays in patient care and increase care efficiency.
* Can you train a neural network to distinguish between different types of blood cells?

### Data
* We used the "Blood Cell Images" Kaggle dataset[1] as a basis for our implementation.
  * 320x240 color images with 4 evenly distributed classes (Eosinophil, Lymphocyte, Monocyte, and Neutrophil).
  * 9957 training images and 2487 testing images.
* Our model transformed the data by applying random rotations, scaling to a size of 40x30, and normalizing images.
  * 99,570 training images, 9957 validation images, 2487 testing images.

### Methodology
* Test out various approaches (regression, SVM) for initial results.
* Use Google Colab for quicker runtimes.
* Experiment and fine-tune hyperparameters for the neural network (# layers, layer widths, batch sizes, epochs, validation %'s).
* Implement a genetic algorithm to find optimal hyperparameters that maximize test accuracy.

### Model
* DenseNet161[2] neural network with 5 linear hidden layers.
  * NLLLoss[3] with Adam optimizer.
  * 50 epochs, batch size 800, ~9% validation set
* Genetic Algorithm[4]
  * Generations of 10 sets of 5 layer widths.
  * The 3 top-performing members were used to populate the next generation.
  * 1 member from each generation generated randomly.

### Results
* Best-performing model with this technique had 95% training accuracy, 48% testing accuracy.
  * Over all methods tested, ~60% testing accuracy.
* Low training / validation loss, high testing loss (overtraining).
* Genetic algorithm proved to do little better than random weight values.

### Discussion
* Shrinking images drastically increased computation speed but lowered testing accuracy.
* Increasing number of images increased training accuracy but not testing accuracy.
* Genetic algorithm hyperparameters need to be more fine-tuned to be effective.
* Optimal DenseNet hyperparameters were not found for this problem (90% is possible[5]).

### Future Work
* Multi-class classification
* Image detection (data available in Kaggle dataset)
* SVM implementation

### References
* [1]https://www.kaggle.com/paultimothymooney/blood-cells/kernels
* [2]https://pytorch.org/hub/pytorch_vision_densenet/
* [3]https://medium.com/udacity-pytorch-challengers/a-brief-overview-of-loss-functions-in-pytorch-c0ddb78068f7
* [4]https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6
* [5]https://www.kaggle.com/drobchak1988/blood-cell-images-acc-92-val-acc-90
* [6]https://pytorch.org/docs/stable.html

---

### Other implementations

#### Master
* https://www.kaggle.com/paultimothymooney/blood-cells/kernels
### High Accuracy
* https://www.kaggle.com/drobchak1988/blood-cell-images-acc-92-val-acc-90
### Calculated Training Dataset Mean/STD

* mean: [0.6786, 0.6413, 0.6605]
* std: [0.2012, 0.2080, 0.1997]

Method:
```
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms

train_root = "/home/nate/Downloads/blood-cells (2)/dataset2-master/dataset2-master/images/TRAIN"

traindata = datasets.ImageFolder(train_root, transforms.ToTensor())
image_means = torch.stack([t.mean(1).mean(1) for t, c in traindata])
img_stds = torch.stack([t.std(1).mean(1) for t, c in traindata])
print(image_means.mean(0))
print(img_stds.mean(0))
```

### Useful Links
* https://medium.com/udacity-pytorch-challengers/a-brief-overview-of-loss-functions-in-pytorch-c0ddb78068f7
* https://pytorch.org/docs/stable/torchvision/transforms.html
* https://medium.com/swlh/image-classification-tutorials-in-pytorch-transfer-learning-19ebc329e200
* https://pytorch.org/docs/stable/data.html?highlight=torch%20utils%20data%20dataloader#torch.utils.data.DataLoader
* https://discuss.pytorch.org/t/about-normalization-using-pre-trained-vgg16-networks/23560/5
* https://stackoverflow.com/questions/48818619/pytorch-how-do-the-means-and-stds-get-calculated-in-the-transfer-learning-tutor
* https://stackoverflow.com/questions/50544730/how-do-i-split-a-custom-dataset-into-training-and-test-datasets#answer-51768651
* https://pytorch.org/docs/stable/nn.html#loss-functions
* https://machinelearningmastery.com/how-to-configure-the-number-of-layers-and-nodes-in-a-neural-network/
* https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6
* https://en.wikipedia.org/wiki/Genetic_algorithm


### Final Report
Joseph Erickson
Nathan Mathews
Anthony Keaveney
December 10th 2019
CSC 461 Final Report

Blood Cell Type Classification Using DenseNet and Genetic Algorithms

Medical science is a fast-growing field servicing an ever-growing population. Reducing the time needed for lab sample processing can be crucial to administering effective treatment for patients.  Automation in the lab can help reduce these times and increase efficiency of patient care. This all led to the question we wanted to try an answer for our final project, Can you train a neural network to distinguish between different types of blood cells?

 We used the Blood Cell Images Kaggle dataset[1] as the foundation for our implementation. The dataset contained 12,500 images of blood cells with cell type labels. The images were of four different evenly distributed cell types, Eosinophil, Lymphocyte, Monocyte, and Neutrophil. All of these images were also grouped into different folders according to cell type. 
We then began with 9957 training images and 2487 testing images from the original data set. 
Our model then transformed the data by applying random rotations. While our model was already randomly rotating images, we decided to also rotate more images on our own. We did this to then add more images to our training set for further testing. We were then working with 99,570 training images, 9957 validation images, and 2487 testing images. The original size of the image was 320x240 which we decided to scale down to 40x30 to increase the speed of our model since we knew we were going to have a ton of testing to do. We then prepared our model to then normalize the images to get them on the proper scale of being in the range of zero to one. 


Once we finally had our data all set up and ready to use, we then decided to test out various approaches for initial results. Two approaches of ours were using regression and support vector machine. Since we were running tests on such large amounts of images, we found some of our testing to take multiple hours to conclude and it wasn’t efficient for us to get the best results. We then decided to work together using Google Colab running it on the GPU for quicker runtimes. Next, we would experiment and fine-tune hyperparameters for a neural network approach.
These hyperparameters consist of the number layers, layer widths, batch sizes, number of epochs, and validation percent. We then decided Implement a genetic algorithm to find hyperparameters that maximize testing accuracy. 


Next was for us to start preparing our model. We used DenseNet161 [2] neural network with five linear hidden layers. DenseNet is used to connect each layer to every other layer in a feed-forward fashion. While trying to find out which loss function would be best for our model, we tried testing with Cross Entropy Loss, Multi Margin Loss, and The Negative Log Likelihood loss [3]. After several test runs, we found our best accuracy to come with the negative log likelihood loss function with the Adam Optimizer.  We then found our best hyperparameters to be with 50 epochs and a batch size of 800, ~9% validation set. The linear layers in the network are used in conjunction with LogSoftMax. Our Genetic Algorithm [4] was then prepared with generations of 10, and each member a set of 5 layer widths. The top three performing members were then carried over to then populate over the next generation. We also set it up for one member of each generation to be generated randomly. The idea behind this was that we wanted to keep breeding the top-performing members until we reached optimal results. 


Our results finally then told us that our best performing model with this technique achieved 95% training accuracy and 48% testing accuracy. Although, we did have another method which achieved approximately 60% testing accuracy, we decided to remain with this one. We saw low training and validation loss, along with high testing loss which proves that we are overtraining our data. The genetic algorithm then proved to do a little better than random weight values. We then plotted graphs to see how our results over the course of the epochs. After analyzing our results, we then began to discuss. Shrinking images drastically increased computed speed but lowered our testing accuracy by about 10%. In our case, we wanted to see results as quickly as we could without having to wait hours for our computers to run. In the future, using a more powerful machine could be much help in testing. Increasing the number of training and validation images improved training accuracy but not testing accuracy. The Genetic algorithm hyperparameters need to be more fine-tuned for this
specific problem. We also would have likely needed more time to run this algorithm to be effective. 
We also were  unable to find optimal DenseNet hyperparameters for this problem, but from doing other research online, we saw achieving a testing accuracy of 90% is possible[5]. Considerations we could have for future research include Multi-class classification, Image detection[1], an SVM implementation, and Variations on hidden layers.


References
1. https://www.kaggle.com/paultimothymooney/blood-cells/kernels 
2. https://pytorch.org/hub/pytorch_vision_densenet/ 
3.https://medium.com/udacity-pytorch-challengers/a-brief-overview-of-loss-functions-in-pytorch-c0ddb78068f7 
4. https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6 
5. https://www.kaggle.com/drobchak1988/blood-cell-images-acc-92-val-acc-90 
6. https://pytorch.org/docs/stable.htm
