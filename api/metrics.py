from prometheus_client import Counter, Gauge, Histogram, Summary

NAMESPACE = "crypto-payment-processor"

pending_creation_payment_methods_count = Gauge(
)

_HIGHR_BUCKETS = (
)
_LOWR_BUCKETS = (0.1, 0.5, 1.0, float("inf"))

http_requests_total = Counter(
)
http_request_size_bytes = Summary(
)
http_response_size_bytes = Summary(
)
http_request_duration_highr_seconds = Histogram(
)
http_request_duration_seconds = Histogram(
)
http_requests_inprogress = Gauge(
)
