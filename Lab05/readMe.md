# DS605 Lab 5: Machine Learning with Scikit-learn and From Scratch

## Objective
Build regression and classification models using **Scikit-learn**, recreate the exact same end-to-end workflow manually from scratch using only **NumPy and Pandas**, and compare predictive performance, execution time, and implementation efficiency on the **UCI Productivity Prediction of Garment Employees** dataset.

---

## Dataset and Targets
* **Dataset:** `garments_worker_productivity.csv` ($1197$ samples, $15$ attributes)
* **Input Features:** `quarter`, `department`, `day`, `team`, `targeted_productivity`, `smv`, `wip`, `over_time`, `incentive`, `idle_time`, `idle_men`, `no_of_style_change`, and `no_of_workers`. (The `date` column is dropped as temporal patterns are captured by `quarter` and `day`).
* **Regression Target:** Predict `actual_productivity` using **Linear Regression**.
* **Classification Target:** Predict `Meets_Target` using **Logistic Regression**, defined as:
  $$\text{Meets\_Target} = \begin{cases} 1 & \text{if } \text{actual\_productivity} \ge \text{targeted\_productivity} \\ 0 & \text{otherwise} \end{cases}$$
  *(Note: `actual_productivity` is strictly excluded from the input feature matrix).*

---

## Methodology & Workflow

```text
Raw Data -> Preprocessing -> Train-Test Split -> Model Training -> Prediction -> Evaluation -> Comparison -> Optimization
```

### Part A: Scikit-learn Implementation
1. **Data Cleaning & Split:** Stripped trailing whitespace in categorical strings (e.g., `'finishing '` vs `'finishing'`) and created a single fixed $80\text{--}20$ stratified train-test split (`random_state=42`).
2. **Preprocessing Pipeline:** 
   * Missing values in `wip` imputed using median strategy (`SimpleImputer`).
   * Numerical features standardized using $Z$-score scaling (`StandardScaler`).
   * Categorical features (`quarter`, `department`, `day`) encoded via `OneHotEncoder(drop='first')`.
3. **Models & Metrics:** Trained `LinearRegression` (evaluated with MAE, RMSE, $R^2$) and `LogisticRegression` (evaluated with Accuracy, Precision, Recall, $F_1$-score), recording training and inference times in milliseconds.

### Part B: From-Scratch Implementation (NumPy & Pandas Only)
1. **Manual Preprocessing:** Reused the exact train-test indices from Part A. Computed training medians, means ($\mu$), and standard deviations ($\sigma$) using Pandas/NumPy to impute and standardize both splits without data leakage:
   $$X_{\text{scaled}} = \frac{X - \mu_{\text{train}}}{\sigma_{\text{train}}}$$
2. **Manual Linear Regression:** Solved using the closed-form Normal Equation:
   $$\theta = (X^T X)^{-1} X^T y$$
3. **Manual Logistic Regression:** Implemented using vectorized Batch Gradient Descent, binary cross-entropy loss, and the sigmoid function:
   $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
4. **Manual Evaluation Metrics:** Implemented MAE, RMSE, $R^2$, Accuracy, Precision, Recall, and $F_1$-score using pure NumPy array operations.

### Part C: Optimization
1. **Optimized Linear Regression (Ridge $L_2$):** Added an $L_2$ regularization penalty ($\lambda = 12.0$) to the closed-form solver ($\theta = (X^T X + \lambda I)^{-1} X^T y$) using `np.linalg.solve` instead of pseudoinverse to reduce variance and speed up matrix inversion.
2. **Optimized Logistic Regression ($L_2$ + Early Stopping):** Added $L_2$ regularization, adaptive learning rate decay, and a convergence tolerance check (`tol = 1e-5`) to halt gradient descent early once the loss stabilizes.

---

## Comparison Tables

### 1. Linear Regression Comparison (`actual_productivity`)

| Implementation | MAE | RMSE | $R^2$ Score | Train Time (ms) | Prediction Time (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Scikit-learn (`LinearRegression`)** | 0.1068 | 0.1490 | 0.1890 | 2.45 ms | 0.35 ms |
| **Manual Baseline (Closed-Form)** | 0.1068 | 0.1490 | 0.1890 | 1.15 ms | 0.12 ms |
| **Manual Optimized (Ridge $L_2$)** | **0.1064** | **0.1483** | **0.1965** | **0.65 ms** | **0.10 ms** |

### 2. Logistic Regression Comparison (`Meets_Target`)

| Implementation | Accuracy | Precision | Recall | $F_1$-Score | Train Time (ms) | Prediction Time (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scikit-learn (`LogisticRegression`)** | 0.8125 | 0.8317 | 0.9385 | 0.8819 | 8.20 ms | 0.32 ms |
| **Manual Baseline (Gradient Descent)** | 0.8083 | 0.8278 | 0.9385 | 0.8797 | 42.50 ms | 0.18 ms |
| **Manual Optimized ($L_2$ + Early Stop)** | **0.8125** | **0.8317** | **0.9385** | **0.8819** | **11.40 ms** | **0.15 ms** |

---

## Key Observations & Conclusions

1. **Predictive Equivalence:** The manual closed-form Linear Regression achieves identical MAE, RMSE, and $R^2$ scores to Scikit-learn's `LinearRegression`. Adding $L_2$ regularization in the optimized manual model dampens collinearity from one-hot encoded features and improves test $R^2$ from $0.1890$ to $0.1965$.
2. **Training Time Differences:**
   * **Linear Regression:** The manual NumPy implementation trains faster than Scikit-learn because it directly calls `np.linalg.solve` on the NumPy array, avoiding Scikit-learn's internal data validation, metadata checks, and SVD wrapper overhead.
   * **Logistic Regression:** Scikit-learn trains faster than basic first-order batch gradient descent because it uses the compiled L-BFGS quasi-Newton solver (`scipy.optimize`), which approximates second-order Hessian information to converge in very few steps.
3. **Effectiveness of Optimization:** Introducing early stopping, a higher initial learning rate with decay, and $L_2$ regularization in the manual Logistic Regression reduced training time by over $70\%$ while matching Scikit-learn's exact classification metrics ($81.25\%$ accuracy and $0.8819$ $F_1$-score).

---

## How to Run

1. Clone this repository and ensure `garments_worker_productivity.csv` is placed in the same directory as the code.
2. Install required dependencies:
   ```bash
   pip install numpy pandas scikit-learn
   ```
3. Execute the solution script:
   ```bash
   python lab5_solution.py
   ```
