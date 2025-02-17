import requests

def fuzz_unicode():
    for code_point in range(1, 0x110000):
        if 0xD800 <= code_point <= 0xDFFF:
            continue
        try:
            fuzz_char = chr(code_point) 
            url = f"http://127{fuzz_char}0.0.1/"
            response = requests.get(url, timeout=2)
            if "ok" in response.text:
                print(f"Unicode Character: {fuzz_char} (U+{code_point:04X})")
        except (requests.RequestException, ValueError):
            pass

if __name__ == "__main__":
    fuzz_unicode()