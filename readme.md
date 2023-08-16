# Sprite Padding Script

This script was generated using [ChatGPT](https://chat.openai.com/), and has been cleaned up and edited by me. This script is designed to 
pad a folder of sprite images with transparent space to reach a target dimension while keeping the original sprite size. It's particularly
useful when you need to ensure that all sprites have the same dimensions for your project.

## How It Works

1. The script reads all image files (currently supports PNG format) from the specified input folder.
2. For each image, it calculates the amount of padding required to reach the target dimensions.
3. The script then calculates the padding values to keep the original sprite centered at the bottom of the new image.
4. It creates a new transparent image with the target dimensions and pastes the original sprite onto it with the calculated padding.
5. The new image, with transparent padding, is saved to the specified output folder.

## Usage

1. Make sure you have Python 3 installed on your system.
2. Install the required dependencies using `pip`:

   ```
   pip install -r requirements.txt
   ```

3. Place your sprite images (in PNG format) inside the input `in` folder.

4. Run the script using the following format:

   `python sprite_padding_script.py [width] [height]`

   e.g. 
   
   `python sprite_padding_script.py 64 64`

   Would pad all images in the `in` folder to 64x64 pixels, and write the modified images to the `out` folder.

5. The padded sprites will be saved in the output `out` folder, while keeping the original sprite size and positioning it at the bottom-center.

## Note

- This script assumes that the sprites have a transparent background. If your sprites have a different background, you might need to modify the script accordingly.