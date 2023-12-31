# Median Filtering Forensics Based on Convolutional Neural Network
This GitHub project presents a CNN-based model for detecting median filtering in images based on the [study](https://ieeexplore.ieee.org/document/7113799) done by Jiansheng Chen, Xiangui Kang, Ye Liu, Z. Jane Wang. I used the [UCID Dataset](https://www.researchgate.net/publication/220979862_UCID_An_uncompressed_color_image_database) for training the model.
The study aims to detect the tempering process on image documents done by forgery makers using median filtering.

# Overview
This project follows the following steps
- Images from the UCID Dataset are used as a negative dataset ($8028$ images) and median filtered images of the same dataset are used as a positive dataset ($5352$ images).
- jpeg compressed images of the same dataset are also included in the positive dataset ($8028$ images).
- jpeg compressed images of median filtered images are included in the negative dataset ($5352$ images).
- Median filtered images of jpeg compressed images are included in the negative dataset ($5352$ images).
- A total $16056$ for each class is used to train the model.
- The MFR layer is applied to each image as the requirement for the model.
- Define and train the model for classification.
- Results are computed for the whole UCID Dataset and compared with the [classical approach](https://github.com/mkreman/Forensic-Detection-of-Median-Filtering-in-Digital-Images-Cao_2010.git).
- CNN based approach is found to be $99.00\\%$ accurate on the test dataset.

# Data Preparing
The UCID Dataset is processed in the following manner
- Images are converted in grayscale and cropped into the size $64 \times 64$
 and converted into lossless *png* format.
- From one image, six images of size $64\times64$ are extracted along the principal diagonal.
- The UCID dataset is considered as negative images (original uncompressed images in PNG format and jpeg compressed image) for the model.
- Positive images are created by applying $5\times5$ median filtering on the same dataset images.
- Thus, the dataset consisting of $32112$ images is prepared with 2 classes.
- MFR layer is applied on each image, where the image is subtracted from a $5\times5$ median filtered image of itself.

# Model Architecture
Since using conventional CNN models with the raw image pixels as inputs
didn’t yield good performances, one additional layer, *the filter
layer* is added to the conventional model.

Through this filter layer, ***the median filtering residual (MFR)*** of an image
is obtained. Then the output MFR is fed into the conventional
network.

The MFR is defined as follows: Applying the $w\times w$ median
filtering window on a image $x(i,j)$ and obtain the output
image $y(i,j)$. 

The MFR is:
$$d(i,j)=med_w(x(i,j))-x(i,j)$$

# Results
For classification between original and median filtered images, the model gives $99.43\\%$ on the training dataset, $99.00\\%$ on the validation dataset and $99.00\\%$ on the test dataset.

For classification between jpeg and median filtered jpeg images, the model gives $99.84\\%$ on the training dataset and $99.55\\%$ on the validation dataset and $99.35\\%$ on the test dataset.

For classification between jpeg and jpeg compressed images of $5\times 5$ median filtered images, the model gives $99.40\\%$ on the whole UCID dataset. In compression, the [classical approach](https://github.com/mkreman/Forensic-Detection-of-Median-Filtering-in-Digital-Images-Cao_2010.git) yields $72.24\\%$.
# Conclusion
CNN-based model is better than [classical approach](https://github.com/mkreman/Forensic-Detection-of-Median-Filtering-in-Digital-Images-Cao_2010.git) and can detect median filtering in small and jpeg compressed image blocks and is able to identify cut-and-paste forgeries well.