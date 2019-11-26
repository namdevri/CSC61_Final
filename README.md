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


### Useful Links
* https://medium.com/udacity-pytorch-challengers/a-brief-overview-of-loss-functions-in-pytorch-c0ddb78068f7
* https://pytorch.org/docs/stable/torchvision/transforms.html
* https://medium.com/swlh/image-classification-tutorials-in-pytorch-transfer-learning-19ebc329e200
* https://pytorch.org/docs/stable/data.html?highlight=torch%20utils%20data%20dataloader#torch.utils.data.DataLoader
* https://discuss.pytorch.org/t/about-normalization-using-pre-trained-vgg16-networks/23560/5
* https://stackoverflow.com/questions/48818619/pytorch-how-do-the-means-and-stds-get-calculated-in-the-transfer-learning-tutor
