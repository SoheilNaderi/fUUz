import requests
import threading

def fuzz_unicode_range(start, end):
    for code_point in range(start, end):
        if 0xD800 <= code_point <= 0xDFFF:
            continue
        try:
            fuzz_char = chr(code_point)
            url = f"http://{fuzz_char}27.0.0.1/"
            response = requests.get(url, timeout=2)
            if "ok" in response.text:
                print(f"Unicode Character: {fuzz_char} (U+{code_point:04X})")
        except (requests.RequestException, ValueError):
            pass

def fuzz_unicode_multithreaded(thread_count=10):
    threads = []
    unicode_range = 0x110000 // thread_count
    
    for i in range(thread_count):
        start = i * unicode_range
        end = (i + 1) * unicode_range if i < thread_count - 1 else 0x110000
        thread = threading.Thread(target=fuzz_unicode_range, args=(start, end))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    fuzz_unicode_multithreaded()
