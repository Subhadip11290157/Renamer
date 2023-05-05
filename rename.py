import os
def main():
	idx = 1
	pwd = os.getcwd()
	folder_path = pwd.replace("\\", "//") + "//folder//"
	for file_name in os.listdir(folder_path):
		if(file_name=="readme.md"):
			continue
		dest_file = "pic" + str(idx) + ".jpg"
		source_file = folder_path + file_name
		dest_file = folder_path + dest_file
		os.rename(source_file, dest_file)
		idx += 1
# Driver Code
if __name__ == '__main__':
	main()