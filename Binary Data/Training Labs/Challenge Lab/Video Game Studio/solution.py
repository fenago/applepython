import struct

# Open binary game file in read mode
with open("binary_game.bin", "rb") as binary_file:
    # Extract information from binary file using struct module
    # The format specifier '32s 32s I' represents two strings of length 32 bytes each and an integer value
    title, publisher, release_date = struct.unpack('32s 32s I', binary_file.read(68))
    # Decode the binary data into text and strip trailing whitespaces
    title = title.decode().strip()
    publisher = publisher.decode().strip()

# Open text file in write mode
with open("game_info.txt", "w") as text_file:
    # Write extracted information into text file
    text_file.write('Title: {}\nPublisher: {}\nRelease Date: {}'.format(title, publisher, release_date))

# Open text file in read mode
with open("game_info.txt", "r") as text_file:
    # Read the file content
    data = text_file.readlines()
    # Extract information from text file
    title = data[0].strip().split(': ')[1]
    publisher = data[1].strip().split(': ')[1]
    release_date = int(data[2].strip().split(': ')[1])
    # Pad the title and publisher with spaces to 32 bytes
    title = title.ljust(32, ' ')
    publisher = publisher.ljust(32, ' ')
    # Pack the title, publisher, and release date into binary data
    binary_data = struct.pack('32s 32s I', title.encode(), publisher.encode(), release_date)

# Open binary file in write mode
with open("binary_game_converted.bin", "wb") as binary_file:
    # Write the binary data
    binary_file.write(binary_data)
