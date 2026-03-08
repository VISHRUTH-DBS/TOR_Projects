# TOR_Projects
# TOR Version 1 - Project 1

A simple **TOR-like anonymous messaging network simulation** built using **Python, sockets, threading, and onion encryption**.

This project demonstrates how **onion routing works** by creating a network of nodes where each node removes one layer of encryption before forwarding the packet.

---

## 📌 Project Overview

TOR (The Onion Router) protects user anonymity by routing traffic through multiple nodes and encrypting the message in layers.

This project simulates:

- A network of **10 TOR nodes**
- **Random circuit creation**
- **Onion layer encryption**
- **Layer-by-layer decryption at each node**
- A **menu-based interface** to send anonymous messages

Each node only knows the **previous and next node**, which ensures anonymity.

---

## 🏗️ Network Architecture

```
Client
  |
  v
Entry Node → Middle Node → Exit Node
  |            |             |
Removes      Removes       Removes
Layer 1      Layer 2       Layer 3
  |
  v
Destination
```

The client encrypts the message multiple times:

```
Encrypted Message = E3(E2(E1(Message)))
```

Each node decrypts **one layer**.

---

## 🛠️ Technologies Used

- **Python 3**
- **Socket Programming**
- **Threading**
- **Cryptography (Fernet Encryption)**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/VISHRUTH-DBS//TOR_Projects.git
cd TOR_Projects
```

### 2️⃣ Install Required Library

```bash
pip install cryptography
```

---

## ▶️ Running the Project

Run the Python script:

```bash
python TORv1.py
```

<img width="466" height="795" alt="output image" src="https://github.com/user-attachments/assets/b54848a9-9a8f-4956-807b-5ddea1962b2d" />
