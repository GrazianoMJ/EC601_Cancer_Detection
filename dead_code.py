# Previous code used to extract the training_text and put it in individual
# Documentation
with open("/home/grazianomj/Desktop/"+"training_text.txt", "r") as file:
    for line in file:
        if line == "ID,Text\n":
            continue
        else:
            temp = line.split(r"||")
            with open("/home/grazianomj/Desktop/training_docs/" +
                      "text{:04d}".format(int(temp[0])) +
                      ".txt", "w"
            ) as target:
                target.write(temp[1])
