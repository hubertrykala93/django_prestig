<p align="center">
  <img src="https://github.com/user-attachments/assets/25ae9709-b036-4e90-b8a0-677166b8305d" width="15%">
</p>
<img src="https://github.com/user-attachments/assets/4d67b3f0-fd64-4c74-b099-3aa49f1e0fe9">

<br/>

## Prestig

Prestig is a modern e-commerce platform designed for selling exclusive clothing for women, children, and youth. The project is built on a responsive and scalable interface, ensuring a smooth and intuitive user experience across various devices. The backend has been optimized for performance and security. The code structure is modular, allowing for easy implementation of new features and scalable growth of the project in the future.

<br/>

## Preview

https://github.com/user-attachments/assets/97d30e92-7c6b-4f81-b2d3-d36c4c00ebc2

<br/>

## Features

**1. Accounts**

- Registration verified by an activation link.
- Password recovery system.
- User account management regarding user data, password changes, profile information, shipping information, as well as product management.

**2. Blog**

- Ability to search for articles by categories, tags, and keywords.
- Comment system implemented.

**3. Shop**

- Ability to add a new product for sale.
- Product sorting options.
- Filtering products based on selected criteria.
- Review system for product listings.

<br/>

## Implemented Languages and Frameworks
<div>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" alt="HTML" title="HTML"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" alt="CSS" title="CSS"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" alt="JavaScript" title="JavaScript"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>
	<code><img width="50" src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" alt="Django" title="Django"/></code>
  <code><img width="50" src="https://user-images.githubusercontent.com/25181517/192107858-fe19f043-c502-4009-8c47-476fc89718ad.png" alt="REST" title="REST"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/192108372-f71d70ac-7ae6-4c0d-8395-51d8870c2ef0.png" alt="Git" title="Git"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/189715289-df3ee512-6eca-463f-a0f4-c10d94a06b2f.png" alt="Figma" title="Figma"/></code>
</div>

<br/>

## File Structure

```
django_prestig
├── prestig
│   ├── settings
│   │   ├── __init__.py
│   │   ├── development.py
│   │   ├── __pycache__
│   │   ├── base.py
│   │   └── production.py
│   ├── asgi.py
│   ├── __init__.py
│   ├── urls.py
│   └── wsgi.py
├── core
│   ├── templatetags
│   │   ├── string_filters.py
│   │   └── __init__.py
│   ├── models.py
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── context_processors.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates
│   │   └── core
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── shop
│   ├── templatetags
│   │   ├── ratings_tags.py
│   │   ├── subcategory_filter.py
│   │   ├── __init__.py
│   │   └── ratings_converter.py
│   ├── models.py
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── context_processors.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates
│   │   └── shop
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog
│   ├── templatetags
│   │   ├── article_filters.py
│   │   ├── date_filters.py
│   │   ├── decode_filters.py
│   │   ├── __init__.py
│   │   └── pagination_filters.py
│   ├── models.py
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── context_processors.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates
│   │   └── blog
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── .gitignore
├── accounts
│   ├── models.py
│   ├── __init__.py
│   ├── apps.py
│   ├── forms.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── tokens.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates
│   │   └── accounts
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .env
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       ├── user.js
│       ├── global.js
│       ├── blog.js
│       ├── scripts.js
│       └── shop.js
└── manage.py
```

<br/>

## Installation

Install Python 3.10 and clone the GitHub repository.

```bash
$ git clone https://github.com/hubertrykala93/django_prestig.git
$ cd django_prestig
```

Create a virtual environment to install dependencies in and activate it:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install the dependencies:

```bash
(venv)$ pip3 install -r requirements.txt
```

Run the project.

```bash
(venv)$ python3 manage.py runserver
```

And then navigate to ```http://127.0.0.1:8000``` or ```http://localhost:8000```.

<br/>

## Authors

- [Hubert Rykała - Backend Developer](https://github.com/hubertrykala93)
- [Szymon Lewandowski - Frontend Developer](https://github.com/Szymon-Levy)

<br/>

## Screenshots and Videos
