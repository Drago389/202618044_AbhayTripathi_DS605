## 🛠️ Tasks Breakdown

### Part A - Data Loading and Preprocessing with Scikit-Learn

#### Task 1 - Load and Understand the Dataset
- Loaded `hotel_bookings.csv` (119,390 rows, 32 columns).
- Examined the class distribution of the target variable `is_canceled` (~37% canceled, ~63% not canceled).
- Separated features (`X`) from the target (`y`) and grouped features into numerical and categorical lists.

#### Task 2 - Missing Values, Leakage, and Outliers
- **Missing Values:** Identified `company` (94% missing), `agent` (16% missing), and `country` (<1% missing).
- **Leakage Prevention:** Dropped `reservation_status` and `reservation_status_date` as they directly reveal the outcome of the booking. Dropped `company` due to extreme missingness.
- **Outliers:** Visualized numerical features with boxplots. Removed extreme outliers using a conservative `3.0 * IQR` multiplier on key continuous variables (e.g., `adr`, `lead_time`) to clean the data without losing valid high-value bookings.

#### Task 3 - Create Two Preprocessing Pipelines
Split the data using `train_test_split` (80/20 split, stratified). Constructed two robust Scikit-learn `ColumnTransformer` pipelines:
- **Pipeline A:** `KNNImputer` (n=5) + `StandardScaler` for numerical features.
- **Pipeline B:** `KNNImputer` (n=5) + `MinMaxScaler` for numerical features.
- Both pipelines applied `SimpleImputer(strategy='most_frequent')` + `OneHotEncoder(handle_unknown='ignore')` to categorical features.

- ### Part B - Model Training and Performance Evaluation

#### Task 4 - Train Two Classification Models
Trained four distinct model-pipeline combinations using the same train-test splits:
1. `LogisticRegression` + `StandardScaler`
2. `LogisticRegression` + `MinMaxScaler`
3. `DecisionTreeClassifier` + `StandardScaler`
4. `DecisionTreeClassifier` + `MinMaxScaler`

#### Task 5 - Evaluate and Compare
- Extracted Training and Testing Accuracy, Precision, Recall, and F1-Score for all four experiments.
- Generated and plotted Confusion Matrices for the best Logistic Regression and best Decision Tree models to analyze false positives and false negatives.

#### Task 6 - Final Observations
1. **Best Overall:** The Decision Tree achieves higher test accuracy and F1-scores due to its ability to capture non-linear relationships.
2. **Overfitting:** The Decision Tree suffers from severe overfitting (Training Accuracy ~99%, Test Accuracy ~80-85%). Logistic Regression is much more stable and generalizes well with almost no train-test gap.
3. **Scaling Impact on Logistic Regression:** Scaling alters Logistic Regression coefficients. `StandardScaler` slightly outperforms `MinMaxScaler` as it centers data perfectly for gradient descent.
4. **Scaling Impact on Decision Trees:** Scaling methods (Standard vs. MinMax) have **zero effect** on the Decision Tree. Tree-based models are scale-invariant, yielding identical precision, recall, and accuracy scores across both pipelines.
