# Recommender System (CCS360)



# 🔥 Topic: Introduction & Basic Taxonomy of Recommender Systems

**diagram: true**
**Google Search:** `taxonomy of recommender systems diagram` or `types of recommender systems`

---

## 📌 INTRODUCTION TO RECOMMENDER SYSTEMS

### 💡 What’s a Recommender System (RS)?

A **Recommender System** is a tool that filters and presents information or products based on a user’s interests and behavior. It’s like a personal shopping assistant in your phone or laptop.

### 🎯 Goal:

To predict what a user might like next and recommend it. Simple, but powerful.

### 📱 Real-Life Examples:

| Platform | What’s Recommended                      |
| -------- | --------------------------------------- |
| Netflix  | Movies and shows                        |
| Amazon   | Products based on purchase/view history |
| Spotify  | Songs you might vibe with               |
| YouTube  | Videos based on past viewing patterns   |

---

## 🤖 WHY RECOMMENDER SYSTEMS EXIST

* **Too much info, not enough time** – Users are overwhelmed. RS helps them decide.
* **Boosts business** – Increases click-through, time spent, purchases.
* **Improves UX** – Makes apps feel smart and personalized.

🧠 Exam Tip:
Short 2-mark question could be:
**"What is a Recommender System? Give any two examples."**

---

## 🧬 BASIC TAXONOMY OF RECOMMENDER SYSTEMS

**Taxonomy** means classification. Think of it like genres in music — you got types based on how they recommend stuff.

---

### 1. 🎯 **Content-Based Filtering (CBF)**

**Idea:** “If you liked this, you’ll like that.”
Recommends items similar to what the user already liked.

#### ✅ How?

* Uses item **features** (genre, category, tags)
* Builds a user profile of their preferences
* Compares new items to this profile using **similarity scores**

#### 🧠 Example:

* Netflix recommends another sci-fi show because you watched “Stranger Things”

**Strengths:**

* Works for new users
* No need for data from other users

**Limitations:**

* Can be *too narrow* (user stuck in filter bubble)
* Can’t recommend diverse stuff

---

### 2. 🧑‍🤝‍🧑 **Collaborative Filtering (CF)**

**Idea:** “People like you also liked this.”

#### ✅ How?

* Looks at what **similar users** liked
* Doesn’t care about item features, just behavior patterns
* Types:

  * **User-based CF** – Finds similar users
  * **Item-based CF** – Finds similar items

#### 🧠 Example:

* Spotify suggests songs liked by people who listen to similar artists as you

**Strengths:**

* Can discover surprising or “serendipitous” items
* No need to know what item is about

**Limitations:**

* Struggles with new users/items (cold start)
* Needs a big pool of data

---

### 3. 🔥 **Hybrid Filtering**

**Idea:** “Let’s take the best of both worlds.”

#### ✅ How?

* Combines Content-Based + Collaborative Filtering
* More accurate and robust

#### 🧠 Example:

* Netflix uses hybrid: combines your ratings with similar users & item genres

**Strengths:**

* Handles cold start better
* More accurate

**Limitations:**

* Can be complex to build

---

### 4. 🌍 **Non-Personalized Recommendations**

**Idea:** “Popular = Good”

#### ✅ How?

* Shows same results to all users
* Based on global stats: popularity, recency, trends

#### 🧠 Example:

* YouTube Trending
* Amazon’s “Top Sellers”

**Strengths:**

* Simple and fast
* No user data needed

**Limitations:**

* Not personalized at all
* Not useful in long-term engagement

---

### 🔁 Summary Table

| Type             | Based On               | Personalized? | Example                        |
| ---------------- | ---------------------- | ------------- | ------------------------------ |
| Content-Based    | Item features          | ✅             | “More like this”               |
| Collaborative    | User behavior patterns | ✅             | “Users like you also liked...” |
| Hybrid           | Combo of above         | ✅             | Netflix                        |
| Non-Personalized | Popularity/trends      | ❌             | “Top 10 Movies” list           |

---

