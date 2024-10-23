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
- Password recovery verified by a one-time code during the user session.
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
├── core
│   ├── templatetags
│   │   ├── __init__.py
│   │   └── core_filters.py
│   ├── models.py
│   ├── __init__.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── permissions.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates
│   │   └── core
│   │       ├── newsletter_mail.html
│   │       ├── offcanvas.html
│   │       ├── page-title.html
│   │       ├── index.html
│   │       ├── about.html
│   │       ├── privacy-policy.html
│   │       ├── base.html
│   │       ├── contact.html
│   │       ├── rodo-rules.html
│   │       ├── main-menu.html
│   │       ├── footer.html
│   │       ├── properties-results.html
│   │       ├── top-agents.html
│   │       ├── header.html
│   │       ├── error.html
│   │       ├── faq.html
│   │       └── contact_mail.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── db.sqlite3
├── blog
│   ├── templatetags
│   │   ├── __init__.py
│   │   └── pagination_tag.py
│   ├── models.py
│   ├── __init__.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── permissions.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates
│   │   └── blog
│   │       ├── blog.html
│   │       ├── pagination.html
│   │       ├── blog-results.html
│   │       ├── article-categories.html
│   │       ├── article-details.html
│   │       ├── article-tags.html
│   │       ├── comments-section.html
│   │       └── sidebar.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── properties
│   ├── templatetags
│   │   └── property_filters.py
│   ├── models.py
│   ├── __init__.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── permissions.py
│   │   ├── urls.py
│   │   ├── filters.py
│   │   └── views.py
│   ├── templates
│   │   └── properties
│   │       ├── pagination.html
│   │       ├── properties-category.html
│   │       ├── properties-cities.html
│   │       ├── properties.html
│   │       ├── schedule_mail.html
│   │       ├── property-details.html
│   │       ├── sidebar.html
│   │       └── add-property.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── accounts
│   ├── signals.py
│   ├── models.py
│   ├── __init__.py
│   ├── tokens.py
│   ├── apps.py
│   ├── admin.py
│   ├── api
│   │   ├── serializers.py
│   │   ├── __init__.py
│   │   ├── permissions.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates
│   │   └── accounts
│   │       ├── forget-password.html
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── activation_email.html
│   │       ├── account-details.html
│   │       ├── password_reset_email.html
│   │       └── account-settings.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       ├── user.js
│       ├── animations.js
│       ├── blog.js
│       ├── scripts.js
│       ├── general.js
│       ├── add-property.js
│       └── fslightbox.js
├── manage.py
└── global_estate_hub
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
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
