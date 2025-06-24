# Recommender System (CCS360)


---

# 📚 UNIT I – INTRODUCTION TO RECOMMENDER SYSTEMS

**diagram: true**
**Google search:** `taxonomy of recommender systems chart`

---

## 🔶 1. INTRODUCTION TO RECOMMENDER SYSTEMS

### ▶️ What is a Recommender System?

A **Recommender System (RS)** is an intelligent software tool designed to **suggest items** to users based on their:

* Past behavior (clicks, purchases, ratings)
* Profile information (age, location, interests)
* Preferences or interactions of similar users

### ▶️ Key Objectives of RS:

* **Personalize** user experience
* **Reduce information overload**
* **Improve engagement & conversions**
* **Drive content discovery**

### ▶️ Applications:

| Platform  | Recommendations Offered               |
| --------- | ------------------------------------- |
| Netflix   | Movies & TV shows                     |
| Amazon    | Products, accessories                 |
| Spotify   | Music and playlists                   |
| YouTube   | Videos, Shorts                        |
| Instagram | Reels, accounts, hashtags             |
| LinkedIn  | Jobs, posts, professional connections |

---

## 🔶 2. BASIC TAXONOMY OF RECOMMENDER SYSTEMS

**diagram: true**
**Google search:** `types of recommender systems diagram`

### ▶️ 2.1 Content-Based Filtering (CBF)

* Uses **item features** (genre, category, tags) to find similar items
* Recommendations are based on what the **user liked in the past**

**How it works:**

* Creates an **item profile** (e.g., a movie = Action, Sci-fi, 2015)
* Builds a **user profile** by aggregating liked items
* Recommends items that match this user profile

**Example:**

> If you liked “Iron Man,” RS recommends “Avengers,” “Captain America”

---

### ▶️ 2.2 Collaborative Filtering (CF)

* Based on the idea: **“users who liked similar things in the past will like similar things in the future”**
* Works purely on **user-item interaction data** (ratings, views)

**Types of CF:**

* **User-Based CF**: Finds users similar to the target user and recommends items they liked
* **Item-Based CF**: Recommends items similar to the ones the user liked

**Example:**

> If user A and B both like 5 action movies, and A watched “John Wick,” recommend it to B

---

### ▶️ 2.3 Hybrid Recommender Systems

* Combines **CBF + CF** (and sometimes more methods)
* Overcomes individual limitations (e.g., cold start, sparsity)

**Approaches:**

* Weighted combination of results
* Switching between methods based on context
* Merging models at feature or prediction level

---

### ▶️ 2.4 Non-Personalized Recommendation

* Gives **same recommendation to all users**
* Based on **popularity, trends, or ratings**

**Example:**

* Amazon Best Sellers
* YouTube Trending
* “Most Viewed Articles” on a news site

---

## 🔶 3. TRADITIONAL VS NON-PERSONALIZED RECOMMENDER SYSTEMS

**diagram: false**

### ▶️ Traditional Recommender Systems:

* **Personalized**
* Based on user history (explicit ratings or implicit behavior)
* Uses CF, CBF, and hybrid models
* Example: Netflix suggesting sci-fi to a sci-fi fan

### ▶️ Non-Personalized Recommender Systems:

* **General** – Same for everyone
* Based on overall item popularity or average ratings
* Works well for new users or anonymous browsing

| Feature         | Traditional RS            | Non-Personalized RS    |
| --------------- | ------------------------- | ---------------------- |
| Personalization | ✅ Yes                     | ❌ No                   |
| Data required   | User-item interaction     | Global item stats only |
| Complexity      | Medium to high            | Low                    |
| Scalability     | Lower                     | Very high              |
| Example         | Netflix personalized feed | Amazon “Top Trending”  |

---

## 🔶 4. DATA MINING METHODS IN RECOMMENDER SYSTEMS

**diagram: false**

### ▶️ Why Data Mining?

* Helps **uncover patterns** and trends
* Transforms raw data into **actionable insights**
* Enables better **user-item matching**

### ▶️ Key Techniques:

#### 📌 4.1 Clustering

* Groups **similar users or items**
* Algorithm: K-Means, DBSCAN
* Use: Create **user segments**, e.g., “Horror Lovers,” “Binge Watchers”

#### 📌 4.2 Classification

* Predicts if a user will **like/dislike** an item
* Algorithm: Decision Trees, Naive Bayes
* Use: Show item if probability of liking is high

#### 📌 4.3 Association Rule Mining

* Finds rules between co-occurring items
* Algorithm: Apriori, FP-Growth
* Use: “Users who bought X also bought Y”

#### 📌 4.4 Regression

* Predicts **numerical ratings** (e.g., out of 5 stars)
* Algorithm: Linear Regression
* Use: Rank items by predicted rating

#### 📌 4.5 Matrix Factorization

* Converts large sparse matrix into **low-rank approximations**
* Leads to **latent features**, which improve predictions
* Includes **SVD** (next topic)

---

## 🔶 5. SIMILARITY MEASURES

**diagram: false**

Used to compare:

* User ↔ User (user-based CF)
* Item ↔ Item (item-based CF)
* Item features (CBF)

### ▶️ Key Similarity Metrics:

| Metric                  | Description                             | Range    | Used In              |
| ----------------------- | --------------------------------------- | -------- | -------------------- |
| **Cosine Similarity**   | Angle between two rating vectors        | 0 to 1   | CF, CBF              |
| **Pearson Correlation** | Linear relationship between ratings     | -1 to +1 | CF                   |
| **Jaccard Index**       | Set overlap ratio (e.g., clicks, views) | 0 to 1   | Binary implicit data |

---

## 🔶 6. DIMENSIONALITY REDUCTION

**diagram: true**
**Google search:** `dimensionality reduction recommender systems`

### ▶️ Problem It Solves:

* User-item matrices are **huge and sparse**
* High dimensionality = slow + overfitting + hard to learn

### ▶️ Techniques:

#### 📌 6.1 Singular Value Decomposition (SVD)

* Decomposes matrix into U × Σ × Vᵗ
* Extracts **latent features**

#### 📌 6.2 PCA (Principal Component Analysis)

* Used more in **pre-processing or visualization**
* Not ideal for predictions

#### 📌 6.3 Autoencoders (Neural Networks)

* Learns compressed representation
* Used in **deep learning recommenders**

---

## 🔶 7. SINGULAR VALUE DECOMPOSITION (SVD)

**diagram: true**
**Google search:** `SVD recommender systems matrix factorization`

### ▶️ What is it?

SVD is a **matrix factorization** technique used to decompose a **user-item matrix (R)** into three matrices:

$$
R \approx U \cdot \Sigma \cdot V^T
$$

| Matrix | Meaning                                |
| ------ | -------------------------------------- |
| **U**  | User-to-feature matrix                 |
| **Σ**  | Strength of latent features (diagonal) |
| **Vᵗ** | Feature-to-item matrix                 |

### ▶️ Use in RS:

* Handles missing data (predicts unknown ratings)
* Reduces dimensions → faster, less memory
* Improves prediction accuracy with **latent features**

### ▶️ Real-World Use Case:

* Used by Netflix in their original recommendation engine
* Part of winning solution in the **Netflix Prize**

### ▶️ Benefits:

* Captures **hidden preferences**
* Makes **sparse data usable**
* Highly **scalable and accurate**

### ▶️ Drawbacks:

* Doesn’t handle **cold start** well
* Requires **retraining** as new data comes in
* **Computationally intensive** for huge datasets

---

<br>
<br>

---

# 📘 UNIT II: CONTENT-BASED RECOMMENDATION SYSTEMS

**Syllabus:**

> High-level architecture of content-based systems — Item profiles — Representing item profiles — Methods for learning user profiles — Similarity-based retrieval — Classification algorithms

---

## 🔷 1. High-Level Architecture of Content-Based Systems

**diagram: true**
**Google this:** `content-based recommender system architecture diagram`

### 🎯 Objective:

Build a system that recommends items **based on the content/features** of what a user has liked or interacted with before.

### 🧱 Architecture Components:

1. **User Profile Generator**

   * Learns the user’s interests from past interactions
   * Aggregates features of previously liked/rated items
   * Stores a vector-like representation of user taste

2. **Item Feature Extractor**

   * Extracts structured attributes (genre, tags, keywords, price, brand) from each item
   * Converts unstructured data like text (descriptions) into usable formats (via TF-IDF, NLP, etc.)

3. **Profile Representation Engine**

   * Transforms both item and user data into a common **feature space**
   * Enables **vector-based comparison**

4. **Similarity Engine**

   * Computes **similarity scores** between user profile and available items
   * Returns ranked list based on closeness

5. **Recommendation Engine**

   * Selects Top-N most similar items
   * Continuously learns and updates as user behavior changes

6. **Feedback Loop**

   * System captures **explicit** (ratings, likes) or **implicit** (clicks, dwell time) feedback
   * Updates user profile over time (real-time or batch-based)

---

## 🔷 2. Item Profiles

**diagram: false**

### 🎯 What Are They?

Item profiles describe **what the item is**, using a set of features. These features are critical in calculating whether the item is relevant to a particular user.

### 📚 Examples:

* **Movie**: title, genre, director, tags, rating, release year
* **Book**: title, author, genre, keywords, page count
* **E-commerce product**: category, brand, price, color, keywords

### 🧩 Types of Features:

| Feature Type     | Example                     | Purpose                         |
| ---------------- | --------------------------- | ------------------------------- |
| **Categorical**  | Genre, Brand, Director      | Grouping & filtering            |
| **Textual**      | Tags, Descriptions, Reviews | Semantic meaning (TF-IDF, NLP)  |
| **Numerical**    | Price, Year, Rating         | Quantitative filtering, sorting |
| **Boolean**      | IsPremium, IsFree, IsOnSale | Yes/No filters                  |
| **Multi-valued** | Tags, Cast, Skills          | Enrich representation           |

---

## 🔷 3. Representing Item Profiles

**diagram: false**

### 🎯 Purpose:

To turn raw item data into a **structured vector** format so the recommender system can apply math to compare it with user preferences.

### 🧠 Key Techniques:

1. **Vector Space Model (VSM)**

   * Most basic & widely used
   * Each feature = dimension
   * Vector = 1 if item has that feature, 0 otherwise

2. **One-Hot Encoding**

   * Converts categorical data to binary columns
   * Example: Genre → Action = \[1, 0, 0], Romance = \[0, 1, 0]

3. **TF-IDF (Term Frequency-Inverse Document Frequency)**

   * Measures how **unique** and **important** a word is to an item
   * Works well with large descriptions, tags, or metadata

4. **Embeddings**

   * Use deep learning to generate **dense vector** representation
   * Captures deeper context from textual content (e.g., BERT, Doc2Vec)

5. **Hybrid Representations**

   * Combine categorical, numerical, and text embeddings into one big vector

### 🧪 Example Vector:

Movie profile:
`[Action: 1, Romance: 0, Sci-Fi: 1, Nolan: 1, Year: 2010] → [1, 0, 1, 1, 0.9]`

---

## 🔷 4. Methods for Learning User Profiles

**diagram: false**

### 🎯 Goal:

Understand and model a user's **preferences** from their past interactions.

### 🧾 Input:

* Items the user has rated, liked, purchased, clicked, or viewed

### 🛠️ Methods:

#### A. **Weighted Feature Aggregation**

* Average the features of items the user liked
* Weighted by rating or confidence
* Simple and effective

#### B. **TF-IDF Aggregation**

* For content-heavy domains (news, books, courses)
* Combine TF-IDF scores of all liked items into one vector

#### C. **Bayesian Profiling**

* Use probabilities to estimate P(UserLikes | FeatureSet)
* Good for binary classification (like/dislike)

#### D. **Machine Learning Approaches**

* Use classifiers (Logistic Regression, Decision Trees, SVM)
* Train with features of liked and disliked items

#### E. **Neural User Embeddings**

* Learn dense, abstract representations of a user's behavior
* Used in deep recommender models (e.g., YouTube, Spotify)

### 🧠 Sample Profile Vector:

User likes Action, Nolan, no Romance →
`User Vector = [1.0, 0.0, 0.8, 0.1]`

---

## 🔷 5. Similarity-Based Retrieval

**diagram: false**

### 🎯 Goal:

Retrieve and rank items **based on how similar** they are to the user profile.

### 📏 Similarity Measures:

| Method                 | When to Use                      | Description                                     |
| ---------------------- | -------------------------------- | ----------------------------------------------- |
| **Cosine Similarity**  | Sparse, high-dimensional vectors | Compares angle between vectors (ignores length) |
| **Dot Product**        | Dense vectors, weighted features | Measures magnitude and direction                |
| **Jaccard Similarity** | Binary, tag-based data           | Measures overlap between sets                   |
| **Euclidean Distance** | Simple, low-dimension data       | Less commonly used, sensitive to scale          |

### ⚙️ Workflow:

1. Represent user and item as vectors
2. Compute similarity between them
3. Rank items by similarity score
4. Recommend Top-N items

---

## 🔷 6. Classification Algorithms

**diagram: false**

### 🎯 Purpose:

Use supervised ML to **predict if a user will like** an item or not, based on its features.

### 📚 Common Algorithms:

| Algorithm               | Use Case                                    |
| ----------------------- | ------------------------------------------- |
| **Naive Bayes**         | Probabilistic filtering of simple features  |
| **Decision Tree**       | Rule-based prediction                       |
| **k-NN**                | Based on nearest neighbors' outcomes        |
| **Logistic Regression** | Predicts probability of like                |
| **SVM**                 | Separates like vs not-like with hyperplanes |
| **Neural Networks**     | For deep, nonlinear, high-dimensional data  |

### 🧠 How It Works:

1. Gather labeled data:
   `Item A → liked`, `Item B → not liked`
2. Extract features of those items
3. Train model on this data
4. Predict label (like/dislike) for new items

### 💡 Application:

* Used in **news/article recommenders**
* Effective when feedback data is large and labeled

---

# 📌 Final Concept Map (Topic Summary)

| Topic                      | Core Concept                                                                   |
| -------------------------- | ------------------------------------------------------------------------------ |
| High-Level Architecture    | Modular flow: extract item features → learn user profile → match and recommend |
| Item Profiles              | Structured set of item attributes used for comparison                          |
| Representing Item Profiles | Transforms raw data into vectors using VSM, TF-IDF, embeddings                 |
| Learning User Profiles     | Models user preferences via aggregation, probability, or ML                    |
| Similarity-Based Retrieval | Uses math (cosine, Jaccard, etc.) to find matching items                       |
| Classification Algorithms  | Learns from labeled data to predict like/dislike using item features           |

---

<br>
<br>


---

# ✅ UNIT III: COLLABORATIVE FILTERING 

**diagram: true**
**Search query:** `Collaborative filtering architecture diagram user item based`

---

## 🔷 1. What is Collaborative Filtering (CF)?

Collaborative Filtering =

> “People like you also liked...”
> This is based on the idea that **users with similar tastes will like similar items.**

CF doesn't care what the item *is*, only how **users interact** with it.

### ✅ Example:

If you and I both rated “Inception” and “Interstellar” high, and you also liked “Tenet”, then I’m probably gonna love “Tenet” too.

---

## 🔷 2. Systematic Approach to CF

This is the step-by-step pipeline every collaborative filtering model follows.

### 🪛 Steps (in order):

1. **Collect User-Item Interaction Data**
   Like rating matrix (users as rows, items as columns)

2. **Preprocess Data**
   Normalize ratings, remove noise (e.g. super old ratings)

3. **Calculate Similarities**
   Between users (user-based CF) or items (item-based CF)

4. **Find Neighbors**
   Choose top-N most similar users/items

5. **Predict Missing Ratings**
   Use weighted averages or matrix methods

6. **Recommend Top-N Items**
   Show the items with highest predicted ratings

### ✅ Subtopics to remember:

* Similarity metrics (cosine, Pearson)
* Rating prediction formula
* Cold start handling

**diagram: true** — Google: `collaborative filtering step by step diagram`

---

## 🔷 3. Nearest-Neighbor Collaborative Filtering

This is OG CF method — find your closest peeps or fav items, and steal recos from them 😎

### 🎯 Two types:

| Type           | Based on...   | Key Idea              |
| -------------- | ------------- | --------------------- |
| **User-based** | Similar users | "People like you"     |
| **Item-based** | Similar items | "Items like this one" |

### ✅ Example:

* User-based:
  *You like A, B → find users who also like A, B → recommend what they liked*
* Item-based:
  *You liked A → find items similar to A → recommend those*

🧠 Use cosine similarity or Pearson correlation to find closeness.

**diagram: true** — Google: `user based vs item based collaborative filtering diagram`

---

## 🔷 4. Components of Neighborhood Methods

### 🧩 (a) Rating Normalization

Users have different rating habits. Normalizing = fair game.

| Method             | Description            |
| ------------------ | ---------------------- |
| **Mean-centering** | Subtract user average: |

$$
r'_{ui} = r_{ui} - \bar{r_u}
$$

\| **Z-score normalization** | Subtract mean & divide by standard deviation

### ✅ Example:

If user always gives 4s & 5s → raw scores misleading
→ Normalize before comparing with others

---

### 🧩 (b) Similarity Weight Computation

To find **how similar** two users/items are.

| Similarity | Formula (Short)            | When to Use            |
| ---------- | -------------------------- | ---------------------- |
| Cosine     | angle between vectors      | Default                |
| Pearson    | correlation (removes bias) | Better for rating data |
| Jaccard    | (A ∩ B) / (A ∪ B)          | Binary preferences     |

### ✅ In exams: write at least 2 with tiny example.

**Formula (Cosine):**

$$
sim(u, v) = \frac{u \cdot v}{||u|| \cdot ||v||}
$$

---

### 🧩 (c) Neighborhood Selection

* Select top-N similar users or items (N = 5, 10, 20)
* These are the “trusted” neighbors used for prediction

### ✅ Pro tip:

In real-world, N is small to reduce noise & overfitting.

---

## 🔷 5. Rating Prediction in CF

Once you’ve got neighbors, time to predict missing rating:

### ✅ User-based prediction formula:

$$
\hat{r}_{ui} = \bar{r}_u + \frac{\sum_{v \in N} sim(u, v) \cdot (r_{vi} - \bar{r}_v)}{\sum_{v \in N} |sim(u, v)|}
$$


### ✅ Item-based prediction formula:

$$
\hat{r}_{ui} = \frac{\sum_{j \in N} sim(i, j) \cdot r_{uj}}{\sum_{j \in N} |sim(i, j)|}
$$

✅ Keep formulas short in exam — no need to derive.

---

## 🔷 6. Matrix Factorization in CF

This is the advanced CF — done using **SVD, ALS, or Funk-SVD**
Instead of finding neighbors, we **learn hidden user/item features**.

| Technique | What It Does                              |
| --------- | ----------------------------------------- |
| SVD       | Factorize rating matrix into 3 (U, Σ, Vᵗ) |
| ALS       | Alternate Least Squares, used at scale    |
| Funk-SVD  | Optimized version used in Netflix Prize   |

✅ Already covered in Unit 1 — mention it in hybrid models.

---

## 🔷 7. Advantages of Collaborative Filtering

* Content-free — works even when item data is missing
* Adapts over time — learns as user behavior changes
* Uncovers surprising patterns (latent preferences)

---

## 🔷 8. Limitations of Collaborative Filtering

| Issue               | Description                                        |
| ------------------- | -------------------------------------------------- |
| **Cold Start**      | New users/items = no data, can’t recommend         |
| **Data Sparsity**   | Most users rate very few items, matrix is empty AF |
| **Scalability**     | With millions of users/items, similarity calc = 🥲 |
| **Popularity Bias** | Recommends popular stuff more than diverse stuff   |

✅ Mitigation: hybrid systems, matrix factorization, attack-resistant design (Unit 4)

---

## 🔷 9. Real-World Applications

| Platform    | Uses CF for...                               |
| ----------- | -------------------------------------------- |
| **Netflix** | Shows based on similar viewers               |
| **Amazon**  | "People who bought this also bought…"        |
| **Spotify** | "Users like you are vibing to..."            |
| **YouTube** | Up next queue personalized via watch history |

---

## 📘 KEY TERMS TO REMEMBER (drop these in every answer):

* User-based CF
* Item-based CF
* Cosine similarity
* Normalization
* Top-N recommendation
* Cold start
* Rating prediction
* Neighborhood
* Matrix factorization

---
