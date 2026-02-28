For your FastAPI user service, we define:

🔹 SLI (Service Level Indicators)

SLI	Meaning
Latency >	Response time
Traffic	> Throughput
Errors	> 5xx
Saturation	> Resource usage (CPU, memory later)

-------------------------------------------

install from prometheus_fastapi_instrumentator import Instrumentator

get metrics at > http://127.0.0.1:8000/metrics


final architecture

```bash
Browser
   ↓
FastAPI (8000)
   ↓
MongoDB (27017)
   ↓
Prometheus (9090)
   ↓
Grafana (3000)
```

### send traffic to search

```bash
for /L %i in (1,1,1000) do curl -X POST http://localhost:8000/search -d "username=user1"
```
