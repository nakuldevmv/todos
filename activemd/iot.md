# Embedded Systems and IoT (CS3691)

<br><br>

# ✅ UNIT I – 8-BIT EMBEDDED PROCESSOR

---

## 🔹 1. **8-Bit Microcontroller (8051 Basics)**

### What is it?

* A **microcontroller** is a compact chip with:

  * CPU
  * Memory (RAM & ROM)
  * I/O Ports
  * Timers
  * Serial Communication Interface
  * Interrupts
* Used for **dedicated control applications** like washing machines, robots, cars.

### 8051 Specifics:

* **8-bit processor** → handles 8-bit data at a time.
* Based on **Harvard Architecture** → separate memory for code and data.
* CMOS-based, low power, used in embedded systems.

### Core Features of 8051:

* 4 KB ROM
* 128 bytes RAM
* 4 parallel I/O ports (P0–P3)
* 2 Timers (Timer 0 and Timer 1)
* Full-duplex UART Serial Port
* 5 interrupt sources
* 1 MHz to 12 MHz operation
* 16-bit Program Counter
* Bit-addressable RAM and SFRs

---

## 🔹 2. **Architecture of 8051 Microcontroller**

**diagram: true**
Search: `8051 microcontroller block diagram`
![alt text](https://polynoteshub.co.in/wp-content/uploads/2024/12/polynoteshub-24.png)

### Key Components:

* **CPU**: Executes instructions from memory.
* **RAM (128 Bytes)**: Temporary data storage during execution.
* **ROM (4 KB)**: Stores permanent program code.
* **I/O Ports**:

  * P0 to P3 (8-bit each)
  * Used to connect peripherals like LEDs, switches.
* **Timers/Counters**:

  * Timer 0 and Timer 1 (16-bit each)
  * Used for generating delays and counting events.
* **Serial Port (UART)**:

  * For sending/receiving serial data.
* **Interrupt Control**:

  * Handles high-priority tasks asynchronously.
* **Oscillator**:

  * Clock signal generator.
* **Bus System**:

  * Address Bus (16-bit), Data Bus (8-bit) for internal communication.

---

## 🔹 3. **Instruction Set and Programming in 8051**

### Categories of Instructions:

| Category             | Use                             | Examples               |
| -------------------- | ------------------------------- | ---------------------- |
| **Data Transfer**    | Move data between registers/mem | `MOV`, `XCH`, `PUSH`   |
| **Arithmetic**       | Perform calculations            | `ADD`, `SUBB`, `INC`   |
| **Logical**          | Logic operations                | `ANL`, `ORL`, `CPL`    |
| **Branching**        | Control flow                    | `SJMP`, `AJMP`, `CALL` |
| **Bit Manipulation** | Set/Clear/test bits             | `SETB`, `CLR`, `JB`    |

### Example Code:

```asm
MOV A, #0AH       ; Load 10 into Accumulator
ADD A, #14H       ; Add 20
MOV R1, A         ; Store result in Register R1
```

### Important Registers:

* **A (Accumulator)** – main register used in operations.
* **B** – used for multiplication/division.
* **DPTR** – Data Pointer (used in external memory).
* **PSW** – Program Status Word (flags like Carry, Zero).
* **PC** – Program Counter.

---

## 🔹 4. **Programming Parallel Ports (I/O Ports)**

**diagram: false**

8051 has **four 8-bit ports** (P0, P1, P2, P3), each can be:

* Input
* Output
* Bi-directional
* Also serve **alternate functions** (especially P3).

| Port | Function             | Special Use                          |
| ---- | -------------------- | ------------------------------------ |
| P0   | Multiplexed I/O      | Address/Data bus for external memory |
| P1   | Simple I/O           | No alternate function                |
| P2   | I/O and High Address | Used in external memory access       |
| P3   | I/O and Special Pins | Interrupts, Timers, Serial Comm.     |

### Example:

```asm
MOV P1, #0FFH  ; Output: Set all pins of Port 1 HIGH
MOV A, P2      ; Input: Read Port 2 into Accumulator
```

---

## 🔹 5. **Timers and Serial Port**

### ⏲️ Timers in 8051

**diagram: true**
Search: `8051 timer block diagram`
[Timer And Counter GeeksForGeeks](https://www.geeksforgeeks.org/electronics-engineering/8051-timers-and-counters/)

* **Timer 0 & Timer 1** – can be used as **timers** (for delays) or **counters** (for event counting).
* Controlled using registers:

  * `TMOD` – Mode selection
  * `TCON` – Control operations (start, overflow flags)
  * `THx/TLx` – High and Low byte for count

#### Modes of Timer:

| Mode | Bit-size          | Use                     |
| ---- | ----------------- | ----------------------- |
| 0    | 13-bit            | Rarely used             |
| 1    | 16-bit            | Normal timing           |
| 2    | 8-bit auto-reload | Repeats automatically   |
| 3    | Split mode        | Only Timer 0 gets split |

### Example:

```asm
MOV TMOD, #01H     ; Timer 0, Mode 1 (16-bit)
MOV TH0, #0FCH
MOV TL0, #066H      ; Load count
SETB TR0            ; Start Timer 0
```

---

### 📡 Serial Port (UART)

**diagram: true**
Search: `8051 serial communication diagram`
![alt text](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgveDwddlIOP_eHRhkg1xZ_FkNDAD4SS9EsU7BrG3P1FlOgHTU-ad_J1uy2C0EcVCjOhsnisxT5ual0UN6mGCbL2PjwU8Uf7J3KMbxzP0HNWYWfnXYlXb2Oz00n_o8HLK4nZqaC_50UuXQ5/s1600/13.jpg)

* Full-duplex asynchronous communication
* **Registers:**

  * `SBUF`: Buffer register
  * `SCON`: Control (mode, transmit, receive)
  * `TI/RI`: Transmit and receive complete flags

### Baud Rate Setting:

* Controlled via **Timer 1** in auto-reload mode

### Serial Transmission Example:

```asm
MOV SCON, #50H     ; Mode 1, 8-bit UART
MOV TMOD, #20H     ; Timer1, Mode2
MOV TH1, #0FDH     ; Set baud rate (9600)
SETB TR1           ; Start Timer1
MOV SBUF, #'A'     ; Transmit char 'A'
WAIT: JNB TI, WAIT ; Wait for complete
CLR TI             ; Clear transmit flag
```

---

## 🔹 6. **Interrupt Handling in 8051**

**diagram: true**
Search: `8051 interrupt flowchart` or `8051 interrupt handling diagram`
![alt text](https://codembedded.wordpress.com/wp-content/uploads/2017/03/862ac-8051_interrupt.png)

### What is an Interrupt?

* A signal that tells the CPU to pause the current task and run a **special routine** (ISR).
* Used to handle **urgent tasks** like input signal, timer overflow, data received, etc.

### 8051 Has 5 Interrupt Sources:

| Interrupt | Vector Address | Trigger             |
| --------- | -------------- | ------------------- |
| INT0      | 0003H          | External pin (P3.2) |
| TF0       | 000BH          | Timer 0 overflow    |
| INT1      | 0013H          | External pin (P3.3) |
| TF1       | 001BH          | Timer 1 overflow    |
| Serial    | 0023H          | TX/RX complete      |

### Registers:

* **IE (Interrupt Enable):** Enable/disable specific interrupts
* **IP (Interrupt Priority):** Set high or low priority
* **TCON:** Edge/level control for external interrupts

### ISR Flow:

1. Interrupt occurs
2. MCU finishes current instruction
3. Saves return address (PC)
4. Jumps to ISR (Interrupt Service Routine)
5. Executes task
6. Returns using `RETI`

### Example:

```asm
ORG 0003H       ; INT0 vector
CLR P1.0        ; ISR task
RETI            ; Return to main
```

---

<br><br>




# 🧠 UNIT II – EMBEDDED C PROGRAMMING

---

## 🔷 1. Memory and I/O Devices Interfacing

### 🔹 What is Interfacing?

Interfacing means **connecting external components** (memory chips or I/O devices) to the microcontroller so it can **read from inputs** and **send commands to outputs**.

---

### 🔹 Memory Interfacing

#### 🔧 Why?

* Internal memory of microcontrollers is limited.
* For large programs or data, **external memory** (RAM/ROM/EEPROM) is connected.

#### 🔧 What’s Needed?

* **Address Bus** (16-bit): Points to memory locations
* **Data Bus** (8-bit): Carries actual data
* **Control Lines**:

  * `RD` – Read enable
  * `WR` – Write enable
  * `CS` – Chip Select

#### 🔧 How it Works:

* CPU sends address through address bus.
* Activates control lines.
* Data flows through data bus.

🔍 **diagram: true**
Search: `8051 external memory interfacing diagram`

---

### 🔹 I/O Device Interfacing

#### 🧠 I/O Devices:

* **Input devices**: switches, sensors
* **Output devices**: LEDs, displays, buzzers, motors

#### 🔧 Two Types:

1. **Memory-Mapped I/O**

   * Devices share the same address space as memory.
   * Uses standard instructions like `MOV`.

2. **I/O-Mapped I/O (Isolated I/O)**

   * Special I/O instructions (`IN`, `OUT`).
   * Used in architectures like Intel x86.

#### 🔧 Techniques:

* **Polling**: Continuously checking device status
* **Interrupts**: Device notifies when it needs attention

🔍 **diagram: true**
Search: `I/O device interfacing with 8051 diagram`

---

## 🔷 2. Programming Embedded Systems in C

### 🔹 Why Use Embedded C?

| Normal C               | Embedded C                               |
| ---------------------- | ---------------------------------------- |
| Runs on OS             | Runs on microcontroller                  |
| Focus on logic         | Focus on **timing, memory, and control** |
| Uses `main()` with I/O | Uses **registers**, ports, timers, etc.  |

### 🔹 Key Features:

* **Direct register access**: `P1 = 0xFF;`
* **Efficient memory handling**: `static`, `volatile`
* **No standard libraries** – everything's custom
* **Infinite loops**: `while(1)` for continuous running
* **Low-level control** over hardware

---

### 🔹 Embedded C Structure:

```c
#include <reg51.h> // header for 8051

void main() {
  while(1) {
    P1 = 0x0F; // send data to port
  }
}
```

#### 🔧 Important Headers:

* `<reg51.h>` for 8051 registers
* `<intrins.h>` for low-level bit instructions

#### 🔧 Key Operations:

* Controlling ports
* Using `delay()` via loops/timers
* Accessing I/O pins like `P1_0`, `P2_5`

---

## 🔷 3. Need for RTOS

> RTOS = Real-Time Operating System.
> Used when your system has to **do multiple things on time**, every time.

---

### 🔹 Why Not Normal OS?

| Normal OS                  | RTOS                                             |
| -------------------------- | ------------------------------------------------ |
| Focuses on user experience | Focuses on **timely task execution**             |
| Delays acceptable          | **Delays are dangerous** (Ex: airbag deployment) |

---

### 🔹 What RTOS Does:

* **Manages multiple tasks**
* **Prioritizes** critical tasks
* Enables **real-time deadlines**
* Handles **task switching** with precision

#### 🔧 Applications:

* Medical devices (timing critical)
* Flight systems
* Robotics
* Industrial automation

🔍 **diagram: true**
Search: `RTOS architecture diagram in embedded systems`

---

## 🔷 4. Multiple Tasks and Processes

> A task = a function or block of logic to be executed.
> RTOS handles **many tasks at the same time**, without crashing.

---

### 🔹 How It Works:

* Each task has:

  * Stack
  * Context
  * Priority
* Tasks are scheduled and executed based on **priority and availability**.

---

### 🔹 Task States in RTOS:

| State         | Meaning                  |
| ------------- | ------------------------ |
| **Ready**     | Task is waiting for CPU  |
| **Running**   | Currently executing      |
| **Blocked**   | Waiting for I/O or delay |
| **Suspended** | Task is paused manually  |

🔍 **diagram: true**
Search: `RTOS task state diagram`

---

### 🔧 Example:

Task 1: Read temperature every 5 sec
Task 2: Send data to cloud every 1 min
Task 3: Alert if temp > threshold

💡 RTOS ensures all these run smoothly using task scheduling.

---

## 🔷 5. Context Switching

### 🧠 What is Context?

Context = **Snapshot** of a task’s current state.
Includes:

* CPU registers
* Program Counter
* Stack pointer
* Flags

---

### 🔁 Context Switching Process:

1. Save the current task’s context
2. Load the new task’s context
3. Start/resume execution of new task

---

### 🔧 Why Important?

* Enables **multitasking**
* Keeps system consistent
* Ensures **data is not lost** when switching

🔍 **diagram: true**
Search: `context switching RTOS diagram`

---

### 🛠️ Example Situation:

Task A is sending data to server
Interrupt occurs
Task B (sensor reading) starts
After it's done, RTOS switches back to Task A — exactly where it left off

---

## 🔷 6. Priority-Based Scheduling Policies

This is how RTOS decides **which task gets the CPU**.

---

### 🔹 Scheduling Policies:

#### ✅ **1. Preemptive Priority Scheduling**

* Higher priority task **interrupts lower** one
* Critical tasks handled ASAP
* Example: Fire alarm interrupting music playback

#### ✅ **2. Non-Preemptive Scheduling**

* Current task **finishes fully**
* Lower overhead, simple
* Example: Washing machine completing a wash cycle

#### ✅ **3. Round Robin with Priority**

* Equal priority tasks take turns
* Balanced CPU usage
* Fair in systems like printers, ticket machines

---

### 🔧 When to Use What?

| System Type               | Scheduling     |
| ------------------------- | -------------- |
| Life-critical (Pacemaker) | Preemptive     |
| Office automation         | Round Robin    |
| Simple devices            | Non-preemptive |

🔍 **diagram: true**
Search: `priority based scheduling in RTOS diagram`

---

### 🧠 Real-World Example:

Let’s say you’re building a **smart agriculture system**:

* Task 1: Sensor reads soil moisture (High priority)
* Task 2: Update mobile app UI (Medium priority)
* Task 3: Store data to SD card (Low priority)

RTOS makes sure Task 1 **always runs first**, ensuring the crops get watered at the right time.

---

<br><br>




# ✅ UNIT III – IoT AND ARDUINO PROGRAMMING



## 1️⃣ **Introduction to the Concept of IoT Devices**

* IoT (Internet of Things) = network of smart devices with sensors, processors, and connectivity.
* Purpose: To sense → compute → communicate.
* Used in home automation, agriculture, industries, healthcare.

**Key Properties:**

* **Connectivity**: Wireless (WiFi, GSM, ZigBee)
* **Data Processing**: Locally (microcontroller) or on cloud
* **Remote Control**: Access/control via apps or dashboards
* **Automation**: Based on logic or AI rules

---

## 2️⃣ **IoT Devices vs Computers**

| Aspect       | IoT Device                  | Computer          |
| ------------ | --------------------------- | ----------------- |
| Task         | Specific                    | General-purpose   |
| Size         | Small/embedded              | Large             |
| OS           | Often none / RTOS           | Full OS           |
| Interface    | Sensors/Actuators           | Mouse/Keyboard    |
| Connectivity | WiFi, GSM, ZigBee           | LAN, WiFi         |
| Power        | Battery or low power        | Plugged-in or UPS |
| Example      | Smart bulb, fitness tracker | Laptop, desktop   |

---

## 3️⃣ **IoT Configurations**

**diagram: true**
🔍 *Google Search:* `IoT network configurations diagram`

### 🧷 Types:

* **Device-to-Device (D2D)**: Local communication (e.g., IR sensor triggering a motor).
* **Device-to-Cloud**: Sends data to a cloud server (e.g., temp sensor uploads to Firebase).
* **Device-to-Gateway**: Data goes via a gateway (e.g., mobile app acts as bridge).
* **Back-End Data Sharing**: Data from one cloud platform shared with another service or app.

Each config depends on:

* Application needs (local vs remote)
* Network availability
* Power constraints

---

## 4️⃣ **Basic Components of an IoT System**

| Component                | Role                          |
| ------------------------ | ----------------------------- |
| **Sensor**               | Detects data (input)          |
| **Actuator**             | Performs action (output)      |
| **Microcontroller**      | Processes logic               |
| **Connectivity Module**  | WiFi, GSM, Bluetooth          |
| **Power Source**         | Battery/AC                    |
| **Cloud/Server**         | Stores data, runs analytics   |
| **Mobile/Web Interface** | For monitoring or controlling |

These work in a loop:
**Sense → Process → Act → Communicate → Store**

---

## 5️⃣ **Introduction to Arduino**

* Open-source platform with microcontroller + IDE.
* Used in DIY projects and prototyping of IoT.
* Supports **Embedded C** & many useful libraries.

**Why Arduino for IoT?**

* Simple to program
* GPIO pins for sensors/actuators
* USB upload + Serial monitor
* Compatible with shields/modules

---

## 6️⃣ **Types of Arduino Boards**

| Board        | Features                     | Use Case                    |
| ------------ | ---------------------------- | --------------------------- |
| **Uno**      | ATmega328P, 14 digital pins  | Standard IoT projects       |
| **Nano**     | Compact version of Uno       | Space-limited projects      |
| **Mega**     | 54 digital pins, 16 analog   | Complex multi-device setups |
| **Leonardo** | Acts as HID (keyboard/mouse) | Human interface apps        |
| **Due**      | 32-bit ARM Cortex-M3         | High-speed, complex apps    |
| **LilyPad**  | Soft and round, sewable      | Wearable tech & e-textiles  |
| **Pro Mini** | No USB port, low power       | Battery-operated sensors    |

Boards differ in:

* Memory (Flash, SRAM)
* Number of I/O pins
* Speed & size

---

## 7️⃣ **Arduino Toolchain**

**Toolchain** = Full process from code → hardware.

diagram: true
🔍 Google search: arduino toolchain workflow diagram

| Stage                  | Function                           |
| ---------------------- | ---------------------------------- |
| **Editor (IDE)**       | Write code (`.ino` sketch)         |
| **Preprocessor**       | Handles `#include` & functions     |
| **Compiler (AVR-GCC)** | Converts to machine code           |
| **Linker**             | Joins all files and libraries      |
| **Uploader**           | Loads binary to Arduino via USB    |
| **Serial Monitor**     | Debugging & viewing real-time data |

Libraries like `WiFi.h`, `Servo.h`, `Adafruit_Sensor.h` are added using `#include`.

---

## 8️⃣ **Arduino Programming Structure**

```cpp
void setup() {
  // Initial settings – runs once
}

void loop() {
  // Main logic – runs again and again
}
```

* **setup()**: Used to initialize sensors, pins, serial communication.
* **loop()**: Keeps running as long as the Arduino is powered.

🧩 Additional Elements:

* **Functions**: Custom reusable code blocks
* **Libraries**: External modules for WiFi, LCDs, etc.
* **Comments (`//`)**: Document your code

---

## 9️⃣ **Sketches / Pins / Input/Output From Pins Using Sketches**

* A **Sketch** = Arduino code file (`.ino`)
* **Digital Pins**: Used for ON/OFF (e.g., `digitalWrite(13, HIGH);`)
* **Analog Pins**: Read variable signals (0–5V) with `analogRead()`

| Function                   | Use                                                           |
| -------------------------- | ------------------------------------------------------------- |
| `pinMode(pin, mode)`       | Set pin as INPUT/OUTPUT                                       |
| `digitalRead(pin)`         | Read ON/OFF (1/0)                                             |
| `digitalWrite(pin, state)` | Set pin HIGH/LOW                                              |
| `analogRead(pin)`          | Get values from 0–1023                                        |
| `analogWrite(pin, value)`  | Output PWM (0–255) – used on PWM pins only (e.g., D3, D5, D6) |

Note: No actual analog output – `analogWrite()` uses PWM for simulating it.

---

## 🔟 **Introduction to Arduino Shields**

**diagram: true**
🔍 *Google Search:* `arduino shields types with functions`

* **Shields** = Expansion boards that "plug in" to Arduino.
* Used for extending features like:

  * Connectivity (WiFi, GSM, Ethernet)
  * Motor driving
  * Display control (LCD, TFT)
  * Sensing (GPS, GSM, RFID)

**Common Shields:**

| Shield       | Purpose                     |
| ------------ | --------------------------- |
| WiFi Shield  | Internet communication      |
| GSM Shield   | SMS/call capabilities       |
| Motor Shield | Controls DC, stepper motors |
| Relay Shield | Switch high-power devices   |
| GPS Shield   | Location tracking           |

Shields simplify interfacing → no need for many wires or complex code.

---

## 🔹 **11. Sensors in IoT & Arduino**

**What is a Sensor?**
A sensor is a device that detects changes in the environment and sends the data to a microcontroller for processing.

### 🧠 Key Points:

* Converts physical signals into electrical signals.
* Mostly used as **INPUT devices**.
* Interfaced using **analog** or **digital** pins.

### 📊 Common Types of Sensors:

| Sensor                             | Type                     | Purpose                       | Arduino Pin |
| ---------------------------------- | ------------------------ | ----------------------------- | ----------- |
| **LDR (Light Dependent Resistor)** | Analog                   | Detects light intensity       | A0          |
| **IR Sensor**                      | Digital                  | Detects obstacles             | D2, D3      |
| **Temperature Sensor (LM35)**      | Analog                   | Measures temperature          | A1          |
| **Ultrasonic Sensor**              | Digital (Trigger + Echo) | Measures distance             | D9, D10     |
| **Gas Sensor (MQ2)**               | Analog                   | Detects gases like smoke, LPG | A2          |
| **DHT11**                          | Digital                  | Temp + Humidity               | D7          |

### 📌 Notes:

* Use `analogRead()` for analog sensors.
* Use `digitalRead()` for digital sensors.

---

## 🔹 **2. Actuators in IoT & Arduino**

**What is an Actuator?**
An actuator is a device that **performs an action** in response to a signal from the microcontroller.

### 🔧 Key Points:

* Converts electrical signals into physical motion or output.
* Mostly used as **OUTPUT devices**.
* Controlled using **digital** or **PWM** pins.

### ⚙️ Common Types of Actuators:

| Actuator         | Purpose             | Arduino Pin          | Function Used        |
| ---------------- | ------------------- | -------------------- | -------------------- |
| **LED**          | Lighting/Indicator  | D13                  | `digitalWrite()`     |
| **Buzzer**       | Sound alert         | D8                   | `digitalWrite()`     |
| **Relay Module** | Switch AC devices   | D7                   | `digitalWrite()`     |
| **DC Motor**     | Continuous rotation | D3/D5 + Motor Driver | `analogWrite()`      |
| **Servo Motor**  | Angle control       | D9 + `Servo.h`       | `servo.write(angle)` |

---

## 🔹 **3. Integration of Sensors & Actuators with Arduino**

**diagram: true**
🔍 *Google Search:* `arduino sensor and actuator interfacing diagram`

### ✅ Basic Steps to Interface:

1. **Connect Sensor**

   * Sensor OUT → Arduino analog/digital pin
   * VCC & GND → Arduino 5V/GND
2. **Connect Actuator**

   * Actuator IN → Arduino digital/PWM pin
   * Use transistor/relay/motor driver if high current
3. **Code Flow**

   * Read sensor value
   * Use conditions to control actuator

---

### 🧪 Simple Example:

**IR Sensor controlling a Buzzer:**

```cpp
int sensor = 2;      // IR Sensor output pin
int buzzer = 9;      // Buzzer pin

void setup() {
  pinMode(sensor, INPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  int value = digitalRead(sensor);
  if (value == 0) {            // 0 means object detected
    digitalWrite(buzzer, HIGH); // Turn buzzer ON
  } else {
    digitalWrite(buzzer, LOW);  // Turn buzzer OFF
  }
}
```

---

<br><br>


# ✅ UNIT IV – IoT Communication and Open Platforms



## 🌐 1. **IoT Communication Models and APIs**

Defines **how devices communicate and manage data exchange** in an IoT ecosystem.

---

### 📘 Communication Models:

These are the **logical structures** used for data transmission.

1. **Request–Response Model:**

   * One device sends a request → other device (usually a server) sends back a response.
   * Used in web-based IoT apps (like REST API calls).
   * 🌍 Example: A smart fridge querying temperature data.

2. **Publish–Subscribe (Pub/Sub) Model:**

   * Devices publish data to a broker → multiple subscribers get notified.
   * Supports asynchronous communication.
   * 🛰️ Protocols: MQTT, AMQP
   * 💡 Example: Smart weather sensors publishing temperature to multiple apps.

3. **Push–Pull Model:**

   * Data is pushed or pulled as needed, often seen in polling mechanisms.
   * Less efficient but easier to implement.

4. **Event-Driven Model:**

   * Data is sent when an **event occurs** (e.g., motion detected).
   * Great for real-time alerts and automation.

📌 **diagram: false**

---

### 🔗 APIs in IoT:

APIs let IoT devices talk to cloud platforms, apps, or each other.

* **RESTful APIs (HTTP-based)**: Most common.
* **GraphQL APIs**: Efficient querying.
* **CoAP**: Lightweight version of HTTP, used in constrained networks.

📌 **diagram: false**

---

## 🛰️ 2. **IoT Communication Protocols**

These are the actual **rules** and standards used to transfer data over networks.

---

### 📘 Layers and Protocols:

| Layer           | Protocols               |
| --------------- | ----------------------- |
| **Application** | MQTT, HTTP, CoAP        |
| **Transport**   | TCP, UDP                |
| **Network**     | IPv6, 6LoWPAN           |
| **Link**        | WiFi, Bluetooth, ZigBee |

Each protocol is chosen based on:

* **Power use**
* **Network range**
* **Speed**
* **Reliability**

📌 **diagram: true**
🔍 *Search:* `IoT communication protocol stack diagram`

---

## 📶 3. **Bluetooth**

A low-power, short-range wireless technology for local IoT device interaction.

---

### 📘 Key Features:

* Operates at **2.4 GHz**.
* Low power, limited to \~10m.
* Ideal for **wearables, sensors, personal devices**.
* Supports **mesh networking** via BLE (Bluetooth Low Energy).

---

### 📘 Architecture:

* **Piconet** – One master, many slaves.
* **Scatternet** – Multiple interconnected piconets.

📌 **diagram: true**
🔍 *Search:* `Bluetooth piconet and scatternet architecture`

---

## 📡 4. **Wi-Fi**

Common wireless tech used in high-speed IoT devices.

---

### 📘 Features:

* Operates at **2.4 GHz and 5 GHz**.
* Supports internet access and real-time cloud interaction.
* Used in **smart TVs, IP cameras, home automation**.

📌 **diagram: false**

---

## 📡 5. **ZigBee**

Low-power, low-data-rate protocol built for **sensor networks and automation**.

---

### 📘 Features:

* Uses **2.4 GHz** ISM band.
* Offers **mesh topology** (high reliability).
* Range: 10–100 meters.
* Applications: Smart lighting, alarms, industrial automation.

📌 **diagram: true**
🔍 *Search:* `ZigBee architecture diagram mesh star tree`

---

## 🌍 6. **GPS – Global Positioning System**

Used for **location tracking and navigation**.

---

### 📘 Features:

* Satellite-based system.
* Gives **latitude, longitude, altitude**.
* Used in **smartwatches, vehicles, drones**.
* Needs **clear sky view** for accuracy.

📌 **diagram: true**
🔍 *Search:* `GPS working block diagram in IoT`

---

## 📲 7. **GSM Modules**

Used for **long-range, cellular communication** in IoT.

---

### 📘 Features:

* Modules like **SIM800/SIM900** use 2G/3G networks.
* Support **SMS, voice, internet**.
* Works even in rural/outdoor environments.

📌 **diagram: true**
🔍 *Search:* `GSM module architecture with SIM800`

---

## 🍓 8. **Open Platform – Raspberry Pi**

A **mini Linux computer** used in complex IoT applications.

---

### 📘 Features:

* Supports **Python, C, Node.js**.
* Has multiple **GPIO pins**.
* Includes **WiFi, Bluetooth, USB, HDMI, Camera support**.
* Used in **edge computing, ML + IoT, smart hubs**.

📌 **diagram: true**
🔍 *Search:* `Raspberry Pi board architecture`

---

## 🧑‍💻 9. **Programming Raspberry Pi**

Writing programs to interact with sensors and perform IoT tasks.

---

### 📘 Languages:

* **Python** (most popular)
* C/C++
* Node.js

### 📘 Libraries:

* `RPi.GPIO` – controls GPIO pins
* `time`, `os`, `serial` – for time delays, serial communication

📌 **diagram: false**

---

## 🔌 10. **Interfacing Raspberry Pi**

Connecting external devices to Raspberry Pi via:

* **GPIO pins** (digital I/O)
* **I2C** (multiple device communication)
* **SPI** (faster than I2C)
* **UART** (serial communication)

📌 **diagram: true**
🔍 *Search:* `Raspberry Pi GPIO interfacing with sensors`

---

## 📍 11. **Accessing GPIO Pins**

GPIO = **General Purpose Input/Output** pins
Used to:

* **Send signals** to actuators (turn on motor, light)
* **Receive inputs** from sensors (motion, temp)

📌 **diagram: true**
🔍 *Search:* `GPIO pin layout Raspberry Pi`

---

## 🔁 12. **Sending and Receiving Signals using GPIO**

This is where the Pi reads data (like temperature) and sends commands (turn on LED).

---

### 📘 Input Examples:

* Motion sensors
* Push buttons

### 📘 Output Examples:

* LEDs
* Buzzers

### Sample Python code:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
```

📌 **diagram: false**

---

## ☁️ 13. **Connecting to the Cloud**

IoT data is sent to cloud for:

* **Data storage**
* **Real-time visualization**
* **Control via dashboards**

---

### 📘 Common Cloud Platforms:

* **ThingSpeak**
* **AWS IoT Core**
* **Google Firebase**
* **Azure IoT Hub**

### 📘 Protocols Used:

* MQTT (lightweight)
* HTTP (RESTful APIs)
* CoAP (for constrained devices)

📌 **diagram: true**
🔍 *Search:* `IoT device connecting to cloud architecture diagram`

---

<br><br>

Absolutely, fam 👨‍🏫 Let’s finish Unit 5 **like a topper but with chill vibes**.
Here's your **full, exam-ready, cleanly formatted explanation** of:

---

# ✅ **UNIT V – APPLICATIONS DEVELOPMENT**



### 1️⃣ **Complete Design of Embedded Systems**

**Definition:**
An **embedded system** is a combo of hardware + software designed to do one specific task efficiently.

**Design Phases:**

* **1. Specification Phase:**
  Understand the system needs (e.g., control temperature, sense gas).

* **2. Hardware Selection:**
  Choose components like:

  * Microcontroller (e.g., 8051, Arduino)
  * Sensors & Actuators
  * Power Source
  * Communication module (WiFi, GSM)

* **3. Software Development:**
  Write embedded C / Arduino code to control the system.
  Use RTOS if multitasking is needed.

* **4. Prototyping:**
  Connect all parts and test if working as expected.

* **5. Testing & Debugging:**
  Remove bugs, optimize performance.

* **6. Deployment & Maintenance:**
  Install the system and provide regular updates if needed.

📌 **diagram: true**
🔍 Google: `embedded system design flow diagram`

---

### 2️⃣ **Development of IoT Applications**

**Definition:**
IoT Applications = systems that use the internet to connect physical devices for real-time data monitoring, control, or automation.

**Steps to Develop IoT Application:**

1. **Identify the Problem** – e.g., automate irrigation, monitor health remotely.
2. **Select Platform** – Arduino, Raspberry Pi, etc.
3. **Choose Sensors/Actuators** – Depends on the use case.
4. **Connectivity** – WiFi, GSM, ZigBee, Bluetooth
5. **Program the Controller** – Write logic in Arduino IDE / Embedded C.
6. **Cloud Integration** – Store/send data using IoT platforms (ThingSpeak, Blynk)
7. **Build User Interface (UI)** – Mobile app/web dashboard
8. **Test and Deploy**

📌 **diagram: true**
🔍 Google: `IoT application development life cycle`

---

### 3️⃣ **Home Automation**

**Definition:**
Automating home appliances using IoT for control via smartphone or sensors.

**Goal:**
Energy saving, comfort, security.

**Components:**

* Sensors (PIR, LDR)
* Actuators (Relays)
* Controller (Arduino, NodeMCU)
* Connectivity (WiFi/GSM)
* Mobile app

**Working:**
Sensor → Controller → Actuator → App Notification or Action

**Examples:**

* Smart lighting
* Fan automation
* Voice control (via Alexa)

📌 **diagram: true**
🔍 Google: `IoT based home automation block diagram`

---

### 4️⃣ **Smart Agriculture**

**Definition:**
Use of IoT to monitor farm conditions and automate irrigation, crop monitoring.

**Goal:**
Maximize yield, reduce water/fertilizer wastage.

**Components:**

* Soil moisture sensor, DHT11 (humidity/temp)
* Arduino/Raspberry Pi
* Water pump (actuator)
* GSM module or Cloud system

**Working:**
Moisture too low? → Sensor detects → Controller activates pump → Data sent to phone

**Benefits:**

* Less manual work
* Precise farming
* Cost-effective

📌 **diagram: true**
🔍 Google: `smart agriculture system using IoT diagram`

---

### 5️⃣ **Smart Cities**

**Definition:**
An urban area that uses IoT to improve infrastructure, public services, and sustainability.

**Goals:**

* Improve traffic, energy, and waste management
* Ensure citizen safety
* Monitor pollution

**Components:**

* Sensors (air quality, motion, sound)
* Controllers & Cloud
* Mobile/web dashboard

**Examples:**

* Smart traffic lights
* Automated street lights
* Waste level monitoring in bins

📌 **diagram: true**
🔍 Google: `IoT based smart city system diagram`

---

### 6️⃣ **Smart Healthcare**

**Definition:**
Application of IoT in medical monitoring and diagnosis.

**Goals:**

* Monitor patients remotely
* Alert caregivers in emergencies
* Enable data sharing with doctors

**Components:**

* Wearable devices (heart rate, BP monitor)
* Controller with WiFi/Bluetooth
* Cloud storage

**Working:**
Data collected → Sent to cloud → Doctor/Family alerted if abnormal

**Examples:**

* Fitness bands (Fitbit, Mi Band)
* Smart ECG/EHR monitors
* Fall detection system for elderly

📌 **diagram: true**
🔍 Google: `IoT in healthcare system block diagram`

---

## 📝 How to Write a Full Answer in Exam

For **each application**, follow this format:

1. **Intro**
2. **Objective**
3. **Components**
4. **Working**
5. **Technologies**
6. **Advantages**
7. **Diagram**
8. **Conclusion**

---


<br><br><br>

# Important Questions 



# Unit 1

## ✍️ **Architecture of 8051 Microcontroller**

**diagram: true**
🔍 *Google search*: `8051 microcontroller architecture block diagram`

---

### 🔹 1. **Introduction**

* The **8051** is an 8-bit microcontroller developed by **Intel** in 1980.
* It follows the **Harvard Architecture** (separate memory for program and data).
* It is **highly integrated**, meaning it has memory, CPU, timers, I/O ports, and serial communication — all on one chip.

---

### 🔹 2. **Key Features of 8051**

* 8-bit data bus and ALU (can process 8-bit data at a time)
* 4KB ROM (program memory)
* 128 bytes of RAM (data memory)
* 4 parallel I/O ports (P0–P3)
* 2 Timers (Timer 0 and Timer 1)
* 1 Serial Port (UART)
* 5 Interrupts
* Clock speed: 12 MHz (standard)

---

### 🔹 3. **Block Diagram Overview**

![8051](https://www.tutorialspoint.com/microprocessor/images/8051_architecture.jpg)

📌 *diagram: true*
🔍 *Search*: `8051 microcontroller architecture diagram`
The main components include:

#### 🧠 a) **Central Processing Unit (CPU)**

* Heart of the microcontroller
* Executes instructions fetched from program memory
* Controls all other parts

#### 💾 b) **ROM (Program Memory)**

* 4KB internal
* Stores the instructions permanently
* Can be extended externally up to 64KB

#### 📥 c) **RAM (Data Memory)**

* 128 bytes internal
* Used for storing temporary data, variables, stack, etc.

#### 🧮 d) **Register Set**

* 34 general purpose registers
* Includes **Accumulator (A)**, **B register**, **Program Counter (PC)**, **Stack Pointer (SP)**, **DPTR** (Data Pointer), and status register (PSW)

#### 🔌 e) **Input/Output Ports**

* Four 8-bit parallel ports (P0 to P3)
* Used to connect external devices (LEDs, sensors, switches, etc.)
* Ports can be configured as input or output

#### ⏱️ f) **Timers and Counters**

* Timer 0 and Timer 1: 16-bit
* Can be used as timers (delay) or counters (count external events)
* Used for time-based operations

#### 📡 g) **Serial Communication (UART)**

* One full duplex serial port (TXD, RXD pins)
* Supports serial data transfer
* Used for communication with PC, Bluetooth, GSM, etc.

#### 🚨 h) **Interrupt Control**

* 5 sources: INT0, INT1 (external), Timer0, Timer1, Serial
* Can pause main program to handle urgent tasks

#### ⚙️ i) **Oscillator and Clock**

* Needs an external crystal oscillator (usually 12 MHz)
* Generates clock signals to control instruction timing

#### 🛣️ j) **Bus System**

* **Address Bus** (16-bit): Carries memory addresses
* **Data Bus** (8-bit): Carries data between components
* **Control Bus**: Manages control signals like RD, WR

---

### 🔹 4. **Internal Memory Organization**

* First 128 bytes → RAM

  * 00H to 1FH → Register banks & bit-addressable memory
  * 20H to 2FH → Bit-addressable area
  * 30H to 7FH → General purpose RAM
* 4KB Program memory: Stores the actual code

---

### 🔹 5. **Special Function Registers (SFRs)**

| Register  | Use                         |
| --------- | --------------------------- |
| A         | Accumulator                 |
| B         | For multiplication/division |
| PSW       | Program Status Word         |
| SP        | Stack Pointer               |
| DPTR      | Data Pointer                |
| PC        | Program Counter             |
| TMOD/TCON | Timer config                |
| SCON      | Serial config               |

---


<br>
<br>

---

## 🧠 **Timer Operation and Interrupt Handling in 8051**

**diagram: true**
🔍 *Search:* `8051 timer and counter block diagram`, `8051 interrupt vector table`

---

### 🔷 **1. What is a Timer in 8051?**

A **timer** is a built-in hardware unit inside the microcontroller that keeps track of time in the form of clock pulses. It can be used for:

* Measuring time intervals ⏱️
* Creating delays
* Counting external pulses (in counter mode)
* Generating baud rates for serial communication

In 8051, timers are **16-bit registers** and can count from 0000H to FFFFH (0 to 65535 in decimal).

---

### 🔷 **2. Timers in 8051 – Overview**

8051 has **2 timers**:

* **Timer 0** (controlled by TH0 and TL0)
* **Timer 1** (controlled by TH1 and TL1)

Each timer has **two 8-bit registers** (High and Low).
Timers work based on the **internal clock** or **external pulses** depending on the mode.

---

### 🔷 **3. TMOD Register – Mode Selection**

🧠 TMOD (Timer Mode Register) is 8 bits:

* Lower 4 bits for Timer 0
* Upper 4 bits for Timer 1

| Bit     | Meaning                                                             |
| ------- | ------------------------------------------------------------------- |
| GATE    | 1 = Timer controlled by external INTx pin                           |
| C/T     | 0 = Timer mode (internal clock), 1 = Counter mode (external pulses) |
| M1 & M0 | Mode selection bits                                                 |

---

### 🔷 **4. Timer Modes Explained**

| Mode   | Description                    | Use Case                                           |
| ------ | ------------------------------ | -------------------------------------------------- |
| Mode 0 | 13-bit timer (used rarely now) | Backward compatibility                             |
| Mode 1 | 16-bit timer (default mode)    | General delays and counting                        |
| Mode 2 | 8-bit auto-reload              | Baud rate generation                               |
| Mode 3 | Split timer mode               | Used to create two 8-bit timers (only for Timer 0) |

🧠 **Auto-reload** = Timer reloads automatically when it overflows (good for periodic tasks).

---

### 🔷 **5. TCON Register – Timer Control**

| Bit     | Description                                      |
| ------- | ------------------------------------------------ |
| TR0/TR1 | Start/stop timers                                |
| TF0/TF1 | Timer overflow flag (set when counter overflows) |
| IT0/IT1 | Type of external interrupt triggering            |
| IE      | Global Interrupt Enable                          |

---

### 🔷 **6. Steps to Use a Timer (Example: Timer 0, Mode 1)**

1. Set TMOD = 0x01 → Timer 0, Mode 1 (16-bit)
2. Load TL0 and TH0 with initial values (for delay)
3. Set TR0 = 1 → Start the timer
4. Wait for TF0 = 1 → Timer overflow flag
5. Stop timer and clear TF0

📝 You can use this for **delay generation**, **event timing**, or **counting pulses**.

---

## 🧩 Example Program (Timer-Based Delay)

```c
TMOD = 0x01;     // Timer 0, Mode 1
TH0 = 0xFC;      // Load high byte
TL0 = 0x66;      // Load low byte
TR0 = 1;         // Start timer

while(TF0 == 0); // Wait for overflow
TR0 = 0;         // Stop timer
TF0 = 0;         // Clear flag
```

---

### 📐 **Diagram**

**8051 Timer Block Diagram**
🔍 Google: `8051 timer block diagram with TCON TMOD TRx TFx`

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20240610023809/mode2.webp)

---

## 🚨 **Interrupt Handling in 8051**

### 🔷 **What is an Interrupt?**

An **interrupt** is a special signal that **pauses** the normal execution of the program to handle an urgent task. After handling it, the system returns to its previous task.

🧠 Example: When a timer overflows, it triggers an interrupt to handle it automatically.

---

### 🔷 **Types of Interrupts in 8051**

8051 has **5 interrupt sources**:

| Source            | Vector Address | Priority (Default) |
| ----------------- | -------------- | ------------------ |
| INT0 (External 0) | 0003H          | High               |
| TF0 (Timer 0)     | 000BH          | Medium             |
| INT1 (External 1) | 0013H          | Medium             |
| TF1 (Timer 1)     | 001BH          | Low                |
| Serial (RI/TI)    | 0023H          | Lowest             |

---

### 🔷 **IE and IP Registers**

* **IE (Interrupt Enable)** – Enables/disables specific interrupts.
* **IP (Interrupt Priority)** – Sets which interrupt has higher priority.

```c
IE = 0x82; // Enable Timer 0 interrupt and global interrupt
```

---

### 🔷 **What is an ISR?**

An **Interrupt Service Routine** is a special function that is executed **when an interrupt occurs.**

🧠 Characteristics:

* It **automatically runs** when triggered
* It must **end with RETI** (Return from Interrupt)
* It is **pre-defined for each interrupt** (based on vector address)

```c
void Timer0_ISR(void) interrupt 1 {
  // Your interrupt handling code here
}
```

---

### 🔷 **Interrupt Execution Flow**

1. Interrupt occurs 🛎️
2. Current instruction is finished
3. CPU jumps to the **vector address**
4. Executes the **ISR**
5. `RETI` is executed
6. Control returns to main program

---

## 🔁 **Using Timer with Interrupt Example**

Timer can overflow and trigger an interrupt automatically:

```c
TMOD = 0x01;       // Timer 0, Mode 1
TH0 = 0xFC; TL0 = 0x66;  
IE = 0x82;         // Enable Timer 0 interrupt
TR0 = 1;           // Start timer

void Timer0_ISR(void) interrupt 1 {
  // Action when timer overflows
  TH0 = 0xFC; TL0 = 0x66; // Reload timer
}
```

---

## 🔷 Why Are Timers + Interrupts Important?

* Enables **real-time responses** to events
* Allows **multi-tasking** without polling
* Improves **efficiency** in embedded systems
* Essential for **alarm systems**, **sensor alerts**, **timed tasks**, etc.

![alt text](https://codembedded.wordpress.com/wp-content/uploads/2017/03/862ac-8051_interrupt.png)

---

<br>
<br>



---

## 💻 **Instruction Set and Programming of 8051 Microcontroller**

**13-Mark Exam-Ready | Detailed & Clear | CS3691 – Unit I**
**diagram: true**
🔍 *Google Search:* `8051 instruction set table pdf`, `8051 addressing modes diagram`

---

### 🔷 **1. What is an Instruction Set?**

An **instruction set** is the complete set of commands that a microcontroller can execute.

For 8051:

* It’s an **8-bit** instruction set
* Total of **255 instructions**
* Each instruction is represented by **an opcode**
* Grouped into **5 categories** based on their functionality

---

### 🔷 **2. Categories of 8051 Instruction Set**

| Category              | Examples                        | Use              |
| --------------------- | ------------------------------- | ---------------- |
| **Data Transfer**     | MOV, PUSH, POP, XCH             | Move data        |
| **Arithmetic**        | ADD, SUBB, INC, DEC, MUL, DIV   | Math operations  |
| **Logical**           | ANL, ORL, XRL, CLR, CPL, RL, RR | Bitwise ops      |
| **Branching**         | AJMP, LJMP, SJMP, JC, JNC, DJNZ | Control flow     |
| **Boolean/Bit-level** | SETB, CLR, CPL, JB, JNB, JBC    | Bit manipulation |

🧠 Each of these instructions operates on registers, memory, or I/O pins.

---

### 🔷 **3. Instruction Size**

* 1-byte, 2-byte, or 3-byte
* Example:

  * `MOV A, B` → 1-byte
  * `MOV A, #45H` → 2-byte
  * `MOV DPTR, #1234H` → 3-byte

---

### 🔷 **4. Addressing Modes in 8051**

**Addressing mode** = way to access operands (data) in instructions.
**diagram: true**
🔍 *Google:* `8051 addressing modes diagram`

| Mode              | Description                            | Example           |
| ----------------- | -------------------------------------- | ----------------- |
| Immediate         | Operand is part of instruction         | `MOV A, #55H`     |
| Register          | Operand is in register                 | `MOV A, R0`       |
| Direct            | Address of operand given directly      | `MOV A, 30H`      |
| Register Indirect | Address is in register (R0/R1 only)    | `MOV A, @R0`      |
| Indexed           | Used with DPTR or PC (for code access) | `MOVC A, @A+DPTR` |

🧠 **Indexed** is mostly used for reading from **lookup tables** in program memory.

---

### 🔷 **5. Sample Instructions & Use Cases**

* **MOV A, #55H** → Load immediate value 55H into accumulator
* **ADD A, R2** → Add content of R2 to accumulator
* **INC DPTR** → Increment 16-bit data pointer
* **CJNE A, #20H, LABEL** → Compare and jump if not equal
* **SETB P1.0** → Set pin P1.0 to 1
* **CLR A** → Clear the accumulator

---

### 🔷 **6. Example: Assembly Code Snippet**

```asm
MOV A, #0A0H       ; Load A with A0
MOV R1, #10        ; Load R1 with 10
ADD A, R1          ; A = A + R1
MOV P2, A          ; Send result to Port 2
```

🧠 Registers like A (accumulator), R0–R7, DPTR, B are used heavily in 8051 assembly.

---

### 🔷 **7. Programming 8051 (Assembly Style)**

Structure of a basic assembly program:

```asm
ORG 0000H          ; Start address
MOV P1, #0FFH      ; Set Port1 as output
LOOP: MOV A, #55H
      MOV P1, A
      SJMP LOOP    ; Infinite loop
END
```

🧠 Keywords:

* `ORG` → start of program memory
* `MOV` → move data
* `SJMP` → short jump (loop)
* `END` → marks end of program

---

### 🔷 **8. Role of Accumulator (A Register)**

* Most operations use A register
* It's the default source/destination in arithmetic and logic operations
* Example: `ADD A, R0` adds R0 to A

---

### 🔷 **9. Role of DPTR & PC**

* **DPTR (Data Pointer)** → 16-bit register for external memory access
* **PC (Program Counter)** → Holds address of next instruction

---

### 🔷 **10. Bit-Level Operations (Specialty of 8051)**

8051 supports **bit-addressable memory**, i.e., you can directly access individual bits.

```asm
SETB 20H     ; Set bit at address 20H
CLR 20H      ; Clear the bit
CPL 20H      ; Complement (toggle)
```

---


<br><br>
<br>



# Unit 2




## 🧠 **Priority-Based Scheduling Policies**

**Subject:** Embedded Systems & IoT (CS3691)
**Unit II – Embedded C Programming**
**Exam Marks:** 13-mark style
**diagram: true**
🔍 *Google Search:* `RTOS priority scheduling diagram`, `task scheduling in embedded systems`

---

### 🔷 1. **What is Scheduling in RTOS?**

In **Real-Time Operating Systems (RTOS)**, **scheduling** is the mechanism that decides *which task runs at what time* based on its **priority, timing constraints, and system state**.

* Embedded systems run **multiple tasks**
* Not all tasks are equal → some are **time-sensitive**
* RTOS uses scheduling policies to pick **which task runs first**

---

### 🔷 2. **What is Priority-Based Scheduling?**

It’s a **task scheduling method** where each task is assigned a **priority number**.
🟢 Higher-priority task = runs before lower-priority ones
🔴 If multiple tasks are ready → the scheduler picks the **one with the highest priority**

---

### 🔷 3. **Types of Priority-Based Scheduling**

Let’s break it down into two main categories:

#### ✅ **A. Static Priority Scheduling**

* Priority is **fixed** at the time of task creation
* Cannot be changed during execution
* Common in **hard real-time systems** (e.g., medical monitors)

💡 *Example:*
Task A (priority 1), Task B (priority 2)
–> Task B always gets the CPU first

#### ✅ **B. Dynamic Priority Scheduling**

* Task priorities can **change at runtime**
* Based on rules like **deadline**, **execution time**, etc.
* More flexible for **soft real-time systems**

💡 *Example:* Earliest Deadline First (EDF)
–> Task closest to its deadline gets CPU

---

### 🔷 4. **Common Priority-Based Scheduling Policies**

| Policy                              | Description                                                                  |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| **Preemptive Priority**             | Higher priority task *interrupts* the currently running lower one            |
| **Non-Preemptive Priority**         | Running task completes first, even if a higher priority task becomes ready   |
| **Rate Monotonic Scheduling (RMS)** | Priority assigned based on task frequency (shorter period = higher priority) |
| **Earliest Deadline First (EDF)**   | Dynamic; task with earliest deadline runs first                              |

---

### 🔷 5. **Preemptive vs Non-Preemptive – Key Difference**

| Aspect            | Preemptive                              | Non-Preemptive  |
| ----------------- | --------------------------------------- | --------------- |
| Interruption      | Allowed if higher priority task appears | Not allowed     |
| Context Switching | More frequent                           | Less frequent   |
| Use Case          | Time-critical systems                   | Simpler systems |

---

### 🔷 6. **Diagram Explanation**

**diagram: true**
🔍 *Google:* `Preemptive vs Non-preemptive priority scheduling RTOS`

![text](https://open4tech.com/wp-content/uploads/2019/10/preemptive_scheduling.jpg)
Preemptive Scheduling

![alt text](https://www.tutorialspoint.com/operating_system/images/categories_of_process_scheduling.jpg)

Show a timeline with Task A, B, and C executing based on priorities to explain:

* Task B preempts Task C
* Task A runs first if highest priority
* Context switch markers between tasks

---

### 🔷 7. **Priority Inversion Problem (Hot Topic!)**

🧨 **What is it?**
Lower-priority task **holds a resource** needed by a higher-priority task → higher-priority task is stuck

🛠️ **Solution:**

* **Priority Inheritance Protocol** → temporarily boost the priority of lower-priority task

---

### 🔷 8. **Real-Life Embedded Example**

👉 In a **smart home** device:

* Fire alarm sensor task (high priority)
* Data logging task (medium)
* LED blinking task (low priority)

➡️ Scheduler ensures fire alarm task **preempts everything else**

---

### 🔷 9. **Why Priority-Based Scheduling is Used in Embedded Systems**

* Ensures **real-time deadlines** are met
* Gives control over **task execution**
* Suitable for **resource-constrained** environments
* Avoids unnecessary CPU load

---

<br><br>


## 🧠 **Real-Time Operating System (RTOS)**

---
![alt text](https://tridentinfosol.com/assets/img/portfolio/rtos.jpg)
### 🔷 1. **What is an RTOS?**

An **RTOS** is an operating system designed to **run tasks within strict timing constraints**.
It ensures that tasks are **executed predictably and on time**, which is crucial in **embedded systems** like:

* Pacemakers
* Car airbags
* Industrial robots
* Smartwatches

⏱️ **Real-time = deterministic behavior**

---

### 🔷 2. **Why Do We Need an RTOS?**

RTOS is needed because:

✅ Embedded systems often handle **multiple tasks** simultaneously
✅ Tasks may have **different urgency levels**
✅ Delays in response can cause **failures** (e.g., delay in airbag = disaster)

**Benefits:**

* Predictable response time (deterministic)
* Efficient task management
* Multitasking support
* Time sharing & real-time scheduling

---

### 🔷 3. **How Does an RTOS Work? (Simplified)**

RTOS works by:

1. Maintaining a **task table** (with all tasks and their priorities)
2. Using a **scheduler** to decide which task runs next
3. Handling **context switching** to switch between tasks
4. Using **inter-process communication (IPC)** methods (like semaphores, queues)
5. Running **interrupts** instantly when external events occur

**diagram: true**
🔍 Google: `RTOS architecture block diagram`

---

### 🔷 4. **Types of RTOS**

| Type          | Description                                    | Use Case                     |
| ------------- | ---------------------------------------------- | ---------------------------- |
| **Hard RTOS** | Strict deadlines; delay = failure              | Pacemakers, Anti-lock brakes |
| **Soft RTOS** | Deadlines preferred but not critical           | Music player, Messaging app  |
| **Firm RTOS** | Occasional delays okay, but may reduce quality | Video calls, Streaming       |

---

### 🔷 5. **RTOS Task States**

Every task in RTOS exists in one of the following **states**:

**diagram: true**
🔍 Google: `RTOS task state diagram`

![text](https://www.digikey.com/maker-media/85de44fb-1e6d-4234-a6d4-e10e4dce1111)


| State          | Meaning                                        |
| -------------- | ---------------------------------------------- |
| **Ready**      | Task is ready to run, waiting for CPU          |
| **Running**    | Task is currently executing                    |
| **Blocked**    | Waiting for event/resource (e.g., input, data) |
| **Suspended**  | Task is paused manually or by system           |
| **Terminated** | Task has finished execution                    |

🌀 **Scheduler** is the component that switches tasks between these states.

---

### 🔷 6. **Key Components of an RTOS**

* **Scheduler** → picks which task runs
* **Task/Thread Manager** → manages multiple tasks
* **Inter-Process Communication (IPC)** → tasks talk via queues, mailboxes
* **Clock Manager** → tracks time, delays
* **Interrupt Handler** → handles real-time interrupts

---

### 🔷 7. **Context Switching in RTOS**

When the CPU switches from one task to another:

* **Saves the state** (registers, PC, etc.) of current task
* **Loads the state** of the next task
  🔁 Happens **fast**, but adds some **overhead**

---

### 🔷 8. **Real-Life Example**

Let’s say you’re building a **smart home security system**:

* Task 1: Monitor door sensor (high priority)
* Task 2: Record video (medium)
* Task 3: Blink LED (low priority)

RTOS will:

* Ensure **Task 1 always runs first**
* Preempt others if needed
* Handle all smoothly and in **real-time**

---

<br><br>



---

### 🔷 What is Context Switching?

**Context Switching** is the process where the CPU **pauses one task**, **saves its current state**, and **switches to another task**.
It’s like a **bookmark** for the CPU — it marks where it left off and continues from there later.

**diagram: true**
🔍 Google: `context switching in RTOS diagram`

---

### 🔷 Why is Context Switching Needed?

Because embedded systems often run **multiple tasks**, and we need to:

* **Switch quickly** between tasks based on **priority**
* **Pause one task**, run a **more urgent task**
* **Avoid data loss** when switching

💡 Used heavily in **RTOS**, where task switching happens based on **schedulers**.

---

### 🔷 How It Works (Step-by-Step)

Let’s say Task A is running, and Task B becomes ready:

1. **Save current state** of Task A
   (Registers, Program Counter, Stack, etc.)
2. **Load saved state** of Task B
3. CPU resumes execution of Task B from where it left off
4. Later, switch back to Task A (from saved state)

⏱️ This whole process happens in **microseconds** but has a small **overhead**.

---

### 🔷 Key Components Involved

* **Program Counter (PC)** – stores current instruction location
* **Stack Pointer (SP)** – tracks function call stack
* **Register values** – all active data in use
* **Task Control Block (TCB)** – where all this info is stored for each task

---

### 🔷 Example for Better Clarity

Imagine you’re running:

* Task 1: Read temperature sensor
* Task 2: Display data on screen

If Task 1 is reading and suddenly an **interrupt** fires from Task 2 (user pressed a button), the RTOS will:

* Save Task 1’s context
* Execute Task 2
* After completion, **restore Task 1’s state** and continue as if nothing happened

---

### 🔷 Context Switching in RTOS

In RTOS, **context switching** is handled by the **scheduler** and is based on:

* **Priorities** (e.g., Task A is more urgent than B)
* **Scheduling Policy** (Round Robin, Rate Monotonic, etc.)
* **Interrupts** (which may force switch instantly)

---

### 🔷 Overhead of Context Switching

| Pros                     | Cons                         |
| ------------------------ | ---------------------------- |
| Enables multitasking     | Uses CPU time (overhead)     |
| Handles priority         | Slight performance loss      |
| Supports real-time needs | Complex in low-power systems |

🔌 In **real-time systems**, the **overhead must be minimal**, or it can miss deadlines.

---

### 🔷 Real-Life Analogy 🎮

Imagine you're playing a video game (Task A), and your mom calls you (Task B):

* You **pause the game** (save state)
* You **attend the call**
* After the call, you **resume the game from where you left off**

That’s **context switching**. Simple but powerful.

---

<br><br>


---


## 🔷 What is Embedded C?

Embedded C is a **special version of the C language**, designed for **programming microcontrollers** (like the 8051 or Arduino) and **interfacing directly with hardware**.

> 🧠 TL;DR: It’s C with the ability to talk to sensors, control LEDs, motors, etc.

---

## 🔷 Why Use C in Embedded Systems?

* 🪶 **Lightweight** – Runs on low-memory devices
* 🛠️ **Hardware-oriented** – Directly accesses ports and memory
* ⚙️ **Fast & efficient** – Less overhead, perfect for real-time needs
* 👨‍💻 **Portable** – Code can be reused on different MCUs with slight tweaks

---

## 🔷 What Makes Embedded C Special?

| Regular C                 | Embedded C                           |
| ------------------------- | ------------------------------------ |
| Runs on PCs               | Runs on microcontrollers             |
| Uses standard libraries   | Uses microcontroller-specific libs   |
| No hardware access needed | Direct hardware access via registers |
| No timing constraints     | Must meet real-time deadlines        |

---

## 🔷 Key Concepts in Embedded C

### 1. **Direct Register Access**

Used to control I/O ports:

```c
P1 = 0xFF;  // Set Port 1 pins as HIGH
```

### 2. **Bitwise Operations**

Used to toggle, set, or clear specific pins:

```c
P1 |= (1<<0);  // Set bit 0 of Port 1
```

### 3. **Delay Functions**

Used to create pauses:

```c
for(int i=0; i<10000; i++);  // crude delay
```

### 4. **Interrupt Service Routines**

Embedded C allows using ISRs (interrupt service routines) directly:

```c
void timer0_ISR(void) interrupt 1 {
   // Code when Timer 0 overflows
}
```

---

## 🔷 Structure of Embedded C Program

```c
#include <reg51.h>        // MCU-specific header file

void main() {
   P1 = 0x00;             // Initialize Port 1
   while(1) {
      P1 = 0xFF;          // Turn all LEDs ON
      delay();
      P1 = 0x00;          // Turn all LEDs OFF
      delay();
   }
}

void delay() {
   int i;
   for(i=0;i<30000;i++); // simple delay
}
```

✅ **Main()** function
✅ **Initialization**
✅ **Continuous loop (while(1))**
✅ **Hardware control using registers**

---

## 🔷 Applications of Embedded C

* Controlling LEDs, sensors, motors
* Reading data from peripherals
* Writing logic for real-time systems (RTOS)
* Automating industrial machines, home appliances

---

<br><br>


## 📚 **Memory and I/O Devices Interfacing**

**diagram: true**
🔍 Search: `Memory and I/O interfacing in embedded systems diagram`

---

### 🧠 What’s “Interfacing” Anyway?

**Interfacing** just means **connecting** external stuff (like memory or sensors) to your microcontroller so they can **talk to each other and work together**.

Think of the microcontroller as a brain 🧠. It **needs memory** to think and **I/O devices** (like LEDs, buttons, sensors) to feel or act.

---

## 🔸 1. Memory Interfacing

💾 You connect **external memory** when:

* Internal memory of microcontroller is not enough
* You need faster or specialized memory (like EEPROM, Flash)

### 🔧 How It Works:

* Microcontroller sends an **address** to memory via **address bus**
* Sends or receives **data** via **data bus**
* Uses **control signals** to read/write (like `RD` or `WR`)

🗂️ Two types of memory interfacing:

1. **ROM (Read-Only Memory)** – Stores permanent programs
2. **RAM (Random Access Memory)** – Stores temporary data during execution

⏱️ Uses address decoders to select memory ranges.

---

## 🔸 2. I/O Devices Interfacing

This is all about **connecting external components** (LEDs, sensors, motors, switches, etc.) to **Input/Output pins** of your microcontroller.

### 🖥️ Two Types:

* **Input devices** → Like sensors or switches (send data IN)
* **Output devices** → Like LEDs or motors (get data OUT)

### 🧰 How It’s Done:

* I/O devices are connected to **I/O ports** (P0 to P3 in 8051)
* The microcontroller sends **HIGH/LOW** signals to control them

```c
P1 = 0xFF;  // Turns ON all pins in Port 1
```

📌 Example:

* **LED** on Port 2 → ON when pin is HIGH
* **Push button** → Reads as 1 (pressed), 0 (not pressed)

---

## 🔁 Summary in Real-World Terms

| Type        | Example Devices        | Role                        |
| ----------- | ---------------------- | --------------------------- |
| Memory      | ROM, RAM, EEPROM       | Store code & data           |
| I/O Devices | LEDs, buzzers, sensors | Interact with outside world |

---

<br><br>
<br>

# Unit 3



## 📘 **IoT Architecture and Functional Components**

**diagram: true**
🔍 Google search: `IoT architecture 4 layer model diagram` or `IoT functional architecture diagram`

![](img\iot.png)
IoT block diagram

---

### 🌐 **What is IoT Architecture?**

IoT architecture refers to the **structured framework** that connects physical devices, networks, and software to enable **smart communication** and **automation**.

It’s the **backbone of IoT systems**, showing **how data flows**, **where it’s processed**, and **how devices interact**.

---

## 🏗️ **IoT 4-Layer Architecture (Standard Model)**

### 1️⃣ **Perception Layer (aka Sensing Layer)**

* 🌱 **What it does:** Collects data from the physical world
* 📦 **Components:** Sensors, actuators, RFID, cameras
* 🧠 **Example:** A temperature sensor in a smart AC system
* ❗It’s the **eyes and ears** of IoT
  **diagram: true**
  🔍 Google: `Perception layer in IoT diagram`

---

### 2️⃣ **Network Layer (aka Transmission Layer)**

* 📡 **What it does:** Transfers data from perception to processing
* 🔌 **Technologies used:** Wi-Fi, Bluetooth, ZigBee, GSM, 5G
* 🌐 Handles **routing, transmission, and encryption**
  **diagram: true**
  🔍 Google: `Network layer in IoT architecture diagram`

---

### 3️⃣ **Middleware Layer (or Processing Layer)**

* 🖥️ **What it does:** Stores, processes, and analyzes data
* ☁️ **Tools used:** Cloud platforms, edge computing, data analytics
* 🧠 Performs **decision-making using AI/ML**
* Acts like a **smart brain** that thinks what to do next
  **diagram: true**
  🔍 Google: `Middleware layer IoT cloud edge`

---

### 4️⃣ **Application Layer**

* 📱 **What it does:** Delivers specific services to end users
* 🧩 **Examples:**

  * Smart homes
  * Smart agriculture
  * Healthcare monitoring apps
* It’s the **face of IoT**, where users interact
  **diagram: true**
  🔍 Google: `IoT application layer with examples`

---

## 🧩 **Functional Components of IoT**

| Component               | Function                                                      |
| ----------------------- | ------------------------------------------------------------- |
| **Sensors & Actuators** | Collect data / Act upon commands                              |
| **Embedded Systems**    | Microcontrollers process data (e.g. Arduino, ESP32)           |
| **Connectivity**        | Network for data transfer (WiFi, ZigBee, GSM)                 |
| **Data Processing**     | Cloud or Edge devices that store, analyze, and make decisions |
| **User Interface**      | Mobile/web apps where users monitor & control devices         |

---

### 💬 Real-Life Example: Smart Agriculture 🌾

* **Sensors** check soil moisture
* **Network** (ZigBee) sends data to cloud
* **Cloud processing** decides to turn ON water pump
* **Actuator** (relay) triggers irrigation
* **User** sees status via smartphone app

---

<br><br>



## 💡 **Arduino – Features, Types, Sketch Structure, and Pin Structures**

**diagram: true**
🔍 Google Search: `Arduino Uno pin diagram`, `Arduino sketch structure example`, `Types of Arduino board comparison`

---

### 🚀 What is Arduino?

**Arduino** is an **open-source microcontroller platform** used to build electronics projects. It includes:

* A **hardware board** (like Arduino Uno)
* A **programming environment (IDE)** to write code
* It is beginner-friendly and widely used in **IoT**, **automation**, and **robotics**.

---

## 🧩 1. **Features of Arduino**

| 🔹 Feature               | 🔍 Explanation                                      |
| ------------------------ | --------------------------------------------------- |
| **Open Source**          | Anyone can use or modify both software and hardware |
| **Cross-Platform**       | Works on Windows, Linux, and macOS                  |
| **USB Interface**        | Easy connection to PC for programming               |
| **Analog & Digital I/O** | Can read sensor values and control devices          |
| **Wide Library Support** | Tons of in-built libraries (e.g. Servo, LCD, etc.)  |
| **Low Power**            | Suitable for battery-powered embedded projects      |

---

## 📦 2. **Types of Arduino Boards (with examples)**

| 🔧 Type              | ✨ Key Features                        | 🧠 Use Case                          |
| -------------------- | ------------------------------------- | ------------------------------------ |
| **Arduino Uno**      | Most common; 14 digital I/O, 6 analog | Beginners, basic projects            |
| **Arduino Nano**     | Compact version of Uno, USB mini port | Space-limited projects               |
| **Arduino Mega**     | More memory and I/O pins              | Large projects, multiple sensors     |
| **Arduino Leonardo** | USB communication built-in            | Emulates keyboard/mouse              |
| **LilyPad Arduino**  | Soft, wearable electronics            | Wearable tech, e-textiles            |
| **Arduino Due**      | 32-bit ARM Cortex processor           | Advanced projects, real-time systems |
| **Arduino Pro Mini** | Very small, no USB, low power         | Embedded/sleep-mode applications     |

> ☝️ These names pop up in exams, so know **1-line features + use case**.

---

## 🧠 3. **Sketch Structure in Arduino Programming**

Arduino programs are called **sketches**. They always have **two main functions**:

```cpp
void setup() {
  // This runs ONCE at the start
}

void loop() {
  // This runs repeatedly like a loop
}
```

### 📄 Sketch Sections:

| Section              | Use                                                   |
| -------------------- | ----------------------------------------------------- |
| **Comments**         | Start with `//` or `/* */`, used for documentation    |
| **Libraries**        | Like `#include <Servo.h>` – adds prewritten functions |
| **Setup()**          | For initialization (e.g. setting pinMode)             |
| **Loop()**           | Runs continuously, where logic goes                   |
| **Custom Functions** | You can define your own functions for readability     |

---

## 🔌 4. **Arduino Pin Structure**

**diagram: true**
🔍 Google: `Arduino Uno pin diagram`

Arduino Uno (most common) pinout includes:

| 🔢 Pin Type                    | 📋 Description                                    |
| ------------------------------ | ------------------------------------------------- |
| **Digital I/O (0–13)**         | Can be input or output (LED, switch)              |
| **Analog Inputs (A0–A5)**      | Reads values like temperature or light            |
| **PWM Pins (\~3,5,6,9,10,11)** | Used for analog-like output using `analogWrite()` |
| **Power Pins**                 | 3.3V, 5V, GND                                     |
| **AREF**                       | Analog reference pin for sensors                  |
| **Reset Pin**                  | Resets the board manually                         |
| **Serial Pins (0=RX, 1=TX)**   | For communication with other devices              |

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20240422180102/Arduino-Board.webp)
---

## 🧠 Example Program (Full Sketch):

```cpp
// Blink LED on pin 13
void setup() {
  pinMode(13, OUTPUT); // Set pin 13 as output
}

void loop() {
  digitalWrite(13, HIGH); // Turn ON LED
  delay(1000);            // Wait 1 second
  digitalWrite(13, LOW);  // Turn OFF LED
  delay(1000);            // Wait 1 second
}
```

---


<br><br>




## 🧠 **Arduino Programming Structure**

**diagram: false** (you can draw the structure as a simple block layout with `setup()` and `loop()` functions)

Arduino programs are written in **C/C++ style** and are called **sketches**. These sketches always follow a specific structure made of **two core functions**.

---

### 🧱 **1. Basic Structure of an Arduino Sketch**

```cpp
void setup() {
  // Runs once when the board is powered ON or reset
}

void loop() {
  // Runs continuously after setup()
}
```

| 🔧 Section  | 📖 Description                                                                                      |
| ----------- | --------------------------------------------------------------------------------------------------- |
| **setup()** | - Runs only **once** at the beginning. <br> - Used to **initialize** pins, libraries, or variables. |
| **loop()**  | - Runs **repeatedly in a cycle**.<br> - Contains the **main program logic** that keeps executing.   |

---

### 🧩 **2. Additional Elements in Arduino Sketch**

| Component            | Use                                                               |
| -------------------- | ----------------------------------------------------------------- |
| `#include <Library>` | To include external libraries (e.g., Servo, LCD, WiFi).           |
| `// Comments`        | Lines starting with `//` are ignored by the compiler (for notes). |
| Global Variables     | Declared **above setup()** and used throughout the sketch.        |
| Custom Functions     | You can create your own functions to organize complex code.       |

---

### 🧪 **3. Sample Arduino Sketch with All Sections**

```cpp
int ldr = A0;     // LDR sensor connected to A0
int led = 9;      // LED connected to pin 9

void setup() {
  pinMode(led, OUTPUT);   // Set LED pin as output
}

void loop() {
  int light = analogRead(ldr);  // Read light level

  if (light < 500) {        // If it's dark
    digitalWrite(led, HIGH);  // Turn ON LED
  } else {
    digitalWrite(led, LOW);   // Turn OFF LED
  }

  delay(100);  // Small pause
}
```

---

### 🧠 **Structure Breakdown**

| Block         | What it does                                                   |
| ------------- | -------------------------------------------------------------- |
| `#include`    | Adds a library                                                 |
| `Global Var`  | Declares variables before setup                                |
| `setup()`     | Initializes servo and serial connection                        |
| `loop()`      | Moves the servo back and forth continuously                    |
| `Custom Code` | Uses `for` loops inside loop to change servo angle dynamically |

---


---
## Integration of Sensors and Actuators

## 🧠 What Does “Integration” Mean?

It means **connecting sensors and actuators to the Arduino**, and writing the code so they **talk to each other** — like:

* **Sensors**: Give data (e.g., temperature, light, motion).
* **Actuators**: Do stuff based on that data (e.g., turn on fan, light, motor).

---

## 🧩 Types of Integration

### 1. **Digital Sensors**

* Sensors that give only `HIGH` or `LOW` values.
* Example: **IR sensor**, **PIR motion sensor**

```cpp
int pir = 2;
int led = 13;

void setup() {
  pinMode(pir, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  int motion = digitalRead(pir);
  if (motion == HIGH) {
    digitalWrite(led, HIGH); // Motion detected: Turn ON LED
  } else {
    digitalWrite(led, LOW);  // No motion: Turn OFF LED
  }
}
```

---

### 2. **Analog Sensors**

* Gives a **range of values** (0–1023).
* Example: **LDR**, **Potentiometer**, **Temp sensors (LM35)**

```cpp
int sensor = A0;
int led = 9;

void loop() {
  int val = analogRead(sensor);
  analogWrite(led, val / 4); // Convert 0–1023 to 0–255 for brightness
}
```

---

### 3. **Actuators**

* Devices that **perform actions** based on commands.
* Common ones:

  * **LEDs** (light)
  * **Buzzers** (sound)
  * **Motors** (motion)
  * **Relays** (switch bigger things like fans)

---

## 🔄 Full Integration Example

Let’s say:

* **Input**: LDR senses darkness
* **Output**: Motor (fan) runs in dark

```cpp
int ldr = A0;
int motor = 8;

void setup() {
  pinMode(motor, OUTPUT);
}

void loop() {
  int light = analogRead(ldr);
  if (light < 500) {
    digitalWrite(motor, HIGH);  // It's dark: Turn ON motor
  } else {
    digitalWrite(motor, LOW);   // Bright: Turn OFF
  }
}
```

---

## ⚙️ How Arduino Handles It

| Arduino Does...  | Example                                  |
| ---------------- | ---------------------------------------- |
| `analogRead()`   | Reads sensor input                       |
| `digitalWrite()` | Turns actuators ON/OFF                   |
| `analogWrite()`  | Controls actuator speed (like dim light) |
| `pinMode()`      | Sets up pin direction                    |

---

## 📸 Diagram: `diagram: true`

**Google this:**
`Arduino sensors and actuators circuit diagram`

---

## 📦 Pro Tip

Always check:

* **Power** (does the sensor need 5V or 3.3V?)
* **Pin type** (digital or analog?)
* **Libraries** (some sensors like DHT11 need them)

---


<br>
<br>
<br>

# Unit 4




## 📡 **1. IoT Communication Protocols**




### 🔌 A. **Network Layer Protocols**

These move data between devices & cloud.

#### 🧊 **IP (Internet Protocol)**

* Used in Internet-based communication.
* IPv6 is more suitable due to IoT's large device count.

---

### 📨 B. **Transport Layer Protocols**

#### 🌐 **TCP (Transmission Control Protocol)**

* Reliable (guarantees delivery)
* Slower.
* Used for apps where data **must** arrive correctly (e.g., firmware updates).

#### 📡 **UDP (User Datagram Protocol)**

* Faster, but no guarantee of delivery.
* Used in **real-time data** (e.g., live temperature streaming).

---

### 🔄 C. **Application Layer Protocols**

These define *how* IoT devices share data.

| Protocol                                     | Use Case             | Features                                       |
| -------------------------------------------- | -------------------- | ---------------------------------------------- |
| **MQTT** (Message Queue Telemetry Transport) | Smart homes, sensors | Lightweight, reliable, publish/subscribe model |
| **CoAP** (Constrained Application Protocol)  | Low-power devices    | Works like HTTP but lightweight                |
| **HTTP/HTTPS**                               | Web-based IoT apps   | Secure, familiar, heavy for small devices      |
| **AMQP**                                     | Banking & industrial | Secure, queue-based                            |
| **DDS** (Data Distribution Service)          | Real-time apps       | High performance, complex                      |

---

📸 **diagram: true**
**Search:** `IoT communication protocols comparison table diagram`

---

## 🧭 **2. IoT Communication Models**

These describe *who talks to whom* and *how often*. Think of it as the conversation flow in IoT.

---

[Communication model GeeksForGeeks](https://www.geeksforgeeks.org/computer-science-fundamentals/communication-models-in-iot-internet-of-things/)


### ✅ 1. **Request-Response (Client-Server) Model**

* **How it works:**
  Client (device) sends a request ➡️ Server responds.
  It’s synchronous — the client waits for a response.

* **Example:**
  Smart sensor sending temperature data to a cloud server and waiting for acknowledgment.

* **Protocol used:** HTTP

* **Use case:** REST APIs, sensor reading, control commands

---

### ✅ 2. **Publish-Subscribe Model**

* **How it works:**
  Devices (publishers) send messages to a **broker**.
  Subscribers get updates from the broker **only for topics they subscribed to.**

* **Example:**
  Smart bulb subscribes to “room/light” topic.
  App publishes “ON” to that topic → bulb receives it.

* **Protocols used:** MQTT, AMQP

* **Use case:** Real-time control, notifications, chat-like systems

---

### ✅ 3. **Push-Pull Model**

* **How it works:**
  Data producers (pushers) keep sending data to a queue.
  Consumers (pullers) pick data when needed.

* **Example:**
  Weather sensors pushing data to a queue.
  Analytics engine pulls only when needed.

* **Protocols used:** AMQP, HTTP

* **Use case:** Efficient data processing pipelines.

---

### ✅ 4. **Exclusive Pair Model (1:1 communication)**

* **How it works:**
  Direct connection between two endpoints for private, secure communication.

* **Example:**
  BLE communication between fitness band and smartphone.

* **Use case:** Wearables, personal IoT gadgets

---

📸 **diagram: true**
**Search:** `IoT communication models (request-response, publish-subscribe, push-pull) diagram`

---

---

## ⚙️ **3. APIs (Application Programming Interfaces)**

> 🔑 **APIs are the rules that allow software to talk to hardware/cloud/apps.**

They help **IoT devices communicate with other systems**, like cloud servers, apps, and dashboards.

---

### A. **Types of APIs**

| API Type            | Use                                                |
| ------------------- | -------------------------------------------------- |
| **REST API**        | Most common, uses HTTP                             |
| **WebSocket API**   | For real-time updates                              |
| **GraphQL API**     | Efficient data fetching                            |
| **MQTT Broker API** | Used with MQTT for publishing/subscribing messages |

---

### B. **Why APIs Are Essential in IoT**

* 📤 **Send data** from device → cloud/server
* 📥 **Receive commands** from cloud → device
* 🔄 **Update apps** with real-time info
* 🔌 **Third-party integration** (e.g., Google Home, Alexa)

---

### 💡 Example:

* Your smart bulb API might let a mobile app:

  * Turn it on/off
  * Change color
  * Get current status

---

📸 **diagram: true**
**Search:** `IoT REST API communication diagram`

---


<br><br>



## 📡 **Bluetooth Architecture – CS3691 Unit IV**

### 📍What is Bluetooth?

Bluetooth is a **short-range wireless communication protocol** used in IoT devices for data exchange — like your phone talking to a smartwatch, or wireless headphones syncing with a laptop.

---

## 🧠 Core Concepts of Bluetooth Architecture

### 1. **Piconet**

* A **small ad-hoc network** formed by **1 master + up to 7 active slaves**.
* All communication happens through the master.
* 🧠 *Think of it like a group chat where only the admin can send messages, and others reply via the admin.*

### 2. **Scatternet**

* A combination of multiple piconets.
* A device can be part of **multiple piconets** (master in one, slave in another).
* Enables **larger and more flexible** Bluetooth networks.

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20240413085123/Untitled-Diagram---2024-04-13T085111331.webp)

### 📘 Use this in your answer:

> Bluetooth supports *Piconets* (1-to-many) and *Scatternets* (many interconnected Piconets) for network formation.

---

## 🧩 Bluetooth Protocol Stack (Optional but good for 13-marks)

### 📌 Layered View (Bottom to Top):

| Layer                                                  | Description                                                |
| ------------------------------------------------------ | ---------------------------------------------------------- |
| **Radio Layer**                                        | Handles the physical wireless transmission (2.4 GHz band). |
| **Baseband**                                           | Manages physical links, addresses, error correction.       |
| **Link Manager Protocol (LMP)**                        | Handles link setup, authentication, encryption.            |
| **Host Controller Interface (HCI)**                    | Acts as bridge between hardware and software.              |
| **Logical Link Control & Adaptation Protocol (L2CAP)** | Data multiplexing, segmentation, reassembly.               |
| **RFCOMM**                                             | Emulates serial ports for legacy compatibility.            |
| **SDP (Service Discovery Protocol)**                   | Lets devices discover each other’s services.               |

🧠 Easy way to remember:
**Radio ➝ Baseband ➝ LMP ➝ HCI ➝ L2CAP ➝ RFCOMM ➝ SDP**

But if you forget, don't panic — just explain **Piconet, Scatternet, and basic data flow**.

---

### 📍Working Steps:

1. Devices **discover** each other (Inquiry).
2. **Connection request** sent to master.
3. Master sets frequency hopping and syncs all devices.
4. Devices **pair** (authentication).
5. Data transfer begins (with encryption if needed).

---

## 💡 Real-Life Applications:

* Wireless earbuds
* Smartwatches
* Fitness trackers
* IoT home devices (Bluetooth smart bulbs, locks)

---

## 🔍 diagram: true

**Google search phrase:**
`Bluetooth architecture protocol stack diagram`
Or
`Bluetooth piconet and scatternet diagram`

---

<br><br>



## 🌐 **Wi-Fi Architecture**

### 📍What is Wi-Fi?

Wi-Fi (Wireless Fidelity) is a **wireless networking technology** that uses radio waves to provide high-speed **internet and network connections** without cables.

---

## 🏗️ Components of Wi-Fi Architecture

### 1. **Station (STA)**

* Any Wi-Fi-enabled device (e.g. laptop, smartphone, IoT sensor).
* It contains a **wireless network interface card (NIC)**.

### 2. **Access Point (AP)**

* Acts as a **central transmitter and receiver**.
* Provides wireless connectivity to the devices.
* Think of it like a router or hotspot.

### 3. **Wireless Medium**

* Uses **radio waves** (2.4 GHz or 5 GHz band) to transmit data.
* Works based on **IEEE 802.11 standards**.

### 4. **Distribution System (DS)**

* Connects **multiple access points** using a **wired** or **wireless** backbone (Ethernet, fiber).
* Helps extend coverage area like in campuses or multi-floor buildings.

---

## 📶 Modes of Operation

### 🔹 **Infrastructure Mode** (most common)

* Devices (STAs) connect to an **Access Point**.
* Access Point connects to **internet or other networks**.
* Used in homes, colleges, offices.

### 🔹 **Ad-Hoc Mode**

* No Access Point needed.
* Devices communicate **directly** with each other.
* Useful in temporary or emergency networks.

![alt text](https://www.researchgate.net/publication/316175326/figure/fig1/AS:495727332610048@1495202014846/Ad-hoc-mode-vs-Infrastructure-mode-IEEE80211-introduced-many-types-of-the-Wi-Fi.png)
---

## 💻 Internal Layers in Wi-Fi (IEEE 802.11 stack)

| Layer                    | Function                                                   |
| ------------------------ | ---------------------------------------------------------- |
| **Physical Layer (PHY)** | Transmission via radio waves                               |
| **MAC Layer**            | Medium Access Control (handles collisions, frame delivery) |
| **Network Layer**        | IP addressing & routing                                    |
| **Transport Layer**      | Ensures error-free delivery (TCP/UDP)                      |
| **Application Layer**    | User applications (browsers, IoT apps)                     |

🧠 For IoT focus more on PHY and MAC layers.

---

## 🛜 How Wi-Fi Works

1. **STA scans** for nearby APs.
2. Connects via **SSID (network name)** and password.
3. AP assigns an **IP address** using DHCP.
4. Devices communicate using **TCP/IP** over radio waves.

---

## 📲 Applications of Wi-Fi in IoT

* Smart homes (lights, locks, thermostats)
* Surveillance systems (IP cameras)
* Healthcare (patient monitoring devices)
* Smart agriculture (sensor networks)
* Wearable IoT gadgets

---

## ✍️ diagram: true

**Google Search Phrase**:
`Wi-Fi architecture diagram IEEE 802.11`
or
`Wi-Fi infrastructure mode vs ad-hoc diagram`

---

<br><br>


## 🌐 Zigbee Architecture

### 🔍 What is Zigbee?

Zigbee is a **low-power, low-data rate, wireless communication protocol** built on **IEEE 802.15.4** standard. It’s designed for **short-range communication** in IoT devices like smart lighting, energy meters, home automation, etc.

---

## 🧠 Key Features:

* **Range**: \~10 to 100 meters
* **Data Rate**: 20 Kbps – 250 Kbps
* **Frequency**: 2.4 GHz (global), 868 MHz (EU), 915 MHz (USA)
* **Power Usage**: Super low 🔋
* **Ideal for**: Sensor networks, home automation, industrial monitoring

---

## 🏗️ Zigbee Network Architecture

Zigbee networks use a **star**, **tree**, or **mesh** topology.

### 1. **Zigbee Coordinator (ZC)**

* Only one per network
* Starts the network, assigns PAN ID
* Stores info about the network

### 2. **Zigbee Router (ZR)**

* Extends network range
* Forwards data to other nodes
* Can connect with other routers or end devices

### 3. **Zigbee End Device (ZED)**

* Has limited functionality
* Communicates only with its parent (ZC or ZR)
* Lowest power consumption (used in sensors, remotes)

🧠 Think of ZC as the "brain", ZRs as the "roads", and ZEDs as the "houses"!

---

## 🔄 Types of Topologies

### 🌟 Star Topology:

* All devices talk to the Coordinator directly
* Easy, but range-limited

### 🌳 Tree Topology:

* Routers help build a tree structure
* More scalable than star

### 🕸️ Mesh Topology:

* Devices can communicate with many neighbors
* Highly reliable, self-healing

![alt text](https://www.blackhillsinfosec.com/wp-content/uploads/2021/08/Picture4.png)

---

## 🗂️ Zigbee Protocol Stack (4 Layers)

| Layer                 | Description                                     |
| --------------------- | ----------------------------------------------- |
| **Application Layer** | Defines how apps use the network                |
| **Network Layer**     | Handles routing, device addressing              |
| **MAC Layer**         | Controls access to the wireless channel         |
| **Physical Layer**    | Modulates and transmits signals (IEEE 802.15.4) |

![alt text](https://www.researchgate.net/publication/265150617/figure/fig2/AS:353974063517705@1461405401407/EEE820154-ZigBee-protocol-stack-architecture.png)

📌 Zigbee is light on resources and heavy on networking. Super useful in **battery-powered IoT devices**.

---

## 📶 Working of Zigbee Network

1. **Coordinator forms network**, assigns PAN ID.
2. **Routers join** to relay data and expand range.
3. **End Devices join** under routers/coordinator.
4. Devices exchange data using short-range radio and sleep often to save power.

---

## 🖼️ diagram: true

**Google search query:**
`Zigbee architecture with coordinator router end device diagram`
or
`Zigbee protocol stack and network topology diagram`

---

## 🔧 Applications of Zigbee

* Smart homes (lights, fans, security)
* Industrial automation
* Smart agriculture (soil moisture sensors)
* Healthcare wearables
* Street lighting systems

---
