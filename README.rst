=============
Stroop Effect
=============

A statistical analysis of a classic experiment


Background Information
----------------------

In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED (is red color), BLUE (is blue color). In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE (is red color), ORANGE (is blue color). In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.

Try it out `here <https://faculty.washington.edu/chudler/java/ready.html>`_

1. What is our independent variable. What is our dependent variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within subject design, where each subject is given two tests using 24 participants.

This gives paired data (congruent vs. incogruent).

The dependent variable is the time a participant takes to respond. This is a quantative, temporal, ratio data type.


2. Hypotheses for this task
---------------------------

The results have come from a repeated measures design so the hypothesis test will compare the
difference between the two sets of results.

.. image:: resources\images\H0.png
   :scale: 100 %

.. image:: resources\images\HA.png
   :scale: 100 %

Where mu d is the mean difference between the paired data.

The null hypothesis is that there will be no difference in the time taken to read through the list when the data is presneted in incongruent or congruent form.

The alternative hypothesis is that if the data is presented in incongruent form the time taken to read through the list will be different than the time taken when the data is presented in congruent form.

As test sample will involve 24 participants, this will not be a measure of the total population.

A two tailed dependent sample t-test will be conducted where α = 0.05.

Limitations
~~~~~~~~~~~

A limitation is the sample size, if this is large enough to give a significant response or if a larger dataset will be required.

Another limitation is we have no information about the source of the data.

What was the sampling method of participants to the experiment, will they give a random sample representative of the population?
We have to assume this an experimental design.

There could be some carry-over effects. The second measurement could be affected
by the first treatment. Particpants could be initially disorientated with the format of the
test, being more familiar may increase response time in the second test.


3. Descriptive statistics regarding the dataset
-----------------------------------------------

.. image:: resources\images\Descriptive_statistics.png
   :scale: 100 %

There are no times that a participants congruent test results are a shorter response time than their incongruent response time.

4. Visualizations of the distribution of the sample data 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A histogram can display the distribution of results from each experiment. This is combined with a faint
rug plot (showing small vertical ticks along the x-axis) to highlight where the individual values occur along the x-axis and kernel density estimation to
highlight the distribution of values. 

Both figures are plotted using the same x-axis.

.. image:: resources\images\Hist_Congruent.png
   :scale: 100 %

.. image:: resources\images\Hist_Incongruent_hist.png
   :scale: 100 %

The first thing that stands out is the genereal different in time between Congruent and Incongruent.

Compared to the descriptive statistics this helps highlight the distribution of the values more clearly.

Q-Q(Quantile Quantile) plots typically need around 1000 samples but still form a way to compare samples to an
ideal distribution.

.. image:: resources\images\Congruent_QQ.png
   :scale: 100 %

.. image:: resources\images\Incongruent_QQ.png
   :scale: 100 %

These plots demonstrate that neither distribution appears completely normal.

5. Inferntial statistics and results
------------------------------------

What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

Results
~~~~~~~

t(23) = -8.02 p ≈ 0, two-tailed

Where p = 4e-08

Confidence interval of the mean difference, 
95% CI = (5.91 to 10.02)

d calculated using Cohen´s d

d = -1.64

R squared coefficient

r² = .74

Based on a critical t statistic of ± 2.069

Conclusion
~~~~~~~~~~

The null hypothesis is rejected.

The difference of the mean between the two samples is not 0, nor does 0 lie within the confidence intervals.

The two tailed t-test suggests this is a very unlikely occurence with close to a probability of 0 of occuring.

A Q-Q plot of the two variables gives an overview of how the two distributions are related.

.. image:: resources\images\QQ_plot.png
   :scale: 100 %

This could be improved by adding a 95% confidence interval to give a visual representation
about the hypothesis test.

The figure alone helps show the magnitude of the difference between the two samples.


6. What is responsible for the effects observed 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!

Resources used
--------------

`Latex symbols <https://www.scribd.com/doc/6328774/LaTeX-Mathematical-Symbols>`_

`TEX Commands available in MathJax <http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm>`_

`Matlibplot tex symbols <https://matplotlib.org/users/mathtext.html#mathtext-tutorial>`_

`Matlibplot tables <http://matplotlib.org/devdocs/api/_as_gen/matplotlib.axes.Axes.table.html>`_

`Change table cell properties <https://stackoverflow.com/questions/37554606/matplotlib-table-row-label-font-color-and-size>`_

`Hypothesis testing forumla <https://en.wikipedia.org/wiki/Statistical_hypothesis_testing>`_

`Auckland computational statistics lecture notes <https://www.stat.auckland.ac.nz/~ihaka/787/slides.html>`_
