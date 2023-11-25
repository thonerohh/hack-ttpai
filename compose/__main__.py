import os
import re
from PIL import Image

def create_gif(folder_path, regex_pattern, gif_name, duration=150):
    # Compile the regex pattern
    pattern = re.compile(regex_pattern)

    # List to hold images
    images = []

    # Loop through the folder
    for filename in os.listdir(folder_path):
        if pattern.match(filename):
            # Open the image and append to the list
            image_path = os.path.join(folder_path, filename)
            images.append(Image.open(image_path))

    # Check if images list is not empty
    if images:
        # Save the images as a gif
        images[0].save(
            gif_name,
            save_all=True,
            append_images=images[1:],
            duration=duration,
            loop=0
        )
        print(f"GIF created successfully: {gif_name}")
    else:
        print("No images found matching the regex pattern.")

# Example usage
create_gif('images\\andrey1', '.*era.*_2\..*', 'era_andrey1_2.gif', 150)
