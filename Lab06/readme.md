# Lab 6: Feature Extraction and Machine Learning - Observations & Results[cite: 1]

This README outlines the key observations and findings after successfully solving **Lab 6: Feature Extraction and Machine Learning with Image and Text Data**[cite: 1].

---

## 📊 Summary of Datasets
* **Image Dataset**: Asphalt Crack Dataset (400 images from Mendeley Data)[cite: 1].
* **Text Dataset**: Email Spam Classification Dataset (5.172 emails from Kaggle)[cite: 1].

---

## 🔍 Key Observations & Findings

### 1. Part A: Image Feature Extraction & Traditional Classification
* **Handcrafted Feature Limitations**: Utilizing NumPy and OpenCV to derive statistical properties (mean brightness, contrast, dark/bright pixel ratios) and Canny edge metrics (edge count and density) successfully bypassed the need for heavy CNNs[cite: 1]. However, these hand-crafted features are inherently sensitive to surface illumination inconsistencies and shadow variations in asphalt images.
* **Classifier Performance**: Traditional machine learning classifiers (e.g., Logistic Regression, SVM) performed well on images with high-contrast, well-defined cracks, but struggled to separate classes when cracks shared visual textures with rough non-crack backgrounds.
* **Computational Efficiency**: Feature extraction time per image was extremely low, making training times for traditional models a fraction of what deep learning approaches typically require.

### 2. Part B: Text Vectorization & Spam Classification
* **CountVectorizer vs. TF-IDF**: 
  * `CountVectorizer` efficiently captures word frequencies, resulting in fast training times, but can overemphasize frequently occurring words that carry little semantic value for spam detection.
  * `TF-IDF Vectorizer` consistently yielded superior precision and F1-scores by down-weighting common terms and scaling up the importance of rare, discriminative words unique to spam emails.
* **Dimensionality**: Both vectorizers generated massive sparse matrices, requiring careful vocabulary restriction (`max_features`) to balance memory consumption and classification accuracy.

### 3. Part C: Representation Improvement & Trade-offs
* **Impact of N-grams**: Introducing bigrams alongside unigrams (`ngram_range=(1, 2)`) during text vectorization successfully captured multi-word phrases (e.g., identifying spam phrases like "click here" or "free money").
* **Trade-off Analysis**: 
  * *Performance vs. Computation*: Enhancing the feature space with n-grams improved classification accuracy and recall, but noticeably increased feature dimensionality and model training time.
  * *Tuning Parameters*: Adjusting Canny edge detection thresholds (`threshold1` and `threshold2`) for Part A[cite: 1] heavily influenced edge density statistics, proving that edge-based features depend heavily on hyperparameter tuning to filter out background asphalt grain noise.

---

## 🚀 Conclusion
The workflow demonstrated that traditional machine learning pipelines combined with intelligent feature engineering (NumPy/OpenCV statistics for images[cite: 1] and TF-IDF/N-grams for text) can achieve competitive performance on small-to-medium classification tasks while maintaining high interpretability and minimal computational resource overhead.
