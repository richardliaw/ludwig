import os
import os.path


for name in ['training', 'testing']:
    with open(os.path.join('data','mnist_dataset_{}.csv'.format(name)), 'w') as output_file:
        print('=== creating {} dataset ==='.format(name))
        output_file.write('image_path,label\n')
        for i in range(10):
            path = os.path.join('data','mnist_png',name,str(i))
            for file in os.listdir(path):
                if file.endswith(".png"):
                    file_path = os.path.join(path, file)
                    file_path = os.path.abspath(file_path)
                    # for i in range(5):
                    output_file.write('{},{}\n'.format(file_path, str(i)))
