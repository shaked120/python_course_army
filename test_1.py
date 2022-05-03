openfile = open("names.txt", 'r')
print(max(openfile.read().split()))

openfile1 = open("names.txt", 'r')
print(sum([len(i) for i in openfile1.read().split()]))

openfile2 = open("names.txt", 'r')
output_file = openfile2.read().split()
s = "\n"
print([i for i in output_file if i == min(output_file)])

openfile4 = open("names.txt", "r")
openfile3 = open("name_length.txt", 'w')
openfile3.write(str([len(i)-1 for i in openfile4]))

openfile5 = open("names.txt", "r")
print("Enter name length")
find_string = input()
print([i for i in openfile5 if len(find_string) == len(i)-1])



