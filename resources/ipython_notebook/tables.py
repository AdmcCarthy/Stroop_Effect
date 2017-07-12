#!/usr/bin/python

import matplotlib.pyplot as plt 
from matplotlib import gridspec
import pandas as pd
import numpy as np
import seaborn as sns


def table_central_tend(data, axs, sample=True, f=2):
    """Returns a plotted table within the axs.
    
    Based on statistics for central tendancy, can
    take one column or more.
    """
    
    # Central tendacy
    v_mean = round(data.mean(), f)
    v_median = round(data.median(), f)
    
    # Use built in tex only, no depandancy needed
    sample_mean_str = "mean, " + r' $\bar x$ '
    sample_median_str = "median" 
    
    symbols = pd.DataFrame([sample_mean_str, sample_median_str])
    val = pd.DataFrame([v_mean, v_median])
    
    data = pd.concat([symbols, val], axis=1)
    
    disperssion = axs.table(cellText=data.values, 
                                    loc='center', colWidths=None,
                                    cellLoc="center", colLoc='center',
                                    # xmin, ymin, width, height
                                    bbox=(0, 0, 1, 1), 
                                    edges="")

    title_color = '#9099A2'
    axs.set_title(('Central Tendancy'),
            fontsize=12, color=title_color)
    
    table_settings(axs, disperssion)
    
def table_disperssion(data, axs, sample=True, f=2):
    """Returns a plotted table within the axs.
    
    Based on statistics for disperssion, can
    take one column or more.
    """
    
    # Measures of disperssion
    v_bessel_sd = round(data.std(), f)
    v_var = round(data.var(), f)
    v_range = round((data.max()-data.min()), f)
    v_iqr = round((data.quantile(0.75)-data.quantile(0.25)), f)
    v_mad = round(data.mad(), f)
    
    # Use built in tex only, no depandancy needed
    sample_std_str = "stan. dev." + r' $s$ '
    sample_var_str = "variance, " + '$s^2$'
    sample_range_str = "range"
    sample_iqr_str = "$IQR$"
    sample_mad_str = "mean abs. dev."
    
    symbols = pd.DataFrame([sample_std_str, sample_iqr_str, sample_mad_str, sample_var_str, sample_range_str])
    val = pd.DataFrame([v_bessel_sd,  v_iqr, v_mad, v_var, v_range])
    
    data = pd.concat([symbols, val], axis=1)
    
    disperssion = axs.table(cellText=data.values,
                                    loc='center', colWidths=None,
                                    cellLoc="center", colLoc='right',
                                    # xmin, ymin, width, height
                                    bbox=(0, 0, 1, 1), 
                                    edges="")

    title_color = '#9099A2'
    axs.set_title(('Disperssion'),
            fontsize=12, color=title_color)
    
    table_settings(axs, disperssion)
    
def table_distribution(data, axs, sample=True, f=2):
    """Returns a plotted table within the axs.
    
    Based on statistics for distribution, can
    take one column or more.
    """
    
    # Measures of distribution
    v_max = round(data.max(), f)
    v_95 = round((data.quantile(0.95)), f)
    v_90 = round((data.quantile(0.9)), f)
    v_75 = round((data.quantile(0.75)), f)
    v_50 = round((data.quantile(0.5)), f)
    v_25 = round((data.quantile(0.25)), f)
    v_10 = round((data.quantile(0.1)), f)
    v_05 = round((data.quantile(0.05)), f)
    v_min = round(data.min(), f)
    
    # quantile returns a series which needs to be recombined
    quantiles = pd.concat([v_max, v_95, v_90, v_75, v_50, v_25, v_10, v_05, v_min], axis=1).transpose().reset_index()
    quantiles.drop('index', axis=1, inplace=True)
    
    # Use built in tex only, no depandancy needed
    sample_max_str = r"maximum"
    sample_95_str = r"$Q(0.95)$"
    sample_90_str = r"$Q(0.90)$"
    sample_75_str = r"$Q(0.75)$"
    sample_50_str = r"$Q(0.50)$"
    sample_25_str = r"$Q(0.25)$"
    sample_10_str = r"$Q(0.10)$"
    sample_05_str = r"$Q(0.05)$"
    sample_min_str = r"minimum"
    
    symbols = pd.DataFrame([sample_max_str, sample_95_str, sample_90_str,
                            sample_75_str, sample_50_str, sample_25_str,
                            sample_10_str, sample_05_str, sample_min_str])
    
    data = pd.concat([symbols, quantiles], axis=1)
    
    distribution = axs.table(cellText=data.values,
                                    loc='center', colWidths=None,
                                    cellLoc="center", colLoc='right',
                                    # xmin, ymin, width, height
                                    bbox=(0, 0, 1, 1), 
                                    edges="")

    title_color = '#9099A2'
    axs.set_title(('Distribution'),
            fontsize=12, color=title_color)
    
    table_settings(axs, distribution)
    

def table_top(data, name, axs):
    """Returns a table with
    count of values and column
    headers.
    """
    
    # Count
    v_count = []
    for i in name:
        v_col_size = data[i].size
        v_count.append(v_col_size)
    
    # Use built in tex only, no depandancy needed
    sample_count_str = "samples, " + r' $n$ '
    
    symbols = pd.DataFrame([sample_count_str])
    val = pd.DataFrame([v_count])
    
    data = pd.concat([symbols, val], axis=1)
    
    labels = [""]
    for i in name:
        labels.append(i)
    
    top = axs.table(cellText=data.values, colLabels=labels, 
                                    loc='center', colWidths=None,
                                    cellLoc="center", colLoc='center',
                                    # xmin, ymin, width, height
                                    bbox=(0, 0, 1, 1), 
                                    edges="")
    
    table_settings(axs, top)
    
    axs.spines['top'].set_color('white')

    
def table_settings(axs_num, table_name):
    """Set style properties on a created
    table.
    
    Used to apply consitency to all outputs.
    """
    
    # iterate through cells of a table to change properties
    table_props = table_name.properties()
    table_cells = table_props['child_artists']
    for cell in table_cells: 
            cell._text.set_fontsize(15)
            cell._text.set_color('#192231')

    axs_num.set_yticklabels([])
    axs_num.set_xticklabels([])

    sns.set_style("whitegrid")
    sns.set_style({'axes.grid': False})
    sns.set_context("poster", rc={'font.sans-serif': 'Gill Sans MT'})

    sns.despine(offset=2, top=False, trim=False, left=True, bottom=True)

    axs_num.spines['top'].set_color('#9099A2')

    plt.setp([axs_num.get_xticklines(), axs_num.get_yticklines()], color="white")


def descriptive_table(data, column_name, fig_size=(8, 8)):
    """Plots a table of descriptive statistics.
    """
    # Set up figure dimensions
    sheet, axs = plt.subplots(4,1, figsize=fig_size)
    gs = gridspec.GridSpec(4, 1, height_ratios=[2, 2, 5, 9])
    
    # Assign all subplots based on figure dimensions
    ax0 = plt.subplot(gs[0])
    ax1 = plt.subplot(gs[1])
    ax2 = plt.subplot(gs[2])
    ax3 = plt.subplot(gs[3])

    title_color = '#9099A2'
    plt.suptitle('Descriptive Statistics', fontsize=16, color=title_color, x=0.25)

    table_top(data, column_name, ax0)
    table_central_tend(data, ax1)
    table_disperssion(data, ax2)
    table_distribution(data, ax3)
    sheet.subplots_adjust(hspace=0.2, top=0.95)