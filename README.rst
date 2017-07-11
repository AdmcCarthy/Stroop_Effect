=============
Stroop Effect
=============

A statistical analysis of a classic experiment


Background Information
______________________

In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED (is red color), BLUE (is blue color). In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE (is red color), ORANGE (is blue color). In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.

Try it out `here <https://faculty.washington.edu/chudler/java/ready.html>`_

1. What is our independent variable. What is our dependent variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The independent variable is nominal, categorical, representing the two experiment conditions incongruent vs congruent words condition. 

The dependent variable is the time a participant takes to respond. This is a quantative temporal ratio data type.  


2. Hypotheses for this task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

     \\alpha

.. math::

    deﬁne \\def\\mathbi#1{\\textbf{\\em #1}}

    \\mathbi{H}

.. math::

    \\mathbi{H}$_{0} :

.. math::

    $\\mathbi{H}$_{1} :

The alternative hypothesis is that the if the data is presented in incongruent form the time taken to read through the list will be greater than the time taken when the data is presented in congruent form.

The null hypothesis is that there will be no difference in the time taken to read through the list when the data is presneted in incongruent or congruent form.

Two experiments can be undertaken with times recorded.

A two tailed statistical test can be perfomed to test if, to an alpha value of 0.05, the incogruent results are significant. 

A two tailed test can be selected in case the opposite of what is expected occurs.

A limitations is the sample size, if this is large enough to give a significant response or if a larger dataset will be required.

Another limitation is we have no information about the source of the data.

What was the sampling method of participants to the experiment, will they give a random sample representative of the population?


3. Descriptive statistics regarding the dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: resources\images\descriptive_statistics.png
   :scale: 100 %

There are no times that a participants congruent test results are a shorter response time than their incongruent response time.

4. Visualizations the distribution of the sample data 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A histogram can display the distribution of results from each experiment. This is combined with a faint
rug plot (showing small vertical ticks along the x-axis) to highlight where the individual values occur along the x-axis and kernel density estimation to
highlight the distribution of values. Both figures are plotted using the same x-axis.

.. image:: resources\images\Congruent_hist.png
   :scale: 100 %

.. image:: resources\images\Incongruent_hist.png
   :scale: 100 %

The first thing that stands out is the genereal different in time between Congruent and Incongruent.

Compared to the descriptive statistics this helps highlight the distribution of the values more clearly.

5. Statistical testing and results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

6. What is responsible for the effects observed 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!

Resources used
--------------

`Latex symbols <https://www.scribd.com/doc/6328774/LaTeX-Mathematical-Symbols>`_

`Matlibplot tex symbols <https://matplotlib.org/users/mathtext.html#mathtext-tutorial>`_

`Matlibplot tables <http://matplotlib.org/devdocs/api/_as_gen/matplotlib.axes.Axes.table.html>`_

`Change table cell properties <https://stackoverflow.com/questions/37554606/matplotlib-table-row-label-font-color-and-size>`_

`Hypothesis testing forumla <https://en.wikipedia.org/wiki/Statistical_hypothesis_testing>`_

`Auckland computational statistics lecture notes <https://www.stat.auckland.ac.nz/~ihaka/787/slides.html>`_
