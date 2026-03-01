COMMON_BEERGAME_CONTEXT = """
You are a supply chain agent helping me play a role-playing game.
The game has four players: retailer / wholesaler / distributor / factory.
All physical lead times are 2 weeks, except factory which has a 1 week lead time with the plant.
All information lag lead times are 2 weeks, except factory which has a 1 week information lag lead time with the plant.
The holding cost is $0.5 per case per week and the backorder cost is $1 per case per week.
There is a steady demand of 4 cases each week, so the pipeline is fully loaded with 4 cases at every stage.
The starting inventory position is 12 cases.
Each week the user will give you the downstream customer’s demand.
The user can override your recommendation.
""".strip()

QUALITATIVE_SYSTEM_INSTRUCTION = (
    "Prioritize plain-language coaching about the ordering direction and decision logic."
)

QUANTITATIVE_SYSTEM_INSTRUCTION = (
    "Prioritize a concrete order recommendation grounded in explicit calculations."
)

qualitative_beergame_prompt = (
    f"{COMMON_BEERGAME_CONTEXT}\n\n"
    f"Mode emphasis: {QUALITATIVE_SYSTEM_INSTRUCTION}"
)

quantitative_beergame_prompt = (
    f"{COMMON_BEERGAME_CONTEXT}\n\n"
    f"Mode emphasis: {QUANTITATIVE_SYSTEM_INSTRUCTION}"
)

STRUCTURED_OUTPUT_COMMON_INSTRUCTION = (
    "Return ONLY valid JSON (no markdown, no extra text) with exactly these keys: "
    "quantitative_reasoning, qualitative_reasoning, short_quantitative_reasoning, "
    "short_qualitative_reasoning, quantitative_answer, qualitative_answer. "
    "Process requirements in this exact order: "
    "1) Compute quantitative_reasoning first using explicit mathematical steps and assumptions. "
    "2) Produce quantitative_answer as the exact final order quantity from that math. "
    "3) Translate the quantitative reasoning into qualitative_reasoning (plain language, no equations). "
    "4) Produce qualitative_answer as a directional recommendation consistent with the quantitative result, but without exact numbers. "
    "If information is missing, make explicit assumptions in reasoning but still provide one exact integer in quantitative_answer."
)

QUANTITATIVE_OUTPUT_INSTRUCTION = (
    "For quantitative fields: quantitative_reasoning can include explicit calculations and "
    "quantitative_answer must be ONE exact integer only (for example: 12), with no words or units."
)

QUALITATIVE_OUTPUT_INSTRUCTION = (
    "For qualitative fields: qualitative_reasoning must avoid equations and express the same logic in plain language. "
    "qualitative_answer must convey the same recommendation direction as quantitative_answer but must not include digits. "
    "short_quantitative_reasoning and short_qualitative_reasoning should each be concise (1-2 sentences)."
)


def build_structured_output_instruction(mode_key: str) -> str:
    if mode_key == "BeerGameQuantitative":
        mode_specific = "Mode emphasis: keep quantitative sections especially direct and calculation-first."
    else:
        mode_specific = "Mode emphasis: keep qualitative sections especially clear, actionable, and non-technical."

    return " ".join(
        [
            STRUCTURED_OUTPUT_COMMON_INSTRUCTION,
            QUANTITATIVE_OUTPUT_INSTRUCTION,
            QUALITATIVE_OUTPUT_INSTRUCTION,
            mode_specific,
        ]
    )

