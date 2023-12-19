import os

def create_dummy_file(file_size_mb):
    file_size_mb = int(file_size_mb)

    file_size_bytes = file_size_mb * 1024 * 1024

    dummy_data = bytearray(b'\x00' * file_size_bytes)

    with open('dummy.txt', 'wb') as file:
        file.write(dummy_data)

    print(f"Dummy file 'dummy.txt' created with size {file_size_mb} megabytes.")

if __name__ == "__main__":
    desired_file_size_mb = input("How many MEGABYTES do you want the file to be (1024MB = 1GB): ")

    create_dummy_file(desired_file_size_mb)
