# A2A Peptides — connect kit

The agentic hub for the peptide industry — Agent-to-Agent (A2A) and Model Context Protocol (MCP), on cleared rails. Operated by GreenCore Solutions Corp.

A2A Peptides is a jurisdiction-and-pathway gate that only exposes items cleared to transact, with a catalogue behind it that only holds what passed. Research-use stock is a reject class the door names and refuses. Every field on every record carries its source page, its reader and its state; counts are produced from records at request time, never typed.

| | |
|---|---|
| Hub | https://a2a-peptides.ai/ · [setup](https://a2a-peptides.ai/setup) · [docs](https://a2a-peptides.ai/docs) · [llms.txt](https://a2a-peptides.ai/llms.txt) |
| MCP door of record | `https://mcp.a2a-peptides.ai/mcp` — streamable-HTTP, stateless, server name `a2a-peptides`, twenty tools at v1.0 |
| Agent Card | https://a2a-peptides.ai/.well-known/agent-card.json — signed ES256, kid `a2ap-2026-09` |
| Keyring | https://a2a-peptides.ai/.well-known/jwks.json |
| Registry | namespace `io.github.A2A-Peptides` (the registry grants the GitHub login case), server `a2a-peptides` — [server.json](server.json) |
| Family | peptides-registry.ai (registry) · peptides-x402.ai (payments door) · peptides-usa.ai (declared-virtual showcase tenant) |

## The gate

Three calls come before any price, availability, order or handoff: `resolve_jurisdiction` → `resolve_actor` → `gate_transaction`. The gate returns `allow`, `deny` or `require_rx` with a frozen reason code and the version of the rule set it read; both travel on every downstream receipt, including x402 settlement receipts.

Jurisdictions: US · CA · MX · EU (member as parameter) · GB. Actors: patient · prescriber · pharmacy or 503B · wholesaler · cosmetic brand · retailer · agent (must present a credential; none returns `DENY_UNLICENSED_AGENT`).

## The twenty tools

| Group | Tools |
|---|---|
| Gate (3) | resolve_jurisdiction · resolve_actor · gate_transaction |
| Regulatory truth (5) | get_substance_record · get_pathway_status · get_compounding_eligibility · get_label_and_indication · get_enforcement_watch |
| Cleared catalogue (3) | search_cleared_items · get_item · compare_presentations |
| Licensed supply (3) | find_licensed_supplier · get_availability · get_price |
| Quality (2) | get_lot_coa · verify_serialization |
| Commerce (2) | create_order_intent · a2a_handoff |
| Operations (2) | get_safety_label · log_audit |

## Connect

Any client that speaks streamable-HTTP MCP connects with the URL alone:

```json
{ "url": "https://mcp.a2a-peptides.ai/mcp", "transport": "streamable-http" }
```

Stock client paths, no adapter — see [examples/](examples/):

- [`examples/generic_mcp_client.py`](examples/generic_mcp_client.py) — the reference MCP Python client
- [`examples/aws_strands.py`](examples/aws_strands.py) — Strands Agents `MCPClient`
- [`examples/azure_semantic_kernel.py`](examples/azure_semantic_kernel.py) — Semantic Kernel `MCPStreamableHttpPlugin`
- [`examples/google_genai.py`](examples/google_genai.py) — google-genai with an MCP `ClientSession` as a tool

The Agent Card sample in this kit is the card as served on the day of the cut: [`agent-card.sample.json`](agent-card.sample.json). Always read the live card; it is signed and the signature verifies against the live keyring.

## Credentials and settlement

Reads need no authentication. An agent that transacts presents a credential issued to a licensed party. Registry-truth tools are metered by x402; `create_order_intent` settles by x402 (USDC on Base); receipts are signed and carry `reason_code` and `rule_set_version`.

## Contact

Registry contact for every listing this hub files: `mcp@a2a-peptides.ai`. Human door: the form at https://a2a-peptides.ai/#contact.

MIT licence — see [LICENSE](LICENSE).
