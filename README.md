
# RealPage QE Test  
  
This project contains the automation framework developed as part of the QE tests for RealPage. The chosen programming language is **Python**.

---  
## Getting Started  
  
The scenarios proposed in the test were:

 1. User can search with "Google Search"
 2. User can search by using the suggestions

The feature that was under test was actually the Google's Homepage search. Because of this, some few other test cases have been added like "using the I'm Feeling Lucky option" and "searching with a typo". 
  
### Prerequisites  
  
**RECOMMENDED:** Create a Python virtual environment on your machine and make it your project interpreter. This way,  
you can work with different dependencies and their versions independently from other projects on your machine.  
  
If you decided to work on a virtual environment, activate it and install the next dependencies  
*(If you are not working on a virtual environment, do it on your command line)*:  
- selenium
- pytest  
  
### Installing  
  
For most, if not all, of the previous dependencies you can run:  
  
```sh  
$ pip3 install <dependency>  
```  
  Or, from the parent folder run:
  ```sh  
$ pip3 install -r requirements.txt  
```
  
### Structure  
  
The project tree is divided into 2 folders: 
- `/pages` : where the locators and page model is developed.
- `/tests`: where the testing scripts are developed and executed.
  
  
---  
## Running the tests  
  
You'll find the tests on the `/tests/test_homepage_search_pytest.py` file.

By default, the tests will run **without** opening a visible browser. 
If you want to see how the tests progress, comment the line in the test file where the *'headless'* option is added to Chrome.

Once you have completed all the previous steps, you can run the tests by:  
- Activating your *virtualenv*  
- Running the pytest command on the `/tests` folder:  
```sh  
$ python3 -m pytest -v 
```  

#### Running with unittest
There's also other file named `/tests/test_homepage_search.py` where the same test cases are implemented using Python's **unittest** module. If you want to run it, first uncomment the tests and then run:
```sh  
$ python3 -m unittest -v  
```  
---  
  
## Results  
  
The results will be written on the command line. 