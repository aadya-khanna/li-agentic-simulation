#!/usr/bin/env bash
# Optional pre-commit helper: block staging secrets and env files.
set -euo pipefail

BLOCKED=(
  ".env"
  ".env.local"
  "*.pem"
  "*credentials*"
)

for pattern in "${BLOCKED[@]}"; do
  if git diff --cached --name-only | grep -qE "${pattern//\*/.*}" 2>/dev/null; then
    echo "harness: blocked — attempted to commit sensitive file matching: $pattern"
    exit 1
  fi
done

# Block API key patterns in staged content (rough heuristic)
if git diff --cached | grep -qE '(sk-[a-zA-Z0-9]{20,}|GEMINI_API_KEY=[^[:space:]]+)'; then
  echo "harness: blocked — staged diff may contain API key material"
  exit 1
fi

exit 0
