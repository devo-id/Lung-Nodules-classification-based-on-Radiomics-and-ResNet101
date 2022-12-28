First we tune the ResNet101 model for better perfomance. Check FineTuningModel Folder.
After that, Run the segmentImageExt.ipynb
## segmentImageExt.ipynb
This program will parse the image and its different segments and saves the slices for each segment in separate folder.

### Requirements
All requirements are given in ```requirements.txt```

### Input
```
0 Data folder
```

### Output
```
This script will create CroppedImageData folder having jpgs of all the segmentations.
```

Now we are ready with cropped (ROI) data and finetuned model. Now we calculate features from these images in ResNetFeatures.ipynb

## ResNetFeatures.ipynb
This program will calculate the radiomics features from different segment images.
### Input
```
CroppedImageData Folder
```

### Output
```
Feature will get saved in ResnetFeatures.csv
```
