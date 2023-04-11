# A Webapp with Flask

Creating an app with a simple implementation of a message bank for a class project. The app has two main features. It allows the user to:
1. Submit a response to a prompt asking them their favorite Arctic Monkey song to the message bank
2. View a sample of the messages currently in the message bank.

---

### Objective

This project was meant to serve as an introductory practice to creating a webapp with Flask, utilizing CSS to customize webpages, and integrating SQL tables for dynamic database management.

---

### Contents

1. **data**:
    1. `messages.db`: The database containing all past messages

2. **static**:
    1. `style.css`: contains styling used across all html files
    2. **images**: a folder containing all images used in the html files

3. **templates**:
    1. `base.html`: a base html file that all other html files extend from
    2. `main.html`: used to render the main page (about Arctic Monkeys)
    3. `submit.html`: used to render the message submission page
    4. `view.html`: used to render the view messages page

4. `app.py`: the main app Flask runs to generate the webapp

---

### Flow of Work

A base template called `base.html` was created along with a python file called `app.py` from which the Flask webapp was run. This contains the base navigation links that are visible from every page.
The first interactive webpage built was rendered using the `submit.html` template, and extends from  `base.html`, containing the `CSS` styling used to customize the submission page.
Two functions were then created to enable database management in `app.py`. These were called `get_message_db()` and `insert_message()` and had the functions of creating a connection to the database, and inserting a user response into the message database respectively. These were then used in a `submit()` to implement the message submission feature.
To create a message viewing functionality, the python function `random_messages()` was created in `app.py`, along with the file `view.html` which was used to generate the styling for the page. The function `view()` was defined putting all components together and rendering the view submissions page.
Finally, a `main.html` was added to generate an about Arctic Monkeys homepage.

---

### Screenshots of webpage

The webpage is not hosted on any servers and was run locally. Here are some screenshots of the completed webpage:

![submit](https://user-images.githubusercontent.com/114946455/231062941-dc391396-48b1-4767-9362-34064bc45434.jpg)
*Submitting a response*

<br>

![submit2](https://user-images.githubusercontent.com/114946455/231062949-e17d05fd-7775-4b71-9d5e-2992b7b3bee9.jpg)
*After submitting the response*

<br>

![view](https://user-images.githubusercontent.com/114946455/231062959-adf9436b-6c66-47bf-b1f0-19ca1f35e8fb.jpg)
*Viewing previous submissions*

