# 🏥 Healthcare Backend System

This project is a backend system for a healthcare application built using Django, Django REST Framework, PostgreSQL, and JWT authentication. It provides secure RESTful APIs for user authentication, managing patients, doctors, and patient-doctor mappings.

## ✅ Features
- User registration and login with JWT (using `djangorestframework-simplejwt`)
- Token-protected endpoints
- CRUD APIs for:
  - Patients (linked to users)
  - Doctors
  - Patient-Doctor relationships
- PostgreSQL database integration
- Input validation and error handling
- Environment variable configuration using `.env`
- Fully tested with Postman

## ⚙️ Tech Stack
- Python 3.11+
- Django 5.x
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt
- python-decouple
- psycopg2-binary

## 📁 Project Structureproject-root/

Healthcare_Backend                   # Root folder
├── core/                            # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                    # Models: User, Patient, Doctor, Mapping
│   ├── serializers.py               # DRF serializers for all models
│   ├── views.py                     # DRF views / viewsets
│   ├── urls.py                      # App-level routes (included in project urls)
│   ├── tests.py
│   └── migrations/
│       └── __init__.py
│       └── 0001_initial.py
│       └── ...
│
├── healthcare/                      # Django project config folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                  # Global settings (uses .env for secrets)
│   ├── urls.py                      # Main router for API endpoints
│   └── wsgi.py
│
├── manage.py                        # Django CLI entrypoint
├── requirements.txt                 # Project dependencies
├── .env.example                     # Sample env file (do not include real .env)
├── README.md                        # Project documentation


## 🛠 Setup Instructions
Follow the steps below to set up the project locally.

### 1. Clone the project or extract the zip
cd path/to/your/folder
	 if zipped, extract here

### 2. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
Create a .env file in the root directory (same level as manage.py),  using .env.example as a reference:
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

### 5. Run migrations
python manage.py makemigrations
python manage.py migrate

### 6. (Optional) Create a superuser
python manage.py createsuperuser

### 7. Start the development server
python manage.py runserver

📮 API Endpoints
⚠️ All routes (except register/login) require a valid Authorization: Bearer <access_token> header.
✅ 1. Patient APIs
Method	        Endpoint	          Description
POST	    /api/patients/	        Create a patient
GET	        /api/patients/	        List all patients
GET	        /api/patients/<id>/	    Retrieve a patient
PUT	        /api/patients/<id>/	    Update a patient
DELETE	    /api/patients/<id>/	    Delete a patient

✅ 2. Doctor APIs
Method	       Endpoint	                Description
POST	    /api/doctors/	           Create a doctor
GET	        /api/doctors/	           List all doctors
GET	        /api/doctors/<id>/	       Retrieve a doctor
PUT	        /api/doctors/<id>/	       Update a doctor
DELETE	     /api/doctors/<id>/	       Delete a doctor

✅ 3. Patient-Doctor Mapping APIs
Method	            Endpoint	                  Description
POST	        /api/mappings/	                Create a mapping
GET	            /api/mappings/	                List all mappings
GET	            /api/mappings/<patient_id>/	    List mappings for a patient
DELETE	        /api/mappings/<id>/	            Delete a mapping

✅ 4. Authentication APIs
Method	Endpoint	            Description
POST	/api/auth/register/	    Register a user
POST	/api/auth/login/	    Obtain JWT tokens

🧪 API Testing with Postman
1.	Use /api/auth/register/ and /api/auth/login/ to register and obtain an access token
2.	Add the token to all subsequent requests:
Key: Authorization
Value: Bearer <access_token>
3.	Test all endpoints as described above
	
👤 Author
Your Name: Arkankhan Pathan
Email: arkankhanpathan008@gmail.com
Submitted for: Backend Internship Assignment


