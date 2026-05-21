# Bookstore API

A simple RESTful API for managing a bookstore's inventory with CRUD operations on books.

## Project Overview

This project implements a backend API that allows users to create, read, update, and delete books from a bookstore database. The API follows REST principles and provides a clean interface for managing book information.

## Technologies Used

- **Backend Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **API Documentation**: Swagger UI (built-in with FastAPI)
- **Environment Management**: python-dotenv
- **Server**: Uvicorn

## Project Structure

```
bookstore-api/
├── app.py                          # Main FastAPI application
├── src/
│   ├── db/
│   │   ├── db_conn.py             # Database connection configuration
│   │   ├── create_tables.py        # Script to create database tables
│   │   └── __init__.py
│   ├── models/
│   │   ├── book.py                # SQLAlchemy book model
│   │   ├── update_book_model.py   # Pydantic model for updates
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── book_schema.py         # Pydantic schemas (BookCreate, BookUpdate, BookResponse)
│   │   └── __init__.py
│   ├── controllers/
│   │   ├── add_book_to_db.py      # Create book logic
│   │   ├── get_books.py           # Get all books logic
│   │   ├── get_book_by_id.py      # Get single book logic
│   │   ├── update_book.py         # Update book logic
│   │   ├── delete_book.py         # Delete book logic
│   │   └── __init__.py
│   └── routes/
│       ├── add_book.py            # POST /books endpoint
│       ├── get_books.py           # GET /books endpoint
│       ├── get_signle_book.py     # GET /books/{id} endpoint
│       ├── update_book.py         # PUT /books/{id} endpoint
│       ├── delete_book.py         # DELETE /books/{id} endpoint
│       └── __init__.py
├── .env                            # Environment variables (database URL)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## How to Run Locally

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd bookstore-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   - Create a `.env` file in the root directory
   - Add your database connection string:
     ```
     database_url=postgresql://username:password@localhost:5432/bookstore_db
     ```

6. **Create database tables**
   ```bash
   python src/db/create_tables.py
   ```

7. **Run the server**
   ```bash
   uvicorn app:app --reload
   ```

   The API will be available at: `http://127.0.0.1:8000`

## API Endpoints

### 1. Create a Book
- **Endpoint**: `POST /books`
- **Request Body**:
  ```json
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 20.99,
    "isbn": "1234567890",
    "published_date": "2018-10-16"
  }
  ```
- **Response**: `{"response": "Book added successfully"}`

### 2. Get All Books
- **Endpoint**: `GET /books`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "title": "Atomic Habits",
      "author": "James Clear",
      "price": 20.99,
      "isbn": "1234567890",
      "published_date": "2018-10-16"
    }
  ]
  ```

### 3. Get a Single Book by ID
- **Endpoint**: `GET /books/{id}`
- **Example**: `GET /books/1`
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 20.99,
    "isbn": "1234567890",
    "published_date": "2018-10-16"
  }
  ```
- **Error Response** (404): `{"detail": "Book not found"}`

### 4. Update a Book
- **Endpoint**: `PUT /books/{id}`
- **Example**: `PUT /books/1`
- **Request Body** (all fields optional):
  ```json
  {
    "title": "Atomic Habits (Revised Edition)",
    "price": 22.99
  }
  ```
- **Response**: `{"response": "Book updated successfully"}`

### 5. Delete a Book
- **Endpoint**: `DELETE /books/{id}`
- **Example**: `DELETE /books/1`
- **Response**: `{"response": "Book deleted successfully"}`
- **Error Response** (404): `{"detail": "Book not found"}`

## Testing the API

### Using Postman

1. Open Postman
2. Create requests for each endpoint listed above
3. For POST and PUT requests, set the request body to JSON format
4. Test each endpoint to verify it works correctly

### Using FastAPI Swagger UI

1. Navigate to: `http://127.0.0.1:8000/docs`
2. Try out each endpoint directly from the interactive documentation
3. All endpoints are listed and can be tested with sample data

## Book Model

Each book record contains:

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Unique identifier (auto-generated) |
| title | String | Book title |
| author | String | Author name |
| price | Float | Book price |
| isbn | String | ISBN identifier |
| published_date | Date | Publication date (optional) |

## Database Schema

```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(50),
    price FLOAT,
    isbn VARCHAR(20),
    published_date DATE
);
```

## Concepts Learned

- RESTful API design principles
- CRUD operations implementation
- Database connectivity with SQLAlchemy ORM
- Request/response validation with Pydantic
- FastAPI framework basics
- Error handling and HTTP status codes
- Environment configuration management

## Notes

- All timestamps should be in ISO 8601 format (YYYY-MM-DD)
- ISBN should be unique in the system
- Price should be a positive float value
- The API includes proper error handling with appropriate HTTP status codes