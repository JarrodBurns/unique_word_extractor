
#@  Change to input when done  @#
try:
    input_file_name = input("Enter file name: ")
    output_file_name = input("Enter name of file to be created: ")

    with open(input_file_name) as file_handle:
        word_list = [line.lower().strip().split() for line in file_handle]

    count = 0
    super_list = []

    for i in word_list:
        super_list = i + super_list

    no_dupes = list(set(super_list))
    no_dupes.sort()

    with open(output_file_name, "w") as new_file:

        for i in no_dupes:
            count += 1
            new_file.writelines(i)
            new_file.write("\n")

    #@  add file input & output names to the console log  @#
    count_format = "{:,}".format(count)
    print(f"Returned {count_format} individual words in: {input_file_name}\n"
          f"Unique words saved to file: {output_file_name}")

except FileNotFoundError:
    print("File not found. Restart to continue.")
