
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
---
---
---
---
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
---
---
---
---
---

# 🌐 **UNIT III**


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
---
---
---
---
---


# 🐘 **UNIT IV**


## Part A – PHP (Server-Side Scripting)

### 1. **Introduction to PHP**

* **Definition:** PHP (Hypertext Preprocessor) is a **server-side scripting language** embedded within HTML to create **dynamic** web pages.
* **Execution Flow (diagram: true):**

  1. Client requests `page.php`
  2. Web server (Apache/Nginx) hands it to PHP interpreter
  3. PHP executes code & outputs HTML
  4. Server returns HTML to client
* **Features:**

  * Free & Open Source
  * Cross-platform (Windows, Linux, macOS)
  * Built-in support for databases (MySQL, PostgreSQL, SQLite)
  * Vast standard library of built-in functions

---

### 2. **Embedding PHP in HTML**

```html
<!DOCTYPE html>
<html>
<head><title>PHP Demo</title></head>
<body>
  <h1><?php echo "Hello, " . htmlspecialchars($_GET['name'] ?? 'Guest'); ?>!</h1>
</body>
</html>
```

* **`<?php … ?>`** tags denote PHP code.
* **`echo`** outputs text.
* Always **sanitize** user inputs (e.g. `htmlspecialchars`) to prevent XSS.

---

### 3. **PHP Variables**

* Begin with `$`, e.g. `$age`, `$userName`.
* **Dynamic Typing:** No need to declare type.
* **Data Types:**

  * **Scalar:** `int`, `float`, `string`, `bool`
  * **Compound:** `array`, `object`
  * **Special:** `resource`, `NULL`

```php
<?php
$name   = "X";
$age    = 21; 
$salary = 50000.75;
$isEmp  = true;
$hobbies = ["coding", "gaming", "reading"];
?>
```

---

### 4. **Program Control Structures**

#### 4.1 Conditional Statements

```php
if ($age < 18) {
  echo "Minor";
} elseif ($age < 65) {
  echo "Adult";
} else {
  echo "Senior";
}
```

#### 4.2 Switch

```php
switch ($role) {
  case 'admin':   echo "Full Access"; break;
  case 'editor':  echo "Edit Access"; break;
  default:        echo "View Only";
}
```

#### 4.3 Loops

* **for**

  ```php
  for ($i = 0; $i < 5; $i++) {
    echo $i;
  }
  ```
* **while**

  ```php
  $i = 0;
  while ($i < 5) {
    echo $i++;
  }
  ```
* **foreach** (arrays)

  ```php
  foreach ($hobbies as $hobby) {
    echo $hobby;
  }
  ```

---

### 5. **Built-In Functions**

PHP ships with thousands of functions. Key categories:

| Category      | Functions Examples                         | Usage                              |
| ------------- | ------------------------------------------ | ---------------------------------- |
| **String**    | `strlen()`, `strpos()`, `str_replace()`    | Text processing                    |
| **Array**     | `count()`, `array_push()`, `sort()`        | Data structure manipulation        |
| **Math**      | `abs()`, `round()`, `pow()`                | Arithmetic operations              |
| **Date/Time** | `date()`, `strtotime()`, `time()`          | Handling dates & timestamps        |
| **File I/O**  | `fopen()`, `fread()`, `fwrite()`, `file()` | Reading/writing files              |
| **Filter**    | `filter_var()`, `filter_input()`           | Validating & sanitizing user input |

**Example:**

```php
<?php
$str = "Hello World";
echo strlen($str);                // 11
echo str_replace("World", "X", $str); // Hello X
$arr = [3, 1, 2];
sort($arr);
print_r($arr); // [1,2,3]
?>
```

---

### 6. **Form Handling & Validation**

#### 6.1 HTML Form (form.php)

```html
<form method="POST" action="process.php">
  Name: <input type="text" name="name"><br>
  Email: <input type="text" name="email"><br>
  Age: <input type="number" name="age"><br>
  <input type="submit" value="Submit">
</form>
```

#### 6.2 PHP Processing (process.php)

```php
if (empty($name)) {
  echo "❌ Name is required<br>";
} elseif (!preg_match("/^[a-zA-Z ]*$/", $name)) {
  echo "❌ Only letters and spaces allowed in name<br>";
} else {
  echo "✅ Name: $name<br>";
}

if (empty($email)) {
  echo "❌ Email is required<br>";
} elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  echo "❌ Invalid email format<br>";
} else {
  echo "✅ Email: $email<br>";
}

if (empty($age)) {
  echo "❌ Age is required<br>";
} elseif (!is_numeric($age) || $age < 0 || $age > 120) {
  echo "❌ Enter a valid age (0-120)<br>";
} else {
  echo "✅ Age: $age<br>";
}
```
> **Exam Tip:** Emphasize **server-side security**, preventing XSS and invalid data.

---

## Part B – XML (Data Representation & Validation)

---

### 7. **Basic XML Structure**

* Plain text, hierarchical, self-descriptive.
* **Well-formed** rules: single root, nested properly, tags closed, case-sensitive, attribute values quoted.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book id="b1">
    <title>Web Tech</title>
    <author>X</author>
    <price>299</price>
  </book>
</bookstore>
```

---

### 8. **Document Type Definition (DTD)**

* **Purpose:** Define valid element names, order, and attributes.
* **Internal DTD** (inside the XML):

  ```xml
  <!DOCTYPE bookstore [
    <!ELEMENT bookstore (book+)>
    <!ELEMENT book (title,author,price)>
    <!ATTLIST book id ID #REQUIRED>
    <!ELEMENT title (#PCDATA)>
    <!ELEMENT author (#PCDATA)>
    <!ELEMENT price (#PCDATA)>
  ]>
  ```
* **External DTD** (in `bookstore.dtd`):

  ```dtd
  <!ELEMENT bookstore (book+)>
  …
  ```

  Reference in XML:

  ```xml
  <!DOCTYPE bookstore SYSTEM "bookstore.dtd">
  ```

> **Exam Tip:** Distinguish between **well-formed** (syntax) vs **valid** (DTD/XSD).

---

### 9. **XML Schema Definition (XSD)**

* **More powerful** than DTD: typed data, namespaces, min/max occurrences.

```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="bookstore">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="book" maxOccurs="unbounded">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="title"   type="xs:string"/>
              <xs:element name="author"  type="xs:string"/>
              <xs:element name="price"   type="xs:decimal"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

Attach via:

```xml
<bookstore xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="bookstore.xsd">
```

---

### 10. **XML Parsers & Validation**

| Parser Type | Description                                        | Use Case                   |
| ----------- | -------------------------------------------------- | -------------------------- |
| **DOM**     | Loads whole document as tree; random access        | Small to medium XML        |
| **SAX**     | Event-driven; reads sequentially; low memory usage | Large XML/log files        |
| **StAX**    | Pull-based; programmer-controlled; read/write      | Streaming & transformation |

```java
// Java DOM parsing example
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse("bookstore.xml");
NodeList books = doc.getElementsByTagName("book");
for (int i = 0; i < books.getLength(); i++) {
  Element book = (Element) books.item(i);
  String title = book.getElementsByTagName("title").item(0).getTextContent();
}
```

> **Validation:**
>
> * **Well-formed** checked by any parser by default.
> * **Valid** only if DTD/XSD is associated and parser is set to validate.

---

### 11. **XSL & XSLT (Transformations)**

* **Purpose:** Transform XML documents into HTML, text, or other XML.
* **XSLT Template Example:**

  ```xml
  <?xml version="1.0"?>
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html"/>
    <xsl:template match="/bookstore">
      <html><body><h2>Books</h2>
        <ul>
          <xsl:for-each select="book">
            <li><xsl:value-of select="title"/> by <xsl:value-of select="author"/></li>
          </xsl:for-each>
        </ul>
      </body></html>
    </xsl:template>
  </xsl:stylesheet>
  ```
* Apply in Java/PHP or via browser’s XSLT processor.

---
---
---
---
---
---

# 🌐 **UNIT V**

---

## Part A – AngularJS

### 1. **Introduction to AngularJS**

* **Definition:** AngularJS is a **JavaScript-based MVC (or MVVM) framework** by Google for building **single-page applications (SPAs)**.
* **Key Features:**

  * **Two-way data binding**
  * **Dependency injection**
  * **Directives** for extending HTML
  * **Modularity** via modules/controllers/services
* **Diagram:** *Draw a high-level SPA architecture showing HTML+Angular front end → REST API back end.*

---

### 2. **MVC Architecture in AngularJS**

| Component      | AngularJS Equivalent                      |
| -------------- | ----------------------------------------- |
| **Model**      | `$scope` / Services                       |
| **View**       | HTML with `{{ }}` bindings and directives |
| **Controller** | JS functions attached to `$scope`         |

**Flow Diagram (diagram: true):**

```
[View (HTML+Directives)] ↔ [$scope (Model)] ←→ [Controller (Logic)]
```

---

### 3. **Understanding ng- Directives**

AngularJS directives extend HTML. Common ones:

| Directive         | Purpose                                       |
| ----------------- | --------------------------------------------- |
| `ng-app`          | Bootstraps AngularJS application              |
| `ng-controller`   | Attaches controller to a DOM element          |
| `ng-model`        | Two-way binds input to `$scope` variable      |
| `ng-bind`         | Replaces element’s innerHTML with model value |
| `ng-repeat`       | Loops over array to generate elements         |
| `ng-if`           | Conditionally includes element in DOM         |
| `ng-show/ng-hide` | Toggles visibility                            |
| `ng-class`        | Dynamically applies CSS classes               |
| `ng-style`        | Dynamically applies inline styles             |

```html
<div ng-app="myApp" ng-controller="MainCtrl">
  <input ng-model="username" placeholder="Enter name">
  <p ng-bind="username"></p>
  <ul>
    <li ng-repeat="item in items">{{item}}</li>
  </ul>
</div>
```

---

### 4. **Expressions & Data Binding**

* **Expressions:** Written as `{{ expression }}`; evaluated against `$scope`.
* **Two-way Binding:** Changing the model updates the view and vice versa.

```html
<input ng-model="count">
<p>Count: {{count}}</p>
```

---

### 5. **Conditional & Style Directives**

* **Conditional Rendering:**

  * `ng-if="condition"` removes/adds element
  * `ng-show="condition"` toggles CSS `display`
* **Dynamic Styling:**

  * `ng-class="{active: isActive}"`
  * `ng-style="{'color': textColor}"`

```html
<button ng-class="{'btn-primary': isPrimary}" ng-style="{'font-size': fontSize+'px'}">
  Styled Button
</button>
```

---

### 6. **Controllers**

* Defined via `module.controller('Name', function($scope){ … })`
* Attach properties and methods to `$scope` for use in the view

```js
var app = angular.module('myApp', []);
app.controller('MainCtrl', function($scope) {
  $scope.greet = function() {
    $scope.message = "Hello, " + $scope.username;
  };
});
```

---

### 7. **Filters**

* Used to **format** data in views.
* Built-in: `uppercase`, `lowercase`, `currency`, `date`, `limitTo`, `filter`, `orderBy`.

```html
<p>{{ price | currency }}</p>
<p ng-repeat="item in items | limitTo:3">{{ item }}</p>
```

---

### 8. **Forms & Validation**

* AngularJS tracks form and field state: `$dirty`, `$valid`, `$invalid`, `$error`.
* Use `ng-model`, `required`, `ng-minlength`, `ng-pattern`.

```html
<form name="userForm" ng-submit="submit()" novalidate>
  <input name="email" ng-model="user.email" required ng-pattern="/^.+@.+\..+$/">
  <span ng-show="userForm.email.$error.required">Email required.</span>
  <span ng-show="userForm.email.$error.pattern">Invalid email.</span>
  <button type="submit" ng-disabled="userForm.$invalid">Submit</button>
</form>
```

---

### 9. **Routers**

* Use `ngRoute` or **UI-Router** for SPA navigation.
* Map URLs to templates and controllers.

```js
app.config(function($routeProvider) {
  $routeProvider
    .when('/home', { templateUrl: 'home.html', controller: 'HomeCtrl' })
    .when('/about', { templateUrl: 'about.html', controller: 'AboutCtrl' })
    .otherwise({ redirectTo: '/home' });
});
```

---

### 10. **Modules & Services**

* **Modules:** Containers for different parts (`angular.module('app', ['ngRoute'])`).
* **Services:** Singleton objects for sharing data/logic (`app.service('DataService', function(){…})`).

```js
app.service('AuthService', function($http) {
  this.login = function(credentials) {
    return $http.post('/api/login', credentials);
  };
});
```

---

## Part B – Modern Web Frameworks & Tools

| Framework/Tool | Purpose                                      | Key Features                                |
| -------------- | -------------------------------------------- | ------------------------------------------- |
| **Firebase**   | Backend-as-a-Service (BaaS)                  | Realtime DB, Auth, Hosting, Functions       |
| **Docker**     | Containerization for consistent environments | Images, Containers, Dockerfile              |
| **Node.js**    | Server-side JS runtime                       | Non-blocking I/O, npm ecosystem             |
| **React**      | UI Library (component-based)                 | Virtual DOM, JSX, one-way data flow         |
| **Django**     | Full-stack Python framework                  | MTV pattern, ORM, Admin UI, Security        |
| **UI/UX**      | Design principles                            | Usability, accessibility, responsive design |

---

### Firebase (BaaS)

* **Realtime Database**: `firebase.database().ref(...).on('value', callback)`
* **Authentication**: `firebase.auth().signInWithEmailAndPassword(...)`
* **Hosting & Functions**: Deploy static assets & serverless code.

---

### Docker

* **Dockerfile** to define environment
* Build image: `docker build -t myapp .`
* Run container: `docker run -p 80:3000 myapp`
* Ensures **“works on my machine”** consistency.

---

### Node.js

* **Express** for web APIs:

  ```js
  const express = require('express');
  const app = express();
  app.get('/', (req, res) => res.send('Hello'));
  app.listen(3000);
  ```
* **npm** for packages
* **Asynchronous** event loop for high concurrency.

---

### React

* **Component** example:

  ```jsx
  function Greeting(props) {
    return <h1>Hello, {props.name}</h1>;
  }
  ```
* **State & Props**, **Lifecycle methods**, **Hooks**
* Use with **Redux** for state management, **Next.js** for SSR.

---

### Django

* **Models** in `models.py` map to DB tables
* **Views** handle requests in `views.py`
* **Templates** for HTML
* **Admin** auto-generated interface.

```python
# models.py
class Book(models.Model):
    title = models.CharField(max_length=100)
```

---
