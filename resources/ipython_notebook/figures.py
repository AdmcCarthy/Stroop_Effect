#!/usr/bin/python

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Color schemes
b_and_w = ['#D5D5D5', '#9099A2', '#6D7993', '#96858F']
ToddTerje = ['#F24C4E', '#EAB126', '#1FB58F', '#1B7B34']
cool_blue = ['#99D3DF','#88BBD6','#CDCDCD', '#E9E9E9']
custom = ['#192231','#3C3C3C','#CDCDCD', '#494E6B']


def common_set_up(ax_size):
    """Common plot set up to be
    re-used in other figures.
    """

    sns.set_style("whitegrid")
    sns.set_style("ticks", {'axes.grid': True, 'grid.color': '.99', 'ytick.color': '.4', 'xtick.color': '.4'})
    sns.set_context("poster", font_scale=0.8, rc={"figure.figsize": ax_size, 'font.sans-serif': 'Gill Sans MT'})


def formatting_text_box(ax, parameters, formatting_right):
    """ Returns the ax(axes within figures) with an
    added text box describing all parameters used.
    """

    font_colour = '#9099A2'

    # Text box set up
    text_box_patch = dict(boxstyle='round', facecolor='white', alpha=0.5, edgecolor='white')

    # Text box position
    if formatting_right:
        box_vertical = 0.83
        box_horizontal = 0.845
    else:
        box_vertical = 0.83
        box_horizontal = 0.05

    ax.text(box_horizontal, box_vertical, parameters, transform=ax.transAxes, fontsize=12,
            verticalalignment='top', color=font_colour, bbox=text_box_patch)
    
    return ax


def annotation_text(ax, string, vert_pos, horz_pos, color_set=custom, strong_colour=True, font_size=12):
    """ Returns the ax(axes within figures) with an
    added text box displaying an annotation
    """

    if strong_colour:
        font_c = color_set[0]
    else:
        font_c = '#9099A2'  # Light pale grey

    # Text box set up
    text_box_patch = dict(boxstyle='round', facecolor='white', alpha=0.2, edgecolor='white')

    ax.text(horz_pos, vert_pos, string, transform=ax.transAxes, fontsize=font_size,
    verticalalignment='top', color=font_c, bbox=text_box_patch)

    return ax


def univariate(x, univariate_name, color_set=custom, bin_n='all_values', ax_size=(12, 6), funky=False, rug=True, formatting_right=True, x_truncation_upper=None, x_truncation_lower=None, ax=None):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    if funky:
        color_set = ToddTerje
    
    common_set_up(ax_size) # Apply basic plot style

    if bin_n == 'all_values':
        x_max = x.max()
        x_min = x.min()
        bin_n = int(x_max)-int(x_min)

    fig = sns.distplot(x, bins=bin_n, rug=rug, ax=ax,
                      hist_kws={"histtype": "bar", "linewidth": 1, 'align': 'mid', 'log': False, 'edgecolor': 'white', "alpha": 1, "color": color_set[2], 'label': 'Histogram'},
                      kde_kws={"color": color_set[0], "lw": 3, "label": "KDE"},
                      rug_kws={"color": color_set[1], 'lw': 0.3, "alpha": 0.5, 'label': 'rug plot', 'height': 0.05})

    title_color = '#192231'
    font_colour = '#9099A2'

    # Title and axis set up
    if rug:
        rugstr = ', with rug plot'
    else:
        rugstr = ''

    # Do not add a title in a multi-figure plot.
    #
    # Title will be added to figure with all sub-plots
    # instead in this case
    if ax is None: 
        fig.set_title(('Distribution of {0}'.format(univariate_name) + rugstr),
                    fontsize=20, color=title_color)
    fig.set_xlabel('{0}'.format(univariate_name),
                color=font_colour)
    fig.set_ylabel('Frequency'.format(univariate_name),
                   color=font_colour)

    # Limit the x axis by truncating
    if x_truncation_upper or x_truncation_lower:
        axes = fig.axes
        axes.set_xlim(x_truncation_lower, x_truncation_upper)
        # To be communicated back in Formatting notes
        x_truncation_upper_str = 'x axis truncated by {0}\n'.format(x_truncation_upper)
        x_truncation_lower_str = 'x axis truncated after {0}\n'.format(x_truncation_lower)
    else:
        x_truncation_upper_str = ''
        x_truncation_lower_str = ''
    
    # Used to describe the format of plot
    if bin_n is None:
        bin_n_str = 'automatic'
    else:
        bin_n_str = bin_n

    # String within text box
    parameters = ('Formatting:\n'
                + x_truncation_lower_str
                + x_truncation_upper_str
                + 'bins = {0}'.format(bin_n_str))
    
    # Will not work on multiple subplots within a figure
    if ax is None:
        # Seaborn despine to remove boundaries around plot
        sns.despine(offset=2, trim=True, left=True, bottom=True)

    fig = formatting_text_box(fig, parameters, formatting_right)

    return fig


def boolean_bar(data, name, color_set=custom, ax_size=(2, 5), funky=False, annotate=True):
    """Make a univariate distribution
    of a variable.

    Returns an object to be plotted.
    """

    if funky:
        color_set = ToddTerje

    common_set_up(ax_size) # Apply basic plot style

    fig = sns.countplot(data, saturation=1,
                       color=color_set[2], label=name
                      )

    sns.despine(offset=2, trim=True, left=True, bottom=True)

    # Set title and axes
    title_color = '#192231'
    fig.set_title('{0}'.format(name),
                 fontsize=20, color=title_color)
    fig.set_ylabel('')
    fig.set_xlabel('')

    # Percentage annotation
    if annotate:
        total = float(len(data))
        for p in fig.patches:
            fig.annotate('{:.2f}'.format((p.get_height()/total)), # Value to be anootated
                        (
                            p.get_x()+p.get_width()/2.,          # X position
                            p.get_height()-1300                  # y position
                        ),
                        ha='center', label='Fraction',
                        color=color_set[0])

    return fig


def qq_plot(data, name, distribution="norm", ax_size=(7, 7)):
    """Plot a qq plot using one data value against a
    known distribution.
    """
    
    common_set_up(ax_size)

    fig = plt.figure(figsize=ax_size)
    ax = fig.add_subplot(111)

    # Use stats function and get out values
    (x, y) = stats.probplot(data, dist=distribution, plot=None, fit=False)
    
    # Add a best fit line
    slope, intercept, r, prob, sterrest = stats.linregress(x, y)
    ax.plot(x, (slope*x + intercept), '#9099A2', 
                linestyle='--', linewidth=1)
    
    ax.scatter(x, y, s=70, facecolors='none', edgecolors='#192231', linewidths=1.4)
    
    title_color = '#192231'
    font_colour = '#9099A2'
    
    ax.set_title("Q-Q plot of {0}".format(name),
                fontsize=20, color=title_color)
    ax.set_ylabel('Quantiles of {0}'.format(name),
                color=font_colour)
    ax.set_xlabel('Quantiles of {0} dist.'.format(distribution),
                   color=font_colour)
    
    sns.despine(ax=ax, offset=2, trim=True, left=True, bottom=True)


def qq_plot_var(data_a, data_b, name_a, name_b, ax_size=(7, 7), fit_zero=True):
    """Plot a qq plot using one data value against a
    known distribution.
    """
    
    common_set_up(ax_size)
   
    fig = plt.figure(figsize=ax_size)
    ax = fig.add_subplot(111)
    
    x = []
    for i in range(1, 100):
        v = np.percentile(data_a, i)
        x.append(v)
        
    y = []
    for i in range(1, 100):
        v = np.percentile(data_b, i)
        y.append(v)
    
    # Plot a base line
    ax.plot(x, (1*x), '#9099A2', 
            linestyle='--', linewidth=1)
    
    ax.scatter(x, y, s=40, facecolors='none', edgecolors='#192231', linewidths=0.5)
    
    if max(x) < max(y):
        upper = max(y)
    else:
        upper = max(x)
    
    if fit_zero:
        axes = ax.axes
        axes.set_xlim(0,)
        axes.set_ylim(0,)
    
    title_color = '#192231'
    font_colour = '#9099A2'
    
    ax.set_title("Q-Q plot of {0} vs {1}".format(name_a, name_b),
                fontsize=20, color=title_color)
    ax.set_ylabel('Quantiles of {0}'.format(name_b),
                  color=font_colour)
    ax.set_xlabel('Quantiles of {0}'.format(name_a),
                   color=font_colour)

    sns.despine(ax=ax, offset=2, trim=True, left=True, bottom=True)

    return ax