# FastAPI & SQLite Student Management System 🚀

مشروع بسيط واحترافي يبين كيفية بناء **RESTful API** باستخدام اطار العمل **FastAPI** وربطه بقاعدة بيانات **SQLite** لإدارة بيانات الطلاب ودعم جميع عمليات الـ **CRUD** (Create, Read, Update, Delete) بشكل دائم.

A simple and practical RESTful API project built with **FastAPI** and integrated with a persistent **SQLite** database to perform full **CRUD** operations on student records.

---

## 📌 الميزات الرئيسية (Key Features)

* **إدارة كاملة للبيانات (CRUD Operations):**
  * **Create:** إضافة طالب جديد بقاعدة البيانات.
  * **Read:** عرض كافة الطلاب المسجلين.
  * **Update:** تعديل بيانات طالب معين بواسطة الـ ID.
  * **Delete:** حذف طالب معين بناءً على الـ ID.
* **حفظ دائم للبيانات (Persistent Storage):** ربط التطبيق بقاعدة بيانات SQLite لضمان عدم ضياع البيانات عند إعادة تشغيل السيرفر.
* **التحقق من صحة البيانات (Data Validation):** استخدام مكتبة `Pydantic` للتحقق من أنواع البيانات المدخلة.
* **توثيق تفاعلي تلقائي (Auto Interactive Docs):** دعم لصفحة Swagger UI لاختبار الـ API مباشرة.

---

## 🛠️ التقنيات المستخدمة (Technologies Used)

* **Python 3.x**
* **FastAPI** (Web Framework)
* **Uvicorn** (ASGI Server)
* **Pydantic** (Data Validation)
* **SQLite3** (Database Engine)

---

## 🚀 طريقة التشغيل والتهيئة (How to Run)

### 1️⃣ استنساخ المشروع (Clone the Repository)
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name