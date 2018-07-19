print(" this  is my lenear regression analysis  programm ")
# Import what you need
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data_log = pd.DataFrame ({
'length' : [94,74,147,58,86,94,63,86,69,72,128,85,82,86,88,72,74,61,90,89,68,76,114,90,78],
'weight' : [130,51,640,28,80,110,33,90,36,38,366,84,80,83,70,61,54,44,106,84,39,42,197,102,57]
})
# ========================
# Model for Original Data
# ========================
 
# Get the linear models
lm_original = np.polyfit(data_log.length, data_log.weight, 1)
 
# calculate the y values based on the co-efficients from the model
r_x, r_y = zip(*((i, i*lm_original[0] + lm_original[1]) for i in data_log.length))
 
# Put in to a data frame, to keep is all nice
lm_original_plot = pd.DataFrame({
'length' : r_x,
'weight' : r_y
})
r_x, r_y = zip(*((i, i*lm_original[0] + lm_original[1]) for i in data_log.length))


# ========================
# Model for Log Data
# ========================

# Get the linear models
lm_log = np.polyfit(data_log.length, data_log.weight, 1)

# calculate the y values based on the co-efficients from the model
r_x, r_y = zip(*((i, i*lm_log[0] + lm_log[1]) for i in data_log.length))

# Put in to a data frame, to keep is all nice
lm_log_plot = pd.DataFrame({
'length' : r_x,
'weight' : r_y
})

# ========================
# Model for Log Data
# ========================
 
# Get the linear models
lm_log = np.polyfit(data_log.length, data_log.weight, 1)
 
# calculate the y values based on the co-efficients from the model
r_x, r_y = zip(*((i, i*lm_log[0] + lm_log[1]) for i in data_log.length))
 
# Put in to a data frame, to keep is all nice
lm_log_plot = pd.DataFrame({
'length' : r_x,
'weight' : r_y
})
# ========================
# Plot the data
# ========================
fig, axes = plt.subplots(nrows=1, ncols=2)
 
# Plot the original data and model
data_log.plot(kind='scatter', color='Blue', x='length', y='weight', ax=axes[0], title='Original Values')
lm_original_plot.plot(kind='line', color='Red', x='length', y='weight', ax=axes[0])
 
# Plot the log transformed data and model
data_log.plot(kind='scatter', color='Blue', x='length', y='weight', ax=axes[1], title='Log Values')
lm_log_plot.plot(kind='line', color='Red', x='length', y='weight', ax=axes[1])
plt.show()
