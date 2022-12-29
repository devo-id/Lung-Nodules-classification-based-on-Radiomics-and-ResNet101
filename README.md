# Lung Nodules classification based on Radiomics and ResNet101 features
## Description
Lung cancer is the second most common cancer in both men and women that afflicts 225,500 people a year in the United States. Nearly 1 out of 4 cancer deaths are from lung cancer, more than colon, breast, and prostate cancers combined. Early detection of the cancer can allow for early treatment which significantly increases the chances of survival. 
This project creates an algorithm that automatically detects candidate nodules and predicts the probability that the lung will be diagnosed with cancer within 1 year of the CT scans. This project aims to 
* Extracting quantitative, hand-crafted radiomics features from lung CT 3D images. 
* Extracting features of same data using pre-trained deep CNN model (ResNet101).
* To train machine learning classification model to verify the performance based on extracted features separately and also by concatenating these features for the classification of Lung Cancer.
* Analysis of the respective results.



## Installation
### Required packages
* anaconda3
* Python 
* Tensorflow
* Keras
* dicom
* h5py \
and many more in requirements.txt in all folders

### Required Data
[**LIDC-IDRI dataset**](https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI)
* Images and their segmentations (DICOM)
* DICOM Metadata Digest (CSV)
* Nodule Size List

**Readme files holds the links for the datasets**



## The pipeline
1.	**Preprocess LIDC**
    * **Inputs:** LIDC dataset, list3_2.csv, LIDC-IDRI_MetaData.csv
	* **Outputs:** 3D images with their segmentations in NRRD format, that we are storing in ***0 Data*** Folder.
2.	**Radiomics**
	* **Inputs:** ***0 Data*** Folder
	* **Outputs:** RadiomicsFeatures.csv
3.	**ResNet101** \
    **FineTuniningModel**
    * **Inputs:** Dataset described in ***3 ResNet101/FineTuniningModel/readme.md***
    * **Outputs:** fineTuneResNet101.h5  
        
    **SegmentImageExt.ipynb**
    * **Inputs:** **0 Data** folder
    * **Outputs:** ***CroppedImageData*** folder
    
    **ResNetFeatures.ipynb**
    * **Inputs:** ***CroppedImageData*** folder, fineTuneResNet101.h5
    * **Outputs:** ResnetFeatures.csv

4.	**Results** \
    SVM classifier \
    ***svm_combine.ipynb***
    * **Inputs:** ResnetFeatures.csv, RadiomicsFeatures.csv

    ***svm_radiomics.ipynb***
    * **Input:** RadiomicsFeatures.csv

    ***svm_Resnet.ipynb***
    * **Input:** ResnetFeatures.csv


Refer respective readme file for better understanding

## Results

| Features | Accuracy |
|:---|:---:|
| Radiomics | 86.21% |
| ResNet101 | 70.69% |
| Features combined | 89.66% |


## Reference

[
Artificial intelligence in cancer imaging: Clinical challenges and applications
](https://pubmed.ncbi.nlm.nih.gov/30720861/)

[
Radiomic features analysis in computed tomography images of lung nodule classification
](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5798832/)

[
Improving the Prediction of Benign or Malignant Breast Masses Using a Combination of Image Biomarkers and Clinical Parameters
](https://pubmed.ncbi.nlm.nih.gov/33828982/)

[
Radiomics: extracting more information from medical images using advanced feature analysis
](https://pubmed.ncbi.nlm.nih.gov/22257792/)


[A survey of transfer learning
](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-016-0043-6)


[
Can radiomics features be reproducibly measured from CBCT images for patients with non-small cell lung cancer?
](https://pubmed.ncbi.nlm.nih.gov/26632036/#:~:text=Purpose%3A%20Increasing%20evidence%20suggests%20radiomics,cell%20lung%20cancer%20(NSCLC).)

[Radiomics and deep learning in lung cancer
](https://pubmed.ncbi.nlm.nih.gov/32367456/)

[
The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans
](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041807/)


