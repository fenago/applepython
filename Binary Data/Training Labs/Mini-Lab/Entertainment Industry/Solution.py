import struct

def extract_movie_info(binary_file):
    # Open the binary movie file
    with open(binary_file, 'rb') as f:
        # Extract information from the binary file using struct.unpack()
        runtime, resolution, file_size = struct.unpack('3i', f.read(12))
        return runtime, resolution, file_size

def convert_to_text(binary_file, text_file):
    # Extract information from the binary movie file
    runtime, resolution, file_size = extract_movie_info(binary_file)
    
    # Write the extracted information into a text file
    with open(text_file, 'w') as f:
        f.write('Runtime: {}\nResolution: {}\nFile size: {}'.format(runtime, resolution, file_size))

def convert_to_binary(text_file, binary_file):
    # Read the extracted information from the text file
    with open(text_file, 'r') as f:
        runtime = int(f.readline().split(': ')[1].strip())
        resolution = int(f.readline().split(': ')[1].strip())
        file_size = int(f.readline().split(': ')[1].strip())
    
    # Convert the text file back into the binary format using struct.pack()
    with open(binary_file, 'wb') as f:
        f.write(struct.pack('3i', runtime, resolution, file_size))
# Open the movie file in binary mode
with open("binary_file.mp4", "rb") as movie_file:
    # Read the binary data from the movie file
    movie_data = movie_file.read()

# Create a new binary file to store the movie data
with open("sample_movie.bin", "wb") as binary_file:
    # Write the binary data to the binary file
    binary_file.write(movie_data)
# Test the program with a sample movie file
binary_file = "sample_movie.bin"
text_file = "movie_info.txt"
convert_to_text(binary_file, text_file)
convert_to_binary(text_file, "sample_movie_converted.bin")
