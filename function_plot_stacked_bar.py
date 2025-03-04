def plot_stacked_bar(df_pivot, figsize_nrows, figsize_ncols):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    """
    Plots a stacked bar chart using Seaborn + Matplotlib.

    Parameters:
    df_pivot (pd.DataFrame): A pivoted DataFrame where:
        - Index is Score categories.
        - Columns is one category.
        - Values represent counts.
    
    """
   
    # Initialize figure
    
    #fig, ax = plt.subplots(figsize=(20, 5))
    fig, ax = plt.subplots(figsize=(figsize_nrows,figsize_ncols))

    # Bottom position for stacking (starting at zero)
    bottom = np.zeros(len(df_pivot))  

    # Define colors using Seaborn's color palette
    colors = sns.color_palette("viridis", n_colors=len(df_pivot.columns))

    # Loop through each department to stack bars
    for i, department in enumerate(df_pivot.columns):
        sns.barplot(
            x=df_pivot.index,  # PerformanceScore on x-axis
            y=df_pivot[department],  # Values for stacking
            label=department,  # Legend label
            ax=ax, 
            bottom=bottom,  # Stacking effect
            color=colors[i]  # Color from palette
        )
        # Update bottom to stack the next bar
        bottom += df_pivot[department]

