import os
import sys
import numpy as np

def rename_files(folder_path, post_name):
    files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
    
    for count, filename in enumerate(files):
        #if ends in jpg
        if not filename.endswith('.jpg'):
            continue
        dst = folder_path + "\\" + str(count) + ".jpg"
        dst = f'{count}.jpg'
        src = folder_path + "\\" + filename
        print(src, dst)
        os.rename(src, dst)



def generate_image_grid(folder_path,identifier, rows, columns, max_width='200px', max_height='200px'):
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    images = [f for f in images if identifier in f]
    print(images)

    html_content = '<table>\n'
    for row in range(rows):
        html_content += '  <tr>\n'
        for col in range(columns):
            index = row * columns + col
            if index >= len(images):
                break
            image = images[index]
            filepath = "{{ site.baseurl }}" + "/"+ folder_path+ "/" + image
            html_content += f'    <td><img src="{filepath}" alt="Image {index}" style="max-width: {max_width}; max-height: {max_height}; width: 100%; height: auto;"></td>\n'
        html_content += '  </tr>\n'
    
    html_content += '</table>'
    
    return html_content


import os
from moviepy.editor import VideoFileClip

def convert_gif_to_mp4(source_directory, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith('.gif'):
            gif_path = os.path.join(source_directory, filename)
            mp4_path = os.path.join(target_directory, os.path.splitext(filename)[0] + '.mp4')
            if os.path.exists(mp4_path):
                continue
            print(f"Converting {gif_path} to {mp4_path}")
            clip = VideoFileClip(gif_path)
            clip.write_videofile(mp4_path, codec='libx264')
            clip.close()
            print(f"Converted {gif_path} to {mp4_path}")
<<<<<<< HEAD
=======

source_directory = 'assets/images/post_pics/an_unexpected_fractal'
target_directory = 'assets/images/post_pics/an_unexpected_fractal'
>>>>>>> 5d66c09 (whats happen in the profile)

#source_directory = 'assets/images/post_pics/an_unexpected_fractal'
#target_directory = 'assets/images/post_pics/an_unexpected_fractal'

<<<<<<< HEAD
#convert_gif_to_mp4(source_directory, target_directory)

=======
sys.exit()
>>>>>>> 5d66c09 (whats happen in the profile)
def generate_video_grid(folder_path, identifier, rows, columns, video_height='200px', video_width='auto'):
    # Get a list of all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    # Filter the files to include only those with the specified identifier
<<<<<<< HEAD
    videos = [f for f in files if identifier in f and f.endswith('.mp4')]
    print(videos)

    # Initialize the HTML content with an opening table tag
    html_content = '<table>\n'
    
    # Iterate over the rows
    for row in range(rows):
        html_content += '  <tr>\n'
        
        # Iterate over the columns
        for col in range(columns):
            index = row * columns + col
            if index >= len(videos):
                break
            video = videos[index]
            filepath = "{{ site.baseurl }}" + "/" + folder_path + "/" + video
            # Add the video tag to the table cell
            html_content += f'''    <td>
      <video controls style="height: {video_height}; width: {video_width};">
        <source src="{filepath}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>\n'''
        
        html_content += '  </tr>\n'
    
    # Close the table tag
    html_content += '</table>'
    
    return html_content

folder_path = 'assets/images/post_pics/an_unexpected_fractal'
identifier = 'fav'
rows = 6
columns = 3
h = w = f'{int(200*4/rows)}px'
max_width = h  # Adjust as needed
max_height = w  # Adjust as needed
html_code = generate_video_grid(folder_path, identifier, rows, columns)
print(html_code)
=======
    videos = [f for f in files if identifier in f]
    print(videos)
>>>>>>> 5d66c09 (whats happen in the profile)

    # Initialize the HTML content with an opening table tag
    html_content = '<table>\n'
    
    # Iterate over the rows
    for row in range(rows):
        html_content += '  <tr>\n'
        
        # Iterate over the columns
        for col in range(columns):
            index = row * columns + col
            if index >= len(videos):
                break
            video = videos[index]
            filepath = "{{ site.baseurl }}" + "/" + folder_path + "/" + video
            # Add the video tag to the table cell
            html_content += f'''    <td>
      <video autoplay loop controls style="height: {video_height}; width: {video_width};">
        <source src="{filepath}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>\n'''
        
        html_content += '  </tr>\n'
    
    # Close the table tag
    html_content += '</table>'
    
    return html_content

sys.exit()
folder_path = 'assets/images/post_pics/an_unexpected_fractal'
identifier = 'small_'
rows = 5
columns = 1
max_width = '200px'  # Adjust as needed
max_height = '200px'  # Adjust as needed
html_code = generate_image_grid(folder_path, identifier, rows, columns, max_width, max_height)
print(html_code)
