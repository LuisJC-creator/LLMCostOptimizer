from dataclasses import dataclass

@dataclass
class ModelConfig:
    name: str
    provider: str
    model: str
    base_url: str
    tier: str
    cost_in_per_million: float
    cost_out_per_million: float
    api_key: str | None = None # for llama testing.
    max_tokens: int = 1000
    timeout: int = 60

@dataclass
class Response:
    text: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    cost: float
    latency_ms: float
    ok: bool = True
    error: str | None = None
    raw: dict | None = None

