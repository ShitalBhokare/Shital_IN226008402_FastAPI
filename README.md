# 🚀 FastAPI Internship Practice — IN226008402

This repository presents my FastAPI internship practice project, where I implemented a complete backend system covering core and advanced API development concepts. The project is designed to simulate real-world backend behavior using a product and order management system, gradually evolving from simple endpoints to more complex and optimized API patterns.

The application is built using FastAPI and demonstrates structured API design, request validation, and efficient data handling using in-memory storage. It includes product management, advanced querying capabilities, and an order processing workflow with proper validations.

## ⚙️ Setup

Install dependencies:
pip install fastapi uvicorn  

Run the server:
uvicorn main:app --reload  

Access the application:
http://127.0.0.1:8000  

Interactive API documentation:
http://127.0.0.1:8000/docs  

## 📌 Implementation Overview

The project begins with product-related operations, where products are stored in memory and can be searched using case-insensitive matching. This ensures better usability and mimics real-world search functionality.

Sorting capabilities are implemented to allow products to be ordered dynamically by fields such as price and name, with support for both ascending and descending order. Proper validation is included to restrict invalid sorting parameters. A custom sorting logic is also developed to group products by category and then sort them by price within each category, demonstrating multi-level sorting.

Pagination is introduced to efficiently handle large datasets by splitting results into pages with configurable limits. This is applied not only to products but also to the order dataset, ensuring scalability and consistency across the application.

A combined API endpoint is implemented to integrate searching, sorting, and pagination into a single request. This reflects real-world backend optimization where multiple operations are handled together for better performance and flexibility.

CRUD operations are supported for managing product data, allowing creation, retrieval, updating, and deletion of products while maintaining data integrity and preventing invalid operations.

An order management system is implemented to simulate transactional workflows. Users can place orders by selecting products, with validation checks for product existence and stock availability. The system calculates total pricing dynamically and stores orders in memory.

Order search functionality is implemented using case-insensitive matching on customer names, improving usability. Additionally, pagination is applied to orders to support efficient browsing as the dataset grows.

The application includes strong validation and error handling mechanisms to ensure robustness. Invalid inputs, unsupported query parameters, missing resources, and edge cases such as empty datasets or out-of-stock products are handled gracefully.

## 🧠 Key Concepts

- FastAPI routing and endpoint design  
- Query parameters and input validation  
- Pydantic models for structured request handling  
- CRUD operations for data management  
- Case-insensitive search implementation  
- Sorting with single and multiple fields  
- Pagination for scalable data handling  
- Combined query operations (search + sort + pagination)  
- Order processing and business logic validation  
- Error handling and edge case management  

## 🎯 Highlights

- Clean and structured backend architecture  
- Progressive implementation from basic to advanced features  
- Real-world API design patterns  
- Reusable and maintainable logic  
- Efficient handling of data operations  
- Fully testable using Swagger UI  

## 👩‍💻 Author

FastAPI Internship Practice — IN226008402  
Assignments 1–5 completed as part of internship training
