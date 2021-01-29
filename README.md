# Salt_identification
TGS Salt Identification challenge

# Kaggle Problem statement:
* Several areas of Earth with large accumulations of oil and gas also have huge deposits of salt below the surface.

But unfortunately, knowing where large salt deposits are precisely is very difficult. Professional seismic imaging still requires expert human interpretation of salt bodies. This leads to very subjective, highly variable renderings. More alarmingly, it leads to potentially dangerous situations for oil and gas company drillers.

To create the most accurate seismic images and 3D renderings, TGS (the world’s leading geoscience data company) is hoping Kaggle’s machine learning community will be able to build an algorithm that automatically and accurately identifies if a subsurface target is salt or not.

# Approach :

● Framework : tf.keras API
● Deployment: AWS, Heroku
● Fronend : HTML
● Backend: Flask, Python
 
 
## Training Related Configuration:
*  Model Architecture : Unet
*  Loss function : Binary cross entropy
*  Evaluation Metric : IOU (Intersection Over Union)
*  Optimizer : Adam
*  Augmentation : leftright

## Kaggle Late Submission Scores: 
* **Public Score** : 0.79
* **Private Score** : 0.815

# Deployment
* Please view [Project report](https://github.com/sumittagadiya/Salt_identification/blob/main/project_report/TGS_SALT_detection_project_report.pdf) for more detail information about my approaches and difficuties which i had faced during this project.

* I have deployed TGS Salt Identification Challenge on AWS EC2 instance and also on Heroku platform.
* You can find AWS deployment link [here](http://ec2-34-227-25-161.compute-1.amazonaws.com:8080/)
* Heroku deploymeny link is [here](https://salt-detection.herokuapp.com/)

# How it works ??
1. First of all download test seismic images from [here](https://github.com/sumittagadiya/Salt_identification/tree/main/test_images)
2. Open any of the above link and then click on choose file and upload any seismic image which you have downloaded.
3. Click on predict button and boooooom !!!. You will get Original uploaded siesmic image and correspoding segmented image by which you can observ that white part is salt area and black part is normal area.


# **Note**: 
1. You may face security related error while loading AWS link. So please try to open it in incognito mode.

2. Heroku link may take some time to load because of limited memory(526 MB) size in free version of heroku so please wait for some time to get it works.
