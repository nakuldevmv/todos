# Embedded Systems and IoT (CS3691)



## 🌟 UNIT I – 8-BIT EMBEDDED PROCESSOR

**Topics Covered:**

* 8-Bit Microcontroller
* Architecture
* Instruction Set and Programming
* Programming Parallel Ports
* Timers and Serial Port
* Interrupt Handling

---

### 🔹 1. 8-Bit Microcontroller

* A **microcontroller** is a compact integrated circuit designed to govern a specific operation in an embedded system.
* “8-bit” means it can process 8 bits of data at a time (the size of its internal registers and ALU).
* **8051** is the most commonly used 8-bit microcontroller.

📌 **Features of 8051:**

* 4K ROM, 128B RAM
* 4 parallel I/O ports (each 8-bit wide)
* 2 Timers
* 1 Serial communication port
* 5 Interrupts (2 external, 3 internal)

---

### 🔹 2. Architecture of 8051

**diagram: true**
🔍 Google: `8051 Microcontroller architecture diagram`

📌 **Key Components:**

* **ALU** – Performs arithmetic/logic operations.
* **Registers** – Includes accumulator (A), B register, R0–R7.
* **ROM** – Stores program code (4K).
* **RAM** – Stores temporary data (128 bytes).
* **Program Counter (PC)** – Tracks instruction address.
* **Timers/Counters** – Handle timing operations.
* **I/O Ports** – P0–P3 used for interfacing with peripherals.
* **Interrupt control unit** – Handles interrupts.
* **Serial port** – For serial communication (TX/RX lines).

---

### 🔹 3. Instruction Set & Programming

📌 Divided into 4 groups:

1. **Data Transfer Instructions** (`MOV`, `PUSH`, `POP`, etc.)
2. **Arithmetic Instructions** (`ADD`, `SUBB`, `INC`, `DEC`)
3. **Logical Instructions** (`ANL`, `ORL`, `XRL`, `CLR`)
4. **Control Instructions** (`SJMP`, `ACALL`, `RET`, `NOP`)

✅ Example:

```asm
MOV A, #45H ; Move 45H to accumulator
ADD A, R2   ; Add register R2 to accumulator
```

---

### 🔹 4. Programming Parallel Ports

**Ports:** P0, P1, P2, P3

📌 Each port is 8-bit wide and can be configured as input/output.
✅ Example:

```c
P1 = 0xFF; // Make Port1 all high (input mode)
P2 = 0x00; // Make Port2 all low (output mode)
```

🧠 Common Uses:

* Interface LEDs, switches, LCDs, etc.

---

### 🔹 5. Timers & Serial Port

**Timers (T0, T1)**
Used for delay generation, counting external pulses.

📌 Timer Modes (M0 to M3)

* Mode 0: 13-bit timer
* Mode 1: 16-bit timer
* Mode 2: 8-bit auto-reload
* Mode 3: Split timer mode

✅ Example use: Generate 1ms delay.

**Serial Port**
Used to send/receive data over serial communication (RS232, UART).

📌 Registers:

* `SBUF` – Serial buffer
* `SCON` – Serial control
* `TI` and `RI` – Transmit and Receive flags

---

### 🔹 6. Interrupt Handling

📌 8051 supports 5 interrupts:

1. INT0 (External 0)
2. TF0 (Timer 0 Overflow)
3. INT1 (External 1)
4. TF1 (Timer 1 Overflow)
5. Serial communication (RI/TI)

✅ **ISR** – Interrupt Service Routine
💡 When an interrupt occurs, control jumps to ISR.

**diagram: true**
🔍 Google: `8051 interrupt vector table`

