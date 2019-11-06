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

## Deliverables
To successfully turn this assignment in, you need to complete the following.
1. Create a new private repo, push all your code.
2. Add the TAs as contributors to your repo.
3. Upload to Gradescope a document to with your answer to question 1.3.1 (be sure to include your cs-login at the top of this document).
