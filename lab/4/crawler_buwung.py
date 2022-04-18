a = input("Masukkan nama file input:")
b = input("Masukkan nama file output:")

file_input = open(a, "r")
file_output = open(b, "w")
new_str = ''
hashtag = 0
mention = 0
url = 0


for line_str in file_input: 
    line_str = line_str.strip() # get rid of carriage return (newline)
    word_list = line_str.split() 
    for word in word_list: 
        if word[0] == "@":
            mention += 1
            new_str += "(M) "
        
        elif word[0] == "#":
            mention += 1
            new_str += "(H) "
        
        elif word[0:4] == "www.":
            mention += 1
            new_str += "(U) "
        
        else:
            new_str += word + " "
        
    new_str += "\n"
    
file_output.write(new_str)
file_output.write("#########\n")
print("Mention : ", mention, file=file_output)
print("Hashtag : ", hashtag, file=file_output)
print("Url : ", url, file=file_output)