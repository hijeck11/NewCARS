# NewCARS
ДЗ на 06.12.23
1. Создал forms.py
2. Добавил во вьюхи новый класс для добавления новых записей
class AutohausCreateView(generics.CreateAPIView):
3. Добавил urls:
path('cars/create/', AutohausCreateView.as_view(), name='autohaus-create'),
4. Созда: 
autohaus_create.html

ДЗ НА 04.12.23
1. Создал новое приложение rest_app;
2. В настройках добавил новое приложение в "INSTALLED_APPS";
3. В urls проекта добавил urls нового приложения "rest_app";
![img_6.png](img_6.png)
4. Добавил модель в models.py;
![img_4.png](img_4.png)
5. Зарегестрировал модель в админке;
![img_5.png](img_5.png)
6. Создал serializers.py сериализатор модели;
![img_1.png](img_1.png)
7. Сделал представление views.py и маршрут urls.py;
![img_3.png](img_3.png)
8. Создал cars_list.html для отображения всех машин из БД;
![img_2.png](img_2.png)
9. в представления добавил функцию "get_queryset(self):" для поиска через /?q=
![img.png](img.png)