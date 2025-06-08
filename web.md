
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
