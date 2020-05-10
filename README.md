


> Written with [StackEdit](https://stackedit.io/).



# Tyba QE Test  
  
This project contains the automation framework developed as part of the QE tests for Tyba. The chosen programming language is **Python**.

---  
## Getting Started  
  
The scenarios proposed in the test were separated into 3 sections:

 1. Test cases for the Header of the page (or navigation bar)
 2. Test cases for the Calculator form (both credit calculator and fee calculator)
 3. Test cases for the Properties available section.

For the first one, the test cases were based on the different button available on the navigation bar. Those button have different behaviors like redirecting the user to another page, open a form or opening a submenu.

For the Calculator functionality, more test cases were added because it was considered to be the main feature of the page. Negative test cases were considered too (i.e writing text on a numerical input). 

The latter feature is the more basic one as it is just a table with some sections and links according to the table. Only one test case was added asserting the link names and the section names.

  
### Prerequisites  
  
**RECOMMENDED:** Create a Python virtual environment on your machine and make it your project interpreter. This way,  
you can work with different dependencies and their versions independently from other projects on your machine.  
  
If you decided to work on a virtual environment, activate it and install the next dependencies  
*(If you are not working on a virtual environment, do it on your command line)*:  
- selenium
- pytest  
- allure-pytest

Also, for the report generator a tool called `allure` was used. It must be installed in the OS for its usage (e.g on MacOS the command is `$ brew install allure`)
  
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
  
The project tree is divided into 3 folders: 
- `/pages` : where the locators and page model is developed.
- `/tests`: where the testing scripts are developed and executed.
- `/logs`: where the test data is stored for report generation.
  
  
---  
## Running the tests  
  
You'll find the tests on the `/tests/test_header.py`, `/tests/test_calculator.py` and `/tests/test_properties.py` files.

By default, the tests will run opening a visible browser (no headless). 
If you don't want to see how the tests progress, uncomment the line in the test file where the *'headless'* option is added to Chrome.

Once you have completed all the previous steps, you can run the tests by:  
- Activating your *virtualenv*  
- Running the pytest command on the `/tests` folder:  
```sh  
$ python3 -m pytest -v --alluredir="../logs"    
```  
---  
  
## Results  
  
The report generated by allure is saved on an `*.html` file located in `/logs/reports/`.
If you want to generate a new report run (from the /tests folder):
```sh  
$ allure generate ../logs -o ../logs/reports --clean    
``` 
And then, in order to open the report generated run:
```sh  
$ allure open ../logs/reports                       
``` 
You should see something like this:
![report overview](images/overview.png)

![suites view](images/suites.png)

![graphs view](images/graphs.png)