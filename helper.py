import os


def rename_files(folder_path):
    for count, filename in enumerate(os.listdir(folder_path)):
        dst = folder_path + "\\" + str(count) + ".jpg"
        src = folder_path + "\\" + filename
        os.rename(src, dst)



import os

def generate_image_grid(folder_path, rows, columns, max_width='200px', max_height='200px'):
    # List all files in the specified folder
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # HTML string to store the result
    html_content = '<div style="display: grid; grid-template-columns: repeat({}, 1fr); gap: 10px;">\n'.format(columns)
    
    for index, image in enumerate(images):
        if index >= rows * columns:
            break
        html_content += '  <img src="{}/{}" alt="Image {}" style="width: 100%; max-width: {}; max-height: {}; object-fit: cover;">\n'.format(
            folder_path, image, index + 1, max_width, max_height)
    
    html_content += '</div>'
    
    return html_content

# Example usage
folder_path = 'assets\images\post_pics\An unexpected fractal'
rows = 5
columns = 4
max_width = '200px'  # Adjust as needed
max_height = '200px'  # Adjust as needed
html_code = generate_image_grid(folder_path, rows, columns, max_width, max_height)
print(html_code)

