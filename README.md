# Intro to Python recap exercise

**Important**: this project is for educational purpose only. Any missuse or comercial use is forbiden.
**NOTE:** The docs assume that you use Pycharm as your editor/IDE of choice. 

What we will build:


We will use some battletested 3rd party libraries: 

* [requests](https://pypi.org/project/requests/) 
  Making HTTP requests from our code
* [click](https://pypi.org/project/click/7.1.2/)
  For parsing (getting) comands and arguments from the command line
* [rich](https://pypi.org/project/rich/) 
  Formating the output to stdout (command line or shell)
* [black](https://pypi.org/project/rich/)
  Auto-code formater for Python
* [pytests](https://pypi.org/project/pytest/)
  Writing and runing tests
  
## Project setup

The url of the project is https://github.com/dasdachs/wd-1-scraping-exercise.git

### Via Pycharm
(from the official [docs](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#))

* From the main menu, choose **VCS | Get from Version Control.**
* In the Get from Version Control dialog, choose **GitHub** on the left.
* Specify the **URL** of the repository that you want to clone. You can select a repository from the list of all GitHub projects associated with your account and the organization that your account belongs to
* In the Directory field, **enter the path to the folder** where your local Git repository will be created.
* **Click Clone.** If you want to create a project based on these sources, click Yes in the confirmation dialog. PyCharm will automatically set Git root mapping to the project root directory. 

### Via command line

```bash
git clone https://github.com/dasdachs/wd-1-scraping-exercise.git
cd wd-1-scraping-exercise
python -m venv venv
pip install -r requirements.txt
# OS specific command
venv\Scripts\activate.bat # Windows
venv/source/activate      # MacOS or Linux
```

## Exercise

## Formating

*Black* is used to ensure code style consistency. 

You can run *black* from the command line

```bash
black -v .
```

Or integrate it with *Pycharm* using this [steps](https://black.readthedocs.io/en/stable/editor_integration.html#pycharm-intellij-idea).

## Tests

When you are done with a task run the test suite.

```bash
pytest -v
```

Or use *Pycharm*

## Misc

Contact the author for bugs etc.
