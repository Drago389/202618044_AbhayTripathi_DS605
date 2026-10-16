# DS605 Lab 7: Image Representation, PCA, Eigenfaces and Face Recognition

## Objective
Represent images numerically, reduce dimensionality using manual NumPy PCA/Eigenfaces, perform face matching in the reduced space, and compare similarities with traditional machine-learning classifiers using the AT&T Database of Faces (ORL) dataset.

## Structure
* **Part A:** Image Representation (Grayscale flattening, stratifed train-test split).
* **Part B:** PCA & Eigenfaces (Manual NumPy SVD, cumulative variance, 90% retention, face reconstruction).
* **Part C:** Recognition in PCA Space (Similarity matching via Euclidean distance).
* **Part D:** Traditional Machine Learning (KNN, SVM, Logistic Regression on PCA features).

## Requirements
* `numpy`
* `matplotlib`
* `pillow` (for image loading)
* `scikit-learn` (for ML models and train_test_split only; **PCA is calculated manually**)

## Instructions
1. Download the AT&T ORL face dataset. Extract it into a folder named `ORL_Faces` in the root directory.
2. Run the Jupyter Notebook `Lab7_Face_Recognition.ipynb` to view outputs, variance plots, and eigenface visualizations.

## Observations & Results

### Variance, Dimensionality Reduction, and Storage
* **Components Retained:** 95 principal components were required to preserve 90% of the variance.
* **Covariance vs. SVD:** The maximum eigenvector difference between the covariance method and SVD was 14.422205.
* **Storage Compression:** 
  * Original storage: 3,091,200 floats
  * Reduced storage: 28,500 floats
  * **Compression Ratio:** 108.46x

### Recognition Accuracy Comparison
Dimensionality reduction not only drastically reduced storage but also filtered out noise, leading to improved performance in the reduced feature space compared to raw pixels.

| Model / Approach | Accuracy |
| :--- | :--- |
| **Raw Pixel Nearest Neighbor** | 96.00% |
| **PCA Similarity (Custom Euclidean NN)** | 97.00% |
| **KNN (k=3)** | 97.00% |
| **Logistic Regression** | 98.00% |
| **SVM (RBF Kernel)** | 98.00% |

### Conclusion
By projecting the faces into the PCA space using 95 components, the dataset was compressed by over 108 times without losing critical facial structures. This dimensionality reduction successfully acts as a noise filter, evidenced by the similarity baseline accuracy improving from 96% (raw pixels) to 97% (PCA space). More sophisticated ML models like Logistic Regression and SVM (RBF) achieved the highest performance at 98% accuracy on the reduced dataset
