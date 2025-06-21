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



# ✅ UNIT II – REQUIREMENTS ANALYSIS AND SPECIFICATION

---

## 1. 🔍 **Requirement Analysis and Specification**

### 💡 Purpose:

To understand what the customer needs and translate that into clear, structured requirements that developers can actually build.

### 🔑 Steps:

1. **Requirements Elicitation** – Finding out what the user wants
2. **Requirements Analysis** – Removing contradictions, resolving ambiguity
3. **Specification** – Writing the requirements formally (→ SRS)
4. **Validation** – Making sure the requirements are complete and correct

### 🎯 Goal:

Make sure **everyone** (client + devs) knows **exactly** what’s being built. No surprises later.

---

## 2. 🧠 **Requirements Gathering and Analysis**

### 📌 Gathering Techniques:

* **Interviews** – 1-on-1 with users
* **Questionnaires** – Mass data collection
* **Observation** – Watch how current systems work
* **Prototyping** – Show rough version, get feedback
* **Brainstorming** – Get ideas from stakeholders

### 🧠 Analysis Techniques:

* Identify conflicts between user expectations
* Classify into:

  * **Functional Requirements** – What system should do
  * **Non-Functional Requirements** – How well it should do it (speed, security)
* Use **prioritization**, **traceability**, and **feasibility checks**

---

## 3. 📄 **Software Requirement Specification (SRS)** 🔥 (Very Important)

### 💡 What it is:

A detailed **document** that describes the complete functionality, behavior, and constraints of the software system.

### ✍️ Contents of SRS:

* Introduction (scope, purpose)
* Overall description
* Functional requirements
* Non-functional requirements
* External interface requirements
* Constraints (legal, safety, hardware, etc.)

### ✅ Qualities of a good SRS:

* **Complete**
* **Unambiguous**
* **Consistent**
* **Modifiable**
* **Verifiable**
* **Traceable**

### 🔥 Example Functional Requirement:

> "The system shall allow users to log in with a valid username and password."

> diagram: true
> Google: `SRS document format software engineering`

---

## 4. 📐 **Formal System Specification**

### 💡 Definition:

Writing requirements in **mathematical logic** form using formal methods like:

* Predicate logic
* Set theory
* Z notation, VDM, or B-methods

### 📌 Used when:

* System is **mission-critical**
* You need to **mathematically prove** correctness

### 🔥 Example:

```
∀ user (validPIN(user) → allowAccess(user))
```

> diagram: true
> Google: `formal specification example Z notation`

---

## 5. 🔄 **Finite State Machines (FSM)**

### 💡 What it is:

A model that describes a system that **changes state** based on **inputs**.

### 🧱 Components:

* States (circles)
* Transitions (arrows)
* Inputs
* Start & End states

### 📌 Example:

**ATM**:
Idle → (Insert Card) → Auth → (Enter PIN) → Transaction → Exit

### 🔥 Use Cases:

* Traffic lights 🚦
* Login systems
* Protocols

> diagram: true
> Google: `FSM ATM system example`

---

## 6. 🧩 **Petri Nets**

### 💡 What it is:

Used for modeling **concurrent** or **parallel** systems.

### 🧠 Components:

* **Places** – Conditions (circles)
* **Transitions** – Events (rectangles)
* **Tokens** – Represent data/state (dots)
* **Arcs** – Show direction

### 📌 System example:

Shared printer system – multiple users sending print jobs.

### 🎯 Use for:

* Workflow control
* Parallel process tracking
* Avoiding deadlocks

> diagram: true
> Google: `petri net printer example`

---

## 7. 🧠 **Object Modelling Using UML**

> UML = Unified Modeling Language
> Used to **visualize**, **design**, and **document** OO systems.

### 🔥 Core Diagrams You Should Know:

---

### 7.1 👤 Use Case Diagram

* Shows **who does what** (Actor → Use case)
* Great for capturing **functional requirements**

> Example: Passport system – Apply, Upload docs, Track status

> diagram: true
> Google: `UML use case diagram passport`

---

### 7.2 📦 Class Diagram

* Shows **classes**, **attributes**, **methods**, and relationships
* Use for **object-oriented structure**

> Example: ATM: Account, Card, Transaction classes

> diagram: true
> Google: `UML class diagram ATM system`

---

### 7.3 🔄 Activity Diagram

* Like a flowchart but better
* Used to model **logic/workflows**

> Example: User login → validate → show dashboard

> diagram: true
> Google: `UML activity diagram login system`

---

### 7.4 🧬 Sequence Diagram

* Focuses on **message flow** between objects over time
* Vertical = time
* Horizontal = participants

> diagram: true
> Google: `UML sequence diagram online shopping`

---

### 7.5 🔄 State Chart Diagram

* Shows how an object **changes state over time**
* Good for modeling **lifecycle**

> Example: Order → Packed → Shipped → Delivered

> diagram: true
> Google: `state chart diagram order process UML`

---

## 8. 🔁 **Functional Modelling (DFD)**

> Shows how **data moves** and how it is **processed** in a system

### 📊 Data Flow Diagram (DFD)

* **Level 0** – Big Picture (context)
* **Level 1** – Sub-processes
* Components:

  * Processes (circles)
  * Data Stores
  * External Entities
  * Arrows (data flow)

> Example: ATM – Card insert → Auth → Show balance → Withdraw

> diagram: true
> Google: `DFD level 0 and level 1 ATM`

---

## 9. 🧰 **CASE Tools (Computer Aided Software Engineering)**

### 💻 What They Do:

* Help in **designing**, **analyzing**, **coding**, **testing**, **documenting**

### 🔧 Types:

* **Upper CASE** – Planning, analysis, design (e.g., StarUML)
* **Lower CASE** – Coding, testing (e.g., Selenium, JUnit)
* **Integrated CASE** – Full support (e.g., Visual Paradigm)

### ✅ Benefits:

* Save time
* Reduce error
* Automate routine tasks
* Ensure documentation consistency

---

