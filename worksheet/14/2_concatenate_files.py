def concatenate_files(filename1, filename2, new_filename):
    with open(filename1) as f1, open(filename2) as f2, open(new_filename, "w") as f_out:
        contents1 = f1.read()
        contents2 = f2.read()
        f_out.write(contents1)
        f_out.write(contents2)