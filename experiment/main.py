import cv2
import os
import numpy as np
import re

def compare_images(img1, img2):
    # Resize images to the same size for comparison
    height, width = 280, 210  # Example size, adjust as needed
    img1_resized = cv2.resize(img1, (width, height))
    img2_resized = cv2.resize(img2, (width, height))

    # Compute the difference
    difference = cv2.absdiff(img1_resized, img2_resized)

    # Calculate similarity (or other metrics)
    similarity = np.sum(difference)

    return similarity, difference

def process_folders(folder1, folder2):
    # Dictionary to store filenames with dates as keys
    era5_files = {}
    wrf_files = {}

    # Regex pattern to extract date
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

    # Populate era5_files dictionary with dates as keys
    for filename in os.listdir(folder1):
        if filename.endswith(".jpg"):
            match = date_pattern.search(filename)
            if match:
                date = match.group()
                era5_files[date] = filename

    # Populate wrf_files dictionary with dates as keys
    for filename in os.listdir(folder2):
        if filename.endswith(".jpg"):
            match = date_pattern.search(filename)
            if match:
                date = match.group()
                wrf_files[date] = filename

    # Compare files based on matching dates
    for date, filename1 in era5_files.items():
        filename2 = wrf_files.get(date)
        if filename2:
            img1_path = os.path.join(folder1, filename1)
            img2_path = os.path.join(folder2, filename2)

            img1 = cv2.imread(img1_path)
            img2 = cv2.imread(img2_path)

            similarity, difference = compare_images(img1, img2)

            # log it into file with filename and both scores
            with open('C:/rohhs/lib/tournament/technical/images/scores.txt', 'a') as f:
                f.write(f"{filename1},{filename2},{similarity}\n")
            


            # Log the results
            print(f"Comparing {filename1} and {filename2}:")
            print(f"Similarity Score: {similarity}")
            # Optionally, save the difference image
            # cv2.imwrite('C:/rohhs/lib/tournament/technical/theory/', difference)

# Example usage
process_folders('C:/rohhs/lib/tournament/technical/images/era5', 'C:/rohhs/lib/tournament/technical/images/wrf')
