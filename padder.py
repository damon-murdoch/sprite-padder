import sys
from PIL import Image
import os

# Folder path containing the sprites
sprites_folder = "in"

# Output folder for resized sprites
output_folder = "out"

# Pad the sprites to the desired width, height
def pad_sprites(target_width=64, target_height=64):

    # Loop through all the files in the sprites folder
    for filename in os.listdir(sprites_folder):
        if filename.endswith(".png"):  # Change this to the appropriate image format
            image_path = os.path.join(sprites_folder, filename)
            
            # Open the image using PIL
            image = Image.open(image_path)
            
            # Calculate the amount of padding required
            pad_x = max(0, target_width - image.width)
            pad_y = max(0, target_height - image.height)
            
            # Calculate the padding for top and left to keep the sprite at bottom-center
            pad_left = pad_x // 2
            pad_top = pad_y
            
            # Create a new blank image with the target dimensions and transparency
            new_image = Image.new("RGBA", (target_width, target_height), (0, 0, 0, 0))
            
            # Paste the original image onto the new image with padding
            new_image.paste(image, (pad_left, pad_top))
            
            # Save the new image to the output folder
            output_path = os.path.join(output_folder, filename)
            new_image.save(output_path)
            
            print(f"Padded and saved {filename} to {output_path}")

# Main process
if __name__ == '__main__': 

    # Default pad size
    width = 64
    height = 64

    # Get the cli args
    args = sys.argv[1:]

    # Length greater than 2
    if len(args) >= 2:

        # Width = first arg
        width = int(args[0])

        # Height = second arg
        height = int(args[1])

        print(f"Using custom {width}w/{height}h dimensions ...")

    # Run the pad sprites script
    pad_sprites(width, height)