from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_data = np.array(image)

    # Ensure the key is in the valid range for uint8
    key = key % 256

    # Encrypt the image by adding the key and applying modulo 256
    encrypted_data = (image_data + key) % 256
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_data = np.array(image)

    # Ensure the key is in the valid range for uint8
    key = key % 256

    # Decrypt the image by subtracting the key and applying modulo 256
    decrypted_data = (image_data - key) % 256
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter the image path: ").strip()
    output_path = input("Enter the output path: ").strip()
    key = int(input("Enter the encryption key (integer): ").strip())

    if mode == "encrypt":
        encrypt_image(image_path, output_path, key)
    elif mode == "decrypt":
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
