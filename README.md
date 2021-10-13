# MVDbase - movies database app
<hr>

## Table of content

1. [Description](#description)
2. [Technologies](#technologies)
3. [Features](#features)

<hr>

### Description

This web application is a database with movies and actors, in which you can find all the most important information about them. It was created using Django framework and Bootstrap.

[Visit MVDbase](https://mvdbase.herokuapp.com/)


### Technologies

This web app has been created using:

- Python 3.9.7
- Django 3.2.3
- Bootstrap

All requirements to run this project can be found in file *requirements.txt*

### Features

This projects contains many features such as:

- Create account

    > To fully use the website, you need to create an account - when creating a user, the program checks whether there is already a user with such login in the database and whether the password is sufficiently strong. If the password later drops out of your head, you can reset it.

- Add and edit movie/actor

    > After creating the account, you can add content to the database. Thanks to YouTube API and the AJAX function, instead of pasting the trailer address, it is possible to search for YT videos directly on the website. Search results are updated one second after you stop typing data into the form. Movies / Actors can then only be edited or removed by the user who added them or the site administrator.

- User Dashboard

    > In the user panel, you can see all the movies and actors you have added and also change your account password or delete it.

- Add reviews and comments

    > In the rating section, you can add comments and give a rating on a scale of 1-5. The average rating for a given movie/actor is displayed on the page with the details.
