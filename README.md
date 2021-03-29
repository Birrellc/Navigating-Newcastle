# Navigating Newcastle 

---

## Description

_this is a fictitious website created for my milestone project 3 with the code institute_.

An online website on "Geordie" dialect which is a rather well known accent widely recognised for being very distinct with many jargon/slang terms used instead of "proper" english. This website will allow users to view "Geordie Slang" and also add their own also with definitions of what each term means incase people ever visit Newcastle.

---

## Table of Contents

- [UX](#ux)
  - [Wireframes](#wireframes)
  - [Database](#database)
  - [User Stories](#user-stories)
    - [User](#user)
    - [Owner](#owner)
    - [Project Goals](#Goals-Derived-From-User-Stories)
---

## UX

### Wireframes

The initial wireframes for this project [Wireframes](https://github.com/Birrellc/Navigating-Newcastle/tree/master/static/wireframes)

---

### Database

- Terms Collection

| Key         | Value              | 
| ------------| -------------------|
| _id         | ObjectId           |
| word        | String             |
| definition  | String             |
| example     | String             |
| by          | String             |

- User Collection

| Key         | Value              | 
| ------------| -------------------|
| _id         | ObjectId           |
| name        | string             |
| username    | string             |
| password    | string             |

The database used for this project is MongoDB via atlas cloud

---

### User Stories

#### User:

- As a user i would like to be able to navigate through the website quickly and clearly.
- As a user i would like to be able to see "Geordie Slang" terms & phrases.
- As a user i would like to be able to contact the owner of the website with any issues or suggestions.
- As a user i would like to be able to register and login seemlessly.
- As a user i would like to be able to create, edit/update and delete my own "Geordie Slang" terms and phrases.


#### Owner:

- As the owner of this website i would like to have my website useable on all platforms from mobile phones to desktop.
- As the owner of this website i would like users to be able to navigate through my website easily.
- As the owner of this website i would like to provide users with the ability to sign up and login with little effort.
- As the owner of this website i would like to users to be able to access all pages apart from the profile page without signing up.
- As the owner of this website i would like users to be able to add their own "Geordie Words" to the website and also edit and delete them.
- As the owner of this website i would like it to be made possible for the users to contact me via email.

#### Goals Derived From User Stories:

- The Goal of this website/project is to create a brief resource on the "Geordie Dialect" of Newcastle.
- The website will be aimed at people interested in the history or dialect of Newcastle and also people interested in visiting.
- This website will also provide a community spirit theme by allowing vistors or residents or former residents to add their own "Geordie Words" to the dictionary.

---

### Landing Page

The landing page actually was originally designed to contain a main image as the background with a clip path slicing the page but as i got into the development of the project i felt for this specific website and its functions it would be best kept minimal so that the soul focus of the website could be viewed and reached with ease and no distraction. The landing page consists of a simple navbar(sidenav for mobile) and a card used as a jumbotron which contains the heading an image of newcastle and two buttons allowing the user to sign up or login to the website to access the dictionary. At the bottom of the page will be a footer used to display socials for proofing but also provide a contact email for the users to submit any issues( I originally aimed for a contact page but felt that for this project a simple button displayed on the footer of each page allowing for email would be more suited)

---

### Geordie Dictionary

Inside the main section will be collapsible fields displaying 'Geordie Dialect' words and phrases which can then be opened up when clicked to show definition, an example and who added the word or phrase to the page. Also at the top of the dictionary page is a search bar for the users to search for words specificially incase the list gets too big for users to identify specific works with ease.

---

### Profile

The profile page will consist of a heading that lists the users username at the top and also a button to add their own word to the dictionary, below this will be a dictionary of all the words the user themselves have added to the website which will be accompanied by 2 buttons, 1 for updating words incase of typo's and also a button to delete the word completely from the database/website.

---

### Login/Signup 

The login page & sign up pages are very similar so will be listed as one, these pages consist of forms created with WTforms which allow the users to login or signup to the website on completion of the form

### Strategy Plane

The purpose of the website created is to be a modern focus on the well known 'Geordie Dialect' and also encouraging community by allowing users to submit content to the website.

- Design a simple to use "dictionary" where users can create, read, update and delete words.
- Design an easy to use website focusing on Newcastle and the Geordie Dialect.
- Design mobile responsive website.
- Provide a login system so users can create accounts and share data to the 'Geordie Dictionary'.

---

### Scope

- The website will provide a clean UX / UI for users to use effectively.
- The website will have full login functionality for users to create accounts
- The website will provide users the ability to interect with the Dictionary page and contribute to it when logged into their accounts
- The website will be an easy to use website focused on simplicity rather than more complicated design.
- All forms that require the input of user data must be validated for efficiency and professionalism.
- Allow Admin to Create, Read, Update and Delete user submitted content (CRUD).
- Allow user to Create, Read, Update and Delete their own content (CRUD).

---

### Structure

- The website is designed with ease of navigation in mind for each section allowing quick transition throughout the website and to avoid any distractions from the users originial purpose on the website.
- The website will also share the same design plan across all pages to keep things neat and easy for the user to use.
- Users without accounts or not logged in will only be able to see home, login and signup pages
- Users that are logged in will also 


---

### Skeleton

- Minimal Theme Navigation.  
- Pages - There will be a Home, Geordie Dictionary page, Login/Signup page and a Profile page and all pages will follow the same principles of design.
- Users - Users will have access to their own profile pages also.

---

### Surface

#### Color Scheme

- My color scheme came from the random color pannels generator on [coolors](https://coolors.co/)

![picture](static/images/nn-colours.png.png)

#### Font

- The font used for this project is "[Comic Neue](https://fonts.google.com/specimen/Comic+Neue?preview.text_type=custom)" which i chose as i wanted a more casual font for this project instead of professional.

#### Images

- I chose only to use one image "[This image](https://github.com/Birrellc/Navigating-Newcastle/tree/master/static/images/nn-home.jpg)" for this project as it was based on a city so i felt i need to represent that city with atleast one image but i did not want to go overboard and distract from the main focus of the website which is the "Dictionary"
