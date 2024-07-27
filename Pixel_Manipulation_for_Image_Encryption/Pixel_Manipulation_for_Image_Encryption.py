from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, output_path, key):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return

    image_data = np.array(image)
    
    # Encrypting the image
    encrypted_data = (image_data + key) % 256
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    
    encrypted_image.save(output_path)
    print(f"Image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return

    image_data = np.array(image)
    
    # Decrypting the image
    decrypted_data = (image_data - key) % 256
    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    
    decrypted_image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    print("Image Encryption and Decryption Program using Pixel Manipulation")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter the image path: ").strip()
    output_path = input("Enter the output path: ").strip()
    key = int(input("Enter the encryption key (integer): ").strip())

    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return

    if mode == 'encrypt':
        encrypt_image(image_path, output_path, key)
    elif mode == 'decrypt':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
