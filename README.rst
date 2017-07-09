=============
Stroop_Effect
=============

A statistical analysis of a classic experiment


Background Information
______________________

In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED, BLUE. In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE, ORANGE. In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.

Try it out 'here <https://faculty.washington.edu/chudler/java/ready.html>'_

1. What is our independent variable. What is our dependent variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The independent variable is nominal, categorical, representing the two experiment conditions incongruent vs congruent words condition. 

The dependent variable is the time a participant takes to respond. This is a quantative temporal ratio data type.  


2. Hypotheses for this task
~~~~~~~~~~~~~~~~~~~~~~~~~~~

..math

    \begin{align*}
    H_0 & : h_1(t) = h_0(t),   \qquad \text{for all $t \in[0,\tau]$}
    \\
    H_a & : h_1
    \end{align*}

The alternative hypothesis is that the if the data is presented in incongruent form the time taken to read through the list will be greater than the time taken when the data is presented in congruent form.

The null hypothesis is that there will be no difference in the time taken to read through the list when the data is presneted in incongruent or congruent form.

Two experiments can be undertaken with times recorded.

A two tailed statistical test can be perfomed to test if, to an alpha value of 0.05, the incogruent results are significant. 

A two tailed test can be selected in case the opposite of what is expected occurs.

A limitations is the sample size, if this is large enough to give a significant response or if a larger dataset will be required.


3. Descriptive statistics regarding the dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Include at least one measure of central tendency and at least one measure of variability.

4. Visualizations the distribution of the sample data 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Write one or two sentences noting what you observe about the plot or plots.

5. Statistical testing and results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

6. What is responsible for the effects observed 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!

Resources used
--------------

'Latex symbols <https://www.scribd.com/doc/6328774/LaTeX-Mathematical-Symbols>'_

