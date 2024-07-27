def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift - shift_base) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")
        return
    
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
