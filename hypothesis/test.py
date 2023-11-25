import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import numpy as np

def generateImage(file_path, root_dir):
    # Load the data from the .npy file
    data = np.load(file_path)

    # Looping over the slices
    # Loop over every [0] value
    for i in range(data.shape[0]):  
        for j in range(data.shape[1]):    # Loop over every [1] value
            slice_data = data[i, j, :, :]

            # flip vertically data
            slice_data = np.flipud(slice_data)

            dpi = 15  # Use a standard DPI and adjust figure size accordingly
            figsize = (slice_data.shape[1] / dpi, slice_data.shape[0] / dpi)  # Width, Height in inches

            # Plotting the slice as a heatmap
            plt.figure(figsize=figsize, dpi=dpi)
            sns.heatmap(slice_data, cmap='gray', cbar=False, xticklabels=False, yticklabels=False)

            # Extract date from file name and create a new file name for the image
            date_str = os.path.basename(file_path).split('_')[-2].rstrip('.npy')
            image_name = f"heatmap_{date_str}_slice_{i}_{j}.jpg"
            # image_dir = os.path.join('images', root_dir.split('dataset')[-1])
            # remove 2 last paths from root_dir
            image_dir = 'C:/rohhs/lib/tournament/technical/images/andrey1/'
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)
            bw_image_path = os.path.join(image_dir, image_name)

            # Remove axes and padding 
            plt.axis('off')
            plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
            plt.margins(0,0)
            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())


            # Save the plot as a jpg image in B&W
            plt.savefig(bw_image_path, format='jpg',  bbox_inches='tight', pad_inches=0, dpi=dpi)
            plt.close()  # Close the figure to free up memory

            print(f"Black and White heatmap saved at {bw_image_path}")

if __name__ == "__main__":
    # Define the root directory
    root_dir = 'dataset/target/'  # Adjust this to your root directory
    
    generateImage( 'dataset/target/era_jan.npy', root_dir)
    

    # # Walk through all subdirectories and files in the root directory
    # for subdir, dirs, files in os.walk(root_dir):
    #     for file in files:
    #         if file.endswith(".npy"):
    #             file_path = os.path.join(subdir, file)
    #             generateImage(file_path, root_dir)
