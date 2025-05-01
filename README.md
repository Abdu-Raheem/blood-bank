# 🩸 Blood Bank Management System

[![Django](https://img.shields.io/badge/Django-4.0-brightgreen.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.14-blue.svg)](https://www.django-rest-framework.org/)
[![JWT Auth](https://img.shields.io/badge/JWT%20Auth-SimpleJWT-yellow.svg)](https://github.com/jazzband/djangorestframework-simplejwt)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A modern blood bank management system for College Of Engineering Thalassery, featuring web portal for student registration and mobile app for admin management with JWT authentication.

## ✨ Key Features

- **Dual Interface System**: Web portal for students + Mobile app for admins
- **Secure JWT Authentication**: Access/refresh token system
- **Password Recovery**: OTP-based password reset flow
- **Blood Group Analytics**: Real-time donor statistics
- **Alumni Management**: Year-out student handling
- **Donor Tracking**: Last donation date monitoring
- **Admin Dashboard**: Comprehensive management interface

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip
- Virtualenv (recommended)

### Installation
```bash
# Clone the repository
git clone [https://github.com/yourusername/blood-bank.git](https://github.com/Abdu-Raheem/blood-bank.git)
cd blood-bank

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## 🌐 System Architecture

```
Web Portal (Students) ↔ REST API ↔ Mobile App (Admins)
                      ↑
                 Django Admin
```

## 🔐 Authentication Flow

1. Obtain JWT tokens:
   ```http
   POST /api/token/
   Content-Type: application/json

   {
     "username": "admin",
     "password": "yourpassword"
   }
   ```

2. Use access token in headers:
   ```
   Authorization: Bearer your.access.token
   ```

## 📊 API Endpoints

### Admin Authentication
| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/admin/` | POST | Admin login | `username`, `password` |
| `/api/token/` | POST | Get JWT tokens | `username`, `password` |
| `/api/token/refresh/` | POST | Refresh access token | `refresh_token` |

### Password Management
| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/api/forget-password/` | POST | Initiate password reset | `email` |
| `/api/otp-verify/` | POST | Verify OTP | `email`, `otp` |
| `/api/reset-password/` | PUT | Set new password | `email`, `password` |

### Donor Management
| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/add-student/` | GET | Student registration form | - |
| `/home/` | GET | Blood group statistics | - |
| `/blood/<str:pk>/` | GET | Donors by blood group | `pk`=blood group |
| `/specific-student-details/<int:pk>/` | GET/PUT | Donor details/update | `pk`=student ID |
| `/year-out-students/` | GET | List graduated donors | - |
| `/specific-year-out-student/<int:pk>/` | GET/DELETE | Grad donor details/remove | `pk`=student ID |

## 🛠️ Admin Operations

### Managing Active Donors
1. View all donors by blood group: `/blood/A+/`
2. Update donor details: PUT to `/specific-student-details/123/`
   ```json
   {
     "phone_number": "9876543210",
     "last_donation_date": "2023-06-15"
   }
   ```

### Managing Graduated Donors
1. List all graduated donors: `/year-out-students/`
2. Remove graduated donor: DELETE to `/specific-year-out-student/123/`

## 📦 Data Structure

### Key Models
- **Donor**: Stores student donor information
  - Blood group (A+, B+, O+, etc.)
  - Contact details
  - Last donation date
  - Availability status

- **GraduatedDonor**: Archived records of graduated students

## 🔒 Security Features

- JWT token authentication (15min access, 1day refresh)
- Password reset via OTP to registered email
- CSRF protection for web forms
- Rate limiting on authentication endpoints
- Secure password hashing

## 📱 Mobile App Integration

Admins should configure the mobile app with these base URLs:
- Authentication: `https://yourdomain.com/api/token/`
- API Root: `https://yourdomain.com/api/`

## 🚨 Emergency Contact

For system issues, contact:  
[Blood Bank Admin](mailto:sample@gmail.com)  
COET Helpdesk: +91-XXXXXXXXXX

---

**Note**: This system uses Django's default SQLite database in development. For production, configure PostgreSQL in `settings.py`.
```
