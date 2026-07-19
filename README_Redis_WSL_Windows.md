# Redis in WSL + Windows Verification

## Scenario
Redis is running inside **WSL (Ubuntu)** and your Django/Celery project is running on **Windows**.

---

## 1. Start Redis in WSL

Open a WSL terminal and run:

```bash
redis-server
```

You should see:

```text
Ready to accept connections tcp
```

**Keep this terminal open.** Do **not** press `Ctrl + C` while using Redis.

---

## 2. Open a New WSL Terminal

Do **not** stop the Redis server. Open another WSL terminal and verify Redis:

```bash
redis-cli ping
```

Expected output:

```text
PONG
```

---

## 3. Verify Redis from Windows

Open **PowerShell** and run:

```powershell
Test-NetConnection localhost -Port 6379
```

Expected output:

```text
TcpTestSucceeded : True
```

If it is `False`, Redis is not reachable from Windows.

---

## 4. Start Celery from Windows

```powershell
cd C:\python\celery
.\.venv\Scripts\Activate.ps1
python -m pip install celery redis
python -m celery -A celery_project worker -l info --pool=solo
```

---

## 5. Django Settings

```python
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
```

---

## Notes

- `redis-cli` is available inside WSL, not Windows PowerShell (unless separately installed on Windows).
- Keep the Redis server terminal running while Celery is using Redis.
- The `vm.overcommit_memory` warning is only a warning for development and does not prevent Redis from starting.
