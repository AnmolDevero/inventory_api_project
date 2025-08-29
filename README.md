# Inventory Management API

A Django REST Framework-based API for managing products in an inventory system.  
This project allows authenticated users to perform CRUD operations on products, with authentication using JWT.

##  Features

- **User Authentication** (JWT-based login & signup)
- **CRUD for Products** (Create, Read, Update, Delete)
- **Pagination** 
- **Filtering, Searching, and Ordering on Products**
- **Logout endpoint** (JWT token blacklist)
- **Delete account endpoint**

---

##  Technologies Used

- **Python**
- **Django**
- **Django REST Framework**
- **Simple JWT Authentication**

---

##  Project Structure

inventory/
│
├── inventory/ # Project settings and URLs
├── products/ # Main app containing models, serializers, views
├── manage.py
├── README.md
└── requirements.txt

---

##  Installation & Setup

### 1️ Clone the Repository
```bash
git clone https://github.com/AnmolDevero/inventory_api_project.git
cd inventory_api_project

# 2️ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3️ Install Dependencies
pip install -r requirements.txt

# 4️ Apply Migrations
python manage.py makemigrations
python manage.py migrate

# 5️ Create Superuser
python manage.py createsuperuser

# 6️ Run the Server
python manage.py runserver
```

---

# Authentication
This API uses JWT (JSON Web Tokens) for authentication.

Sign Up → /api/signup/

Login → /api/token/

Refresh Token → /api/token/refresh/

Include the token in the Authorization Header for protected requests:
Authorization: Bearer your_access_token

---

# API Endpoints

Authentication
Method	 Endpoint	          Description
POST	 /api/signup/	      Create a new user
POST	 /api/token/	      Get JWT access and refresh tokens
POST	 /api/token/refresh/  Refresh access token
POST	/api/logout/	        Logout (blacklist refresh token)
DELETE	/api/delete/account/	Delete the authenticated user's account

Products
Method	 Endpoint	            Description
GET	     /api/products/	        List all products (paginated)
POST	 /api/products/	        Create a new product
GET	     /api/product/{id}/	Retrieve a specific product
PUT	     /api/product/{id}/	Update a product
patch    /api/product/{id}/    
DELETE	 /api/product/{id}/	Delete a product

---

# Example Request (Create Product)
POST /api/products/

{
    "name": "Laptop",
    "description": "Dell Inspiron 15",
    "price": 1200,
    "quantity": 10
}
Headers:

Authorization: Bearer your_access_token
Content-Type: application/json


# Example Request (Get Products)
GET /api/products/

Headers:
Authorization: Bearer your_access_token

---

# Pagination

Products list is paginated:
Default page size: 3
Example:
GET /api/products/?page=2

---

# Admin Panel

Django admin panel available at:
http://127.0.0.1:8000/admin/

---

# License
This project is licensed under the MIT License.


