# 🐾 Adoptify – A Pet Adoption Platform

Adoptify is a pet adoption web application designed to connect animal shelters with potential adopters. The platform aims to streamline the adoption process by providing an easy-to-use, modern interface for viewing, filtering, and adopting pets. It also allows shelters to apply for registration and post pets for adoption.

---

## 🌟 Features

### 👤 User Side:
- Register/login with secure authentication
- Responsive dark-themed user interface
- Browse pets by category, breed, age, size, etc.
- View pet profiles with images and detailed info
- Submit inquiries for specific pets
- Email confirmation upon inquiry
- Mobile-friendly design with modern aesthetics

### 🛠 Admin Features:
- Admin dashboard with pet, inquiry, and shelter management
- Email notifications for new inquiries
- View and manage user and shelter applications

### 🐶 Shelter Side:
- Apply to become a verified shelter
- Shelter registration form with email, contact, and description
- Shelter-admin can list and manage pets

---

## 📦 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Django |
| Database | PostgreSQL (for development) |
| Deployment | Render |
| Version Control | Git & GitHub |
| Email Service | Django’s `send_mail` with SMTP |
| UI Styling | Custom CSS with modern fonts and dark theme |

---

## 💻 Requirements

### Software:
- Python 3.10+
- Django 5.x
- Git
- Any modern browser

### Python Packages:
```bash
pip install -r requirements.txt
```

---

## 🔧 How to Run

```bash
# Clone the repo
git clone https://github.com/your-username/Adoptify.git
cd Adoptify

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

---

## 📌 Folder Structure

```
Adoptify/
├── accounts/
├── pets/
├── inquiries/
├── shelters/
├── templates/
├── static/
├── media/
├── db.sqlite3
└── manage.py
```

---

## 📈 Future Enhancements

- Integrate a UPI-based donation system
- Add reviews/testimonials for shelters
- Implement advanced pet filters (e.g., vaccination status)
- Shelter admin login & dashboards
- Role-based permission system
- Push notifications / SMS alerts

---

## 🔐 Security

- Password hashing using Django’s built-in auth system
- Form validation (email, phone number, strong password)
- CSRF protection for all forms
- Input sanitization

---

## 🧪 Testing

Manual testing & test case validation done for:
- User registration & login
- Pet detail access
- Inquiry submission
- Shelter application

---

## 📜 License

MIT License. Free to use and modify for educational or commercial use.

---

## 📷 Screenshots

![Home](https://github.com/user-attachments/assets/ed1ba2ee-1de5-4c25-8036-88bb2729912e)

![About Us](https://github.com/user-attachments/assets/5f3b56cf-8cff-429f-8d80-12bfd0548d9f)

![Donation ](https://github.com/user-attachments/assets/494e1ed4-02e1-4fcd-8d23-c9cc91dc3b30)

![Pets](https://github.com/user-attachments/assets/eb08c7a4-1658-4bf7-ba17-7994910cdf25)

![Pet Details ](https://github.com/user-attachments/assets/19e3e526-6b20-44b2-9c21-d3744f51b339)

---
