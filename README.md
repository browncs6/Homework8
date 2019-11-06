# Homework 8
For this homework you will be working in your local environment. The templates for this homework are [here](https://github.com/browncs6/Homework8.git). You will need to duplicate this repo (read: [duplicating](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)). When creating a new repo (to duplicate to) please name it cs0060-_your-cs-login_-hw8, then set it to be [private](https://help.github.com/en/github/administering-a-repository/setting-repository-visibility#making-a-repository-private). Then complete all your work/testing locally and push to your private repo. Then add the following github usernames as [contributors](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository) (so we can access your code). 

* jnrolfe
* samstronghammer
* leonhardfs
* hershgupta404
* caoruiming
* aninah

__We will need to clone your repo and run your code for grading__.

__NOTE__: If you do not have a Github Pro account you cannot add more than 3 collaborators to a private repo. You can get Github Pro for free by signing up for the [education pack](https://education.github.com/pack) using your Brown email address.

If you choose to use your personal computer and do not have Python installed, go [here](https://www.python.org/downloads/) and get Python 3._x_._x_

### Flask
This homework will be using [Flask](https://github.com/pallets/flask). Flask is a popular lightweight web application framework written in Python. To install Flask, use [pip](https://pypi.org/project/pip/) by calling the following command via the command line.

```pip install flask```

We will also be using [WTForms](https://wtforms.readthedocs.io/en/stable/) (yes, that's the name). To use these run:

```pip install WTForms```

For good measure, add the bootstrap package as well.

```pip install flask_bootstrap```

__NOTE__: you may have to use `pip3` instead of `pip`.


## 1. Flask Hello

__NOTE__: for this problem, we will be working in the `problem1` directory.

### 1. Hello World
1. In the `app.py` file create a new route for `'/hello'`
2. Make the route return a bolded __hello world!__ as full HTML5 document. 
_HINT_: this means your html should start with something like `<!DOCTYPE ... >`

### 2. Parameter Parsing & Forms
1. In the `app.py` file create a new route for `'/greet'`
2. Specify the methods this route can take as both `POST` and `GET`
    a. If the request method is `POST`, get both values `user` and `msg`. Store them in some variables to use later.
    b. If the request method is `GET`, get both arguments `user` and `msg`. Store them in some variables to use later.
3. For both request methods, if `user` equals any variation of `tux` (_e.g._ `Tux, tUx`, etc) then set `pic` to `tux.png` else, set `pic` to a randomly chosen `.png` file from `'static/img/'` folder excluding `tux.png`. 
_I.e._ `tux.png` should only be displayed when the user is Tux.
4. Render the `home.html` template passing the `user`, `msg`, `pic` variables.
5. In the `templates/home.html` file under the html form code, use flask templating to accomplish the following
    a. If `user` display a something like `Hi [user]!`, else display `Hello, no user detected`
    b. If `user` and `msg` then display something like `Your message is: [msg]`, else display `No message detected!`
    c. If `pic`, display the appropiate image, else do nothing. 
6. In `templates/layout.html` link the `css/main.css` stylesheet using Flask templating under the `<title>`.
_HINT_: look into the `url_for()` function

### 3. `POST` vs `GET` 
1. In a few sentences, describe the difference between a `POST` and `GET` request. Which one should you use for a form containing sensitive information and why? Write this in a PDF along with your cs login and submit it to Gradescope.

## 2. TODO
Alicia the Australian little penguin is totally swamped. She finds herself going through pages and pages of paper recording her todo lists and crossing things off. To help her out, you're going to make an application that records todo items and allows them to be checked off.

We have provided a template that outlines the application. There are five places that you need to fill in. These instructions leave room to interpretation. They are not meant to be exact. We expect you to fill in the gaps. This problem is _goal oriented_. We care about the finished product and its functionality. We will be checking for these things:
1. Can create new todo items with names and optional notes.
2. Cannot create a todo item without a name.
3. Never errors.
4. Can remove batches of todo items using their corresponding checkboxes.
5. Relatively intuitive to use. If you are concerned about this, add a README that explains how to use your app.
6. Server can be run with `python3 ./app.py` when in the root directory of your project.
7. Website is found at `http://localhost:5000/` while the application is live.
8. Auto-updates display when new todo items are added (don't need to refresh page to see change).

Here is an example of what we are expecting:

![](https://i.imgur.com/BWp9kdw.png)

### templates/main&#46;html
We have removed the line that allows `todo.html` to be a child of `main.html`. Fill in this line. Read about this [here](https://jinja.palletsprojects.com/en/2.10.x/templates/#template-inheritance).

### templates/todo&#46;hmtl
This is the template that we want to render. We have given you a basic outline, but you need to fill in the todo item removal form. It should send a POST request to the "/remove" endpoint.

Use an HTML table to display each element in the `todo_list` with a corresponding checkbox. You may find it helpful to give all of the checkboxes the same name and values corresponding to the index in the `todo_list` like [so](https://stackoverflow.com/questions/12145434/how-to-output-loop-counter-in-python-jinja-template).

### app&#46;py
The structure of the `todo_list` is mostly up to you. We recommend a list of tuples.

1. **AddForm:** This will be the form you use to submit new todo items to the backend. We are leveraging the FlaskForm to make it easer to do form validation and rendering. Each todo consists of two parts: name and notes. For example, if I needed to go to the grocery store today, I could make the name "groceries" and the notes my grocery list.<br/><br/> Use [this](https://wtforms.readthedocs.io/en/stable/fields.html#field-definitions) documentation to help inform your form creation. In the end there should be three fields: 
    * A name field that must not be empty (_hint:_ use validation)
    * A notes field
    * A submit field
1. **main_page():** This will be the main endpoint for your page. First, fill in the @app.route annotation. This function should handle the "/" endpoint and accept GET or POST requests.<br/><br/>In this function you'll need to do several things:
    * Make an instance of AddForm.
    * If the form is validated correctly, add an element to the todo_list and clear the form.
    * Return a rendering of `todo.html`. `todo.html` asks for two arguments: `todo_list` and `form`. Fill these in appropriately.
1. **remove_todo():** This will be the endpoint that serves the "Done" button which removes elements of your todo list. First, fill in the @app.route annotation. This handles the "/remove" endpoint and only accepts POST requests. Then fill in the following:
    * Extract the list of checked boxes from the form.
    * Use the list to remove the appropriate todo items from the `todo_list`. This should work if multiple boxes are selected. (_hint_: try removing the highest index first and moving to the lowest to avoid issues with `del`eting the wrong indices).
    * Redirect to "/" to reload the page.
### Bonus
Haven't had enough? Want the todo application to be even better? There are two ways you can earn bonus points. 

__NOTE:__ If you have not made a good faith effort on the rest of this problem, we will not grade the bonus.
1. CSS practice. We have provided an empty CSS file at `static/css/main.css`. Use this to spice up your application's look. We will award up to 3 bonus points depending on how cool your site looks. You may also modify `templates/main.html` and `templates/todo.html` if you want to modify the structure.
2. Steady state. Soon, you will be learning about databases and how to make your application handle being shut down and restarted without losing data. You may not know how to use databases, but you do know how to work with text files. Figure out a way to store your todo list information in a file and read from it whenever the application starts up so the list is never lost. [This](https://www.w3schools.com/python/python_file_write.asp) and [this](https://www.makeuseof.com/tag/json-python-parsing-simple-guide/) might help you get started. This is also worth up to 3 bonus points.

## Deliverables
To successfully turn this assignment in, you need to complete the following.
1. Create a new private repo, push all your code.
2. Add the TAs as contributors to your repo.
3. Upload to Gradescope a document to with your answer to question 1.3.1 (be sure to include your cs-login at the top of this document).
