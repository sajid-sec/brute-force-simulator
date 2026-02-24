# Web Login Brute-Force Simulator

An educational lab environment designed to demonstrate the mechanics of dictionary-based brute-force attacks against web authentication forms. 

## Overview
This project consists of two main components:
1. **The Target (`app.py`):** A vulnerable local web server built with Flask, featuring a simulated admin login portal.
2. **The Attacker (`attacker.py`):** An automated Python script that utilizes the `requests` library to systematically iterate through credential wordlists until a successful login is achieved.

## Prerequisites
* Python 3.x
* `flask`
* `requests`

## Setup & Usage

**1. Clone the repository and navigate to the directory:**
`git clone https://github.com/sajid-sec/brute-force-simulator.git`
`cd brute-force-simulator`

**2. Set up a virtual environment (Recommended):**
`python3 -m venv lab_env`
`source lab_env/bin/activate`
`pip install flask requests`

**3. Start the target server:**
`python3 app.py`
*(The server will run locally on http://127.0.0.1:5000)*

**4. Launch the attack:**
Open a second terminal window, navigate to the project folder, activate the virtual environment, and run:
`python3 attacker.py`

## Disclaimer
**Educational Purposes Only.** This project was created strictly for local, academic demonstration. Do not use these scripts against any system or network that you do not explicitly own or have written permission to test.
