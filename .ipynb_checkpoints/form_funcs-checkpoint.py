import matplotlib.pyplot as plt
import numpy as np

def split_unique_plus_stats(df, column, week = False):
    '''
    Splits the data, gets its unique values and computes the statistics out of it.
    '''
    
    df = df.copy()
    
    df = df.dropna(subset = [column])
    
    split = df[column].str.split(';', expand=True)
    
    if week == False:
        unique = []
        for col in split.columns:
            u = split[col]
            for item in u:
                if item not in unique:
                    unique.append(item)
    else:
        unique = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
                
    # Counting Statistic
    sizes = []
    for i in unique:
        counter = 0
        for col in split.columns:
            counter += split[col][split[col] == i].count()

        # Normalized Versions
        sizes.append([i, counter / split.shape[0]])
      
    s = [j * 100 for _, j in sizes]
    l = [i for i, _ in sizes]
    
    # Cleaning the possible `None` entries
    g = l[:]
    for i in range(0, len(g)):
        if g[i] == None:
            del s[i]
            del l[i]
            
    return s, l

def sups_loop(df, column, column_restriction):
    '''
    Loops with `split_unique_plu_stats()`.
    '''
    
    df = df.copy()
    
    loopy = {}
    for a in df[column_restriction].unique():

        t = df[df[column_restriction] == a]

        s, l = split_unique_plus_stats(t, column)

        loopy[a] = [s, l]
        
    return loopy

def plot_sups(size_figure,
              s, l,
              xlabel,
              ylabel,
              title,
              title_font_size,
              path,
              file_name):
    '''
    Plots a graph and saves it for `split_unique_plus_stats()`.
    ''' 
    
    plt.figure(figsize = size_figure)
    plt.barh(y = np.arange(len(s)), width = s)
    plt.yticks(np.arange(len(s)), l)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, fontsize = title_font_size)
    for i, v in enumerate(s):
        plt.text(v, i, ' ' + str(round(v, 2)) + '%')
    plt.xlim(xmax = 100)
    plt.savefig(path + file_name, dpi = 200, bbox_inches = 'tight')
    plt.show()
    
def normed_hist(pd_series, bins):
    '''
    Returns a normed histogram-like sequence based on the input.
    '''
    
    stepper = np.linspace(pd_series.min(), pd_series.max(), bins)
    delta = stepper[1] - stepper[0]
    
    bars = []
    for i in range(0, stepper.shape[0]):

        if i < stepper.shape[0] - 1:
            bar = pd_series[(pd_series >= stepper[i]) & (pd_series < stepper[i + 1])].count()
        else: # for catching the items that are exactly on the max()
            bar = pd_series[(pd_series >= stepper[i]) & (pd_series < stepper[i] + 1)].count()

        bars.append(bar)

    bars = np.array(bars) / pd_series.shape[0]
    
    return stepper, bars

def plot_normed_hist(stepper, bars, figsize, xlabel, ylabel, title, fontsize, path_img, file_name, dpi):
    '''
    Plots and Saves the Normed Histogram.
    '''
    
    plt.figure(figsize = figsize)
    plt.bar(stepper, bars * 100)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title, fontsize = fontsize)
    plt.savefig(path_img + file_name, dpi = dpi, bbox_inches = 'tight')
    plt.show()

def pie_sizes(df, column):
    '''
    Returns the sizes of the slices of the Pie Chart.
    '''
    
    sizes = df[column].value_counts() / df[column].count()
    
    return sizes

def plot_pie(sizes, figsize, title, fontsize, path_img, file_name, dpi):
    '''
    Plots and Saves the Pie Chart.
    ''' 
    
    plt.figure(figsize = figsize)
    plt.pie(sizes, labels = sizes.index, autopct='%1.1f%%')
    plt.title(title, fontsize = fontsize)
    plt.savefig(path_img + file_name, dpi = dpi, bbox_inches = 'tight')
    plt.show()