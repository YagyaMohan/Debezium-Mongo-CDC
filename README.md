# Debezium MongoDB CDC to Kafka

This project demonstrates real-time Change Data Capture (CDC) using MongoDB, Kafka, and Debezium. It includes a Python Kafka consumer that listens to change events from a MongoDB collection via Debezium and prints them in the terminal.

---

## Project Components

- **MongoDB (Replica Set)** – Source database for CDC
- **Kafka + Zookeeper** – Message broker for change events
- **Debezium Connect** – Captures MongoDB changes and publishes them to Kafka
- **Python Kafka Consumer** – Consumes CDC events from Kafka and displays them

---
