# Object Oriented Software Engineering (CCS356)



# ✅ UNIT I – Software Process and Agile Development

---

## 1. 📘 Introduction to Software Engineering

### 🧠 Definition:

> **Software Engineering** is the application of **engineering principles** to the development, operation, and maintenance of software.

It ensures that software is:

* Reliable
* Maintainable
* Delivered on time
* Cost-effective

---

### 🎯 Objectives of Software Engineering:

* Deliver **high-quality** software that meets user requirements
* Ensure **efficiency**, **scalability**, and **reusability**
* Improve **team coordination** and **project control**
* Handle **complexity** through structured methods

---

### 🧱 Key Characteristics of Good Software:

| Characteristic  | What it means                          |
| --------------- | -------------------------------------- |
| Correctness     | Meets all specified requirements       |
| Efficiency      | Uses resources optimally               |
| Reliability     | Performs without crashing              |
| Maintainability | Easy to fix and update                 |
| Portability     | Works on different systems             |
| Usability       | Easy for users to learn and operate    |
| Security        | Resists unauthorized access or threats |

> `diagram: false`

---

## 2. ⚙️ Software Process

### 💡 Definition:

A **Software Process** is a structured sequence of activities to develop, deliver, and maintain software systems.

---

### 🔄 Activities in a Typical Software Process:

1. **Requirement Analysis**
2. **System Design**
3. **Implementation (Coding)**
4. **Testing**
5. **Deployment**
6. **Maintenance**

Each step feeds into the next, ensuring **smooth progress and quality control**.

> `diagram: true`
> Google: `Software Development Life Cycle diagram`

---

### ✅ Benefits of Following a Process:

* Structured development
* Better project tracking
* Easier maintenance
* Team accountability
* Reduced risk of failure

---

## 3. 📊 Perspective Process Models

### a) **Waterfall Model**

* Linear & sequential
* Each phase must finish before the next begins
* Not flexible to changes

**Best for**: Projects with fixed, well-defined requirements

> `diagram: true`
> Google: `Waterfall model software engineering`

---

### b) **Incremental Model**

* Software is developed and delivered in **parts (increments)**
* Feedback is used after each increment

**Best for**: Feature-rich projects needing fast partial releases

---

### c) **V-Model (Validation & Verification Model)**

* Each dev phase has a corresponding testing phase
* Emphasizes **quality through parallel testing**

**Best for**: Mission-critical systems (healthcare, defense)

---

### d) **Spiral Model**

* Combines iterative nature with **risk analysis**
* Each loop = 4 phases:

  1. Planning
  2. Risk Analysis
  3. Engineering
  4. Evaluation

**Best for**: Large, high-risk, long-term projects

> `diagram: true`
> Google: `Spiral model diagram software engineering`

---

### e) **Agile Model**

* Fast, flexible, customer-focused
* Software is built in **iterations (sprints)** with regular feedback

**Best for**: Projects with frequently changing requirements

---

## 4. 🛠️ Specialized Process Models

### a) **Component-Based Development**

* Reuse of pre-built software components

**Advantage**: Saves time and ensures standardization

---

### b) **Formal Methods Model**

* Uses **mathematics** to define and verify correctness

**Used in**: Safety-critical systems (e.g., aviation, nuclear)

---

### c) **Concurrent Development Model**

* Activities like coding, testing, and design occur **in parallel**

**Used in**: Real-time or distributed systems

> `diagram: false`

---

## 5. ⚡ Introduction to Agility

### 💡 What is Agility?

* Agility = **Speed + Flexibility + Customer Focus**
* Agile teams deliver **small, working features** quickly
* Feedback and changes are welcomed at any stage

---

### 🔥 Agile Manifesto (4 Core Values):

| Agile Prefers ✅            | Over ❌                 |
| -------------------------- | ---------------------- |
| Individuals & interactions | Tools & processes      |
| Working software           | Documentation          |
| Customer collaboration     | Contract negotiation   |
| Responding to change       | Following a fixed plan |

---

### 🧠 Agile Principles (Most Common in Exams):

1. Deliver working software frequently
2. Welcome changing requirements
3. Face-to-face conversation is best
4. Simplicity is essential
5. Build around motivated teams
6. Reflect regularly and adjust

> `diagram: true`
> Google: `Agile process flow scrum diagram`

---

## 6. 🚀 Agile Process

### 🔄 Typical Agile Workflow:

1. Collect requirements as **User Stories**
2. Organize work into **Sprints (2–4 weeks)**
3. Daily **stand-up meetings**
4. **Deliver working software**
5. Take feedback and refine

---

### 👤 Agile Team Roles:

| Role             | Responsibility                          |
| ---------------- | --------------------------------------- |
| Product Owner    | Defines features, priorities            |
| Scrum Master     | Ensures team follows Agile              |
| Development Team | Builds, tests, and delivers the product |

---

## 7. 🧩 Extreme Programming (XP)

### 💡 What is XP?

> A high-discipline agile method focused on **code quality**, **team collaboration**, and **rapid delivery**.

Best for: Projects with **changing requirements** and **tight deadlines**

---

### 🔧 Core XP Practices:

| Practice                   | Meaning                                        |
| -------------------------- | ---------------------------------------------- |
| **Pair Programming**       | Two devs code together, one types, one reviews |
| **TDD (Test-Driven Dev)**  | Write test first, then write code              |
| **Refactoring**            | Clean code without changing behavior           |
| **Continuous Integration** | Merge and test code frequently                 |
| **Small Releases**         | Push updates often for feedback                |
| **Simple Design**          | Build what’s needed now, not extra features    |
| **Collective Ownership**   | Anyone can change any part of the code         |
| **On-site Customer**       | Customer stays available for constant input    |

---

### ⏱️ XP Process Phases:

1. **Planning** – Create user stories, set priorities
2. **Design** – Keep it simple, write test plans
3. **Coding** – Pair programming + TDD
4. **Testing** – Run unit tests & acceptance tests
5. **Listening** – Gather feedback → adapt next sprint

> `diagram: true`
> Google: `XP process diagram software engineering`

---

## 8. 🧪 Case Study – Online Ticket Booking (XP)

* **User stories**: “Search tickets”, “Book seat”, “Cancel booking”
* Devs write unit tests → code with pair programming
* Release every 2 weeks → collect feedback
* System improves with each cycle

---

<br><br>