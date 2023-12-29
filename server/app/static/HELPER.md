# Для вёрстки

#### Добавление/подгрузка изображений в шаблон
```
<img src="{{ url_for('static', filename='assets/example.jpg') }}" alt="Example Image">
```

#### Добавление/подгрузка Bootstrap в шаблон
В head добавить тег link отсюда - https://getbootstrap.com/ (CDN)
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
```

#### Добавление и использование кастомных компонентов
Все компоненты находятся в папке templates/components. Компонент представляет из себя файл формата .html.
Чтобы добавить компонент внутрь шаблона нужно использовать include. Пример:
```
{% include 'components/button' with button_text ='Test text' %}
```
