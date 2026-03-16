file_path = "readfile.txt"

# try:
#     with open(file_path, 'r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print(f"Error: The file '{file_path}' was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

with open(file_path, 'r') as file:
    for i in file:
        print(i)
