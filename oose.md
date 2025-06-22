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

<br><br>


# 🧠 **UNIT III – SOFTWARE DESIGN**

> *Design is not just what it looks like, but how it works.*
> This unit dives deep into the blueprint stage of software — how it’s structured, how its pieces fit, and how it all runs smoothly behind the scenes.

---

## 🧱 1. Software Design

**Definition:**
The process of **transforming requirements** into a detailed design blueprint to guide implementation.

**Goals:**

* Satisfy functional & non-functional requirements
* Promote reusability, reliability, and simplicity
* Make code modular, scalable, and maintainable

**Outcome:**

* Design Documents
* Architecture Diagrams
* Component Specifications

---

## 🔧 2. Design Process

A step-by-step method to structure the design of software from requirements to components.

### 🌀 Phases:

1. **Architectural Design**

   * High-level structure of the system
   * Defines major modules & how they interact
   * *Output*: Architecture Diagram
2. **Component-Level Design**

   * Internal logic & structure of each module
   * Interfaces, data flow, algorithms
3. **Interface Design**

   * User interfaces (UID)
   * Interfaces between components
4. **Data Design**

   * Structures for input, output, and internal data
   * Database schema, file formats, etc.

> `diagram: true`
> Google: `software design process diagram`

---

## 💡 3. Design Concepts

| Concept                     | Meaning                                                   |
| --------------------------- | --------------------------------------------------------- |
| **Abstraction**             | Focus only on essential details; hide complexity          |
| **Modularity**              | Divide software into small, manageable parts (modules)    |
| **Information Hiding**      | Hide inner logic from other modules                       |
| **Refinement**              | Develop from general ideas to detailed steps              |
| **Functional Independence** | Keep modules independent via low coupling + high cohesion |
| **Design for Change**       | Build in flexibility for future changes                   |

---

## 🔗 4. Coupling and Cohesion

### 🔌 Coupling (Between modules – should be low)

* **High coupling = Bad** → Modules depend too much on each other
* **Low coupling = Good** → Easy to change one without breaking others

**Types of Coupling:**

* Content (worst)
* Common
* Control
* Stamp
* Data
* No coupling (best)

### 🧬 Cohesion (Within a module – should be high)

* **High cohesion = Good** → Module does one thing well
* **Low cohesion = Bad** → Unrelated responsibilities

**Types of Cohesion:**

* Coincidental (worst)
* Logical
* Temporal
* Procedural
* Communicational
* Sequential
* Functional (best)

✅ **Golden Rule:**
**High Cohesion + Low Coupling = Clean Design**

---

## 🧠 5. Functional Independence

**Meaning:**
Modules should work independently — **self-contained, focused, and loosely connected**.

**Achieved by:**

* Designing for single responsibility
* Minimizing coupling
* Maximizing cohesion

**Benefits:**

* Easier debugging
* Reusability
* Parallel development possible

---

## 🧩 6. Design Patterns

Pre-tested solutions to common design problems.

### 🌐 Model-View-Controller (MVC) – `diagram: true`

Google: `mvc architecture diagram`

* **Model** – Manages data and logic
* **View** – UI/display to the user
* **Controller** – Takes input and updates model/view

Example: In a shopping app

* View = Product page
* Controller = “Add to cart” logic
* Model = Cart data

---

### 🔀 Common Design Patterns

| Pattern               | Purpose & Real-Life Example                                        |
| --------------------- | ------------------------------------------------------------------ |
| **Observer**          | Notify many objects when one changes (📢 News update system)       |
| **Strategy**          | Choose algorithm at runtime (💳 Payment method selection)          |
| **Command**           | Encapsulate requests as objects (🧾 Undo/Redo in Word)             |
| **Adapter**           | Convert interface to another (🔌 Laptop charger adapter)           |
| **Facade**            | Simplified interface to complex system (🏨 Hotel front desk)       |
| **Proxy**             | Placeholder that controls access (🛡️ Firewall or caching server)  |
| **Publish-Subscribe** | Loose communication via events (📬 Newsletter system, event buses) |

---

## 🏛️ 7. Architectural Styles

### 1. **Layered Architecture**

* Stack of layers (Presentation → Business Logic → Data Access → DB)
* Easy to manage, test, scale
* `diagram: true`
  Google: `layered architecture software engineering`

---

### 2. **Client–Server Architecture**

* Clients request, servers respond
* Used in most internet/web systems
* `diagram: true`
  Google: `client server architecture diagram simple`

---

### 3. **Tiered (N-Tier) Architecture**

* Like Layered but deployed on **different machines**
* Eg: UI on mobile, logic on server, DB in cloud
* `diagram: true`
  Google: `n-tier architecture diagram`

---

### 4. **Pipe and Filter Architecture**

* Data flows through processing units (filters) in sequence
* Eg: Audio/Video processing, Compilers
* `diagram: true`
  Google: `pipe and filter architecture diagram`

---

## 🎨 8. User Interface Design (UID)

**Goal:**
Make the system **easy, clear, and enjoyable** to use.

### ✨ UID Principles:

* **Clarity**: Everything should be obvious
* **Consistency**: Keep similar designs across screens
* **Feedback**: Let users know something happened
* **Affordance**: Buttons should look like buttons
* **Error Recovery**: Undo options, helpful error messages
* **Responsiveness**: Fast UI, no lag

### 🧪 UID Design Process:

1. Understand the user (age, skills, goals)
2. Create use cases
3. Design layout (wireframes)
4. Build prototype
5. Test & Improve

> `diagram: true`
> Google: `user interface design process diagram`

---

## 🧾 9. Case Study (Example: ATM System)

**Architecture Used:** Layered
**Patterns Used:**

* MVC for screen flow
* Strategy for transaction types (Withdraw, Deposit)
* Observer to update balance on screen

**UID Elements:**

* Clear button layout
* Error messages for invalid PIN
* Feedback for transaction success

---

<br><br>


# ✅ **UNIT IV – SOFTWARE TESTING AND MAINTENANCE**

---

## 🔹 1. **Testing**

> Testing is the process of executing software to detect bugs and verify correctness.

* Ensures software meets user needs
* Detects defects early = cheaper fixes
* Done before release and after updates

**Types of Testing:**

* Manual vs Automated
* Static vs Dynamic
* Functional vs Non-functional

**diagram: false**

---

## 🔹 2. **Unit Testing**

> Testing the **smallest testable parts of code** (functions, methods).

* Done by developers
* Focuses on **individual components**
* Usually uses **White Box Testing**

**Tools**: JUnit (Java), NUnit (.NET)

**diagram: false**

---

## 🔹 3. **Integration Testing**

> Testing combined modules to ensure they work together.

### Types of Integration Testing:

* **Top-Down**: Start with high-level modules; use **stubs**
* **Bottom-Up**: Start with low-level modules; use **drivers**
* **Big Bang**: All modules integrated at once

  > High risk but easy setup

**diagram: true**
Google: `top down vs bottom up integration testing diagram`

---

## 🔹 4. **System Testing**

> Test the **entire system** as a whole.
> Simulates real-world use by end users.

* Checks compliance with requirements
* Includes performance, load, usability, etc.
* Done after integration testing

**diagram: false**

---

## 🔹 5. **Regression Testing**

> Re-testing software after code changes to ensure **existing features still work**.

* Detects side-effects of new code
* Often automated
* Critical for maintenance

✅ Example: Fix in login module → Check if dashboard, logout, etc., still work

**diagram: false**

---

## 🔹 6. **Black Box Testing**

> Tester checks **input → output** without seeing internal code.

* Focus on **functionality**
* Tests user interface, features
* Used in **System & Acceptance Testing**

### Techniques:

* Equivalence Partitioning
* Boundary Value Analysis

**diagram: true**
Google: `black box testing diagram input output`

---

## 🔹 7. **White Box Testing**

> Tester knows the **code and internal logic**

* Used in Unit Testing
* Focus on conditions, branches, loops
* Done by developers

### Techniques:

* Statement Coverage
* Branch Coverage
* Loop Testing
* Path Testing

**diagram: true**
Google: `white box testing flow diagram`

---

## 🔹 8. **Debugging**

> Process of **identifying and fixing bugs** after testing.

### Techniques:

* Print statements/logs
* Breakpoints
* Step-by-step execution
* Watching variables
* IDE Debugging tools

✅ It’s like a doctor diagnosing and treating code sickness 🧑‍⚕️

**diagram: false**

---

## 🔹 9. **Program Analysis**

> Examining the source code to detect issues — with or without execution.

### Types:

* **Static Analysis**: Without running code
  e.g. Lint tools
* **Dynamic Analysis**: During execution
  e.g. Memory profilers

✅ Helps find unused variables, unreachable code, memory leaks

**diagram: false**

---

## 🔹 10. **Symbolic Execution**

> Program is executed with **symbolic inputs** (like `x`, `y`) instead of real values to explore **all possible paths**.

* Builds **path conditions**
* Detects deep logic errors
* Used in **security & verification tools**

✅ Example: `if (x > 0)` explored as both true and false

**diagram: true**
Google: `symbolic execution path tree example`

---

## 🔹 11. **Model Checking**

> Exhaustively verifies if a system model satisfies properties like **safety** and **liveness**.

* Uses finite state machines
* Explores **all possible system states**
* Used in **critical systems** like aircraft, banking, etc.

✅ Example: Check if a train system never allows two trains on the same track

**Tools**: SPIN, NuSMV

**diagram: true**
Google: `model checking finite state machine example`

---

## 🔹 12. **Case Study Example: Railway Reservation System**

### Applies:

* **Unit Testing**: Login, seat selection
* **Integration Testing**: Search → Book → Payment
* **System Testing**: Full user journey
* **Regression Testing**: After bug fix in payment
* **Black Box**: Tester checks error handling, UI
* **White Box**: Dev checks internal logic
* **Debugging**: Fix for double-booking issue
* **Maintenance**:

  * **Corrective**: Fix printing bug
  * **Adaptive**: Add UPI support
  * **Perfective**: Speed up search
  * **Preventive**: Refactor seat allocation logic

---

<br><br>



# ✅ UNIT V – PROJECT MANAGEMENT

**Subject: Object Oriented Software Engineering – CCS356**
**Focus:** Software Project Management + DevOps (full-stack breakdown, no fluff, only that real stuff)
**diagram: true** (for project scheduling + deployment pipeline)

---

## 💼 1. **Software Project Management (SPM)**

### 🔍 What is SPM?

SPM is the art and science of **planning, executing, monitoring, and closing software projects** — making sure the product is delivered on time, within budget, and with the desired quality.

### 🧱 Key Objectives:

* **On-time delivery**
* **Budget control**
* **Scope clarity**
* **Stakeholder satisfaction**

### 🧠 Core Activities in SPM:

1. **Project Planning**

   * Define scope, goals, budget, timeline
   * Create Work Breakdown Structure (WBS)
   * Identify resources and constraints
   * Risk analysis & mitigation planning

2. **Project Execution**

   * Assign tasks to team members
   * Coordinate efforts, hold standups
   * Communicate status to stakeholders

3. **Monitoring and Controlling**

   * Track progress (time, cost, scope)
   * Manage changes
   * Control risks
   * Update plans based on project health

4. **Project Closure**

   * Final delivery
   * Project documentation
   * Lessons learned
   * Post-mortem analysis

### 💥 Challenges in SPM:

* Scope creep
* Budget overruns
* Poor communication
* Underestimated timelines
* Inexperienced teams

---

## 🗂️ 2. **Software Configuration Management (SCM)**

### 🎯 Purpose:

SCM is all about **controlling changes** to software to maintain integrity and traceability.

### 🧩 SCM = Control + Trace + Audit

### 🧰 Key Components:

1. **Version Control**

   * Track file changes over time
   * Enable team collaboration without conflict
   * Examples: Git, SVN, Mercurial

2. **Configuration Identification**

   * Label all config items (source code, docs, libs)
   * Define structure of software system

3. **Change Control**

   * Set process for reviewing, approving, and tracking changes
   * Change requests → Impact analysis → Approval/rejection

4. **Configuration Status Accounting**

   * Record/report on status of config items
   * Version history, who changed what & when

5. **Configuration Auditing**

   * Ensure system conforms to requirements
   * Verify approved changes are applied correctly

### 💡 Benefits of SCM:

* Prevents overwriting
* Maintains system stability
* Easier debugging with version history
* Accountability and traceability

---

## 📆 3. **Project Scheduling**

### 🧠 What It Means:

Project scheduling is the process of defining **when tasks happen**, **who does them**, and **how long they take**, so that the entire project gets done smoothly.

### 🧰 Steps in Scheduling:

1. **Identify activities**
   Break the project into small tasks using WBS.

2. **Determine dependencies**
   Figure out what tasks must be done before others.

3. **Estimate time & resources**
   Calculate how long each task takes and what tools/people are needed.

4. **Create the schedule**
   Use tools like Gantt charts and CPM to visualize the plan.

5. **Track & update**
   Continuously monitor and tweak schedule during the project.

### 🧩 Techniques & Tools:

* **Gantt Chart**
  Visual timeline with task bars (📌 diagram: true)
  Use Google: `Gantt chart project scheduling software engineering`

* **PERT (Program Evaluation Review Technique)**
  Graph that shows task dependencies with estimated times
  Optimistic, Pessimistic, Most likely times

* **Critical Path Method (CPM)**
  Find the sequence of tasks that directly affects project duration
  If a task on this path delays → whole project delays

### 🛠️ Terms You Gotta Know:

* **Slack/Float**: Extra time a task can take without delaying project
* **Milestone**: Key checkpoints in the schedule
* **Baseline Schedule**: Original timeline used for comparison

---

## 🛠️ 4. **DevOps** (The Real MVP)

---

### a) ⚡ **Motivation for DevOps**

Before DevOps, dev and ops were two separate worlds.

* Devs: "It works on my machine!"
* Ops: "But it's crashing in prod!"

#### DevOps Fixes That With:

* **Automation over manual processes**
* **Fast, frequent, reliable deployments**
* **Collaboration and feedback loops**
* **Continuous delivery of value**

### 🤝 Dev + Ops + QA + Security = One Team

It’s a **culture shift** powered by tools and mindset.

---

### b) ☁️ **Cloud as a Platform**

Cloud platforms make DevOps scalable, flexible, and powerful.
Examples: **AWS, Azure, Google Cloud**

### 🚀 Benefits of Cloud in DevOps:

* **On-demand infrastructure**: Spin servers up/down anytime
* **Auto-scaling**: Handle traffic spikes
* **Global deployments**: Launch services worldwide
* **Service integrations**: Databases, AI, storage, etc.

### 🧠 Cloud Features Used:

* Infrastructure as a Service (IaaS)
* Platform as a Service (PaaS)
* Serverless Functions (like AWS Lambda)
* Virtual Machines and Containers

---

### c) 🔧 **Operations in DevOps**

### 👨‍💻 Key Ops Tasks:

1. **Infrastructure Provisioning**

   * Automate server setup using Terraform/CloudFormation

2. **Environment Management**

   * Maintain Dev, QA, Staging, Production separately

3. **Monitoring & Alerting**

   * Use tools like Prometheus, Datadog, or ELK stack
   * Detect issues before users do

4. **Security Management**

   * Ensure secure deployments
   * Handle secrets, credentials, and vulnerability scanning

5. **Log Management**

   * Centralized logs = faster debugging and root cause analysis

---

### d) 🚀 **Deployment Pipeline**

A DevOps pipeline is an automated sequence from **code commit → production deployment**.
(📌 diagram: true)
Search: `CI CD DevOps pipeline diagram`

### ⚙️ Stages in the Pipeline:

1. **Source**

   * Dev commits code to repo (GitHub, GitLab)

2. **Build**

   * Code compiled, dependencies installed

3. **Test**

   * Run unit/integration tests (e.g., JUnit, Selenium)

4. **Package**

   * Bundle into deployable artifact or Docker image

5. **Release**

   * Move package to artifact repo (e.g., DockerHub)

6. **Deploy**

   * Automatic/Manual push to production (Kubernetes, Ansible)

7. **Operate & Monitor**

   * Alerting, logging, uptime checks

### 🧠 Benefits:

* Faster delivery
* Fewer bugs in production
* Easier rollback
* Confidence in deployments

---

### e) 🔧 **DevOps Tools**

| **Purpose**              | **Popular Tools**              |
| ------------------------ | ------------------------------ |
| Version Control          | Git, GitHub, Bitbucket         |
| CI/CD                    | Jenkins, CircleCI, TravisCI    |
| Containerization         | Docker, Podman                 |
| Container Orchestration  | Kubernetes, Docker Swarm       |
| Configuration Management | Ansible, Puppet, Chef          |
| Infra as Code (IaC)      | Terraform, CloudFormation      |
| Monitoring & Logging     | Prometheus, Grafana, ELK Stack |
| Collaboration & Tracking | JIRA, Slack, Teams             |
| Code Quality & Testing   | SonarQube, Selenium, JUnit     |

---

### f) 📘 **Case Study – DevOps in Action**

Let’s say a **food delivery app** like Zomato went DevOps-mode.

### ⚙️ Problems Faced:

* Crashes during promo hours
* Bugs going unnoticed
* Delays in deploying new features

### 🛠️ DevOps Implementation:

* Source Code: GitHub
* CI/CD: Jenkins → automated builds and tests
* Containerization: Docker
* Deployment: Kubernetes
* Infra Mgmt: Terraform (IaC)
* Monitoring: Prometheus + Grafana
* Communication: Slack + JIRA

---
