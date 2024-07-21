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



def generate_image_grid(folder_path, rows, columns, max_width='200px', max_height='200px'):
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    html_content = '<table>\n'
    for row in range(rows):
        html_content += '  <tr>\n'
        for col in range(columns):
            index = row * columns + col
            if index >= len(images):
                break
            image = images[index]
            print(image)
            filepath = f'{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/{image}'
            html_content += f'    <td><img src="{filepath}" alt="Image {index}" style="max-width: {max_width}; max-height: {max_height}; width: 100%; height: auto;"></td>\n'
        html_content += '  </tr>\n'
    
    html_content += '</table>'
    
    return html_content

# Example usage
folder_path = 'assets\\images\\post_pics\\an_unexpected_fractal'
rows = 5
columns = 4
max_width = '200px'  # Adjust as needed
max_height = '200px'  # Adjust as needed
html_code = generate_image_grid(folder_path, rows, columns, max_width, max_height)
print(html_code)

