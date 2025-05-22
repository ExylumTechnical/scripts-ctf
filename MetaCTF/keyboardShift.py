## Used in the May 2025 flash ctf after the writeups were released

import sys
# Define keyboard rows as pairs: (unshifted, shifted)
KEYBOARD_ROWS = [
    ("`1234567890-=", "~!@#$%^&*()_+"),
    ("qwertyuiop[]\\", "QWERTYUIOP{}|"),
    ("asdfghjkl;'", "ASDFGHJKL:\""),
    ("zxcvbnm,./", "ZXCVBNM<>?")
]

def build_shift_maps():
    left_shift = {}
    right_shift = {}

    for row_unshifted, row_shifted in KEYBOARD_ROWS:
        # Handle unshifted row
        for i, c in enumerate(row_unshifted):
            if i > 0:
                left_shift[c] = row_unshifted[i - 1]
            if i < len(row_unshifted) - 1:
                right_shift[c] = row_unshifted[i + 1]

        # Handle shifted row
        for i, c in enumerate(row_shifted):
            if i > 0:
                left_shift[c] = row_shifted[i - 1]
            if i < len(row_shifted) - 1:
                right_shift[c] = row_shifted[i + 1]

    return left_shift, right_shift

LEFT_SHIFT_MAP, RIGHT_SHIFT_MAP = build_shift_maps()

def keyboard_shift_decode(text, direction="left"):
    shift_map = LEFT_SHIFT_MAP if direction == "left" else RIGHT_SHIFT_MAP
    return ''.join([shift_map.get(c, c) for c in text])

# Example usage
try:
	print("[*] Trying left shift:")
	print(keyboard_shift_decode(ciphertext, direction="left"))

	print("\n[*] Trying right shift:")
	print(keyboard_shift_decode(ciphertext, direction="right"))
except:
	print("Expected usage keyboardShift.py finger-fumbled-string")
