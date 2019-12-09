# aplikacje-www
141313/133214

# Model bazy danych
![db_schema](db_schema.png)

# Jak uruchomić
Sklonować repozytorium lokalnie:
```bash
git clone "repo.git"
```
W project/app_www/ należy zainstalować środowisko:
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
ścieżki:

    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path("", Index.as_view(), name="index"),
    path("users/", Users.as_view(), name="users"),
    path("rooms/", Rooms.as_view(), name="rooms"),
    path("comments/", Comments.as_view(), name="comments"),
    path("users/add/", CreateUser.as_view(), name="new_user"),
    path("rooms/add/", CreateRoom.as_view(), name="new_room"),
    path("comments/add/", AddComment.as_view(), name="new_comment"),
    path("users/edit/", EditProfile.as_view(), name="edit_profile"),
    path("rooms/edit/", EditRoom.as_view(), name="edit_room"),
    path("users/<int:id>/address/", CreateUserAddress.as_view(), name="address"),

path("admin/", admin.site.urls), - dostep do bazy danych Django

path("", Index.as_view(), name="index"),  - Strona startowa

path("users/", Users.as_view(), name="users"),  - Zwraca liste zarejestrowanych użytkownikow

path("rooms/", Rooms.as_view(), name="rooms"),  - Zwraca liste utworzonych pokojów
    
path("comments/", Comments.as_view(), name="comments"),   - Zwraca liste dodanych komentarzy



