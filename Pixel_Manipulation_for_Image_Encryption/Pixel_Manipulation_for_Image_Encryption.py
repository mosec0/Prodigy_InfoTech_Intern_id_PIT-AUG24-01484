from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_data = np.array(image, dtype=np.int32)

    # Encrypt the image by adding the key
    encrypted_data = image_data + key
    encrypted_image = Image.fromarray(np.clip(encrypted_data, 0, 255).astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_data = np.array(image, dtype=np.int32)

    # Decrypt the image by subtracting the key
    decrypted_data = image_data - key
    decrypted_image = Image.fromarray(np.clip(decrypted_data, 0, 255).astype('uint8'))
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
