from prometheus_client import Counter, Histogram

# 1. Contador de peticiones por endpoint y método
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Número total de peticiones HTTP",
    ["method", "endpoint"]
)

# 2. Histograma de latencias
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Duración de las peticiones HTTP",
    ["method", "endpoint"],
    buckets=[0.1, 0.3, 1, 2.5, 5, 10]
)

# 3. Contador de errores
ERROR_COUNT = Counter(
    "http_request_errors_total",
    "Errores HTTP (status >= 400)",
    ["method", "endpoint", "status_code"]
)
