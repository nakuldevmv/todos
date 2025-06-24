# Recommender System (CCS360)

<br>

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

![alt text](https://www.researchgate.net/publication/353416188/figure/fig2/AS:1134447600640000@1647484793982/Taxonomy-of-recommender-system.png)

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
<br><br>


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
<br><br>



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
\hat{r}_{ui} = \bar{r_u} + \frac{\sum_{v \in N} sim(u, v) \cdot (r_{vi} - \bar{r_v})}{\sum_{v \in N} |sim(u, v)|}
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

<br>
<br><br>



---

# 🎯 UNIT IV – ATTACK-RESISTANT RECOMMENDER SYSTEMS

*Protecting recommendation systems from spam, fake users, manipulation, and trust issues*

---

## 🔷 1. INTRODUCTION TO ATTACK-RESISTANT RS

**diagram: false**

### ❓ Why this matters:

* Recommender Systems (RS) rely heavily on **user-generated data** (ratings, reviews, interactions)
* Attackers can **manipulate** this data to:

  * Promote their own product/content
  * Sabotage others
  * Game the system for visibility or financial gain

### 🎯 Goal of Attack-Resistant RS:

* **Detect**, **mitigate**, and **withstand** attacks on the system
* Ensure fair, unbiased, and accurate recommendations
* Maintain **user trust and system integrity**

---

## 🔷 2. TYPES OF ATTACKS ON RS

**diagram: true**
*Google search:* `types of shilling attacks recommender systems`

### 2.1 Profile Injection (Shilling Attacks):

Attackers inject **fake user profiles** to manipulate recommendations.

#### Subtypes of Shilling Attacks:

| Attack Type          | Description                                         | Goal                   |
| -------------------- | --------------------------------------------------- | ---------------------- |
| **Push Attack**      | Fake profiles give high ratings to a target item    | Boost ranking          |
| **Nuke Attack**      | Fake profiles give low ratings to a target item     | Damage reputation      |
| **Random Attack**    | Fill fake profile with random ratings + target item | Bypass detection       |
| **Average Attack**   | Use average ratings + push target item              | Appear realistic       |
| **Bandwagon Attack** | Rate popular items + target item                    | Blend into legit users |

---

### 2.2 Behavior-Based Attack Types:

| Type                     | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Individual Attack**    | One user creates a single fake profile to push/nuke |
| **Group (Sybil) Attack** | Multiple fake users act together to game the RS     |

---

## 🔷 3. DETECTING ATTACKS IN RECOMMENDER SYSTEMS

**diagram: true**
*Google search:* `anomaly detection recommender system`

### 🧠 Key Methods to Detect Malicious Behavior:

#### 3.1 Statistical Analysis

* Detect **outliers** in rating behavior
* Look for users with very high/low mean ratings
* Spot users with unusual rating variance

#### 3.2 Time-Based Behavior Monitoring

* Identify **suspiciously fast or batch-like rating activity**
* Sudden spikes in ratings = bot-like behavior

#### 3.3 Rating Pattern Analysis

* Users who rate only:

  * One category
  * One item (always 5 or 1 stars)
  * Never interact with content

#### 3.4 Similarity-Based Clustering

* Use clustering algorithms (k-means, DBSCAN)
* If a group of users have **very similar** behavior → red flag 🚩

#### 3.5 Trust Scoring / Credibility Checks

* Assign trust score based on:

  * Account age
  * Purchase history
  * Consistency of ratings
  * Engagement behavior

#### 3.6 Anomaly Detection Models

* Use **machine learning** to identify suspicious profiles based on multi-dimensional features

---

## 🔷 4. INDIVIDUAL VS GROUP ATTACK

**diagram: true**
*Google search:* `individual vs sybil attack recommender system`

| Feature             | Individual Attack                | Group (Sybil) Attack            |
| ------------------- | -------------------------------- | ------------------------------- |
| Number of attackers | One fake profile                 | Many fake profiles              |
| Execution           | Simple, low effort               | Coordinated, scripted           |
| Detectability       | Easier to detect (clear anomaly) | Harder (mimics real behavior)   |
| Impact              | Localized                        | Large-scale manipulation        |
| Behavior pattern    | Obvious                          | Distributed and camouflaged     |
| Defense             | Outlier detection                | Clustering, behavioral analysis |

---

## 🔷 5. STRATEGIES FOR ROBUST RECOMMENDER DESIGN

**diagram: false**

### 5.1 Trust-Aware System Design

* Assign **reputation scores** to users
* Base recommendations on **trusted ratings** only
* Ignore/discount ratings from new or suspicious accounts

### 5.2 Weighted Ratings

* Give more importance to users with:

  * Longer platform history
  * Verified purchases
  * Normal rating behavior

### 5.3 Outlier Detection and Filtering

* Identify and **remove extreme/abnormal profiles** before training the RS model

### 5.4 Rating Restrictions

* Put caps on:

  * How many ratings a user can give per day
  * How often the same item can be rated
  * What categories they can rate initially

### 5.5 Hybrid Recommender Models

* Use **multiple techniques** (CF + content + demographic)
* If one fails (e.g., collaborative filtering gets attacked), the others act as fallback

### 5.6 Clustering-Based Filtering

* Detect groups of **suspiciously similar** profiles
* Flag/remove clusters of fake users

### 5.7 Time-Based Decay

* Older ratings lose influence over time
* Prevents old spam attacks from still affecting recommendations

### 5.8 Behavior Monitoring & CAPTCHA Defense

* Track:

  * IP address
  * Device fingerprint
  * Login time
* Block or flag suspicious bot-like behavior

---

## 🔷 6. ROBUST RECOMMENDATION ALGORITHMS

**diagram: optional**

### 6.1 Trust-Aware Collaborative Filtering

* Use trust score to weigh user ratings
* Reduces impact of fake/new profiles

### 6.2 Probabilistic Matrix Factorization (PMF)

* Models ratings as:
  `Observed Rating = True Preference + Noise`
* Filters out noisy/fake data automatically

### 6.3 Bayesian User Modeling

* Models user preferences with **probability**
* Adjusts recommendations based on **confidence level**

### 6.4 Robust SVD

* Variation of Singular Value Decomposition
* Ignores or down-weights **outlier values** during factorization

### 6.5 Clustering-Based Filtering

* Groups users into clusters
* Only uses **legit, clean clusters** for generating recommendations

### 6.6 Adversarial Learning-Based Models

* Simulate **attacks during training**
* Help RS learn how to defend itself
* Makes it resilient to unknown future attacks

---

<br>
<br><br>



---

# ✅ UNIT V – EVALUATING RECOMMENDER SYSTEMS


---

## 🔷 1. Evaluation Paradigms

**diagram: true**
**Search this:** `recommender system evaluation paradigms diagram`

### 📊 Definition:

Evaluation paradigms are **broad strategies** used to assess how well a recommender system performs.

Each paradigm is suitable for **different use cases and stages** of system development.

---

### 💡 Types of Paradigms:

| Type                   | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| **User Studies**       | Controlled environments where real users interact with the RS        |
| **Online Evaluation**  | Live deployment using real-time user interaction (e.g., A/B testing) |
| **Offline Evaluation** | Lab-based testing using historical data (no live users)              |

---

### 🔁 Workflow Comparison:

| Step             | User Study           | Online Eval        | Offline Eval           |
| ---------------- | -------------------- | ------------------ | ---------------------- |
| Data Source      | Real-time user input | Live site/app data | Pre-collected datasets |
| User Involved?   | Yes                  | Yes                | No                     |
| Metrics Measured | Satisfaction, Trust  | Engagement, CTR    | Accuracy, Ranking      |
| Use Case         | Early testing        | Deployed system    | Model tuning           |

---

## 🔷 2. User Studies

**diagram: false**

### 🔬 What is it?

A **qualitative** approach. Real users interact with your RS and give feedback via surveys, interviews, or ratings.

---

### 🎯 What it Evaluates:

* User satisfaction 😊
* Ease of use
* Trust in recommendations
* Perceived relevance
* UX design effectiveness

---

### 💻 Working:

1. Build prototype/system
2. Recruit participants
3. Let them use RS in a test scenario
4. Collect feedback via:

   * Likert scales
   * Observations
   * Follow-up interviews

---

### ✅ Advantages:

* Deep insights into human behavior
* Can capture trust, transparency, explainability

### ❌ Limitations:

* Expensive
* Time-consuming
* Small sample size = not always generalizable

---

## 🔷 3. Online Evaluation

**diagram: true**
**Search this:** `A/B testing recommender systems`

### 🖥️ What is it?

Real-time testing of RS **with real users** in a production system (like Amazon or Netflix).

---

### 🔧 Working:

1. Deploy multiple versions of RS (Model A vs Model B)
2. Split traffic randomly → send some users to each version
3. Track user behavior (clicks, purchases, time spent)
4. Compare performance using online metrics

---

### ⚙️ Methods:

| Method                 | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **A/B Testing**        | Users split into groups, each sees different model           |
| **Interleaving**       | Merge results from 2 models into 1 ranked list shown to user |
| **Multi-Armed Bandit** | Dynamically picks best model during testing                  |

---

### 📏 Metrics Measured:

* Click Through Rate (CTR)
* Conversion Rate
* Bounce Rate
* Average Session Time
* Purchase Rate

---

### ✅ Advantages:

* Real-world effectiveness
* Captures live behavior + context

### ❌ Limitations:

* Needs high user traffic
* Risky if model performs poorly
* Ethical concerns (user testing unknowingly)

---

## 🔷 4. Offline Evaluation

**diagram: true**
**Search this:** `train test split recommender evaluation`

### 🗂️ What is it?

Simulated evaluation of RS using **historical data** (no real-time interaction).

---

### ⚙️ Working:

1. Take a dataset (e.g., MovieLens)
2. **Split** into training + test sets

   * Common splits: 80-20, 70-30
3. Train RS on training set
4. Predict ratings or rankings in test set
5. Compare predictions with actual values
6. Evaluate with metrics like MAE, RMSE, Precision

---

### 🧪 Example:

User rated:

* Titanic: ⭐⭐⭐⭐
* Interstellar: ⭐⭐⭐⭐⭐
* Matrix: ⭐⭐⭐⭐
  (Hidden: Inception: ⭐⭐⭐⭐)

Train RS → Predict rating for Inception → Compare with actual (4 stars)

---

### ✅ Pros:

* Fast, low-cost, repeatable
* Good for early development + benchmarking

### ❌ Cons:

* Can’t simulate real-time behavior
* Cold start, novelty, UX can't be evaluated

---

## 🔷 5. Goals of Evaluation Design

**diagram: false**

### 🎯 What Should We Measure?

Recommender Systems aren't just about accuracy. We need to measure things that improve **user experience**, **system performance**, and **business value**.

---

### 📋 Key Goals:

| Goal                   | Description                           |
| ---------------------- | ------------------------------------- |
| **Accuracy**           | Predict right items/ratings           |
| **Coverage**           | Handle all users & items              |
| **Diversity**          | Recommend varied content              |
| **Novelty**            | Suggest new, unknown items            |
| **Serendipity**        | Surprise + delight users              |
| **User Satisfaction**  | Keep users happy and engaged          |
| **Scalability**        | Perform well at scale                 |
| **Trust/Transparency** | Recommendations should be explainable |

---

## 🔷 6. Design Issues in Evaluation

**diagram: false**

### 🚨 Why evaluation often fails in real-world:

| Issue                       | Impact                                 |
| --------------------------- | -------------------------------------- |
| **Cold Start**              | RS fails for new users/items (no data) |
| **Sparsity**                | Too few interactions = poor learning   |
| **User Behavior is Random** | Clicks ≠ preferences                   |
| **Bias in Data**            | Popular items dominate results         |
| **No Context**              | Doesn’t factor in time, mood, device   |
| **Overfitting to Metrics**  | Optimizes numbers, not experience      |
| **Slow Algorithms**         | Accurate but unscalable models         |

---

## 🔷 7. Accuracy Metrics

**diagram: true**
**Search this:** `recommender evaluation metrics RMSE MAE Precision Recall`

### 🧮 1. Rating Prediction Metrics

| Metric   | Formula                           | Use                      |
| -------- | --------------------------------- | ------------------------ |
| **MAE**  | Avg. of absolute errors           | Measures general error   |
| **RMSE** | Square root of mean squared error | Penalizes large mistakes |

---

### 🎯 2. Top-N Recommendation Metrics

| Metric        | Meaning                                      |
| ------------- | -------------------------------------------- |
| **Precision** | % of relevant items in top-N list            |
| **Recall**    | % of relevant items successfully recommended |
| **F1 Score**  | Harmonic mean of Precision & Recall          |
| **nDCG**      | Cares about rank/order of relevant items     |
| **MAP**       | Average Precision across all users           |

---

### ✅ Other Metrics:

* **Hit Rate** → Did user click at least one recommended item?
* **Coverage** → % of users/items the RS gives predictions for

---

## 🔷 8. Limitations of Evaluation Measures

**diagram: false**

### 🚫 Why metrics can lie:

| Limitation      | Impact                                  |
| --------------- | --------------------------------------- |
| Ignores Emotion | MAE ≠ User Delight                      |
| Offline Bias    | Uses old behavior, can't test new       |
| No Context      | Can’t factor in time, location, mood    |
| Cold Start      | Metrics assume data exists              |
| Overfitting     | Models can cheat metrics                |
| Not Scalable    | Accurate models may lag on real servers |

---

<br>
<br>
<br>
<br>

# 📘 Possible Questions


<br>
<br>
<br>


---

## **UNIT I – INTRODUCTION**

### **Q1. Explain the different types of recommender systems with suitable examples. Also differentiate between traditional and non-personalized recommender systems.**

**Answer:**
Recommender systems are classified into various types based on how they generate recommendations:

1. **🌐 Content-Based Filtering:**

   * Recommends items similar to those the user liked in the past.
   * Example: Spotify recommending songs similar to your playlists.

2. **🤝 Collaborative Filtering:**

   * Uses preferences of similar users to make recommendations.
   * Example: Netflix recommending shows watched by users with similar watch history.

3. **📊 Hybrid Systems:**

   * Combines content-based and collaborative filtering.
   * Example: Amazon considering both your product views and similar users' purchases.

4. **📅 Demographic-Based Filtering:**

   * Uses user demographic data to recommend items.
   * Example: Recommending products based on age group or gender.

5. **🔧 Knowledge-Based Filtering:**

   * Uses domain knowledge to recommend items.
   * Example: Real estate sites suggesting houses based on budget and location.

**Traditional vs Non-Personalized Recommenders:**

* *Traditional:* Personalize recommendations using historical user-item interaction data.
* *Non-Personalized:* Show popular/trending items to all users without personalization.

### **Q2. Discuss the various similarity measures used in recommender systems. Explain with formulas and examples how they impact recommendation quality. Also mention how dimensionality reduction techniques like SVD are used in recommendation.**

**Answer:**

**Similarity Measures:**

1. **✏️ Cosine Similarity:**
   Measures the cosine of the angle between two vectors.
   $sim(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$

2. **🔄 Pearson Correlation:**
   Measures linear correlation between users/items.
   $sim(A, B) = \frac{\sum (A_i - \bar{A})(B_i - \bar{B})}{\sqrt{\sum (A_i - \bar{A})^2} \sqrt{\sum (B_i - \bar{B})^2}}$

3. **📊 Jaccard Similarity:**
   Used for binary attributes.
   $sim(A, B) = \frac{|A \cap B|}{|A \cup B|}$

**Impact on Recommendation:**
Better similarity = more accurate predictions. Choosing the right similarity measure improves neighborhood quality in collaborative filtering systems.

**Dimensionality Reduction – SVD (Singular Value Decomposition):**

* 🧹 Reduces high-dimensional rating matrix to lower dimensions.
* 📊 Captures latent factors (e.g., taste, genre, popularity).
* ✅ Improves performance by removing noise and sparsity.
* Matrix R is factorized as:
  $R = U \Sigma V^T$

---

## **UNIT II – CONTENT-BASED RECOMMENDATION SYSTEMS**

### **Q3. Describe the high-level architecture of a content-based recommendation system. Explain how item profiles and user profiles are constructed and used.**

**Answer:**

**High-Level Architecture:**

1. **🔄 Item Profile Builder:** Extracts features from items (e.g., genre, director for movies).
2. **👤 User Profile Learner:** Learns preferences from past interactions.
3. **🧠 Similarity Engine:** Compares user and item profiles.
4. **🔢 Recommendation Generator:** Ranks items based on similarity scores.

**Item Profile:**

* 📂 Structured representation of an item.
* Example: Movie with features like \[Action:1, Comedy:0, Drama:1]

**User Profile:**

* 🤓 Represents user's preferences derived from liked items.
* Example: Averaging profiles of movies the user rated highly.

**Usage:**

* Match user profile with new items to compute similarity.
* Recommend top-N items with highest similarity.

### **Q4. Explain various classification algorithms used in content-based systems. Also discuss the concept of similarity-based retrieval and how it improves personalization.**

**Answer:**

**Classification Algorithms:**

1. **🌐 Naive Bayes:** Probabilistic, assumes feature independence.
2. **🌳 Decision Trees:** Rule-based classification.
3. **🤝 k-Nearest Neighbors (kNN):** Classifies based on closest item profiles.
4. **🚀 Support Vector Machines (SVM):** Finds optimal boundary between classes.

**Similarity-Based Retrieval:**

* 💡 Retrieves items based on similarity between user and item profiles.
* Common measures: cosine similarity, Euclidean distance.
* ✨ Improves personalization by considering unique user preferences.

---

## **UNIT III – COLLABORATIVE FILTERING**

### **Q5. With a neat flow, explain user-based and item-based collaborative filtering techniques. Include steps like similarity computation, rating prediction, and examples.**

**Answer:**

**User-Based CF:**

1. ✏️ Find users similar to the target user.
2. 🔢 Use their ratings to predict missing ratings.
3. 🔍 Recommend items highly rated by similar users.

**Item-Based CF:**

1. 🔢 Find items similar to those the user liked.
2. 🧸 Predict rating for a new item based on similar items' ratings.
3. 🔝 Recommend top-N items.

**Steps in CF:**

1. **⚖️ Similarity Computation:** Cosine/Pearson between users/items.
2. **👥 Neighborhood Selection:** Pick top-k similar entities.
3. **✅ Rating Prediction:** Weighted average of neighbors.
4. **🌟 Recommendation:** Items with highest predicted ratings.

**Example:**
If User A and B both like Item X, and B likes Y, then recommend Y to A.

### **Q6. Discuss the key components of neighborhood-based CF systems: Rating normalization, Similarity weight computation, Neighborhood selection. Also add a real-life example scenario.**

**Answer:**

1. **📊 Rating Normalization:**

   * Adjust ratings to remove user bias.
   * Formula: $r' = r - \bar{r}_{user}$

2. **🤝 Similarity Weight Computation:**

   * Use similarity functions to assign weights.
   * More similar = more influence in prediction.

3. **👥 Neighborhood Selection:**

   * Choose top-k users/items with highest similarity.
   * Impacts both accuracy and scalability.

**Real-life Scenario:**
In an e-commerce app, recommend products based on what users with similar purchase history bought, normalizing for rating patterns.

---

## **UNIT IV – ATTACK-RESISTANT RECOMMENDER SYSTEMS**

### **Q7. Explain the types of attacks on recommender systems: Individual attack, Group attack. How do these affect the system? Give examples.**

**Answer:**

**1. 🛡️ Individual Attack:**

* A single fake user profile is inserted.
* Goal: promote or demote specific items.
* Example: Fake account rating one product 5 stars.

**2. 🧳 Group Attack:**

* Multiple coordinated fake profiles used.
* More difficult to detect due to volume.
* Example: 100 fake accounts upvoting a new app.

**Impact:**

* ❌ Skewed recommendations.
* ❄️ Loss of trust from users.
* 🚨 System performance degrades.

### **Q8. What are robust recommendation algorithms? Discuss strategies for designing attack-resistant recommender systems. Also explain detection mechanisms.**

**Answer:**

**🛡️ Robust Algorithms:**

* Designed to resist manipulation by attackers.
* Examples: Using user trust scores, anomaly detection.

**🤨 Strategies:**

1. **🔎 Profile Analysis:** Detect unusual rating patterns.
2. **📊 Clustering:** Identify groups of suspicious profiles.
3. **✨ Trust Networks:** Prioritize ratings from verified/trusted users.

**🔍 Detection Mechanisms:**

* **⚠️ Outlier Detection:** Identify profiles far from norm.
* **🕷️ Behavioral Analysis:** Track login times, rating speeds.
* **📊 Statistical Filters:** Identify statistical anomalies in rating distributions.

---

## **UNIT V – EVALUATING RECOMMENDER SYSTEMS**

### **Q9. Explain the different evaluation paradigms in recommender systems. Compare user studies, online and offline evaluation methods with pros and cons.**

**Answer:**

**Evaluation Paradigms:**

1. **👨‍🏫 User Studies:**

   * Direct feedback from users.
   * Pros: Qualitative insights.
   * Cons: Expensive, time-consuming.

2. **🌐 Online Evaluation (A/B Testing):**

   * Live system testing.
   * Pros: Real user behavior.
   * Cons: Risky to deploy weak model.

3. **🔄 Offline Evaluation:**

   * Uses historical datasets.
   * Pros: Fast, reproducible.
   * Cons: May not reflect real-world behavior.

### **Q10. Discuss various accuracy metrics used to evaluate recommendation quality. Explain design issues and limitations in evaluation with suitable examples.**

**Answer:**

**🔢 Accuracy Metrics:**

1. **🔢 MAE (Mean Absolute Error):**

   * Measures average prediction error.
2. **📊 RMSE (Root Mean Square Error):**

   * Penalizes large errors more than MAE.
3. **✅ Precision & Recall:**

   * Precision: % of relevant recommended items.
   * Recall: % of relevant items successfully recommended.

**🔧 Design Issues:**

* Cold start problem.
* Data sparsity.
* Scalability concerns.

**🌟 Limitations:**

* Metrics like MAE don’t capture user satisfaction.
* Offline metrics may not reflect real-time performance.
* Diversity and novelty often ignored in numeric metrics.

**📄 Example:**
A system with high accuracy might still show boring or irrelevant recommendations due to lack of novelty.
