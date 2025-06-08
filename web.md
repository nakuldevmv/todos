
## ✅ **UNIT I**

### 🌐 Web Essentials: Clients, Servers & Communication

* **Client:** User’s browser (Chrome, Firefox). Sends request.
* **Server:** Stores resources (HTML, CSS, images). Sends response.
* **Communication:** Follows **HTTP Protocol** → Client sends request → Server responds.
* **Diagram: true**
  ➤ *Google “Client-Server architecture diagram”*

---

### 🌍 The Internet vs. World Wide Web

* **Internet:** A global **network of networks**.
* **WWW (Web):** Collection of **web pages** and **resources** accessed via the internet using **HTTP/HTTPS**.
* **URL:** Uniform Resource Locator. Ex: `https://example.com/about.html`

---

### 🔁 HTTP Request & Response Messages

* **Request:** Sent by client to server. Includes:

  * Method (GET, POST)
  * URL
  * Headers
  * Optional Body (in POST)
* **Response:** Sent by server.

  * Status Code (200 OK, 404 Not Found)
  * Headers
  * Body (HTML, JSON, etc.)
* **Diagram: true**
  ➤ *Google “HTTP Request and Response cycle diagram”*

---

### 🧠 Web Clients vs. Web Servers

| Aspect   | Web Client             | Web Server            |
| -------- | ---------------------- | --------------------- |
| Role     | Sends request          | Sends response        |
| Examples | Browser (Chrome, Edge) | Apache, Nginx, Tomcat |
| Language | HTML, CSS, JS          | Java, PHP, Python     |

---

### 💻 HTML5 – Major Features

* **New Elements:** `<article>`, `<section>`, `<nav>`, `<header>`, `<footer>`
* **Multimedia:** `<audio>`, `<video>` with built-in controls
* **Form controls:** `<input type="email">`, `<input type="date">`, `<range>`, etc.
* **Drag and Drop:** Built-in support with JS.
* **Semantic Structure:** Easy accessibility and SEO

---

### 🧾 Tables

Used to display tabular data

```html
<table>
 <tr><th>Name</th><th>Age</th></tr>
 <tr><td>Alice</td><td>21</td></tr>
</table>
```

---

### 📋 Lists

* **Ordered List:** `<ol>` → numbered
* **Unordered List:** `<ul>` → bullets
* **Definition List:** `<dl>`, `<dt>`, `<dd>`

---

### 🖼️ Images

```html
<img src="photo.jpg" alt="Sample Image" width="200">
```

---

### 🔊 Multimedia Controls in HTML5

```html
<audio controls>
  <source src="sound.mp3" type="audio/mpeg">
</audio>

<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
</video>
```

---

### 🎨 CSS3 – Overview

Used to **style** HTML elements. Types:

* **Inline CSS** (inside HTML tag)
* **Internal CSS** (within `<style>` tag)
* **External CSS** (in separate `.css` file)

---

### 📚 Rule Cascading & Inheritance

* **Cascading:** When multiple rules apply, priority: Inline > Internal > External
* **Inheritance:** Child elements inherit parent styles unless overridden

---

### 🌈 CSS3 Features (with examples)

| Feature             | Example                                   |
| ------------------- | ----------------------------------------- |
| **Backgrounds**     | `background-image: url('bg.jpg');`        |
| **Border Images**   | `border-image: url(border.png) 30 round;` |
| **Colors**          | `color: #FF5733;`                         |
| **Shadows**         | `box-shadow: 5px 5px 10px gray;`          |
| **Text Effects**    | `text-shadow: 2px 2px #FF0000;`           |
| **Transformations** | `transform: rotate(10deg);`               |
| **Transitions**     | `transition: background 0.5s ease;`       |
| **Animations**      | Uses `@keyframes` to animate elements     |

---

### 🎯 Example: CSS3 Animation

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.fade {
  animation: fadeIn 2s ease-in;
}
```

---

### 🥾 Bootstrap Framework

* **Responsive CSS framework** developed by Twitter
* Uses **12-column grid system**
* Predefined classes for styling (`btn`, `card`, `alert`, etc.)
* **Responsive Design:** Auto-adjust layout for mobile, tablet, desktop

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">Left</div>
    <div class="col-md-6">Right</div>
  </div>
</div>
```

---


## ✅ **UNIT II**


## 🧠 1. **Introduction to JavaScript**

**JavaScript (JS)** is a **scripting language** used to make websites **interactive**.

* JS runs **on the client-side** (in the browser).
* Used for form validation, animations, event handling, dynamic content, etc.

**Why JS?**

* HTML = structure
* CSS = style
* **JS = behavior / logic**

📌 **Example**: Alert on button click

```html
<button onclick="sayHi()">Click Me</button>
<script>
  function sayHi() {
    alert("Hello there!");
  }
</script>
```

---

## 🌳 2. **DOM Model (Document Object Model)**

DOM is the **tree-like structure** of HTML elements.
JS uses DOM to **access and manipulate HTML/CSS** dynamically.

### 🔧 DOM Core Concepts:

* **document** = the whole webpage.
* **getElementById()**, **getElementsByClassName()**, **querySelector()** — used to grab elements.
* You can **change content, style, structure**.

📌 Example: Change text on click

```html
<p id="demo">Old Text</p>
<button onclick="changeText()">Click Me</button>
<script>
  function changeText() {
    document.getElementById("demo").innerHTML = "New Text";
  }
</script>
```

---

## 🚨 3. **Exception Handling**

JS provides a way to handle **errors at runtime** using:

```js
try {
  // risky code
} catch (err) {
  // error handling
} finally {
  // optional cleanup
}
```

📌 Example:

```js
try {
  let x = y + 1; // y not defined
} catch (err) {
  alert("Error occurred: " + err.message);
}
```

---

## ✅ 4. **Validation**

Form validation ensures **user input is correct** before submission.

📌 Example: Check if name is filled

```html
<form onsubmit="return validateForm()">
  <input type="text" id="name" />
  <input type="submit" />
</form>

<script>
function validateForm() {
  let x = document.getElementById("name").value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
}
</script>
```

---

## 🔄 5. **Built-in Objects in JavaScript**

| Object     | Use                   |
| ---------- | --------------------- |
| **String** | For text manipulation |
| **Number** | For numbers           |
| **Array**  | For list/collection   |
| **Date**   | For date/time         |
| **Math**   | For calculations      |

📌 Example:

```js
let x = Math.sqrt(25);       // 5
let y = "Hello".length;      // 5
let arr = [1, 2, 3];          // array
```

---

## 🧠 6. **Event Handling**

Events = user actions like click, hover, keypress etc.

**JS handles these events using functions called Event Handlers.**

📌 Example:

```html
<button onclick="alert('Button clicked')">Click</button>
```

| Event       | Use             |
| ----------- | --------------- |
| onclick     | Clicked element |
| onmouseover | Mouse hovers    |
| onsubmit    | Form submitted  |
| onkeyup     | Key released    |

---

## 💫 7. **DHTML (Dynamic HTML)**

DHTML = **HTML + CSS + JavaScript + DOM**

It lets webpages **change dynamically without reloading.**

📌 Example:

```html
<p id="para">Hello</p>
<button onclick="document.getElementById('para').style.color='blue'">Change Color</button>
```

---

## 🔗 8. **JSON (JavaScript Object Notation)**

JSON = A lightweight **data exchange format**.

* Used to **send/receive data** between server and browser.
* Easy to read/write.
* Based on **key-value** pairs.

📌 JSON Syntax:

```json
{
  "name": "X",
  "age": 21,
  "city": "Chennai"
}
```

📌 JS Example:

```js
let json = '{"name":"X", "age":21}';
let obj = JSON.parse(json);
console.log(obj.name); // X
```

---

## 📁 9. **Function Files (External JS Files)**

Instead of writing JS in HTML, we can use **external `.js` files**.

📌 Steps:

1. Create `script.js`

```js
function greet() {
  alert("Hello from JS file!");
}
```

2. Link in HTML

```html
<script src="script.js"></script>
```

**Advantage**: Clean code, reusable functions, easy maintenance.

---

# 🌐 **UNIT III**

---

## 1. Java Servlet Architecture

**Definition:** A *Servlet* is a Java class that runs inside a servlet container (e.g., Tomcat) to handle HTTP requests and generate dynamic responses (HTML, JSON, etc.).

### 1.1 Components

* **Client** (Browser): Sends HTTP requests.
* **Web Server / Servlet Container**: Receives requests, manages servlets, handles threading, lifecycle.
* **Servlet**: Java class implementing `javax.servlet.Servlet` (or extending `HttpServlet`).
* **Web Application**: A collection of servlets, JSPs, static files, packaged as a WAR.
* **Database/Backend**: Accessed via JDBC or other APIs.

### 1.2 Request–Response Flow

```text
[Client] ––HTTP Request––> [Servlet Container] ––dispatch––> [Servlet.doGet()/doPost()]
      <--HTTP Response––             <–– Response generation––
```

* **Container** maps URL to servlet, calls its methods, then sends response back.

---

## 2. Servlet Life Cycle

Diagram: **true**

```
Container starts  
    ↓
Load Servlet class & instantiate  
    ↓
init() called once → Servlet ready  
    ↓
service() called per request → doGet()/doPost()  
    ↓
destroy() called once on shutdown → cleanup  
```

### 2.1 Phases

1. **Loading & Instantiation**

   * Container loads servlet class and creates instance.
2. **Initialization** (`init(ServletConfig config)`)

   * One-time setup (DB pools, read config).
3. **Request Handling** (`service()` → `doGet()`/`doPost()`)

   * Called for each request. Branches on HTTP method.
4. **Destruction** (`destroy()`)

   * Called before container unloads servlet. Release resources.

### 2.2 Exam Tips

* Mention that servlets are **multithreaded**: same instance handles concurrent requests.
* Always close DB connections in `destroy()` or after use.

---

## 3. Form GET and POST Actions

### 3.1 GET Method

* **URL Parameters:** `?name=value&…`
* **Visibility:** Data in URL
* **Size Limit:** \~2 KB
* **Use Case:** Data retrieval, bookmarking
* **Servlet Handler:** `doGet(HttpServletRequest, HttpServletResponse)`

```html
<form method="GET" action="SearchServlet">
  <input name="q">
  <button type="submit">Search</button>
</form>
```

```java
protected void doGet(HttpServletRequest req, HttpServletResponse res) {
  String q = req.getParameter("q");
  // process search…
}
```

### 3.2 POST Method

* **Request Body:** Data hidden
* **No Size Limit**
* **Use Case:** Form submissions, sensitive data
* **Servlet Handler:** `doPost(...)`

```html
<form method="POST" action="LoginServlet">
  <input name="user"><input type="password" name="pass">
  <button>Login</button>
</form>
```

```java
protected void doPost(HttpServletRequest req, HttpServletResponse res) {
  String user = req.getParameter("user");
  // authenticate…
}
```

### 3.3 GET vs POST Summary

| Aspect      | GET           | POST               |
| ----------- | ------------- | ------------------ |
| Visibility  | URL           | Body               |
| Security    | Low           | Higher             |
| Idempotent? | Yes           | No                 |
| Use Cases   | Fetch, search | Login, file upload |

---

## 4. Session Handling

### 4.1 Why Session?

HTTP is stateless—server doesn’t remember previous requests. Sessions maintain user state across multiple requests.

### 4.2 How It Works

1. **Client requests** servlet → `request.getSession()`
2. If no session, container creates one and sends a cookie `JSESSIONID` to client.
3. Client sends `JSESSIONID` cookie in subsequent requests.
4. Server matches ID to `HttpSession` object.

```java
// Creating or retrieving session
HttpSession session = request.getSession(true);
session.setAttribute("username", "X");

// Retrieve data later
String user = (String) session.getAttribute("username");

// Invalidate session on logout
session.invalidate();
```

### 4.3 Exam Points

* Sessions stored **server-side** → more secure than cookies.
* Default timeout \~30 min; configurable in `web.xml`.

---

## 5. Understanding Cookies

### 5.1 What Are Cookies?

Small key–value pairs stored on client’s browser.

### 5.2 Setting & Reading in Servlets

```java
// Setting a cookie
Cookie c = new Cookie("theme", "dark");
c.setMaxAge(60*60*24); // 1 day
response.addCookie(c);

// Reading cookies
Cookie[] cookies = request.getCookies();
for (Cookie ck : cookies) {
  if ("theme".equals(ck.getName())) {
    String theme = ck.getValue();
  }
}
```

### 5.3 Cookie vs Session

| Feature    | Cookie               | Session                  |
| ---------- | -------------------- | ------------------------ |
| Storage    | Client               | Server                   |
| Security   | Less (user can edit) | More                     |
| Size Limit | \~4 KB               | Depends on server memory |

---

## 6. Database Connectivity: JDBC

### 6.1 JDBC Workflow

1. **Load Driver**

   ```java
   Class.forName("com.mysql.cj.jdbc.Driver");
   ```
2. **Open Connection**

   ```java
   Connection conn = DriverManager.getConnection(
     "jdbc:mysql://localhost:3306/mydb", "root", "pass");
   ```
3. **Create Statement**

   ```java
   PreparedStatement ps = conn.prepareStatement(
     "INSERT INTO students(name,age) VALUES(?,?)");
   ps.setString(1, name);
   ps.setInt(2, age);
   ```
4. **Execute Query**

   * `executeUpdate()` for INSERT/UPDATE/DELETE
   * `executeQuery()` for SELECT
5. **Process ResultSet**

   ```java
   ResultSet rs = ps.executeQuery("SELECT * FROM students");
   while (rs.next()) {
     String n = rs.getString("name");
   }
   ```
6. **Close Resources**

   ```java
   rs.close(); ps.close(); conn.close();
   ```

### 6.2 Example Servlet with JDBC

```java
@WebServlet("/RegisterServlet")
public class RegisterServlet extends HttpServlet {
  protected void doPost(HttpServletRequest req, HttpServletResponse res)
      throws ServletException, IOException {
    String name = req.getParameter("name");
    int age = Integer.parseInt(req.getParameter("age"));

    try {
      Class.forName("com.mysql.cj.jdbc.Driver");
      Connection conn = DriverManager
        .getConnection("jdbc:mysql://localhost:3306/webdb","root","");
      PreparedStatement ps = conn.prepareStatement(
        "INSERT INTO users(name,age) VALUES(?,?)");
      ps.setString(1, name);
      ps.setInt(2, age);
      int count = ps.executeUpdate();
      res.getWriter().println(count + " record(s) inserted");
      ps.close(); conn.close();
    } catch (Exception e) {
      throw new ServletException(e);
    }
  }
}
```

---
