# Currency Exchange Dashboard | Flask, SQLite, REST API

A complete end-to-end web application built with Python and Flask, allowing users to check real-time currency exchange rates.
The app connects to the official NBP (National Bank of Poland) API and stores historical data in a local SQLite database. It features an interactive, responsive UI for seamless user experience.

## Tech Stack:

- **Python** – backend logic, API integration
- **Flask** – web framework
- **SQLite** – lightweight relational database
- **HTML/CSS** – frontend styling
- **NBP REST API** – data source

---

## Screen Shot
![image](https://github.com/user-attachments/assets/384791d0-7cf8-4d9c-8c20-51cb793747a3)


---

## Features

- Fetches current exchange rates from the official NBP API
- Stores historical data in SQLite for offline access and trend analysis
- Clean, mobile-responsive UI
- Real-time currency lookup for PLN to other currencies
- Flask-based backend for performance and simplicity
- (Planned) Daily job scheduler for automatic updates

---

## App Workflow

1. **Extract**: Flask app fetches data from NBP public API (JSON format)
2. **Load**: Data is saved into a local SQLite database
3. **Serve**: Data is displayed on the web dashboard using Flask templates

---

##  Project Goals
This project was created to:
- Practice REST API integration and data persistence in a real-world web context
- Build and deploy a functional web app using Flask
- Explore full-stack development from backend to frontend