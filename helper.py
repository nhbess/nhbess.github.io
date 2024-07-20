import os


def rename_files(folder_path):
    for count, filename in enumerate(os.listdir(folder_path)):
        post_name = folder_path.split("\\")[-1]
        print(post_name)
        dst = folder_path + "\\" + str(count) + ".jpg"
        dst = f'{count}.jpg'
        src = folder_path + "\\" + filename
        print(src, dst)
        os.rename(src, dst)


folder_path = 'An unexpected fractal'
rename_files(folder_path)
import os
import sys
sys.exit()
import os

def generate_image_grid(folder_path, rows, columns, max_width='200px', max_height='200px'):
    # List all files in the specified folder
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # HTML string to store the result
    html_content = '<table>\n'
    
    for row in range(rows):
        html_content += '  <tr>\n'
        for col in range(columns):
            index = row * columns + col
            if index >= len(images):
                break
            image = images[index]
            html_content += '    <td><img src="{}/{}" alt="Image {}" style="max-width: {}; max-height: {}; width: 100%; height: auto;"></td>\n'.format(
                folder_path, image, index + 1, max_width, max_height)
        html_content += '  </tr>\n'
    
    html_content += '</table>'
    
    return html_content


# Example usage
folder_path = 'assets/images/post_pics/An unexpected fractal'
rows = 5
columns = 4
max_width = '200px'  # Adjust as needed
max_height = '200px'  # Adjust as needed
html_code = generate_image_grid(folder_path, rows, columns, max_width, max_height)
print(html_code)

