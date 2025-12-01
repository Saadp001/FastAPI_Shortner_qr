# 🚀 URL Shortener + QR Generator (FastAPI + PostgreSQL)

A production-ready **URL Shortener Web App** built using **FastAPI**, **Neon PostgreSQL**, and **QR code generation**, deployed on **Render + Vercel**.

Users can shorten long URLs, generate QR codes, download them, and access redirects instantly — just like Bitly.

---

## 🔗 **Live Project Links**

| Component               | URL                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 🌐 Frontend (Vercel)    | **[https://short-urlxqr.vercel.app](https://short-urlxqr.vercel.app)**                                               |
| ⚙️ Backend API (Render) | **[https://fastapi-shortner-qr.onrender.com](https://fastapi-shortner-qr.onrender.com)**                             |
| 🖥 Frontend Repo        | [https://github.com/Saadp001/FastAPI_Shortner_qr_frontend](https://github.com/Saadp001/FastAPI_Shortner_qr_frontend) |
| 🔧 Backend Repo         | [https://github.com/Saadp001/FastAPI_Shortner_qr](https://github.com/Saadp001/FastAPI_Shortner_qr)                   |

---

# ⭐ Features

* 🔗 Shorten any long URL
* 🧠 Deterministic short code generation (same input → same short URL)
* 🆔 Fast redirect using short code
* 🧾 QR code generation for each short URL
* 📥 Download QR image
* 🗃 Stored securely in **Neon PostgreSQL**
* 🎨 Clean, modern UI (on Vercel)
* 🌍 Fully deployed backend (Render)

---

# 🏗 **Tech Stack**

### **Backend**

* FastAPI
* SQLAlchemy ORM
* Neon PostgreSQL
* Uvicorn
* qrcode / Pillow
* Render (deployment)

### **Frontend**

* HTML + CSS + JS
* Vercel (deployment)

---

# 📐 **Architecture Overview**

```
Frontend (Vercel)
    ↓ POST /shorten
Backend API (Render, FastAPI)
    ├── Generate short code
    ├── Generate QR
    ├── Store in Neon PostgreSQL
    └── Return short URL + QR path
    ↓
Frontend displays QR + short link
    ↓
Scan QR → redirect to /<short_code>
    ↓
FastAPI → looks up DB → RedirectResponse(long_url)
```

---

# 📂 Folder Structure

```
src/
│── main.py            # App entry point, CORS, router mounting
│── database.py        # PostgreSQL connection + session
│── models.py          # SQLAlchemy URL model
│── schemas.py         # Pydantic schemas
│── utils.py           # Short code + QR generator logic
│── routers/
│     ├── shortener.py  # POST /shorten
│     └── redirect.py   # GET /{short_url}
qr_codes/               # Generated QR images
```

---

# 🔌 API Endpoints

### **1️⃣ Shorten URL**

`POST /shorten/`

Request:

```json
{
  "long_url": "https://youtube.com/somevideo"
}
```

Response:

```json
{
  "id": 1,
  "long_url": "https://youtube.com/somevideo",
  "short_url": "you146",
  "qr_code": "qr_codes/you146.png"
}
```

---

### **2️⃣ Redirect to original URL**

`GET /{short_url}`

Example:

```
/you146
```

Redirects → `https://youtube.com/...`

---

### **3️⃣ Download QR**

`GET /qr/{filename}`

Example:

```
/qr/you146.png
```

---

# 🛠 Installation & Local Setup

### 1️⃣ Clone the repo

```
git clone https://github.com/Saadp001/FastAPI_Shortner_qr
cd FastAPI_Shortner_qr
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv/Scripts/activate     # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Add `.env` file

```
DATABASE_URL=your_postgresql_url_here
```

(Use Neon for PostgreSQL.)

### 5️⃣ Run the server

```
uvicorn src.main:app --reload
```

---

# 🌐 Deployment

### **Backend → Render**

* Render pulls GitHub repo automatically
* Environment variable:

  ```
  DATABASE_URL = <Neon PostgreSQL link>
  ```
* Auto deploys on new commits

### **Database → Neon PostgreSQL**

* Cloud-hosted
* Persistent
* Very fast & free tier

### **Frontend → Vercel**

* Deployed separately using frontend repo
* Calls Render API directly

---

# 👨‍💻 Author

**Saad Patel**
🔗 LinkedIn: [https://www.linkedin.com/in/saad-patel-469016314/](https://www.linkedin.com/in/saad-patel-469016314/)
🌐 GitHub: [https://github.com/Saadp001](https://github.com/Saadp001)

---

# 🎉 Final Words

This project demonstrates:

* Real backend architecture
* FastAPI production deployment
* Cloud PostgreSQL database
* Static QR generation
* Frontend–backend integration
* Clean UI + working redirects

A perfect project for **portfolio + resume**.

---

