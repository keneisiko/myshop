# MyShop

A simple e-commerce web application built with Django.

## Features

- User registration, login, and profile management
- Product catalog with detailed product pages
- Shopping cart functionality
- Checkout process
- Admin panel for managing products and users
- Media support for product images and user avatars

## Project Structure

```
myshop/
  accounts/      # User authentication and profile management
  shop/          # Product catalog, cart, and shop logic
  media/         # Uploaded media files (avatars, product images)
  static/        # Static files (CSS, images)
  templates/     # HTML templates
  manage.py      # Django management script
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo/myshop
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database:**

   - Create a new database and user in PostgreSQL (you can use pgAdmin or psql):
     ```sql
     CREATE DATABASE myshop_db;
     CREATE USER myshop_user WITH PASSWORD 'yourpassword';
     GRANT ALL PRIVILEGES ON DATABASE myshop_db TO myshop_user;
     ```
   - Update your `myshop/settings.py` with the following configuration:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'myshop_db',
             'USER': 'myshop_user',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```
   - **Note:** The database itself must be created manually. Django will create the tables automatically after running migrations.

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the app:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register a new user or log in with an existing account.
- Browse products, add them to your cart, and proceed to checkout.
- Admins can log in to `/admin/` to manage products and users.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. 
