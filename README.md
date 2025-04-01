# ROT13 Encryption

1. **str.maketrans** creates a translation table to replace characters in a string.
2. **The first argument** is the list of original characters: all lowercase followed by all uppercase ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ').

3. **The second argument** is the list of replacement characters:
    - For lowercase (string.ascii_lowercase):
    string.ascii_lowercase[13:] takes the letters from the 13th position onwards ('nopqrstuvwxyz').
    string.ascii_lowercase[:13] takes the first 13 letters ('abcdefghijklm').
    Concatenating them gives: 'nopqrstuvwxyzabcdefghijklm' (ROT13 for lowercase).
    - For uppercase (string.ascii_uppercase):
    Same logic: string.ascii_uppercase[13:] ('NOPQRSTUVWXYZ') + string.ascii_uppercase[:13] ('ABCDEFGHIJKLM') → 'NOPQRSTUVWXYZABCDEFGHIJKLM' (ROT13 for uppercase).

```bash
# Encryption
message = "Hello World!"
encrypted = rot13(message)
print(encrypted) # Output: "Pvnb Zbaqb!"

# Decryption (same function)
decrypted = rot13(encrypted)
print(decrypted) # Output: "Hello World!"
```

To see how rot13 encryption works see here [ROT13 Encryption](https://github.com/RykerWilder/notes/blob/main/ROT-13.md).