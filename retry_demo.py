from tenacity import retry, stop_after_attempt

attempt_count = 0

@retry(stop=stop_after_attempt(5))
def unstable_api_call():
    global attempt_count
    attempt_count += 1
    print(f"Trying... (attempt {attempt_count})")
    if attempt_count < 4:
        raise ValueError("Oops")
    print("Success!")

unstable_api_call()
