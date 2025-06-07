# Django Configuration

1. Virtual Environment yaradırıq 
    # (python -m venv .venv)

2. Virtual Environment aktivləşdiririk.
    # (.venv\Scripts\activate)

3. Django vəya hər hansı kitabxananı yükləyirik.
    # (pip install Django)

4. Onu requirements.txt faylına yazırıq.
    # (pip freeze > requirements.txt)

5. Proyekti yaradırıq və ad qoyuruq.
    # (django-admin startproject config .)

6. Serveri işə salıb, yoxlayırıq.
    # (python manage.py runserver)

7. Server işləməyəcək çünki migrate edilməyən fayllar mövcuddur.
    # (python manage.py migrate)

8. Serveri yenidən işə salıb, yoxlayırıq.
    # (python manage.py runserver)

9. Django administrasiyasına giriş etmək üçün istifadəçi yaradırıq.
    # (python manage.py createsuperuser)

10. Serveri yenidən işə salıb, yoxlayırıq.
    # (python manage.py runserver)

11. Tətbiqlər (app) yaradırıq və hər birinin içərisində "templates" qovluğu yaradırıq.
    # (python manage.py core)
    # (python manage.py account)
    # (python manage.py product)
    # (python manage.py blog)

12. settings.py faylına tətbiqləri əlavə edirik.

13. Proyektin fayllarını app-lara uyğun bölürük.

14. Hər app(tətbiqin) özünə görə urls.py faylını və templates qovluğunu yaradıb settings.py-da əlaqələndiririk.

15. MEDIA_URL və STATIC_URL fayllarının lazımi konfiqurasiyasını setting.py-a əlavə edirik.

16. Hər html faylına {% load static %} əlavə edirik və düzəldirik.

17. base.html faylını index.html-ə əsasən yaradıb digər fayllar üçün ordan inherit alırıq.

<!-- All pages are ready -->