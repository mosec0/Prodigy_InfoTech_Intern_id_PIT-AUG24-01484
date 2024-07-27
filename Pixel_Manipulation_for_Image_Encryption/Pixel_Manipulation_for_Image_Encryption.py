from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image and convert it to a numpy array
    image = Image.open(image_path)
    image_data = np.array(image)
    
    # Apply encryption by adding the key to each pixel value
    encrypted_data = (image_data + key) % 256
    
    # Create a new image from the encrypted data and save it
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to: {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the image and convert it to a numpy array
    image = Image.open(image_path)
    image_data = np.array(image)
    
    # Apply decryption by subtracting the key from each pixel value
    decrypted_data = (image_data - key) % 256
    
    # Create a new image from the decrypted data and save it
    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to: {output_path}")

def main():
    print("Image Encryption and Decryption Program using Pixel Manipulation")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")
        return
    
    image_path = input("Enter the image path: ")
    output_path = input("Enter the output path: ")
    key = int(input("Enter the encryption key (integer): "))
    
    if mode == 'encrypt':
        encrypt_image(image_path, output_path, key)
    elif mode == 'decrypt':
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()
