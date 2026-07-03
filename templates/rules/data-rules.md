# Data Rules

## Classification Before Use

| Data Type | Examples | Allowed Use | External Transfer | Redaction/Tokenization | Retention |
|---|---|---|---|---|---|

## Default Rules

- Prefer synthetic, redacted, or tokenized data in demos.
- Do not send raw regulated data to external models unless architecture explicitly permits it.
- Record source, timestamp, and confidence for evidence.
- Make retention and deletion assumptions explicit.
- Treat unknown data permission as blocked until reviewed.
