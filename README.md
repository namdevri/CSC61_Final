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
For our project, we decied to Train an artificial neural network to identify different blood cell types present within an in image of blood cells. Our main goal for our project was to be able to classify different blood cell subtypes based on images of blood cells while using PyTorch. Diagnosing blood-based diseases typically involves identifying and characterizing the patients blood samples. An automated method being able to detect and classify blood cell subtypes are important applications in the medical field. This dataset contains 12,500 augmented images of blood cells (JPEG) with accompanying cell type labels (CSV). There are approximately 3,000 images for each of 4 different cell types grouped into 4 different folders (according to cell type). The cell types are Eosinophil, Lymphocyte, Monocyte, and Neutrophil. 

Methodology - Training an artificial neural network to identify different blood cell types present within an in image of blood cells. 
 Once we found the dataset that we wanted to use, we wanted to find good accuracy as quickly as possible. We went with a DenseNet implementation and attempted to fine tune its layer widths using a genetic algorithm. Most of our process was tuning hyperparamters. We all would separately test different numbers of epochs, batch sizes, and random layer widths to try and find a good set of hyperparamters to use. Testing different loss functions with our paramaters was something we also did until We found the Negative Log-Likelihood Loss to use with our classifcation. 
 
Results - 

* Poster Display. Short text segments / 10
* Legible pictures, tables and legends (size, font, contrast) / 10
* Organization and logic appropriate for a broad audience / 10
* General style, liveliness, & stage presence / 10
* Effectiveness in answering questions / 10
* Overall impression of the poster and its presentation / 10



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
