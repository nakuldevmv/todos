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
