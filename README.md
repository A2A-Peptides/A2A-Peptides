# A2A Peptides — the first agentic commerce hub for peptides in 35 countries

Agent-to-Agent (A2A) + Model Context Protocol (MCP) hub for peptides.

The Agent-to-Agent (A2A) surface for peptides, served over the Model Context Protocol (MCP) — the record, a registry for security, and x402 to pay on it. AI agents for authorized trading partners. Not marketing. Not advertising. Operated by GreenCore Solutions Corp.

- Six frontier AI labs in the build — Anthropic, OpenAI, Google, Perplexity, xAI, Mistral — 10K agent requests a day.
- 5,301 peptide products.
- 24,694 licensed peptide providers.
- 35 countries — runs on Cloudflare, Amazon, Microsoft and Google hyperscalers.
- First agentic commerce hub for peptides on the Model Context Protocol (MCP) registry.

**Connect:** `https://mcp.a2a-peptides.ai/mcp` — streamable-HTTP, no adapter. Hub: https://a2a-peptides.ai/ · [llms.txt](https://a2a-peptides.ai/llms.txt) · [Agent Card](https://a2a-peptides.ai/.well-known/agent-card.json)

## Connect kit

Agent-to-Agent (A2A) + Model Context Protocol (MCP) hub for peptides. AI agents for authorized trading partners. Not marketing. Not advertising. Operated by GreenCore Solutions Corp.

| | |
|---|---|
| Hub | https://a2a-peptides.ai/ · [setup](https://a2a-peptides.ai/setup) · [docs](https://a2a-peptides.ai/docs) · [llms.txt](https://a2a-peptides.ai/llms.txt) |
| MCP door of record | `https://mcp.a2a-peptides.ai/mcp` — <!-- door:begin -->streamable-HTTP, stateless, server name `a2a-peptides`, door version 1.6.5, 20 tools (read from the wire 2026-09-19)<!-- door:end --> |
| A2A endpoint | `https://<hostname>/a2a` on every agent — A2A 0.3.0 JSON-RPC, `message/send` and `tasks/get`; the preferred interface on every card |
| Agent Card | https://a2a-peptides.ai/.well-known/agent-card.json — signed ES256, kid `a2ap-2026-09` |
| Keyring | https://a2a-peptides.ai/.well-known/jwks.json |
| Issuer | https://peptides-registry.ai/.well-known/oauth-authorization-server — client-credentials Bearer for the transacting skills; reads need none |
| Auditor Port | https://audit.a2a-peptides.ai/packs/index.json — the public index of sealed review packs |
| Registry | namespace `io.github.A2A-Peptides` (the registry grants the GitHub login case), server `a2a-peptides` — [server.json](server.json) |
| Family | hub · peptides-registry.ai (registry) · peptides-x402.ai (payments door) · a2a-pharma.ai (pharma gate) · peptides-usa.ai (first tenant) |

## Agents (A2A)

Every agent lives at its own hostname and answers two addresses: `https://<hostname>/.well-known/agent-card.json` (the signed card) and `https://<hostname>/a2a` (A2A 0.3.0 JSON-RPC: `message/send`, `tasks/get`). There is no inference behind the endpoint. A DataPart `{"skill": ..., "params": {...}}` runs the gate chain on the door — `resolve_jurisdiction` → `resolve_actor` → `gate_transaction` — and then the skill; the artifact carries the result, the notice, the resolved jurisdiction and the rule-set version. A plain text part gets the deterministic skill list with each input schema. A text part whose text is a JSON object with a `skill` key is read as the same `{skill, params}` request, so text-only clients can send structured requests too. Transacting skills take the issuer's Bearer; without it the answer is `DENY_UNLICENSED_AGENT`.

<!-- agents:begin -->
| Role | Hostname | Agents | Region |
|---|---|---|---|
| Hub (concierge) | a2a-peptides.ai | 1 | South Central US |
| Registry (token questions) | peptides-registry.ai | 1 | South Central US |
| Payments door (receipt questions) | peptides-x402.ai | 1 | South Central US |
| Country agents | country code + .a2a-peptides.ai (the United Kingdom is uk; the European Union level is eu) | 36 | South Central US |
| Actor-class entry points | pharmacy · prescriber · wholesaler · brand + .a2a-peptides.ai | 4 | South Central US |
| Pharma gate | a2a-pharma.ai | 1 | South Central US |
| Handoff (referral only) | handoff.a2a-peptides.ai | 1 | South Central US |
| Enforcement watch | watch.a2a-peptides.ai | 1 | South Central US |
| Auditor Port | audit.a2a-peptides.ai | 1 | South Central US |
| Tenant concierge | peptides-usa.ai | 1 | South Central US |
| State and territory agents | us- + state or territory code + .peptides-usa.ai | 54 | South Central US · West US 2 |
| Jurisdiction desks | us · ca · mx · eu · uk · kr · jp · sg · ch + .peptides-usa.ai | 9 | South Central US |

111 agents live, 36 product-line slots reserved on the tenant table; by region: South Central US 97 · West US 2 14. Counted from the hub's `list_agents` on 2026-09-19; door version 1.6.5, 20 tools.
<!-- agents:end -->

Human-readable text on every card says UK; the machine field carries the ISO code. A country agent's hostname is the country code in lower case (the United Kingdom is `uk`, Germany is `de`, and the European Union level is `eu`) before `.a2a-peptides.ai`.

## The gate

Three calls come before any price, availability, order or handoff: `resolve_jurisdiction` → `resolve_actor` → `gate_transaction`. The gate returns `allow`, `deny` or `require_rx` with a frozen reason code and the version of the rule set it read; both travel on every downstream receipt, including x402 settlement receipts.

Jurisdictions: United States · Canada · Mexico · European Union (member as parameter) · UK · Korea · Japan · Singapore · Switzerland. Actors: authorized trading partner and its members (manufacturer, repackager, wholesale distributor, dispenser, third-party logistics provider; cosmetic responsible person and natural-health-product licence holder on the non-drug pathways) · prescriber · patient and public (referral classes) · agent (inherits the class of the credential it presents; none returns `DENY_UNLICENSED_AGENT`).

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

## Auditor Port

`audit.a2a-peptides.ai` is prepared for independent review: a read-only agent with seven skills (list_agents, get_pack_index, get_pack, verify_receipt, get_rule_set_versions, get_azure_posture, get_audit_log) and no transacting skill.
Review packs are sealed with a signed manifest (SHA-256 per file, a pack hash) and listed on a public index; a pack is never overwritten, later packs sit beside the old.
Pack contents and the audit log take an auditor credential; auditor credentials are issued by the operator only, time-boxed, and every call made with one is written to the audit log.
The port is review-ready as served; it makes no claim beyond what is on the wire.

## The first tenant

The first tenant, peptides-usa.ai, has its agents on the wire today — a concierge, fifty-four state and territory agents, nine jurisdiction desks — and they answer every read and gate skill. Order intake for the tenant opens when a sourced licence is on the record; until then `create_order_intent` scoped to the tenant answers `DENY_EXPIRED_LICENCE` together with the licensed-destination referral.

## Connect

Any client that speaks streamable-HTTP MCP connects with the URL alone:

```json
{ "url": "https://mcp.a2a-peptides.ai/mcp", "transport": "streamable-http" }
```

Stock client paths, no adapter — see [examples/](examples/):

- [`examples/generic_mcp_client.py`](examples/generic_mcp_client.py) — the reference MCP Python client
- [`examples/aws_strands.py`](examples/aws_strands.py) — Strands Agents `MCPClient`
- [`examples/azure_semantic_kernel.py`](examples/azure_semantic_kernel.py) — Semantic Kernel `MCPStreamableHttpPlugin`
- [`examples/google_genai.py`](examples/google_genai.py) — google-genai with the door's tools as function declarations
- [`examples/a2a_google_sdk.py`](examples/a2a_google_sdk.py) — a2a-sdk against a country agent: card, signature, one read, the refusal
- [`examples/a2a_aws_strands.py`](examples/a2a_aws_strands.py) — Strands Agents `A2AClientToolProvider`, the same exchange
- [`examples/a2a_azure_agent_framework.py`](examples/a2a_azure_agent_framework.py) — Microsoft Agent Framework `A2AAgent`, the same exchange

Sample cards as served on the day of the cut: [`agent-card.sample.json`](agent-card.sample.json) (hub), [`agent-card.country.sample.json`](agent-card.country.sample.json) (one country agent), [`agent-card.audit.sample.json`](agent-card.audit.sample.json) (the Auditor Port). Always read the live card; it is signed and the signature verifies against the live keyring.

## Credentials and settlement

Reads need no authentication. An agent that transacts presents a credential issued to a licensed party by the issuer at peptides-registry.ai. Registry-truth tools are metered by x402; `create_order_intent` settles by x402 (USDC on Base); receipts are signed and carry `reason_code` and `rule_set_version`.

## Contact

Registry contact for every listing this hub files: `mcp@a2a-peptides.ai`. Human door: the form at https://a2a-peptides.ai/#contact.

MIT licence — see [LICENSE](LICENSE).
