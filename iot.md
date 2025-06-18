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

The next unit will be updated soon...
