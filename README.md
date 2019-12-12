# aplikacje-www
141313/133214

[Model bazy danych](README.md#model-bazy-danych)

[Jak uruchomić](README.md#jak-uruchomić)

[Jak przetestować aplikacje](README.md#jak-przetestować-aplikacje)

# Model bazy danych
![db_schema](db_schema.png)

# Jak uruchomić
Sklonować repozytorium lokalnie:
```bash
git clone "repo.git"
```
W folderze ./project/app_www/ należy zainstalować i uruchomić środowisko:
```bash
pipenv install
pipenv shell
```
Następnie utworzyć migrację:
```bash
./manage.py makemigrations
./manage.py migrate
```
Tworzymy admina:
```bash
./manage.py createsuperuser
```
I uruchamiamy serwer:
```bash
./manage.py runserver
```

# Jak przetestować aplikacje
ścieżki i ich przeznaczenia:

     - dostep do bazy danych Django (na admina należy się zalogować 
     utworzonym wcześniej kontem superusera)
    path("admin/", admin.site.urls),
    
    path("api/", include("rest_framework.urls")),
    
    - Strona startowa (GET)
    path("", Index.as_view(), name="index"),
    
    - Zwraca liste zarejestrowanych użytkownikow (GET)
    path("users/", Users.as_view(), name="users"),  
    
    - Zwraca liste utworzonych pokojów (GET)
    path("rooms/", Rooms.as_view(), name="rooms"),  
    
    - Zwraca liste dodanych komentarzy(GET)
    path("comments/", Comments.as_view(), name="comments"),
    
    - Dodaj uzytkownika (POST):
    wymagane pola - login, email, password (min. 8 znaków, conajmniej jedna wielka litera)
    path("users/add/", CreateUser.as_view(), name="new_user"),
    
    - Dodaj pokój (POST):
    wymagane pole - name
    path("rooms/add/", CreateRoom.as_view(), name="new_room"),
    
    - dodaj komentarz (POST):
    wymagane pola - conetent, user(login), room(name)
    path("comments/add/", AddComment.as_view(), name="new_comment"),
    
    - Edytuj profil (PATCH): 
    pola - name,  surname, email, login, password
    path("users/edit/", EditProfile.as_view(), name="edit_profile"),
    
    - Edytuj pokój (PATCH):
    pola - name
    path("rooms/edit/", EditRoom.as_view(), name="edit_room"),
    
    - Edytuj użytkownika address użytkownika (zalogowany użytkownik edytuje tutaj swój adres)
    (PATCH)
    path("users/edit/address/", CreateUserAddress.as_view(), name="address"),

    - Zbanuj użytkownika po numerze id (admin only)
    (GET)
    path("ban/user=<int:id>/", BanUser.as_view(), name="ban"),
    
    -Obserwuj innego użytkownika (GET, POST)
    Metodą post należy wysłać login użytkownika, którego chcemy obserwować
    path("users/follow/", FollowUser.as_view(), name="follow"),