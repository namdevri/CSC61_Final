# Currently Running Code:

## Joe:
```
# Image size 30x40
# Original data + 10 random rotations.
t_epochs = 50
t_batches = 800
t_val = 0.2

gen = 20
population = freshGeneration(10,5)
#population = [[[1966, 264, 2557, 2118, 159],0.513121],
#              [[2846, 1622, 1610, 904, 1704],0.505431],
#              [[2071, 1445, 415, 2881, 851],0.498373],
#              [[1736, 2826, 246, 1294, 2039],0.492680],
#              [[2862, 1980, 2730, 2992, 128],0.492626],
#              [[225, 2699, 1359, 1854, 2259],0.492565],
#              [[1638, 1353, 1522, 1035, 227],0.492435],
#              [[1302, 1379, 1355, 1397, 1308],0.491566],
#              [[2353, 2982, 114, 2300, 439],0.491559],
#              [[597, 1083, 476, 2025, 2133],0.489555]]

#print(population[0][0])
#print(population[0][1])
#print(population[0][0][1])
i = 0
while i < 10:
    #print(population[i])
    print("\t{} - {:.6f}".format(population[i][0],population[i][1]))
    i = i + 1

# Note: pretrained=True should be used ONLY if training over 25 epochs with batch size 800, otherwise results will be skewed.
bestParameters = geneticAlgorithm(population,gen,False)
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

```
# CODE
t_epochs = 50
t_batches = 800
t_val = 0.2

gen = 20
population = freshGeneration(10,5)
#population = [[[1966, 264, 2557, 2118, 159],0.513121],
#              [[2846, 1622, 1610, 904, 1704],0.505431],
#              [[2071, 1445, 415, 2881, 851],0.498373],
#              [[1736, 2826, 246, 1294, 2039],0.492680],
#              [[2862, 1980, 2730, 2992, 128],0.492626],
#              [[225, 2699, 1359, 1854, 2259],0.492565],
#              [[1638, 1353, 1522, 1035, 227],0.492435],
#              [[1302, 1379, 1355, 1397, 1308],0.491566],
#              [[2353, 2982, 114, 2300, 439],0.491559],
#              [[597, 1083, 476, 2025, 2133],0.489555]]

#print(population[0][0])
#print(population[0][1])
#print(population[0][0][1])
i = 0
while i < 10:
    #print(population[i])
    print("\t{} - {:.6f}".format(population[i][0],population[i][1]))
    i = i + 1

# Note: pretrained=True should be used ONLY if training over 25 epochs with batch size 800, otherwise results will be skewed.
bestParameters = geneticAlgorithm(population,gen,False)
```

```
# Genetic ALgorithm Testing - RESULTS:

	[720, 1610, 943, 1952, 997] - 0.000000
	[1537, 880, 1134, 119, 609] - 0.000000
	[771, 1264, 664, 1845, 163] - 0.000000
	[441, 785, 1855, 442, 1175] - 0.000000
	[1720, 1210, 1085, 812, 1653] - 0.000000
	[1848, 281, 1573, 281, 828] - 0.000000
	[1782, 1082, 1915, 1991, 1762] - 0.000000
	[1135, 1699, 1665, 474, 1678] - 0.000000
	[333, 1651, 877, 793, 1067] - 0.000000
	[1593, 1046, 907, 662, 1532] - 0.000000
	
***** GENETIC ALGORITHM INITIAL GENERATION:

	[720, 1610, 943, 1952, 997] - 0.000000
	[1537, 880, 1134, 119, 609] - 0.000000
	[771, 1264, 664, 1845, 163] - 0.000000
	[441, 785, 1855, 442, 1175] - 0.474935
	[1720, 1210, 1085, 812, 1653] - 0.460255
	[1848, 281, 1573, 281, 828] - 0.441009
	[1782, 1082, 1915, 1991, 1762] - 0.456771
	[1135, 1699, 1665, 474, 1678] - 0.490377
	[333, 1651, 877, 793, 1067] - 0.477877
	[1593, 1046, 907, 662, 1532] - 0.474874

***** RESULTS OF GENERATION 1:

	[331, 781, 886, 469, 1173] - 0.517428
	[1135, 1699, 1665, 474, 1678] - 0.490377
	[333, 1651, 877, 793, 1067] - 0.477877
	[899, 1893, 1694, 1711, 1040] - 0.475004
	[441, 785, 1855, 442, 1175] - 0.474935
	[1133, 519, 1672, 464, 1177] - 0.471315
	[260, 1693, 884, 792, 341] - 0.465880
	[1867, 1704, 1856, 801, 1059] - 0.452694
	[333, 792, 1848, 476, 1178] - 0.449447
	[451, 1649, 1437, 802, 1570] - 0.440704

***** RESULTS OF GENERATION 2:

	[331, 781, 886, 469, 1173] - 0.517428
	[1133, 784, 1660, 785, 1672] - 0.510241
	[328, 1658, 871, 803, 1069] - 0.506300
	[333, 782, 1670, 787, 1668] - 0.491430
	[1135, 1699, 1665, 474, 1678] - 0.490377
	[465, 1359, 1790, 1177, 448] - 0.479623
	[333, 1651, 877, 793, 1067] - 0.477877
	[326, 1645, 1209, 787, 1678] - 0.477320
	[335, 791, 886, 795, 1169] - 0.473441
	[330, 1652, 892, 468, 1182] - 0.446886

***** RESULTS OF GENERATION 3:

	[331, 781, 886, 469, 1173] - 0.517428
	[1133, 784, 1660, 785, 1672] - 0.510241
	[328, 1658, 871, 803, 1069] - 0.506300
	[1189, 1162, 440, 836, 1682] - 0.500248
	[1126, 789, 1670, 797, 678] - 0.488373
	[334, 777, 1668, 461, 1673] - 0.470445
	[560, 774, 872, 460, 1077] - 0.467870
	[1134, 790, 1664, 799, 1667] - 0.465445
	[329, 790, 1650, 795, 1172] - 0.461695
	[929, 405, 888, 472, 1079] - 0.461505
	
***** RESULTS OF GENERATION 4:

	[331, 781, 886, 469, 1173] - 0.517428
	[1133, 784, 1660, 785, 1672] - 0.510241
	[328, 1658, 871, 803, 1069] - 0.506300
	[1130, 1666, 876, 791, 1183] - 0.485995
	[323, 781, 1922, 807, 1062] - 0.473509
	[326, 1651, 893, 805, 1179] - 0.472306
	[329, 789, 1208, 785, 1175] - 0.469569
	[415, 792, 885, 799, 1180] - 0.464386
	[324, 826, 886, 1974, 1170] - 0.451261
	[554, 1154, 18, 1619, 214] - 0.420650

***** RESULTS OF GENERATION 5:

	[331, 781, 886, 469, 1173] - 0.517428
	[1133, 784, 1660, 785, 1672] - 0.510241
	[328, 1658, 871, 803, 1069] - 0.506300
	[333, 775, 886, 470, 1671] - 0.490682
	[319, 1649, 1660, 519, 1673] - 0.483121
	[330, 1661, 865, 467, 1671] - 0.466818
	[325, 1664, 883, 798, 1680] - 0.461315
	[1978, 184, 1691, 1945, 1864] - 0.455758
	[336, 777, 885, 476, 1071] - 0.452945
	[1511, 773, 877, 776, 1166] - 0.448136

***** RESULTS OF GENERATION 6:

	[331, 781, 886, 469, 1173] - 0.517428
	[1133, 784, 1660, 785, 1672] - 0.510241
	[328, 1658, 871, 803, 1069] - 0.506300
	[678, 1660, 876, 795, 1177] - 0.482877
	[1605, 872, 1365, 540, 1045] - 0.480499
	[333, 778, 1660, 793, 1070] - 0.468631
	[340, 783, 1466, 788, 1077] - 0.462633
	[327, 784, 876, 804, 1063] - 0.458761
	[323, 778, 1670, 801, 1674] - 0.458258
	[335, 1655, 861, 793, 1663] - 0.450819

***** RESULTS OF GENERATION 7:

	[331, 781, 886, 469, 1173] - 0.517428
	[1133, 784, 1660, 785, 1672] - 0.510241
	[328, 1658, 871, 803, 1069] - 0.506300
	[323, 1659, 867, 790, 1180] - 0.501110
	[1551, 783, 725, 783, 1165] - 0.497496
	[1576, 171, 1127, 939, 462] - 0.484752
	[387, 783, 1652, 574, 1167] - 0.482306
	[338, 1654, 1651, 788, 1163] - 0.481932
	[339, 792, 1653, 795, 1677] - 0.469256
	[1140, 1650, 874, 412, 1173] - 0.450384

```

## Nate

### Config
```
t_epochs = 50
t_batches = 800
t_val = 0.2

gen = 20
population = freshGeneration(10,5)
#population = [[[1966, 264, 2557, 2118, 159],0.513121],
#              [[2846, 1622, 1610, 904, 1704],0.505431],
#              [[2071, 1445, 415, 2881, 851],0.498373],
#              [[1736, 2826, 246, 1294, 2039],0.492680],
#              [[2862, 1980, 2730, 2992, 128],0.492626],
#              [[225, 2699, 1359, 1854, 2259],0.492565],
#              [[1638, 1353, 1522, 1035, 227],0.492435],
#              [[1302, 1379, 1355, 1397, 1308],0.491566],
#              [[2353, 2982, 114, 2300, 439],0.491559],
#              [[597, 1083, 476, 2025, 2133],0.489555]]

#print(population[0][0])
#print(population[0][1])
#print(population[0][0][1])
i = 0
while i < 10:
    #print(population[i])
    print("\t{} - {:.6f}".format(population[i][0],population[i][1]))
    i = i + 1

# Note: pretrained=True should be used ONLY if training over 25 epochs with batch size 800, otherwise results will be skewed.
bestParameters = geneticAlgorithm(population,40,True)
```
### Resuls
```
	[1459, 895, 1011, 1642, 368] - 0.000000
	[1087, 1784, 884, 348, 1392] - 0.000000
	[184, 1020, 1931, 1382, 751] - 0.000000
	[212, 683, 251, 1381, 100] - 0.000000
	[1616, 332, 1234, 1618, 86] - 0.000000
	[704, 1144, 541, 804, 1641] - 0.000000
	[1205, 1586, 587, 1493, 733] - 0.000000
	[1191, 1249, 1604, 1471, 265] - 0.000000
	[1119, 522, 1194, 924, 1141] - 0.000000
	[81, 126, 619, 1229, 1148] - 0.000000

***** GENETIC ALGORITHM INITIAL GENERATION:

	[1459, 895, 1011, 1642, 368] - 0.000000
	[1087, 1784, 884, 348, 1392] - 0.000000
	[184, 1020, 1931, 1382, 751] - 0.000000
	[212, 683, 251, 1381, 100] - 0.000000
	[1616, 332, 1234, 1618, 86] - 0.000000
	[704, 1144, 541, 804, 1641] - 0.000000
	[1205, 1586, 587, 1493, 733] - 0.000000
	[1191, 1249, 1604, 1471, 265] - 0.000000
	[1119, 522, 1194, 924, 1141] - 0.000000
	[81, 126, 619, 1229, 1148] - 0.000000

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1097, 1777, 885, 1382, 744]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Downloading: "https://download.pytorch.org/models/densenet161-8d451a50.pth" to /root/.cache/torch/checkpoints/densenet161-8d451a50.pth
100%|██████████| 110M/110M [00:02<00:00, 54.5MB/s]
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.477869 	Training Loss: 1.377197 	Validation Loss: 1.337729 
Epoch: 5 	Accuracy: 0.586438 	Training Loss: 0.925233 	Validation Loss: 0.931252 
Epoch: 10 	Accuracy: 0.653205 	Training Loss: 0.539650 	Validation Loss: 0.974301 
Epoch: 15 	Accuracy: 0.679192 	Training Loss: 0.240436 	Validation Loss: 1.060614 
Epoch: 20 	Accuracy: 0.672621 	Training Loss: 0.108112 	Validation Loss: 1.445581 
Epoch: 25 	Accuracy: 0.694782 	Training Loss: 0.066656 	Validation Loss: 1.420038 
Epoch: 30 	Accuracy: 0.701736 	Training Loss: 0.083994 	Validation Loss: 1.415295 
Epoch: 35 	Accuracy: 0.677827 	Training Loss: 0.115517 	Validation Loss: 1.298581 
Epoch: 40 	Accuracy: 0.703364 	Training Loss: 0.027834 	Validation Loss: 1.635006 
Epoch: 45 	Accuracy: 0.673570 	Training Loss: 0.047982 	Validation Loss: 1.604133 
Epoch: 50 	Accuracy: 0.712646 	Training Loss: 0.030541 	Validation Loss: 1.495848 
Training... (13/13)/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type DenseNet. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type Sequential. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type Conv2d. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type BatchNorm2d. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type ReLU. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type MaxPool2d. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type _DenseBlock. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type _DenseLayer. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type _Transition. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type AvgPool2d. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type Linear. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "
/usr/local/lib/python3.6/dist-packages/torch/serialization.py:292: UserWarning: Couldn't retrieve source code for container of type LogSoftmax. It won't be checked for correctness upon loading.
  "type " + obj.__name__ + ". It won't be checked "

Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.459195 	Training Loss: 0.299098 	Testing Loss: 1.886461

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[180, 1785, 1937, 357, 1401]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.379544 	Training Loss: 1.378036 	Validation Loss: 1.299298 
Epoch: 5 	Accuracy: 0.584733 	Training Loss: 0.895307 	Validation Loss: 0.927586 
Epoch: 10 	Accuracy: 0.676884 	Training Loss: 0.570730 	Validation Loss: 0.845739 
Epoch: 15 	Accuracy: 0.687377 	Training Loss: 0.299880 	Validation Loss: 1.086173 
Epoch: 20 	Accuracy: 0.679039 	Training Loss: 0.173048 	Validation Loss: 1.341351 
Epoch: 25 	Accuracy: 0.657994 	Training Loss: 0.238265 	Validation Loss: 1.306570 
Epoch: 30 	Accuracy: 0.690615 	Training Loss: 0.068986 	Validation Loss: 1.543997 
Epoch: 35 	Accuracy: 0.704954 	Training Loss: 0.067206 	Validation Loss: 1.449920 
Epoch: 40 	Accuracy: 0.701166 	Training Loss: 0.064723 	Validation Loss: 1.603106 
Epoch: 45 	Accuracy: 0.701659 	Training Loss: 0.026335 	Validation Loss: 1.774912 
Epoch: 50 	Accuracy: 0.702224 	Training Loss: 0.035350 	Validation Loss: 1.592486 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.447755 	Training Loss: 0.316858 	Testing Loss: 2.025111

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1085, 1780, 886, 1375, 1386]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.475651 	Training Loss: 1.400751 	Validation Loss: 1.289582 
Epoch: 5 	Accuracy: 0.433754 	Training Loss: 1.152300 	Validation Loss: 1.169537 
Epoch: 10 	Accuracy: 0.568957 	Training Loss: 0.794968 	Validation Loss: 0.976486 
Epoch: 15 	Accuracy: 0.590399 	Training Loss: 0.627086 	Validation Loss: 1.023123 
Epoch: 20 	Accuracy: 0.677186 	Training Loss: 0.336080 	Validation Loss: 0.928836 
Epoch: 25 	Accuracy: 0.684724 	Training Loss: 0.146930 	Validation Loss: 1.349216 
Epoch: 30 	Accuracy: 0.693589 	Training Loss: 0.116155 	Validation Loss: 1.297583 
Epoch: 35 	Accuracy: 0.699782 	Training Loss: 0.067542 	Validation Loss: 1.525165 
Epoch: 40 	Accuracy: 0.706870 	Training Loss: 0.060743 	Validation Loss: 1.531195 
Epoch: 45 	Accuracy: 0.697282 	Training Loss: 0.055129 	Validation Loss: 1.394157 
Epoch: 50 	Accuracy: 0.708762 	Training Loss: 0.029877 	Validation Loss: 1.648074 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.457443 	Training Loss: 0.321427 	Testing Loss: 1.699034

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[192, 1029, 879, 1372, 368]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.417025 	Training Loss: 1.345344 	Validation Loss: 1.263731 
Epoch: 5 	Accuracy: 0.612065 	Training Loss: 0.853744 	Validation Loss: 0.920132 
Epoch: 10 	Accuracy: 0.641860 	Training Loss: 0.520053 	Validation Loss: 0.904561 
Epoch: 15 	Accuracy: 0.674475 	Training Loss: 0.308989 	Validation Loss: 1.037507 
Epoch: 20 	Accuracy: 0.677186 	Training Loss: 0.140497 	Validation Loss: 1.328627 
Epoch: 25 	Accuracy: 0.691525 	Training Loss: 0.115287 	Validation Loss: 1.468554 
Epoch: 30 	Accuracy: 0.693153 	Training Loss: 0.066650 	Validation Loss: 1.382518 
Epoch: 35 	Accuracy: 0.693852 	Training Loss: 0.048863 	Validation Loss: 1.608639 
Epoch: 40 	Accuracy: 0.671481 	Training Loss: 0.029282 	Validation Loss: 1.708530 
Epoch: 45 	Accuracy: 0.674858 	Training Loss: 0.029368 	Validation Loss: 1.882182 
Epoch: 50 	Accuracy: 0.671673 	Training Loss: 0.040216 	Validation Loss: 1.786975 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.454203 	Training Loss: 0.317010 	Testing Loss: 1.734506

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1087, 889, 1936, 358, 761]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.465273 	Training Loss: 1.352879 	Validation Loss: 1.266999 
Epoch: 5 	Accuracy: 0.610854 	Training Loss: 0.854022 	Validation Loss: 0.899598 
Epoch: 10 	Accuracy: 0.664116 	Training Loss: 0.514883 	Validation Loss: 0.897254 
Epoch: 15 	Accuracy: 0.678737 	Training Loss: 0.207305 	Validation Loss: 1.185602 
Epoch: 20 	Accuracy: 0.696942 	Training Loss: 0.093702 	Validation Loss: 1.310346 
Epoch: 25 	Accuracy: 0.695313 	Training Loss: 0.069510 	Validation Loss: 1.486462 
Epoch: 30 	Accuracy: 0.707679 	Training Loss: 0.057427 	Validation Loss: 1.282710 
Epoch: 35 	Accuracy: 0.708858 	Training Loss: 0.038497 	Validation Loss: 1.466313 
Epoch: 40 	Accuracy: 0.695993 	Training Loss: 0.027747 	Validation Loss: 1.762556 
Epoch: 45 	Accuracy: 0.711051 	Training Loss: 0.037325 	Validation Loss: 1.392701 
Epoch: 50 	Accuracy: 0.719025 	Training Loss: 0.029565 	Validation Loss: 1.630202 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.492306 	Training Loss: 0.298340 	Testing Loss: 1.839703

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[178, 1022, 1013, 1374, 370]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.250951 	Training Loss: 1.374625 	Validation Loss: 1.386987 
Epoch: 5 	Accuracy: 0.570221 	Training Loss: 0.949364 	Validation Loss: 0.981989 
Epoch: 10 	Accuracy: 0.626860 	Training Loss: 0.710563 	Validation Loss: 0.938099 
Epoch: 15 	Accuracy: 0.631879 	Training Loss: 0.441842 	Validation Loss: 1.000871 
Epoch: 20 	Accuracy: 0.661084 	Training Loss: 0.264406 	Validation Loss: 1.186071 
Epoch: 25 	Accuracy: 0.671673 	Training Loss: 0.144335 	Validation Loss: 1.371652 
Epoch: 30 	Accuracy: 0.672032 	Training Loss: 0.077815 	Validation Loss: 1.581688 
Epoch: 35 	Accuracy: 0.665352 	Training Loss: 0.096166 	Validation Loss: 1.564822 
Epoch: 40 	Accuracy: 0.676429 	Training Loss: 0.052575 	Validation Loss: 1.603694 
Epoch: 45 	Accuracy: 0.659096 	Training Loss: 0.162197 	Validation Loss: 1.226657 
Epoch: 50 	Accuracy: 0.674571 	Training Loss: 0.034018 	Validation Loss: 1.664691 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.464195 	Training Loss: 0.317752 	Testing Loss: 1.804921

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1847, 247, 1505, 1427, 1019]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.332910 	Training Loss: 1.367424 	Validation Loss: 1.334276 
Epoch: 5 	Accuracy: 0.567951 	Training Loss: 0.933861 	Validation Loss: 0.952105 
Epoch: 10 	Accuracy: 0.660500 	Training Loss: 0.571780 	Validation Loss: 0.936854 
Epoch: 15 	Accuracy: 0.694102 	Training Loss: 0.279954 	Validation Loss: 1.022397 
Epoch: 20 	Accuracy: 0.705179 	Training Loss: 0.099442 	Validation Loss: 1.125202 
Epoch: 25 	Accuracy: 0.642051 	Training Loss: 0.241039 	Validation Loss: 1.325779 
Epoch: 30 	Accuracy: 0.708038 	Training Loss: 0.028526 	Validation Loss: 1.308046 
Epoch: 35 	Accuracy: 0.703172 	Training Loss: 0.023433 	Validation Loss: 1.520488 
Epoch: 40 	Accuracy: 0.705237 	Training Loss: 0.036022 	Validation Loss: 1.538958 
Epoch: 45 	Accuracy: 0.706942 	Training Loss: 0.061770 	Validation Loss: 1.166029 
Epoch: 50 	Accuracy: 0.707832 	Training Loss: 0.049176 	Validation Loss: 1.358181 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.452313 	Training Loss: 0.266826 	Testing Loss: 1.840466

***** RESULTS OF GENERATION 1:

	[1087, 889, 1936, 358, 761] - 0.492306
	[178, 1022, 1013, 1374, 370] - 0.464195
	[1097, 1777, 885, 1382, 744] - 0.459195
	[1085, 1780, 886, 1375, 1386] - 0.457443
	[192, 1029, 879, 1372, 368] - 0.454203
	[1847, 247, 1505, 1427, 1019] - 0.452313
	[180, 1785, 1937, 357, 1401] - 0.447755
	[1459, 895, 1011, 1642, 368] - 0.000000
	[1087, 1784, 884, 348, 1392] - 0.000000
	[184, 1020, 1931, 1382, 751] - 0.000000


Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1102, 882, 1004, 1391, 921]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.439947 	Training Loss: 1.421904 	Validation Loss: 1.249062 
Epoch: 5 	Accuracy: 0.545201 	Training Loss: 0.961143 	Validation Loss: 0.985428 
Epoch: 10 	Accuracy: 0.620796 	Training Loss: 0.597422 	Validation Loss: 0.965714 
Epoch: 15 	Accuracy: 0.667698 	Training Loss: 0.277590 	Validation Loss: 1.088385 
Epoch: 20 	Accuracy: 0.676237 	Training Loss: 0.145333 	Validation Loss: 1.328024 
Epoch: 25 	Accuracy: 0.663038 	Training Loss: 0.089923 	Validation Loss: 1.510467 
Epoch: 30 	Accuracy: 0.696262 	Training Loss: 0.096895 	Validation Loss: 1.368753 
Epoch: 35 	Accuracy: 0.695198 	Training Loss: 0.043161 	Validation Loss: 1.614012 
Epoch: 40 	Accuracy: 0.696602 	Training Loss: 0.049494 	Validation Loss: 1.559098 
Epoch: 45 	Accuracy: 0.693910 	Training Loss: 0.035075 	Validation Loss: 1.584132 
Epoch: 50 	Accuracy: 0.700371 	Training Loss: 0.016958 	Validation Loss: 1.650006 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.461642 	Training Loss: 0.289371 	Testing Loss: 1.698722

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1097, 69, 1013, 1386, 770]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.396723 	Training Loss: 1.352212 	Validation Loss: 1.294537 
Epoch: 5 	Accuracy: 0.602276 	Training Loss: 0.933843 	Validation Loss: 0.976925 
Epoch: 10 	Accuracy: 0.637712 	Training Loss: 0.505774 	Validation Loss: 0.957659 
Epoch: 15 	Accuracy: 0.634244 	Training Loss: 0.240175 	Validation Loss: 1.177073 
Epoch: 20 	Accuracy: 0.681616 	Training Loss: 0.094559 	Validation Loss: 1.386538 
Epoch: 25 	Accuracy: 0.685788 	Training Loss: 0.076240 	Validation Loss: 1.306827 
Epoch: 30 	Accuracy: 0.706319 	Training Loss: 0.023546 	Validation Loss: 1.490398 
Epoch: 35 	Accuracy: 0.722306 	Training Loss: 0.017011 	Validation Loss: 1.540918 
Epoch: 40 	Accuracy: 0.702153 	Training Loss: 0.028724 	Validation Loss: 1.579904 
Epoch: 45 	Accuracy: 0.687698 	Training Loss: 0.047072 	Validation Loss: 1.504982 
Epoch: 50 	Accuracy: 0.660097 	Training Loss: 0.271105 	Validation Loss: 0.950142 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.477626 	Training Loss: 0.304636 	Testing Loss: 1.733096

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1087, 887, 1934, 357, 747]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.483702 	Training Loss: 1.364203 	Validation Loss: 1.278206 
Epoch: 5 	Accuracy: 0.570508 	Training Loss: 0.910572 	Validation Loss: 0.947158 
Epoch: 10 	Accuracy: 0.638545 	Training Loss: 0.600716 	Validation Loss: 0.938167 
Epoch: 15 	Accuracy: 0.660179 	Training Loss: 0.302933 	Validation Loss: 1.180376 
Epoch: 20 	Accuracy: 0.667071 	Training Loss: 0.134723 	Validation Loss: 1.477064 
Epoch: 25 	Accuracy: 0.680102 	Training Loss: 0.085183 	Validation Loss: 1.497954 
Epoch: 30 	Accuracy: 0.670366 	Training Loss: 0.090997 	Validation Loss: 1.475724 
Epoch: 35 	Accuracy: 0.676314 	Training Loss: 0.064747 	Validation Loss: 1.770247 
Epoch: 40 	Accuracy: 0.689858 	Training Loss: 0.039841 	Validation Loss: 1.736793 
Epoch: 45 	Accuracy: 0.687526 	Training Loss: 0.048752 	Validation Loss: 1.507319 
Epoch: 50 	Accuracy: 0.689192 	Training Loss: 0.022951 	Validation Loss: 1.721844 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.481627 	Training Loss: 0.314368 	Testing Loss: 1.635318

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1544, 893, 894, 349, 751]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.245989 	Training Loss: 1.397412 	Validation Loss: 1.380609 
Epoch: 5 	Accuracy: 0.557079 	Training Loss: 1.039119 	Validation Loss: 1.004617 
Epoch: 10 	Accuracy: 0.622219 	Training Loss: 0.702537 	Validation Loss: 0.904375 
Epoch: 15 	Accuracy: 0.657071 	Training Loss: 0.355390 	Validation Loss: 1.016166 
Epoch: 20 	Accuracy: 0.677301 	Training Loss: 0.121957 	Validation Loss: 1.442557 
Epoch: 25 	Accuracy: 0.684590 	Training Loss: 0.073043 	Validation Loss: 1.518387 
Epoch: 30 	Accuracy: 0.681673 	Training Loss: 0.062010 	Validation Loss: 1.645602 
Epoch: 35 	Accuracy: 0.689571 	Training Loss: 0.052761 	Validation Loss: 1.639798 
Epoch: 40 	Accuracy: 0.693326 	Training Loss: 0.045394 	Validation Loss: 1.504550 
Epoch: 45 	Accuracy: 0.686237 	Training Loss: 0.029916 	Validation Loss: 1.560157 
Epoch: 50 	Accuracy: 0.680596 	Training Loss: 0.179097 	Validation Loss: 1.100114 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.484935 	Training Loss: 0.270097 	Testing Loss: 1.716864

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[180, 887, 881, 1372, 748]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.381646 	Training Loss: 1.361261 	Validation Loss: 1.304726 
Epoch: 5 	Accuracy: 0.604455 	Training Loss: 0.832224 	Validation Loss: 0.948472 
Epoch: 10 	Accuracy: 0.655763 	Training Loss: 0.491672 	Validation Loss: 1.041806 
Epoch: 15 	Accuracy: 0.691544 	Training Loss: 0.274296 	Validation Loss: 1.065511 
Epoch: 20 	Accuracy: 0.684877 	Training Loss: 0.156271 	Validation Loss: 1.289026 
Epoch: 25 	Accuracy: 0.690615 	Training Loss: 0.111094 	Validation Loss: 1.428037 
Epoch: 30 	Accuracy: 0.684006 	Training Loss: 0.070525 	Validation Loss: 1.555879 
Epoch: 35 	Accuracy: 0.693307 	Training Loss: 0.045132 	Validation Loss: 1.559859 
Epoch: 40 	Accuracy: 0.689006 	Training Loss: 0.048469 	Validation Loss: 1.573709 
Epoch: 45 	Accuracy: 0.699897 	Training Loss: 0.062169 	Validation Loss: 1.357804 
Epoch: 50 	Accuracy: 0.701127 	Training Loss: 0.035612 	Validation Loss: 1.644071 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.467511 	Training Loss: 0.295991 	Testing Loss: 1.649350

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[171, 127, 879, 1390, 370]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.406172 	Training Loss: 1.337239 	Validation Loss: 1.252869 
Epoch: 5 	Accuracy: 0.604033 	Training Loss: 0.995960 	Validation Loss: 0.977490 
Epoch: 10 	Accuracy: 0.639604 	Training Loss: 0.633107 	Validation Loss: 0.875524 
Epoch: 15 	Accuracy: 0.647013 	Training Loss: 0.440124 	Validation Loss: 1.033315 
Epoch: 20 	Accuracy: 0.667282 	Training Loss: 0.236012 	Validation Loss: 1.175047 
Epoch: 25 	Accuracy: 0.671352 	Training Loss: 0.143892 	Validation Loss: 1.445126 
Epoch: 30 	Accuracy: 0.700864 	Training Loss: 0.058010 	Validation Loss: 1.588736 
Epoch: 35 	Accuracy: 0.673359 	Training Loss: 0.053966 	Validation Loss: 1.696484 
Epoch: 40 	Accuracy: 0.654891 	Training Loss: 0.072309 	Validation Loss: 1.719869 
Epoch: 45 	Accuracy: 0.680294 	Training Loss: 0.042586 	Validation Loss: 1.770515 
Epoch: 50 	Accuracy: 0.700294 	Training Loss: 0.028221 	Validation Loss: 1.757804 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.470873 	Training Loss: 0.355324 	Testing Loss: 1.829623

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1295, 1030, 1681, 603, 1328]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.358160 	Training Loss: 1.385142 	Validation Loss: 1.369955 
Epoch: 5 	Accuracy: 0.506068 	Training Loss: 1.134622 	Validation Loss: 1.062660 
Epoch: 10 	Accuracy: 0.638674 	Training Loss: 0.713722 	Validation Loss: 0.879395 
Epoch: 15 	Accuracy: 0.693397 	Training Loss: 0.417196 	Validation Loss: 0.894585 
Epoch: 20 	Accuracy: 0.717377 	Training Loss: 0.200900 	Validation Loss: 1.099585 
Epoch: 25 	Accuracy: 0.721961 	Training Loss: 0.119288 	Validation Loss: 1.213549 
Epoch: 30 	Accuracy: 0.711147 	Training Loss: 0.065538 	Validation Loss: 1.395795 
Epoch: 35 	Accuracy: 0.726717 	Training Loss: 0.042765 	Validation Loss: 1.481951 
Epoch: 40 	Accuracy: 0.719844 	Training Loss: 0.039409 	Validation Loss: 1.570434 
Epoch: 45 	Accuracy: 0.708153 	Training Loss: 0.035659 	Validation Loss: 1.642325 
Epoch: 50 	Accuracy: 0.715352 	Training Loss: 0.024278 	Validation Loss: 1.635619 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.499432 	Training Loss: 0.290008 	Testing Loss: 1.744025

***** RESULTS OF GENERATION 2:

	[1295, 1030, 1681, 603, 1328] - 0.499432
	[1087, 889, 1936, 358, 761] - 0.492306
	[1544, 893, 894, 349, 751] - 0.484935
	[1087, 887, 1934, 357, 747] - 0.481627
	[1097, 69, 1013, 1386, 770] - 0.477626
	[171, 127, 879, 1390, 370] - 0.470873
	[180, 887, 881, 1372, 748] - 0.467511
	[178, 1022, 1013, 1374, 370] - 0.464195
	[1102, 882, 1004, 1391, 921] - 0.461642
	[1097, 1777, 885, 1382, 744] - 0.459195


Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1551, 897, 1928, 357, 759]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.420703 	Training Loss: 1.358716 	Validation Loss: 1.256998 
Epoch: 5 	Accuracy: 0.600418 	Training Loss: 0.912161 	Validation Loss: 0.938053 
Epoch: 10 	Accuracy: 0.679877 	Training Loss: 0.519367 	Validation Loss: 0.846821 
Epoch: 15 	Accuracy: 0.689691 	Training Loss: 0.148497 	Validation Loss: 1.225035 
Epoch: 20 	Accuracy: 0.695730 	Training Loss: 0.114805 	Validation Loss: 1.148325 
Epoch: 25 	Accuracy: 0.664039 	Training Loss: 0.072594 	Validation Loss: 1.799161 
Epoch: 30 	Accuracy: 0.687717 	Training Loss: 0.057600 	Validation Loss: 1.508535 
Epoch: 35 	Accuracy: 0.705404 	Training Loss: 0.026452 	Validation Loss: 1.562780 
Epoch: 40 	Accuracy: 0.709346 	Training Loss: 0.039101 	Validation Loss: 1.560140 
Epoch: 45 	Accuracy: 0.677487 	Training Loss: 0.066481 	Validation Loss: 1.485045 
Epoch: 50 	Accuracy: 0.707454 	Training Loss: 0.030180 	Validation Loss: 1.693058 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.498991 	Training Loss: 0.312550 	Testing Loss: 2.098745

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1087, 1039, 887, 348, 768]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.392499 	Training Loss: 1.363453 	Validation Loss: 1.304034 
Epoch: 5 	Accuracy: 0.609699 	Training Loss: 0.922416 	Validation Loss: 0.955533 
Epoch: 10 	Accuracy: 0.627142 	Training Loss: 0.540748 	Validation Loss: 1.025992 
Epoch: 15 	Accuracy: 0.672737 	Training Loss: 0.259248 	Validation Loss: 1.122732 
Epoch: 20 	Accuracy: 0.689422 	Training Loss: 0.127011 	Validation Loss: 1.378566 
Epoch: 25 	Accuracy: 0.692166 	Training Loss: 0.046833 	Validation Loss: 1.580377 
Epoch: 30 	Accuracy: 0.664020 	Training Loss: 0.045651 	Validation Loss: 1.745688 
Epoch: 35 	Accuracy: 0.680045 	Training Loss: 0.047870 	Validation Loss: 1.692390 
Epoch: 40 	Accuracy: 0.663488 	Training Loss: 0.063455 	Validation Loss: 1.523616 
Epoch: 45 	Accuracy: 0.691659 	Training Loss: 0.025148 	Validation Loss: 1.855321 
Epoch: 50 	Accuracy: 0.695294 	Training Loss: 0.024611 	Validation Loss: 1.866365 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.437198 	Training Loss: 0.315428 	Testing Loss: 2.025062

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1288, 1033, 895, 1395, 993]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.398749 	Training Loss: 1.358911 	Validation Loss: 1.271083 
Epoch: 5 	Accuracy: 0.561361 	Training Loss: 0.965182 	Validation Loss: 0.995961 
Epoch: 10 	Accuracy: 0.662391 	Training Loss: 0.509340 	Validation Loss: 0.875675 
Epoch: 15 	Accuracy: 0.697397 	Training Loss: 0.256086 	Validation Loss: 1.001841 
Epoch: 20 	Accuracy: 0.674077 	Training Loss: 0.108950 	Validation Loss: 1.306518 
Epoch: 25 	Accuracy: 0.688038 	Training Loss: 0.068352 	Validation Loss: 1.428996 
Epoch: 30 	Accuracy: 0.702794 	Training Loss: 0.053360 	Validation Loss: 1.359743 
Epoch: 35 	Accuracy: 0.698115 	Training Loss: 0.035630 	Validation Loss: 1.482389 
Epoch: 40 	Accuracy: 0.704973 	Training Loss: 0.057772 	Validation Loss: 1.305381 
Epoch: 45 	Accuracy: 0.680705 	Training Loss: 0.032571 	Validation Loss: 1.522715 
Epoch: 50 	Accuracy: 0.713441 	Training Loss: 0.016144 	Validation Loss: 1.766421 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.475812 	Training Loss: 0.309391 	Testing Loss: 1.928707

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1085, 1031, 1187, 340, 769]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.370320 	Training Loss: 1.343267 	Validation Loss: 1.284973 
Epoch: 5 	Accuracy: 0.577726 	Training Loss: 0.973642 	Validation Loss: 0.960774 
Epoch: 10 	Accuracy: 0.653622 	Training Loss: 0.639102 	Validation Loss: 0.874267 
Epoch: 15 	Accuracy: 0.687698 	Training Loss: 0.375818 	Validation Loss: 0.907096 
Epoch: 20 	Accuracy: 0.690672 	Training Loss: 0.154068 	Validation Loss: 1.100186 
Epoch: 25 	Accuracy: 0.697320 	Training Loss: 0.077212 	Validation Loss: 1.339073 
Epoch: 30 	Accuracy: 0.687301 	Training Loss: 0.106212 	Validation Loss: 1.346388 
Epoch: 35 	Accuracy: 0.685955 	Training Loss: 0.028287 	Validation Loss: 1.668992 
Epoch: 40 	Accuracy: 0.697320 	Training Loss: 0.095056 	Validation Loss: 1.230193 
Epoch: 45 	Accuracy: 0.669551 	Training Loss: 0.036374 	Validation Loss: 1.751305 
Epoch: 50 	Accuracy: 0.696070 	Training Loss: 0.022882 	Validation Loss: 1.750401 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.477443 	Training Loss: 0.295171 	Testing Loss: 1.662862

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1548, 887, 1941, 339, 1333]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.273168 	Training Loss: 1.384717 	Validation Loss: 1.366963 
Epoch: 5 	Accuracy: 0.554182 	Training Loss: 0.943631 	Validation Loss: 1.024727 
Epoch: 10 	Accuracy: 0.632885 	Training Loss: 0.625753 	Validation Loss: 1.018053 
Epoch: 15 	Accuracy: 0.662147 	Training Loss: 0.344459 	Validation Loss: 1.052433 
Epoch: 20 	Accuracy: 0.685461 	Training Loss: 0.171600 	Validation Loss: 1.216462 
Epoch: 25 	Accuracy: 0.683019 	Training Loss: 0.093433 	Validation Loss: 1.469969 
Epoch: 30 	Accuracy: 0.675955 	Training Loss: 0.075485 	Validation Loss: 1.632707 
Epoch: 35 	Accuracy: 0.700371 	Training Loss: 0.042918 	Validation Loss: 1.695738 
Epoch: 40 	Accuracy: 0.679192 	Training Loss: 0.072805 	Validation Loss: 1.504375 
Epoch: 45 	Accuracy: 0.699461 	Training Loss: 0.030337 	Validation Loss: 1.756420 
Epoch: 50 	Accuracy: 0.724806 	Training Loss: 0.030498 	Validation Loss: 1.600455 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.480873 	Training Loss: 0.292540 	Testing Loss: 1.826082

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1087, 892, 890, 593, 1318]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.440632 	Training Loss: 1.364038 	Validation Loss: 1.306758 
Epoch: 5 	Accuracy: 0.512792 	Training Loss: 1.010885 	Validation Loss: 1.066043 
Epoch: 10 	Accuracy: 0.648397 	Training Loss: 0.668625 	Validation Loss: 0.899373 
Epoch: 15 	Accuracy: 0.681692 	Training Loss: 0.312026 	Validation Loss: 1.030355 
Epoch: 20 	Accuracy: 0.687526 	Training Loss: 0.146077 	Validation Loss: 1.238775 
Epoch: 25 	Accuracy: 0.703460 	Training Loss: 0.071535 	Validation Loss: 1.344080 
Epoch: 30 	Accuracy: 0.690672 	Training Loss: 0.073801 	Validation Loss: 1.356203 
Epoch: 35 	Accuracy: 0.695217 	Training Loss: 0.038790 	Validation Loss: 1.519155 
Epoch: 40 	Accuracy: 0.701942 	Training Loss: 0.043019 	Validation Loss: 1.575525 
Epoch: 45 	Accuracy: 0.696448 	Training Loss: 0.038102 	Validation Loss: 1.418369 
Epoch: 50 	Accuracy: 0.700026 	Training Loss: 0.025873 	Validation Loss: 1.528468 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.432511 	Training Loss: 0.280622 	Testing Loss: 1.930926

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1487, 399, 1734, 577, 1647]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.399166 	Training Loss: 1.358707 	Validation Loss: 1.337731 
Epoch: 5 	Accuracy: 0.567534 	Training Loss: 0.875027 	Validation Loss: 1.004068 
Epoch: 10 	Accuracy: 0.681410 	Training Loss: 0.560278 	Validation Loss: 0.858210 
Epoch: 15 	Accuracy: 0.680897 	Training Loss: 0.226478 	Validation Loss: 1.138470 
Epoch: 20 	Accuracy: 0.691942 	Training Loss: 0.101442 	Validation Loss: 1.287362 
Epoch: 25 	Accuracy: 0.713249 	Training Loss: 0.111088 	Validation Loss: 1.059297 
Epoch: 30 	Accuracy: 0.705275 	Training Loss: 0.051859 	Validation Loss: 1.409453 
Epoch: 35 	Accuracy: 0.718403 	Training Loss: 0.025351 	Validation Loss: 1.436340 
Epoch: 40 	Accuracy: 0.726415 	Training Loss: 0.046433 	Validation Loss: 1.425144 
Epoch: 45 	Accuracy: 0.717967 	Training Loss: 0.037543 	Validation Loss: 1.343290 
Epoch: 50 	Accuracy: 0.698743 	Training Loss: 0.037539 	Validation Loss: 1.636341 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.454943 	Training Loss: 0.300369 	Testing Loss: 1.935405

***** RESULTS OF GENERATION 3:

	[1295, 1030, 1681, 603, 1328] - 0.499432
	[1551, 897, 1928, 357, 759] - 0.498991
	[1087, 889, 1936, 358, 761] - 0.492306
	[1544, 893, 894, 349, 751] - 0.484935
	[1548, 887, 1941, 339, 1333] - 0.480873
	[1085, 1031, 1187, 340, 769] - 0.477443
	[1288, 1033, 895, 1395, 993] - 0.475812
	[1487, 399, 1734, 577, 1647] - 0.454943
	[1087, 1039, 887, 348, 768] - 0.437198
	[1087, 892, 890, 593, 1318] - 0.432511


Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1553, 895, 1936, 593, 1116]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.446844 	Training Loss: 1.376746 	Validation Loss: 1.319282 
Epoch: 5 	Accuracy: 0.560111 	Training Loss: 0.873901 	Validation Loss: 0.993356 
Epoch: 10 	Accuracy: 0.612539 	Training Loss: 0.513472 	Validation Loss: 1.072360 
Epoch: 15 	Accuracy: 0.653718 	Training Loss: 0.230380 	Validation Loss: 1.177802 
Epoch: 20 	Accuracy: 0.652506 	Training Loss: 0.148822 	Validation Loss: 1.401962 
Epoch: 25 	Accuracy: 0.658565 	Training Loss: 0.077902 	Validation Loss: 1.587673 
Epoch: 30 	Accuracy: 0.674595 	Training Loss: 0.056311 	Validation Loss: 1.560531 
Epoch: 35 	Accuracy: 0.655610 	Training Loss: 0.037995 	Validation Loss: 1.827248 
Epoch: 40 	Accuracy: 0.676865 	Training Loss: 0.047125 	Validation Loss: 1.631468 
Epoch: 45 	Accuracy: 0.692018 	Training Loss: 0.030538 	Validation Loss: 1.798531 
Epoch: 50 	Accuracy: 0.671237 	Training Loss: 0.035501 	Validation Loss: 1.681318 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.498190 	Training Loss: 0.280496 	Testing Loss: 1.630518

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1549, 1024, 1924, 366, 1331]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.439697 	Training Loss: 1.379134 	Validation Loss: 1.328983 
Epoch: 5 	Accuracy: 0.552342 	Training Loss: 0.874997 	Validation Loss: 0.965524 
Epoch: 10 	Accuracy: 0.617142 	Training Loss: 0.547230 	Validation Loss: 1.034288 
Epoch: 15 	Accuracy: 0.681827 	Training Loss: 0.314424 	Validation Loss: 1.022626 
Epoch: 20 	Accuracy: 0.677717 	Training Loss: 0.098887 	Validation Loss: 1.450492 
Epoch: 25 	Accuracy: 0.679154 	Training Loss: 0.100736 	Validation Loss: 1.396980 
Epoch: 30 	Accuracy: 0.689935 	Training Loss: 0.054909 	Validation Loss: 1.590895 
Epoch: 35 	Accuracy: 0.683570 	Training Loss: 0.058662 	Validation Loss: 1.491521 
Epoch: 40 	Accuracy: 0.689705 	Training Loss: 0.043150 	Validation Loss: 1.403414 
Epoch: 45 	Accuracy: 0.677770 	Training Loss: 0.020775 	Validation Loss: 1.820212 
Epoch: 50 	Accuracy: 0.688833 	Training Loss: 0.030542 	Validation Loss: 1.573186 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.464881 	Training Loss: 0.303442 	Testing Loss: 2.037451

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1297, 1022, 1926, 613, 757]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.423979 	Training Loss: 1.359905 	Validation Loss: 1.290388 
Epoch: 5 	Accuracy: 0.571533 	Training Loss: 0.920071 	Validation Loss: 0.989582 
Epoch: 10 	Accuracy: 0.679686 	Training Loss: 0.519878 	Validation Loss: 0.883177 
Epoch: 15 	Accuracy: 0.546887 	Training Loss: 0.259682 	Validation Loss: 2.206376 
Epoch: 20 	Accuracy: 0.686070 	Training Loss: 0.087307 	Validation Loss: 1.562171 
Epoch: 25 	Accuracy: 0.685237 	Training Loss: 0.057837 	Validation Loss: 1.558474 
Epoch: 30 	Accuracy: 0.709102 	Training Loss: 0.046240 	Validation Loss: 1.492450 
Epoch: 35 	Accuracy: 0.692621 	Training Loss: 0.049262 	Validation Loss: 1.556075 
Epoch: 40 	Accuracy: 0.695045 	Training Loss: 0.043998 	Validation Loss: 1.471450 
Epoch: 45 	Accuracy: 0.678340 	Training Loss: 0.037996 	Validation Loss: 1.828301 
Epoch: 50 	Accuracy: 0.712153 	Training Loss: 0.035487 	Validation Loss: 1.592572 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.450316 	Training Loss: 0.307548 	Testing Loss: 1.760508

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1297, 891, 1930, 367, 759]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.379788 	Training Loss: 1.387455 	Validation Loss: 1.254104 
Epoch: 5 	Accuracy: 0.525111 	Training Loss: 1.002734 	Validation Loss: 1.053573 
Epoch: 10 	Accuracy: 0.601988 	Training Loss: 0.632534 	Validation Loss: 0.938618 
Epoch: 15 	Accuracy: 0.674211 	Training Loss: 0.312506 	Validation Loss: 1.030387 
Epoch: 20 	Accuracy: 0.665519 	Training Loss: 0.209155 	Validation Loss: 1.314348 
Epoch: 25 	Accuracy: 0.679096 	Training Loss: 0.084540 	Validation Loss: 1.495281 
Epoch: 30 	Accuracy: 0.681218 	Training Loss: 0.099484 	Validation Loss: 1.458597 
Epoch: 35 	Accuracy: 0.675346 	Training Loss: 0.058572 	Validation Loss: 1.665022 
Epoch: 40 	Accuracy: 0.690481 	Training Loss: 0.042887 	Validation Loss: 1.496069 
Epoch: 45 	Accuracy: 0.686711 	Training Loss: 0.039158 	Validation Loss: 1.707301 
Epoch: 50 	Accuracy: 0.691563 	Training Loss: 0.027506 	Validation Loss: 1.710188 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.455758 	Training Loss: 0.297561 	Testing Loss: 2.091434

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1090, 885, 1137, 359, 1338]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.319994 	Training Loss: 1.367280 	Validation Loss: 1.342763 
Epoch: 5 	Accuracy: 0.599450 	Training Loss: 0.893237 	Validation Loss: 0.936182 
Epoch: 10 	Accuracy: 0.602899 	Training Loss: 0.529495 	Validation Loss: 1.055094 
Epoch: 15 	Accuracy: 0.645135 	Training Loss: 0.289135 	Validation Loss: 1.232644 
Epoch: 20 	Accuracy: 0.691903 	Training Loss: 0.122142 	Validation Loss: 1.206372 
Epoch: 25 	Accuracy: 0.692660 	Training Loss: 0.085591 	Validation Loss: 1.461548 
Epoch: 30 	Accuracy: 0.710256 	Training Loss: 0.059712 	Validation Loss: 1.228005 
Epoch: 35 	Accuracy: 0.701262 	Training Loss: 0.039022 	Validation Loss: 1.475814 
Epoch: 40 	Accuracy: 0.699877 	Training Loss: 0.039748 	Validation Loss: 1.512110 
Epoch: 45 	Accuracy: 0.709743 	Training Loss: 0.032064 	Validation Loss: 1.355857 
Epoch: 50 	Accuracy: 0.718005 	Training Loss: 0.026340 	Validation Loss: 1.459104 
Training... (13/13)
Testing... (1/4)
Testing... (2/4)
Testing... (3/4)
Testing... (4/4)
Final Results:	Accuracy: 0.452701 	Training Loss: 0.289087 	Testing Loss: 1.657247

Loss Function: NLLLoss 	Number of Epochs: 50 	Batch Size: 800 	Validation Percent: 0.2
Images resized to 30x40px.
Layers: 	[1289, 901, 1203, 360, 749]
Beginning setup...
Setting up train, test, and validation sets...
Full train set size:  9957
Train set size:  7966
Validation set size:  1991
Test set size:  2487
Training... (10/10)
Validating... (1/3)
Validating... (2/3)
Validating... (3/3)
Epoch: 1 	Accuracy: 0.473965 	Training Loss: 1.358741 	Validation Loss: 1.283877 
```
