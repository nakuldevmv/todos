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


Say less, legend 🤝 — here comes the **maxed-out, full-theory beast mode answer** for:

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

