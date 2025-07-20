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

18. Database dəyişmək üçün sqlite silirik.

19. docker-compose.yml yaradırıq.

20. dockerhub-dan postgres faylını əlavə edib, bəzi təhlükəsizlik parametrlərini daxil edirik.

21. Postgresin portunu və volume-ni əlavə edirik. 
(ports:
      -5432:5432 )
(volumes:
      - ../pgdb:/var/lib/postgresql/data)

22. settings.py konfiqurasiya edirik.
(DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecom',
        'USER': 'project',
        'PASSWORD': '12345',
        'PORT': 5432,
        'HOST': 'localhost'
    }
})

23. python manage.py runserver edirik. Xəta gəlir və pip install psycop2-binary edirik. migrate edirik. Yenə python manage.py runserver edirik və cədvəllər görünürsə deməli veb qoşulub.

24. Bundan sonra proyekti hər açanda environmentlə yanaşı dockeridə işə salacıq.

25. Istifadəçi yaradırıq 
    python manage.py createsuperuser

26. adminer, proyektin admin səhifəsində baxabilərik (user-a)

27. Modellərə keçid edirik.

28. Modeli account app-ində quranda User cədvəli yaratdıq və təbii olaraq admin paneldədə user cədvəli olduğundan settings.py hansı cədvəli əsas götürəcəyimizi yazmalıyıq. 
(AUTH_USER_MODEL = 'account.user')

29. Migration ilə bağlı problemlə üzləşirik. Biz migrate, user modelini yaratdıqdan sonra etməliydik deyə dockeri down edirik. pgdb silirik. daha sonra migration fayllarini silirik. docker yenidən işə salırıq. pgdb yenidən yaranır. daha sonra makemigrations edirik. sonra migrate edirik.

29. * Migration xətası ilə üzləşməyək deyə birinci modeli yaradıb makemigrate edirik daha sonra isə migrate.

30. Məsələn bunu accountda models.py içərisinə yazırıq.

(
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField('photo', null=True, blank=True)
    phone = models.CharField('phone', max_length=100, null=True, blank=True)
    bio = models.TextField('bio', null=True, blank=True)
)

  * admin.py-da isə bunu yazmaqla database-də account app-i yaradırıq və içində User cədvəli yaradılır.
    (
    from account.models import User

    # Register your models here.

    admin.site.register(User)
    )
 daha sonra python manage.py makemigrations 
            python manage.py migrate 
            edib database yollayırıq həmin field-i.
31. User, Contact, Subsriber cədvəlləri qurulur.

32. productda ProductCategory cədvəlini yaradırıq. admin paneldə categoriyalarımızı yaradırıq.

33. Product cədvəlinidə yaradırıq. Many-to-One əlaqəsini qururuq.

34. ProductCategory cədvəlini özü ilə əlaqələndiririk.

35. backup qurmaq lazım olur txt formatında və ona uyğun qovluq (backup) yaradıb ilk sətiri ora atırıq.

36. ProductImage cədvəlini qururuq. makemigrations və migrate edirik databaseyə yollayırıq.

37. Databasedən shop-a fronta məlumat ötürürük.

38. ProductReview cədvəli qururuq.

39. Blog cədvəli qururuq.

40. Sonuncu dəfə shop url düzəltdik id ilə müraciət və product details cədvəlini həll elədik.

41. Django interface üçün admin.py advance formaya gətiririk.

42. ContactForm,RegisterForm və LoginForm hazır edirik.

<<<<<<< HEAD
43. Django Email Confirmation hazir edilir.
 
43. Django Email Confirmation hazir edirik.

44. Pagination və Category/Product filterasiyası düzəldirik.

45. Blog və BlogCreate, Slugify düzəldirik