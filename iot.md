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

The next unit will be updated soon...


