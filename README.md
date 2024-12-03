# AI-Powered Clothing Recommendation System

## Overview
#### This project is an AI-powered clothing recommendation system that integrates Vanna AI with OpenAI's GPT-3.5-turbo and interacts with an SQLite database containing various clothing items categorized by occasion, material, brand, size, and more. The system allows users to ask queries related to clothing items, and the AI provides relevant recommendations and details from the database based on their input.
## Features
#### Natural Language Querying: Users can enter queries in natural language, and the AI interprets them to fetch relevant data from the database.
#### Occasion-Based Clothing Recommendations: The system recommends clothing based on occasions like marriage, office, winter, etc.
#### AI Integration: Uses Vanna AI integrated with OpenAI's GPT-3.5-turbo model to process user queries and fetch data.
#### SQLite Database: The clothing data is stored in an SQLite database, which contains detailed information on items such as color, size, category, material, and occasion.
## Requirements
#### ython 3.x
#### Vanna AI library
#### OpenAI API key
#### SQLite database (clothing data)
#### Libraries: sqlite3, chromadb, openai, and other dependencies as required
## How It Works
#### Vanna AI: The Vanna AI library is used to connect to OpenAI's GPT-3.5-turbo, which processes the user query and generates SQL queries to fetch relevant data from the SQLite database.
#### Database Operations: The script updates the database schema (e.g., making values lowercase), retrieves relevant data, and trains the AI on the schema.
#### AI Learning: The AI continuously learns from the queries and responses to provide better recommendations over time.
