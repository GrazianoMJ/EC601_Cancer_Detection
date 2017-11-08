import zipfile 

MAIN_DIR = "/home/grazianomj/Desktop/"
FILE_DIR = "training_docs/"

def main():
    with zipfile.ZipFile(MAIN_DIR+"test_dir.zip", "w") as zf:
        for i in range(0, 50):
            text_file = "text{0:04d}.txt".format(i)
            zf.write(MAIN_DIR+FILE_DIR+text_file, 
                     arcname=text_file
            )

if __name__ == '__main__':
    main()
