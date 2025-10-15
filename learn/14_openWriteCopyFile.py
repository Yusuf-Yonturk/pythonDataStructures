with open("./src/example1.txt","r") as philoLine:
    sequence=philoLine.read()
    philoLine.seek(0)
    lines=philoLine.readlines(40)
    print(sequence)
    print(lines)

with open("./src/example1.txt","w") as philoDoc:
     philoDoc.write("\nYusuf")
     philoDoc.write("Yonturk")
with open("./src/source.txt","r") as source_file:
    with open("./src/destination.txt","w") as destination_file:
        for line in source_file:
            destination_file.write(line)

