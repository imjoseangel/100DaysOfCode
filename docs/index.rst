Log: 100 Days Of Code
=====================

Day 0: March 10, 2019 (Preparation)
-----------------------------------

**Today's Progress:** Prepare GitHub Repo and Twitter, read documentation.

**Thoughts:** I will start with Python doing Master Python through building real-world applications but I would like to work on a PowerShell Module for Ansible.

**Link to work:**

1. See `imjoseangel GitHub #100HoursOfCode <https://imjoseangel.github.io/100-hours-of-code>`_

Day 1: March 11, 2019
---------------------

**Today's Progress:** Prepare Python Script for Travis and Checking PyLint in all Python Files.

**Thoughts:** Unexpected script for Travis CI to check Lint in all Python Files in the Repo.

**Link to work:**

1. See `pylint_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/pylint_check.py>`_
2. See `wargames Krypton Level0 -> Level1 <http://overthewire.org/wargames/krypton/krypton0.html>`_
3. See `WarGames Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/wargames/>`_

Day 2: March 13, 2019
---------------------

**Today's Progress:** Building an Interactive Dictionary.

**Thoughts:** I have learn that instead of type, isinstance can be used in a conditional, also learning about the `difflib` library to manage words similarities.

**Link to work:**

1. See `dictionary.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/interactive-dictionary/dictionary.py>`_

Day 3: March 14, 2019
---------------------

**Today's Progress:**

1. Create Volcanos in the US Script and play with folium module
2. Improve pylint_check.py script
3. Improve PyLint to have better code
4. Improve Data Read in File Path

**Thoughts:** Good Module to create maps (folium)

**Link to work:**

1. See `map.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/volcanoes-in-the-United-States/map.py>`_
2. See `choropleth.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/volcanoes-in-the-United-States/choropleth.py>`_

Day 4: March 15, 2019
---------------------

**Today's Progress:**

1. Create documentation with Sphinx and readthedocs.io

**Thoughts:** Important for Company Projects and Documentation as Code

**Link to work:**

1. See `100 Days of Code Documentation - Imjoseangel <https://100-days-of-code-imjoseangel.readthedocs.io>`_
2. See `GitHub Documentation <https://github.com/imjoseangel/100-days-of-code/blob/devel/docs/>`_

Day 5: March 16, 2019
---------------------

**Today's Progress:**

1. Adding Pre-Commit to Project and Changing PyLint for Rating
2. Creating Site Blocker for Working Hours

.. note:: Need to create more stable pre-commit based in score and not rc as in CI.

**Thoughts:** Good way of doing CI with python by score.

Check the following code to find matches in lines iterating a list:

    >>> for line in CONTENT:
    ...     if not any(website in line for website in WEBSITE_LIST):

**Link to work:**

1. See `pylint_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/pylint_check.py>`_
2. See `pre-commit-config <https://github.com/imjoseangel/100-days-of-code/blob/devel/.pre-commit-config.yaml>`_
3. See `webblocker.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/website-blocker/webblocker.py>`_

Day 6: March 17, 2019
---------------------

**Today's Progress:**

1. Studying about `decorators <http://book.pythontips.com/en/latest/decorators.html>`_
2. Continuing Improving pylint_check.py utility

**Thoughts:** Now clearer how using them, but still need to use them more frequently (Logging and Flask)

**Link to work:**

1. See `decorators <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/decorators>`_
2. See `pylint_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/pylint_check.py>`_

Day 7: March 20, 2019
---------------------

**Today's Progress:**

1. Using Flake8 also for Pre-Commit and Fixing Other Lint Issues
2. Adding Code Complexity to Travis (Just Reporting)

**Thoughts:** Still need to work with py.test and unittest to understand better different scenarios. Adding radon for Code Complexity

**Link to work:**

1. See `radon_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/radon_check.py>`_

Day 8: March 21, 2019
---------------------

**Today's Progress:**

1. Flask Tutorial Completed

**Thoughts:** Need to work more with Flask to understand better its complexity

**Link to work:**

1. See `Flask Tutorial <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/flask-tutorial>`_

Day 9: March 22, 2019
---------------------

**Today's Progress:**

1. Working with sockets. Creating Basic Client and Server

**Thoughts:** Basic Socket Connectivity and Fixing Linters and some bugs in the Linting Script. Learning about how to skip a specific pylint in a specific file.

**Link to work:**

1. See `Basic Socket Client and Server <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/socket_programming>`_

Day 10: March 23, 2019
---------------------

**Today's Progress:**

1. Working with sockets. Creating Advanced Client and Server

**Thoughts:** Need to study more about sockets and focus on how to apply on infra and network debugging tools

**Link to work:**

1. See `Advanced Socket Client and Server <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/socket_programming>`_

Day 11: March 24, 2019
---------------------

**Today's Progress:**

1. Playing with fbprophet, Forecast from Facebook

**Thoughts:** Nice one to understand how to play with dates and Pandas and doing some data forecasting with Python

**Link to work:**

1. See `Python Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/forecasting>`_
2. See `URL with some tips and data <https://mode.com/example-gallery/forecasting_prophet_python_cookbook/>`_

Day 12: March 25, 2019
---------------------

**Today's Progress:**

1. Docker Creation for Data Science
2. Matplotlib Tutorial

**Thoughts:** Good Docker to Play with DataScience and Jupyter without breaking my environment

**Link to work:**

1. See `Matplotlib Tutorial <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/plotting>`_
2. See `Docker DataScience <https://github.com/imjoseangel/docker-data-science>`_

Day 13: March 28, 2019
---------------------

**Today's Progress:**

1. Created Speech Recognition Script with Command Execution

**Thoughts:** Google Speech Recognition works fine. Probably quite slow if you are impatient ;)

**Link to work:**

1. See `Speech Recognition <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/speech>`_

Day 14: March 31, 2019
---------------------

**Today's Progress:**

1. Created Men Restroom Algorithm

**Thoughts:** Idea from `Reddit <https://www.reddit.com/r/learnpython/comments/b7kq94/men_restroom_algorithm/>`_

**Link to work:**

1. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_

Day 15: April 1, 2019
---------------------

**Today's Progress:**

1. Adding Threading and Average to Men Restroom Algorithm

**Thoughts:** Investigating Threading although not easy to stop process when list is full. Needs further investigation

**Link to work:**

1. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_

Day 16: April 2, 2019
---------------------

**Today's Progress:**

1. Fixing Wifi and Code for Python 3 for DisplayOtronHat from Pimoroni

**Thoughts:** Wifi Display didn't work in Python3 due to the map/list difference

**Link to work:**

1. See `Pull Request on Pimoroni <https://github.com/pimoroni/displayotron/pull/59/files>`_

Day 17: April 3, 2019
---------------------

**Today's Progress:**

1. Adding Some Wifi and Inky from Pimoroni examples and Thinking about some Men Restroom algorithm changes

**Thoughts:** Not easy to split men in stall. Need some thoughts to distribute them.

**Link to work:**

1. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_
2. See `InkyTest <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/pimoroni>`_
3. See `WifiTest <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/wifi>`_

Day 18: April 4, 2019
---------------------

**Today's Progress:**

1. Starting Machine Learning Project Walk-Through in Python

**Thoughts:** Nice one to settle ML knowledge.

**Link to work:**

1. See `Machine Learning Walk-Through <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mlenergyandwater>`_
2. See `Original Project <https://morioh.com/p/b56ae6b04ffc/a-complete-machine-learning-project-walk-through-in-python>`_

Day 19: April 6, 2019
---------------------

**Today's Progress:**

1. Continuing with Machine Learning Project Walk-Through in Python

**Thoughts:** Need to focus in the two variables plot as from there the data is not properly working. I will investigate how to fix it.

**Link to work:**

1. See `Machine Learning Walk-Through <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mlenergyandwater>`_
2. See `Original Project <https://morioh.com/p/b56ae6b04ffc/a-complete-machine-learning-project-walk-through-in-python>`_

Day 20: April 7, 2019
---------------------

**Today's Progress:**

1. Continuing with Machine Learning Project Walk-Through in Python
2. Finishing Men Restroom Algorithm. Now supporting taking alternate further stalls to the door

**Thoughts:** Fully Working Projects Now. Need to finish Voice Recognition with API, Swagger and SQLLite

.. note:: For the ML Project, only finished first part

**Link to work:**

1. See `Machine Learning Walk-Through <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mlenergyandwater>`_
2. See `Original Project <https://morioh.com/p/b56ae6b04ffc/a-complete-machine-learning-project-walk-through-in-python>`_
3. See `Men RestRoom Python <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/menrestroom>`_

Day 21: April 8, 2019
---------------------

**Today's Progress:**

1. How to Generate FiveThirtyEight Graphs in Python
2. Understanding Data Wrangling

**Thoughts:** Find the way to create beautiful plots with Python

**Link to work:**

1. See `Machine Learning Walk-Through <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/fivethirtyeight>`_
2. See `Original Documentation from DataQuest <https://www.dataquest.io/blog/making-538-plots/>`_
3. See `A Comprehensive Introduction to Data Wrangling <https://www.springboard.com/blog/data-wrangling/>`_
4. See `Data Wrangling Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/datawrangling>`_

Day 22: April 9, 2019
---------------------

**Today's Progress:**

1. How to Build a Python GUI Application With wxPython

**Thoughts:** Easy to implement, issues with Mac OSX (Class FIFinderSyncExtensionHost)

**Link to work:**

1. See `GUI With wxPython <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mp3player>`_
2. See `Original Documentation from Real Python <https://realpython.com/python-gui-with-wxpython/>`_

Day 23: April 10, 2019
----------------------

**Today's Progress:**

1. Interactive Data Visualization in Python With Bokeh

**Thoughts:** First Part of the Tutorial from Real Python

**Link to work:**

1. See `Data Visualization Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/interactive-data>`_
2. See `Original Documentation from Real Python <https://realpython.com/python-data-visualization-bokeh/>`_

Day 24: April 11, 2019
----------------------

**Today's Progress:**

1. An Intro to Threading in Python

**Thoughts:** Tutorial from Real Python. Need to check how to launch two threads from outside the function in the MensRoom Algorithm

**Link to work:**

1. See `Threading Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/threads>`_
2. See `Original Documentation from Real Python <https://realpython.com/intro-to-python-threading/>`_

Day 25: April 12, 2019
----------------------

**Today's Progress:**

1. Interactive Data Visualization in Python With Bokeh
2. Adding FileSystem Magic

**Thoughts:** Second Part of Bokeh Tutorial from Real Python. Also added Util Filesystem examples

**Link to work:**

1. See `Bokeh Data Visualization Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/interactive-data>`_
2. See `Original Bokeh Documentation from Real Python <https://realpython.com/python-data-visualization-bokeh/>`_
3. See `FileSystem Magic Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/filesystem-magic>`_
4. See `Original FileSystem Magic Documentation from Will Mcgugan <https://www.willmcgugan.com/blog/tech/post/filesystem-magic-with-python/>`_

Day 26: April 13, 2019
----------------------

**Today's Progress:**

1. Machine Learning CookBook. Understanding Basics

**Thoughts:** Creating Plots to understand the different ML Algorithms and when to use them

**Link to work:**

1. See `Machine Learning Cookbook Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mlcookbook>`_

Day 27: April 14, 2019
----------------------

**Today's Progress:**

1. Machine Learning CookBook. Outliers
2. 200 Python Problems

.. note:: IMHO, for the 200 Python Problems in Udacity there are better solutions than the exposed. I keep mine in the code as I consider easier to implement in some cases and more accurate in others.

**Thoughts:** Learning about Outliers and Continuing Playing with Python Challengues

**Link to work:**

1. See `Machine Learning Cookbook Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mlcookbook>`_
2. See `200 Python Problems Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/200problems>`_
3. See `200 Python Problems Site <https://www.udemy.com/python-handon>`_

Day 28: April 15, 2019
----------------------

**Today's Progress:**

1. Couple of Py, one to understand Binary Search and Decorator for Time Measurement

**Thoughts:** Very useful decorator for future Python Code.

**Link to work:**

1. See `Binary Search <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/200problems/binarysearch.py>`_
2. See `Time Decorator <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/decorators/timescript.py>`_

Day 29: April 17, 2019
----------------------

**Today's Progress:**

1. Playing With Python Types, Part 1

**Thoughts:** Python 3 Types. Annotations and Comments

**Link to work:**

1. See `Code (Cards Deck) <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/cardsdeck/game.py>`_
2. See `Documentation in Real Python <https://realpython.com/python-type-checking/>`_

Day 30: April 18, 2019
----------------------

**Today's Progress:**

1. Playing With Python Types, Part 2

**Thoughts:** Python 3 Types. Annotations and Comments. Cards Deck

**Link to work:**

1. See `Code (Cards Deck) <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/cardsdeck/cards.py>`_
2. See `Documentation in Real Python <https://realpython.com/python-type-checking/>`_

Day 31: April 28, 2019
----------------------

**Today's Progress:**

1. Continuing with 200 Problems and Adding Recursive Example from Grokking Algorithms Book

**Thoughts:** One of the best Algorithm Books and with Python Concepts and Examples

**Link to work:**

1. See `Recursive Examples <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/200problems/recursive.py>`_
2. See `200 Python Problems Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/200problems>`_
3. See `200 Python Problems Site <https://www.udemy.com/python-handon>`_

Day 32: May 1, 2019
----------------------

**Today's Progress:**

1. Supercharge Your Classes With Python super()

**Thoughts:** Too complicated in complex code. Be careful using it

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/super/shapes.py>`_
2. See `Documentation in Real Python <https://realpython.com/python-super/>`_

Day 33: May 2, 2019
----------------------

**Today's Progress:**

1. Creating a GUI Application for NASA’s API with wxPython

**Thoughts:** Learning Code. Although finished, I will take another day studying it

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/nasasapi/>`_
2. See `Documentation Mouse vs Python <https://www.blog.pythonlibrary.org/2019/04/18/creating-a-gui-application-for-nasas-api-with-wxpython/>`_

Day 34: May 5, 2019
----------------------

**Today's Progress:**

1. Working with functions and decorators

**Thoughts:** Continuing with Complex Decorators and Functions

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/decorators/>`_
2. See `Documentation in Real Python <https://realpython.com/primer-on-python-decorators/>`_

Day 35: May 6, 2019
----------------------

**Today's Progress:**

1. Continuing Working with functions and decorators

**Thoughts:** Continuing with Complex Decorators and Python Inner Functions

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/functions/encapsulation.py>`_
2. See `Documentation in Real Python <https://realpython.com/inner-functions-what-are-they-good-for/>`_

Day 36: May 8, 2019
----------------------

**Today's Progress:**

1. Finalizing decorators

**Thoughts:** Continuing with Complex Decorators and Classes Decorators

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/decorators/>`_
2. See `Documentation in Real Python <https://realpython.com/primer-on-python-decorators/>`_

Day 37: May 9, 2019
----------------------

**Today's Progress:**

1. Thinking Recursively

**Thoughts:** Recursive Functions as learned in Grokking Algorithms Book

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/recursive/>`_
2. See `Documentation in Real Python <https://realpython.com/python-thinking-recursively/>`_

Day 38: May 12, 2019
----------------------

**Today's Progress:**

1. Lambda, Args and Kwargs exercises

**Thoughts:** Really easy so far to understand. Now is the time to play with these concepts and understand them quickly

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/argskwargs/>`_
2. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/lambda/>`_

Day 39: May 17, 2019
----------------------

**Today's Progress:**

1. Sammy’s Generators in Python
2. Things you’re probably not using in Python 3 – but should

**Thoughts:** One pending from long time ago, another cool one about Python 3

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/generators/>`_
2. See `Documentation in Medium <https://medium.com/canopy-tax/sammys-generators-in-python-57e43386b89e>`_
3. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/python3should/>`_
4. See `Documentation in Data, what now? <https://datawhatnow.com/things-you-are-probably-not-using-in-python-3-but-should/>`_

Day 40: May 18, 2019
----------------------

**Today's Progress:**

1. Faster Parallel Python with ray

**Thoughts:** Ray is really nice one to give it a try. Easy to install and implement.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/fasterparallel/>`_
2. See `Documentation in Medium <https://towardsdatascience.com/10x-faster-parallel-python-without-python-multiprocessing-e5017c93cce1>`_

Day 41: May 19, 2019
----------------------

**Today's Progress:**

1. Speed Up Your Python Program With Concurrency

**Thoughts:** Threading, AsyncIO and Multiprocessing

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/concurrency/>`_
2. See `Documentation in Real Python <https://realpython.com/python-concurrency/>`_

Day 42: May 25, 2019
----------------------

**Today's Progress:**

1. Web Scraping with Scrapy: Advanced Examples

.. note:: Whole week busy reviewing Python for Games Book.

**Thoughts:** Nice to see but doesn't add inmediate value to my projects. Most of the examples found are incompleted or not properly documented.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/webscrapping/>`_
2. See `Documentation in Kite.com <https://kite.com/blog/python/web-scraping-scrapy>`_

Day 43: June 1, 2019
----------------------

**Today's Progress:**

1. Logging, Setter and Pointers Like in Python
2. Change Travis Version to 3.7

.. note:: Whole week busy reviewing Python for Games Book.

**Thoughts:** Still checking logging. Need to find a better way to setup Travis CI for only commited files

**Link to work:**

1. See `Code for Logging <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/logging/>`_
2. See `Code for Pointers <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/pointers/>`_
3. See `Code for Decorators <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/decorators/>`_
4. See `Logging Documentation in Real Python <https://realpython.com/python-logging-source-code/>`_
5. See `Pointers Documentation in Real Python <https://realpython.com/pointers-in-python//>`_

Day 44: June 2, 2019
----------------------

**Today's Progress:**

1. Functional programming from Julien Danjou Blog
2. Custom Exceptions from Dan Bader
3. Logging Debugging
4. Some Linter Fixing

**Thoughts:** Nice to see but doesn't add inmediate value to my projects. Most of the examples found are incompleted or not properly documented.

**Link to work:**

1. See `Code for Functional Programming <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/functionalprog/>`_
2. See `Code for Custom Exceptions <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/customexceptions/>`_
3. See `Code for Logging <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/logging/>`_
4. See `Documentation in julien.danjou.info for Functional Programming <https://julien.danjou.info/python-and-functional-programming/>`_
5. See `Documentation in dbader.org for Custom Exceptions <https://dbader.org/blog/python-custom-exceptions/>`_
6. See `Logging Documentation in Real Python <https://realpython.com/python-logging-source-code/>`_

Day 45: June 6, 2019
----------------------

**Today's Progress:**

1. Prometheus and ML for Kubernetes Scale

**Thoughts:** Good Linux Academy Training to understand Prometheus API and reinforce ML Concepts for Linear Regression.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/prometheus/>`_
2. See `Course on Linux Academy <https://linuxacademy.com/cp/modules/view/id/304>`_

Day 46: June 8, 2019
----------------------

**Today's Progress:**

1. Script to Update Git Repositories given a path

**Thoughts:** I have used git commands instead git module to use standard libraries

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/gitsync/>`_

Day 47: June 9, 2019
----------------------

**Today's Progress:**

1. Refresh some ML Concepts - Linear Regression

**Thoughts:** Good to remember some concepts and code as this is not in my daily tasks

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mltraining/>`_
2. See `Training on GitHub <https://github.com/machinelearningmindset/machine-learning-course>`_

Day 48: June 10, 2019
----------------------

**Today's Progress:**

1. Python Curses Tutorial. Wrapper and CleanUp added to *centertext.py*

**Thoughts:** Nice tutorial to implement in shell scripts. I will modify yesterday's script for better output

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/cursesprog/>`_
2. See `Document on Dev_Dungeon <https://www.devdungeon.com/content/curses-programming-python>`_

Day 49: June 13, 2019
----------------------

**Today's Progress:**

1. Refresh some ML Concepts - Regularization

**Thoughts:** New Concepts Ridge and Lasso to avoid Overfitting

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mltraining/>`_
2. See `Training on GitHub <https://github.com/machinelearningmindset/machine-learning-course>`_

Day 50: June 14, 2019
----------------------

**Today's Progress:**

1. Learning and Refreshing some ML Concepts - Cross Validation and Decision Trees

**Thoughts:** Cool Maths explaining Decision Trees and Gini Index

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mltraining/>`_
2. See `Training on GitHub <https://github.com/machinelearningmindset/machine-learning-course>`_
3. See `Decision Trees <http://www.cs.cmu.edu/~bhiksha/courses/10-601/decisiontrees/>`_
4. See `A visual introduction to machine learning <http://www.r2d3.us/visual-intro-to-machine-learning-part-1/>`_

Day 51: June 16, 2019
----------------------

**Today's Progress:**

1. Python Concepts Classes, Instances and Static Methods

**Thoughts:** Studying  Different Python Concepts and Tricks

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/baseclasses/>`_
2. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/classvsinstancevars/>`_
3. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/instanceclassstatic/>`_

Day 52: June 17, 2019
----------------------

**Today's Progress:**

1. Creating Twitter Bot

**Thoughts:** Create Toy to play with Twitter API

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/twitter/>`_
2. See `First part of the Twitter Bot Documentation in Real Python <https://realpython.com/twitter-bot-python-tweepy/>`_

Day 53: June 19, 2019
----------------------

**Today's Progress:**

1. Continue with Twitter Bot

**Thoughts:** Continue with Toy to play with Twitter API

.. note:: Got the Docker properly working as there is a missing line in the Documentation.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/twitter/>`_
2. See `Second part of the Twitter Bot Documentation in Real Python <https://realpython.com/twitter-bot-python-tweepy/>`_

Day 54: June 22, 2019
----------------------

**Today's Progress:**

1. OOP with Python vs Java

**Thoughts:** Few refreshes and some new cool concepts for Python OOP

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/ooppython/>`_
2. See `Documentation in Real Python <https://realpython.com/oop-in-python-vs-java/>`_

Day 55: June 25, 2019
----------------------

**Today's Progress:**

1. ML Concepts - K-Nearest Neighbors and Naive Bayes

**Thoughts:** Good to remember some concepts and code as this is not in my daily tasks

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mltraining/>`_
2. See `Training on GitHub <https://github.com/machinelearningmindset/machine-learning-course>`_

Day 56: June 26, 2019
----------------------

**Today's Progress:**

1. ML Concepts - Logistic Regression

**Thoughts:** Tomorrow I will check more code and more tutorials about this ML Topic

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mltraining/>`_
2. See `Training on GitHub <https://github.com/machinelearningmindset/machine-learning-course>`_
3. See `Medium Article about LR <https://towardsdatascience.com/5-reasons-logistic-regression-should-be-the-first-thing-you-learn-when-become-a-data-scientist-fcaae46605c4>`_

Day 57: June 30, 2019
----------------------

**Today's Progress:**

1. ML Concepts - Logistic Regression and SVM

**Thoughts:** Checking more Tutorials about LR, needs to study even more

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mltraining/>`_
2. See `Training on GitHub <https://github.com/machinelearningmindset/machine-learning-course>`_
3. See `Medium Article about LR <https://blog.goodaudience.com/classifying-flowers-using-logistic-regression-in-sci-kit-learn-38262416e4c6>`_
4. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mllogregression/iris.py>`_

Day 58: July 03, 2019
----------------------

**Today's Progress:**

1. Improve Linter Scripts

**Thoughts:** Check only uploaded code compared with **devel** branch

**Link to work:**

1. See `pylint_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/pylint_check.py>`_
2. See `radon_check.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/radon_check.py>`_

Day 59: July 07, 2019
----------------------

**Today's Progress:**

1. Unify Linter Scripts to lint_checker.py

**Thoughts:** Unify linter scripts to have only one with a configuration file. Keeping old ones as reference

**Link to work:**

1. See `lint_checker.py <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/lint_checker.py>`_

Day 60: July 11, 2019
----------------------

**Today's Progress:**

1. AsyncIO in Python

**Thoughts:** First part of this really nice tutorial. I have to study deeply the rand code.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/concurrency>`_
2. See `Original Documentation from Real Python <https://realpython.com/async-io-python/>`_

Day 61: July 21, 2019
----------------------

**Today's Progress:**

1. AsyncIO in Python. Chained Code.
2. Adding Technical Debt in Python

**Thoughts:** Second part of this really nice tutorial. Spending Three days on technical debt for pre-commit. See also pre-commit config.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/concurrency>`_
2. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/hooks/techdebt.py>`_
3. See `pre-commit config <https://github.com/imjoseangel/100-days-of-code/blob/devel/.pre-commit-config.yaml>`_
4. See `Original Documentation from Real Python <https://realpython.com/async-io-python/>`_

Day 62: July 31, 2019
----------------------

**Today's Progress:**

1. New Ansible Module for Datalake ACLs

**Thoughts:** Working the whole week to get this module.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/ansiblemodules/azure_rm_datalakeacl.py>`_

Day 63: August 16, 2019
-----------------------

**Today's Progress:**

1. New Ansible Module for SP Creation
2. Ansible Datalake ACLs improvement

**Thoughts:** Busy with my new project. These last module is the starting point to improve the SP Creation. Other features need to be added as password generation or expiration date.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/ansiblemodules/azure_rm_datalakeacl.py>`_
2. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/ansiblemodules/azure_rm_appregistration.py>`_

Day 64: August 18, 2019
-----------------------

**Today's Progress:**

1. New Ansible Module for Datalake directory creation

**Thoughts:** Quick one from the Datalake acl creation.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/ansiblemodules/azure_rm_datalakedir.py>`_

Day 65: August 25, 2019
-----------------------

**Today's Progress:**

1. Starting with Go

**Thoughts:** Time to start with Go thinking on cloud developments.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/go/>`_
2. See `Tour <https://tour.golang.org/>`_

Day 66: August 27, 2019
-----------------------

**Today's Progress:**

1. Second Go Lesson. Basics

**Thoughts:** Finishing Variables

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/go/>`_
2. See `Tour <https://tour.golang.org/>`_

Day 67: August 29, 2019
-----------------------

**Today's Progress:**

1. Improving Ansible Module for Datalake ACLs before PRing to Ansible

**Thoughts:** Previous to tests, this module is a good one for Ansible Azure.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/ansiblemodules/azure_rm_datalakeacl.py>`_

Day 68: September 14, 2019
--------------------------

**Today's Progress:**

1. Some go and some python gpu tests

**Thoughts:** Really busy at work but I still have time to do some programming ;)

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/go/>`_
2. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/gpuvscpu/>`_

Day 69: September 23, 2019
--------------------------

**Today's Progress:**

1. Madrid Bicimad Time Series

**Thoughts:** Playing with Bicimad data and getting some cool graphs from it

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/bicimad/>`_

Day 70: September 28, 2019
--------------------------

**Today's Progress:**

1. Graph Algorithms from Grokking Algorithms

**Thoughts:** Understanding Graph Algorithms from this great book

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/grokalgorithms/>`_

Day 71: October 5, 2019
--------------------------

**Today's Progress:**

1. Greedy Algorithms from Grokking Algorithms

**Thoughts:** Understanding Greedy Algorithms from this great book

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/grokalgorithms/>`_

Day 72: October 26, 2019
--------------------------

**Today's Progress:**

1. Start Learning PyTest

**Thoughts:** Just realized that I'm not good at all at unit testing. I need to learn how to do good testing with Python. This is the first stage and probably would take over 10 to fully understand it.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/tests/>`_

Day 73: October 27, 2019
--------------------------

**Today's Progress:**

1. Continue with PyTest

**Thoughts:** Second PyTest Session. Fixtures

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/pytest_project/>`_

Day 74: October 30, 2019
--------------------------

**Today's Progress:**

1. Docker Signal Management for K8S

**Thoughts:** Some testing with K8S Configuration, Docker and Python

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/signals/>`_

Day 75: November 11, 2019
--------------------------

**Today's Progress:**

1. Continuing with Python Testing

**Thoughts:** Discovered bandit for security flaws testing. Continuing with testing with unittest

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/tests/>`_

Day 76: November 17, 2019
--------------------------

**Today's Progress:**

1. MongoDB Tests with Docker

**Thoughts:** Adding some MongoDB testing. Just easy functions.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/mongodb/>`_

Day 77: December 9, 2019
--------------------------

**Today's Progress:**

1. Add emailcrawler python (Lost source)

**Thoughts:** Study and play with bandit with this Python code. Don't like too much but gives me several ideas.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/emailcrawler/>`_

Day 78: December 10, 2019
----------------------

**Today's Progress:**

1. AsyncIO in Python. areq.py Code.

**Thoughts:** Third part of this really nice tutorial.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/asyncio>`_
2. See `Original Documentation from Real Python <https://realpython.com/async-io-python/>`_

Day 79: December 14, 2019
----------------------

**Today's Progress:**

1. Python Performance with pytest-benchmark mostly

**Thoughts:** Didn't know about pytest-benchmark with this part, I'm learning also about how to create better python tests.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/highperf>`_
2. See `Original Documentation from Packt <https://www.packtpub.com/eu/application-development/python-high-performance-second-edition>`_

Day 80: December 15, 2019
----------------------

**Today's Progress:**

1. Python Performance: Finding bottlenecks with cProfile

**Thoughts:** Didn't know about cProfiling. Testing different visual tools for debugging and performance

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/highperf>`_
2. See `Original Documentation from Packt <https://www.packtpub.com/eu/application-development/python-high-performance-second-edition>`_

Day 81: December 22, 2019
----------------------

**Today's Progress:**

1. Machine Learning: Detecting Fake News

**Thoughts:** Use scikit learn with Passive Aggressive Classifier

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/fakenews>`_
2. See `Original Documentation from Data-Flair <https://data-flair.training/blogs/advanced-python-project-detecting-fake-news/>`_

Day 82: January 03, 2020
----------------------

**Today's Progress:**

1. Python Performance: Profiling memory usage with memory_profiler

**Thoughts:** Finding Memory Issues using this module. Also discovered the __slots__ dunder, although it has a drawback: It prevents the addition of attributes other than the ones specified in it.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/blob/devel/python/highperf>`_
2. See `Original Documentation from Packt <https://www.packtpub.com/eu/application-development/python-high-performance-second-edition>`_

Day 83: January 6, 2020
---------------------

**Today's Progress:**

1. Build a Mobile Application With the Kivy Python Framework

**Thoughts:** Easy to implement and understand

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/kivy_project>`_
2. See `Original Documentation from Real Python <https://realpython.com/mobile-app-kivy-python/>`_

Day 84: January 12, 2020
---------------------

**Today's Progress:**

1. Learn object-oriented programming with Python

**Thoughts:** Just Playing with more OO Programing. Adding Detect-Secrets to Code whether on pre-commit and build

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/ooppython>`_
2. See `Original Documentation from OpenSource.com <https://opensource.com/article/19/7/get-modular-python-classes/>`_

Day 85: February 29, 2020
---------------------

**Today's Progress:**

1. Discovering Logzero for Logging

**Thoughts:** I love this one. Colourful and easy to use. I'm quite slow finishing this project as other projects are alive

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/logging>`_
2. See `Original Documentation from OpenSource.com <https://opensource.com/article/20/2/logzero-python>`_

Day 86: March 29, 2020
---------------------

**Today's Progress:**

1. Playing with email

**Thoughts:** Good to have this code for email. Check documentation attached to this project for reference.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/smtpimap>`_
2. See `Original Documentation from DevDungeon.com <https://www.devdungeon.com/content/read-and-send-email-python>`_

Day 87: March 30, 2020
---------------------

**Today's Progress:**

1. Ansible Plugin and Filter

**Thoughts:** lookup plugin to merge lists from a given key and filter to get a Microsoft SAS Token

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/ansibleplugins>`_
2. See `Ansible Developer Guide <https://docs.ansible.com/ansible/devel/dev_guide/index.html>`_

Day 88: April 7, 2020
---------------------

**Today's Progress:**

1. OpenDNS Updater

**Thoughts:** As the opendns updater doesn't work for macos, I have developed my own. Simple one for now, but
I will improve it in the future, probably with some UI and logging.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/opendns>`_
2. See `OpenDNS API Documentation <https://support.opendns.com/hc/en-us/articles/227986527-FAQ-OpenDNS-Developer-Resources>`_

Day 89: April 10, 2020
---------------------

**Today's Progress:**

1. Simulating Real-World Processes With SimPy

**Thoughts:** Curious Subject I didn't heard of before reading this article from Real Python. Nice to have in the radar.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/simulation>`_
2. See `SimPy: Simulating Real-World Processes With Python <https://realpython.com/simulation-with-simpy>`_

Day 90: April 18, 2020
---------------------

**Today's Progress:**

1. Replace Conditional with Polymorphism

**Thoughts:** Reading Conditionals from the refactoring guru and playing with the example.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/polymorphism>`_
2. See `Replace Conditional with Polymorphism <https://refactoring.guru/replace-conditional-with-polymorphism>`_

Day 91: April 23, 2020
---------------------

**Today's Progress:**

1. ML Titanic with VSCode

**Thoughts:** Test VSCode Jupyter functionality

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mltitanic>`_
2. See `Data Science in Visual Studio Code <https://code.visualstudio.com/docs/python/data-science-tutorial>`_

Day 92: May 3, 2020
---------------------

**Today's Progress:**

1. Mocking with Python

**Thoughts:** Learn about db testing mocking with Python

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mocking>`_
2. See `Mocking with Python Part I <https://kirankoduru.github.io/python/mocking-with-python-part-1.html>`_
3. See `Mocking with Python Part II <https://kirankoduru.github.io/python/mocking-with-python-part-2.html>`_

Day 93: May 11, 2020
---------------------

**Today's Progress:**

1. BDD with Python

**Thoughts:** I had some ideas about BDD and implementing it with Ansible. I also had some ideas about generating infrastructure with NLP or Gherkin. This is the first step and I will come back when playing with it some more time.
Wanted also to start to understand how distributing software with Torrent as Facebook does. I want to understand the whole Torrent process so I just started decode torrent files.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/bdd>`_
2. See `Test Automation with Python Behave and Ansible <https://phalient.tech/blog/2019-06-18-test-automation-with-python-behave-and-ansible/>`_
3. See `Some Torrent information but not using this approach <https://markuseliasson.se/article/bittorrent-in-python/>`_
4. See `Bitorrent Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/bittorrent>`_

Day 94: May 17, 2020
---------------------

**Today's Progress:**

1. azure_rm_privatednszone for Ansible

**Thoughts:** Development of a new module for Ansible Azure.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/ansiblemodules/azure_rm_privatednszone.py>`_

Day 95: May 23, 2020
---------------------

**Today's Progress:**

1. azure_rm_privatednszone_info for Ansible

**Thoughts:** Development of a new module for Ansible Azure.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/ansiblemodules/azure_rm_privatednszone_info.py>`_

Day 96: May 24, 2020
---------------------

**Today's Progress:**

1. Web scraping with Python

**Thoughts:** Easy web scrapping with BeautifulSoup

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/scrappingb4s>`_
2. See `A beginner's guide to web scraping with Python <https://opensource.com/article/20/5/web-scraping-python>`_

Day 97: June 6, 2020
---------------------

**Today's Progress:**

1. Play with Toga

**Thoughts:** Toga is a Python native, OS native, cross platform GUI toolkit. Toga consists of a library of base components with a shared interface to simplify platform-agnostic GUI development.

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/playwithtoga>`_
2. See `Toga Documentation <https://toga.readthedocs.io/en/latest/index.html>`_

Day 98: June 7, 2020
---------------------

**Today's Progress:**

1. Mocking External APIs in Python

**Thoughts:** How to test the use of an external API using Python mock objects. Run with `nosetests --verbosity=2 mockingapi` from the Python Directory

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/mockingapi>`_
2. See `Real Python Tutorial <https://realpython.com/testing-third-party-apis-with-mocks/>`_

Day 99: June 14, 2020
---------------------

**Today's Progress:**

1. API Connection with Go

**Thoughts:** Learn how to GET and POST JSON with GO

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/go/apiconnect>`_
2. See `Consume RESTful API Endpoints <https://www.thepolyglotdeveloper.com/2017/07/consume-restful-api-endpoints-golang-application/>`_

Day 100: June 20, 2020
---------------------

**Today's Progress:**

1. API Client Certificates for Python

**Thoughts:** Learn and test possibilities loading client certificates in Python. It can be tested with:

* https://server.cryptomix.com/secure/
* https://prod.idrix.eu/secure/

**Link to work:**

1. See `Code <https://github.com/imjoseangel/100-days-of-code/tree/devel/python/apiconnect>`_
