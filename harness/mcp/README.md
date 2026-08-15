# MCP servers (planned)

MCP tools populate the agent prompt — keep descriptions tight and trusted. See `harness/tools/registry.yaml` for bash equivalents until these exist.

## villa-logs (sketch)

**Purpose:** Read experiment tape without loading full files into context.

| Tool | Description |
|------|-------------|
| `list_events` | Filter `run.jsonl` by day, kind, actor |
| `get_state` | Return `run-state.json` summary |
| `contact_matrix` | Talk/whisper counts from checkpoint |

**Spec:** `harness/mcp/villa-logs.json`

## villa-run (sketch)

**Purpose:** Trigger stub seasons from an agent session (sandbox only).

| Tool | Description |
|------|-------------|
| `run_stub` | `--days N`, returns log path + event count |
| `validate` | Shell out to `./harness/hooks/validate.sh` |

## Wiring (when implemented)

Add to Cursor MCP config or Claude Code settings pointing at the server entrypoint. Do not install untrusted MCP descriptions — they are prompt injection surface.
