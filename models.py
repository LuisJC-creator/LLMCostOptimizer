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
    latency_ms: float
    ok: bool = True
    error: str | None = None
    raw: dict | None = None

    def cost(self, config: ModelConfig) -> float:
        return (
            (self.prompt_tokens / 1_000_000) * config.cost_in_per_million
            + (self.completion_tokens / 1_000_000) * config.cost_out_per_million
        )