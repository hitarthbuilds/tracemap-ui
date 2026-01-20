import time
import requests

BASE_URL = "https://tracemap-backend-production.up.railway.app"

def submit_trace(code: str) -> dict:
    r = requests.post(
        f"{BASE_URL}/v1/trace",
        json={"code": code},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()

def poll_trace(job_id: str, timeout_s: int = 10) -> dict:
    start = time.time()
    while time.time() - start < timeout_s:
        r = requests.get(f"{BASE_URL}/v1/trace/{job_id}")
        r.raise_for_status()
        data = r.json()
        if data["status"] == "done":
            return data
        time.sleep(0.5)
    raise TimeoutError("Trace execution timed out")
