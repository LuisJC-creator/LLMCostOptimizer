# LLM Optimizer

By **Luis Chavez**

## What it is

A router that reroutes expensive LLM requests to cheaper/simpler models when the
cheaper model is sufficient, falling back to the expensive one when it isn't.
The foundation (Phase 1) is a **unified model interface**: call any model, local
Ollama, or a hosted API through one `send_request(config, prompt) -> Response`
function.

See [`docs/plan.md`](docs/plan.md) for the full architecture and build order.

## Structure

- `main.py` — current entry point. a POST request to a local Ollama model, being
  refactored into the `send_request` adapter (in-progress)
- `docs/plan.md` — phased plan, the `ModelConfig` and `Response` contracts.
- `docs/Documentation.md` — session log / development journal.
- `docs/ai_questions.md` — record of prompts asked to AI while building.

## Documentation & AI transparency

This project treats its documentation as a first-class deliverable, with a
deliberate focus on **how AI was used** during development and attempts to provide 
guidelines while exploring generative AI use:

- **`ai_questions.md`** logs the prompts asked to AI, in order — including the
  throwaway ones — for an honest record of what was consulted.
- **`Documentation.md`** journals each session: what was attempted, what broke,
  and for each AI answer whether it was **used, adapted, or rejected**.
- An **`[AI]` / `[LC]`** attribution convention marks which lines were written by
  the AI assistant versus by Luis Chavez.

The intent is a transparent build log where AI is a documented tool, and where 
reaching the middleground of efficiency while building a strong understanding
of the foundations is the goal.
