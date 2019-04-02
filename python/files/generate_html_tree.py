import subprocess

def read_tree(dir_to_output, output_file):
    '''Execute `tree` command to output HTML with colors. Filter out the
    noise and keep the essential part as a template to be included in
    `tree.html`.'''
    subprocess.run(f'tree -C -H . {dir_to_output} > tree.txt', shell=True)
    body = False
    extracted_tree = []
    with open('tree.txt') as f:
        for line in f:
            if not body:
                if '<body>' in line:
                    body = True
            else:
                if '</body>' in line:
                    break
                extracted_tree.append(line)
    with open(output_file, 'w') as f:
        for line in extracted_tree:
            f.write(line)
