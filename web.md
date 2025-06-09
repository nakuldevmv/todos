
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
if ($_SERVER["REQUEST_METHOD"] == "POST") {

  $name = trim($_POST["name"]);
  $email = trim($_POST["email"]);
  $age = trim($_POST["age"]);

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
---
---
---
---
## 📜 **2 Marks Questions**

1. **Q:** Define client and server in web communication.
   **A:** A client is a user-agent (e.g., browser) that sends HTTP requests. A server is software (e.g., Apache) that listens for requests and returns responses.

2. **Q:** What is the role of communication protocols in client-server interaction?
   **A:** Protocols (like HTTP) define rules for data exchange—how requests/responses are formatted, transmitted, and parsed.

3. **Q:** Differentiate between Internet and World Wide Web.
   **A:** The Internet is a global network of interconnected computers. The WWW is a system of interconnected hypertext documents accessed via the Internet using HTTP.

4. **Q:** What is a URL? Give an example.
   **A:** A URL (Uniform Resource Locator) specifies the address of a web resource, e.g., `https://example.com/index.html`.

5. **Q:** What is the purpose of an HTTP request message?
   **A:** To ask a web server for a resource or to send data; it contains method, URL, headers, and optional body.

6. **Q:** List any two elements of an HTTP response message.
   **A:** Status line (e.g., `HTTP/1.1 200 OK`) and headers (e.g., `Content-Type: text/html`).

7. **Q:** List two features of HTML5.
   **A:** New semantic tags (`<article>`, `<section>`) and native multimedia support (`<audio>`, `<video>`).

8. **Q:** Write an HTML5 tag to embed an image.
   **A:** `<img src="image.jpg" alt="Description">`

9. **Q:** Mention any two HTML5 control elements.
   **A:** `<input type="date">` and `<input type="range">`.

10. **Q:** What is the use of `<audio>` and `<video>` tags in HTML5?
    **A:** To natively embed and control audio and video playback without external plugins.

11. **Q:** Define inline and external stylesheets in CSS3.
    **A:** Inline uses the `style` attribute on an element. External uses a separate `.css` file linked via `<link>`.

12. **Q:** What do you mean by CSS inheritance? Give an example.
    **A:** Child elements inherit certain properties from parent. E.g., if `body { color: red; }`, all text inside inherits red.

13. **Q:** What is rule cascading in CSS?
    **A:** The process by which conflicting CSS rules are resolved based on specificity, origin, and order.

14. **Q:** Mention any two features of CSS3 transitions.
    **A:** Smooth property changes via `transition-duration` and easing via `transition-timing-function`.

15. **Q:** Mention two components of the Bootstrap framework.
    **A:** Grid system (`.container`, `.row`, `.col-*`) and prebuilt components like `.btn` and `.card`.

16. **Q:** What is JavaScript? Mention one of its uses.
    **A:** A client-side scripting language used to add interactivity, e.g., form validation.

17. **Q:** Mention two features of JavaScript.
    **A:** Dynamic typing and first-class functions.

18. **Q:** Define the DOM in JavaScript.
    **A:** The Document Object Model is a tree representation of an HTML document, manipulable via JS.

19. **Q:** Mention any two mouse-related DOM events.
    **A:** `click` and `mouseover`.

20. **Q:** What is exception handling in JS?
    **A:** Using `try…catch` blocks to catch and handle runtime errors without crashing the script.

21. **Q:** Write a simple JavaScript validation check for empty input.
    **A:**

    ```js
    if (document.getElementById('name').value === '') {
      alert('Name required');
    }
    ```

22. **Q:** What is JSON? Write a simple example.
    **A:** JavaScript Object Notation, a lightweight data format. Example: `{"name":"X","age":21}`.

23. **Q:** What is client-side programming?
    **A:** Writing code (usually JS) that runs in the browser to control UI and behavior.

24. **Q:** Mention any two built-in objects in JavaScript.
    **A:** `Math` and `Date`.

25. **Q:** What is the use of function files in JavaScript?
    **A:** To organize and reuse code by placing functions in external `.js` files.

26. **Q:** What is an event in JavaScript? Give an example.
    **A:** An action that occurs (e.g., `onclick` when a button is clicked) that JS can respond to.

27. **Q:** What is DHTML in JavaScript?
    **A:** Dynamic HTML: combining HTML, CSS, and JS to create interactive, animated web pages.

28. **Q:** What is a Java Servlet?
    **A:** A Java class that handles HTTP requests/responses on a server to generate dynamic content.

29. **Q:** Mention the phases of servlet life cycle.
    **A:** `init()`, `service()` (doGet/doPost), and `destroy()`.

30. **Q:** What is the difference between GET and POST methods?
    **A:** GET appends data in URL (visible, length-limited); POST sends data in the request body (hidden, no size limit).

31. **Q:** How is session tracking done in servlets?
    **A:** Using `HttpSession` objects and cookies (JSESSIONID) to maintain user state.

32. **Q:** Define cookies. Mention one use.
    **A:** Small key-value pairs stored in the browser. Used for session tracking or user preferences.

33. **Q:** What is JDBC used for in web applications?
    **A:** To connect Java applications/servlets to relational databases and execute SQL.

34. **Q:** What is the purpose of a firewall in web systems?
    **A:** To filter and control incoming/outgoing network traffic based on security rules.

35. **Q:** Define a proxy server.
    **A:** An intermediary server that forwards client requests to other servers, often for caching or anonymity.

36. **Q:** What is PHP? Mention one application.
    **A:** A server-side scripting language used for dynamic web pages, e.g., form processing.

37. **Q:** What is a variable in PHP? Give an example.
    **A:** A storage container for data. Example: `$name = "X";`

38. **Q:** What is form validation in PHP?
    **A:** Server-side checking of user form inputs for correctness and security before processing.

39. **Q:** Mention any one built-in function in PHP.
    **A:** `strlen()` returns the length of a string.

40. **Q:** What is XML? Write a sample XML tag to define a book title.
    **A:** eXtensible Markup Language, for structured data. Example: `<title>Web Tech</title>`

41. **Q:** What is the purpose of XML in web development?
    **A:** To store and transport structured data between systems in a platform-independent way.

42. **Q:** What is a DTD in XML?
    **A:** Document Type Definition: defines allowed elements and attributes in an XML.

43. **Q:** Define XML Schema.
    **A:** An XML-based language for defining structure, content, and data types of an XML document.

44. **Q:** Define XSL in XML.
    **A:** eXtensible Stylesheet Language used to transform XML into other formats (e.g., HTML) via XSLT.

45. **Q:** What is an XML parser?
    **A:** A software component that reads an XML document and provides access to its structure and data.

46. **Q:** What is AngularJS? Mention one feature.
    **A:** A JS framework for single-page apps. Feature: two-way data binding.

47. **Q:** What is MVC architecture?
    **A:** A design pattern dividing an app into Model (data), View (UI), and Controller (logic).

48. **Q:** How is MVC implemented in AngularJS?
    **A:** Models are `$scope` data, views are templates with directives, controllers are JS functions on `$scope`.

49. **Q:** Define UI and UX.
    **A:** UI is the look and layout of an application; UX is the user’s overall experience and satisfaction.

50. **Q:** What is data binding in AngularJS?
    **A:** Automatic synchronization of data between model and view.

51. **Q:** Mention any two conditional directives in AngularJS.
    **A:** `ng-if` and `ng-show`.

52. **Q:** What is a router in Angular?
    **A:** A component that manages navigation between views in a single-page application.

53. **Q:** What is a filter in AngularJS?
    **A:** A function that formats or transforms data for display in templates (e.g., `currency`).

54. **Q:** Mention any two ng-attributes.
    **A:** `ng-model` and `ng-repeat`.

55. **Q:** Name any two web application frameworks.
    **A:** React and Django.

56. **Q:** What is the purpose of Firebase in web development?
    **A:** A BaaS offering real-time database, authentication, and hosting.

57. **Q:** Mention one difference between Node.js and Django.
    **A:** Node.js uses JavaScript runtime on server; Django is a Python web framework.

---
---
---
---
---
## 📜 **Extras**

#### a) Signup Form (HTML + basic PHP processing)

```html
<!-- signup.html -->
<!DOCTYPE html>
<html>
<head><title>Signup</title></head>
<body>
  <h2>Sign Up</h2>
  <form action="signup.php" method="POST">
    Username: <input type="text" name="username" required><br>
    Email:    <input type="email" name="email" required><br>
    Password: <input type="password" name="password" required><br>
    <input type="submit" value="Sign Up">
  </form>
</body>
</html>
```

```php
<?php // signup.php
$username = $_POST['username'];
$email    = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT);
echo "Registered $username with email $email.";
// Here you’d normally insert into a database
?>
```

---

#### b) Arithmetic Operations in HTML + JavaScript

```html
<!DOCTYPE html>
<html>
<head><title>Arithmetic</title></head>
<body>
  <h2>Simple Calculator</h2>
  <input id="a" type="number" placeholder="A">
  <input id="b" type="number" placeholder="B">
  <button onclick="calc()">Compute A + B</button>
  <p>Result: <span id="res"></span></p>

  <script>
    function calc() {
      const a = parseFloat(document.getElementById('a').value);
      const b = parseFloat(document.getElementById('b').value);
      document.getElementById('res').innerText = a + b;
    }
  </script>
</body>
</html>
```

---

#### c) Webpage for a College Event

```html
<!DOCTYPE html>
<html>
<head>
  <title>College Tech Fest 2025</title>
  <style>
    header { background:#004080; color:#fff; padding:10px; text-align:center; }
    .event { margin:20px; border:1px solid #ccc; padding:10px; }
  </style>
</head>
<body>
  <header><h1>College Tech Fest 2025</h1></header>
  <div class="event">
    <h2>Hackathon</h2>
    <p>Date: July 15–16, 2025</p>
    <p>Register at <a href="signup.html">signup page</a></p>
  </div>
  <div class="event">
    <h2>Robotics Workshop</h2>
    <p>Date: July 17, 2025</p>
    <p>Fee: ₹500</p>
  </div>
</body>
</html>
```

---

#### d) Webpage for Displaying Your Profile

```html
<!DOCTYPE html>
<html>
<head><title>My Profile</title></head>
<body>
  <h1>John Doe</h1>
  <img src="profile.jpg" alt="John Doe" width="150">
  <h3>About Me</h3>
  <p>Computer Science student at XYZ University. Passionate about web development and AI.</p>
  <h3>Contact</h3>
  <ul>
    <li>Email: john.doe@example.com</li>
    <li>Phone: +91 98765 43210</li>
  </ul>
</body>
</html>
```

---

#### a) PHP Code to Read from and Write to a File

```php
<?php
$filename = "data.txt";

// Write to file
file_put_contents($filename, "Hello, PHP File!\n", FILE_APPEND);

// Read from file
$content = file_get_contents($filename);
echo "<pre>$content</pre>";
?>
```

---

#### b) HTML5 Code Snippet to Embed Video

```html
<!DOCTYPE html>
<html>
<head><title>Video Embed</title></head>
<body>
  <h2>Sample Video</h2>
  <video width="640" height="360" controls>
    <source src="sample.mp4" type="video/mp4">
    <source src="sample.webm" type="video/webm">
    Your browser does not support the video tag.
  </video>
</body>
</html>
```
