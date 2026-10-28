# Retrieval review: source-11

Index: `workspace/source-11/index/knowledge.sqlite3` (10 chunks, text-embedding-3-small, 512 dims, top_k 5).
All evidence below comes from the saved search files; full sources were not read to supplement it.
Cosine scores are similarities, not confidence probabilities.

## Summary

| id | answerable | search file | best supporting chunk (rank) | verdict |
|---|---|---|---|---|
| q1 | yes | search-35c90b4f74da.json | current-guide Access and equipment (#4) | Found, but **historical rule ranked higher (#2)** |
| q2 | yes | search-7099c665c182.json | current-guide Normal departure sequence (#1) | Found at top |
| q3 | yes | search-5a060a506aea.json | previous-policy Terms before 2026-09-01 (#1) | Found at top |
| q4 | yes | search-761877b2c674.json | operational-record CASE-EXIT-214 (#1) + Exceptions (#2) | Found at top, both parts |
| q5 | no | search-857ae8947b7b.json | none | Correctly unsupported; abstain |

## q1: How many business days does a departing employee have to return Nimbus equipment under the current guide?

| rank | chunk | cosine | version / status | relevance | supports answer? |
|---|---|---|---|---|---|
| 1 | source-11-current-guide:0-306:13a089e8 | 0.6775 | 2026.2 / null | Title, version, effective date, applicability | Context only: no deadline |
| 2 | source-11-previous-policy:359-733:6358b75b | 0.6351 | 2025.1 / historical | "Equipment return was due within ten business days" | **No: outdated rule** |
| 3 | source-11-previous-policy:0-229:7599a261 | 0.6308 | 2025.1 / historical | "Superseded on 2026-09-01 by current-guide.md" | Shows #2 is outdated |
| 4 | source-11-current-guide:619-941:831bead6 | 0.5651 | 2026.2 / null | "Return equipment within five business days after the final working day" | **Yes: the answer** |
| 5 | source-11-previous-policy:231-357:6017b9f1 | 0.5497 | 2025.1 / historical | Historical scope | No |

Missing information: the Exceptions chunk (courier delay handling) was not returned, so this result set cannot speak to exceptions.
Risk: the outdated ten-day rule outranks the correct five-day rule. An answer that trusted rank order alone would be wrong. The `status: historical` / `superseded_by` metadata is what makes the right choice possible.

## q2: How far in advance must a manager name replacement owners?

| rank | chunk | cosine | version / status | supports answer? |
|---|---|---|---|---|
| 1 | source-11-current-guide:308-617:c5ede928 | 0.5740 | 2026.2 / null | **Yes**: "at least three business days before departure" |
| 2 | source-11-previous-policy:231-357:6017b9f1 | 0.4956 | 2025.1 / historical | No: scope only |
| 3 | source-11-previous-policy:359-733:6358b75b | 0.4769 | 2025.1 / historical | Outdated: "one business day before departure" |
| 4 | source-11-current-guide:943-1203:38ab4b18 | 0.4598 | 2026.2 / null | Related (data handover), not the deadline |
| 5 | source-11-current-guide:0-306:13a089e8 | 0.4555 | 2026.2 / null | Context: version and effective date |

Missing information: none for the question as asked. The historical one-day rule is present but correctly labelled historical.

## q3: What was the equipment return deadline before 2026-09-01?

| rank | chunk | cosine | version / status | supports answer? |
|---|---|---|---|---|
| 1 | source-11-previous-policy:359-733:6358b75b | 0.7035 | 2025.1 / historical | **Yes**: "ten business days" under "Terms before 2026-09-01" |
| 2 | source-11-previous-policy:0-229:7599a261 | 0.5741 | 2025.1 / historical | Supports the period: effective 2025-01-01, superseded 2026-09-01 |
| 3 | source-11-current-guide:0-306:13a089e8 | 0.5422 | 2026.2 / null | Context only |
| 4 | source-11-current-guide:619-941:831bead6 | 0.5367 | 2026.2 / null | Current five-day rule: not the asked period |
| 5 | source-11-operational-record:0-758:56d6b0ee | 0.4873 | 1.0 / case-record | No |

Missing information: none. Here the historical content is the correct evidence, which shows why historical versions must be kept, not deleted.

## q4: What happened in CASE-EXIT-214, and does it change the return target?

| rank | chunk | cosine | version / status | supports answer? |
|---|---|---|---|---|
| 1 | source-11-operational-record:0-758:56d6b0ee | 0.7142 | 1.0 / case-record | **Yes**: missed collection October 12, rebooked October 14, receipt October 16; "does not extend the five-business-day return target" |
| 2 | source-11-current-guide:1205-1635:fa511e2b | 0.5576 | 2026.2 / null | **Yes**: policy basis: "A courier delay is recorded with tracking evidence and a revised collection date" |
| 3 | source-11-current-guide:0-306:13a089e8 | 0.4916 | 2026.2 / null | Context only |
| 4 | source-11-previous-policy:231-357:6017b9f1 | 0.4822 | 2025.1 / historical | No |
| 5 | source-11-current-guide:308-617:c5ede928 | 0.4810 | 2026.2 / null | Related (handover), not needed |

Missing information: none. Both parts of the question are supported, and the case record carries its own "not a policy amendment" qualification.

## q5: Which courier company does Nimbus use? (expected unsupported)

| rank | chunk | cosine | supports answer? |
|---|---|---|---|
| 1 | source-11-current-guide:0-306:13a089e8 | 0.5543 | No |
| 2 | source-11-previous-policy:0-229:7599a261 | 0.5232 | No |
| 3 | source-11-current-guide:619-941:831bead6 | 0.4662 | No: mentions "the tracked Nimbus shipping label" but no company |
| 4 | source-11-operational-record:0-758:56d6b0ee | 0.4478 | No: mentions "the courier" but no company |
| 5 | source-11-previous-policy:231-357:6017b9f1 | 0.4358 | No |

Missing information: no returned passage names a courier company. Search still returned 5 results with scores near the other questions' (0.44–0.55), which shows that a score alone cannot tell supported from unsupported. Correct outcome: **abstain**.

## Cited answer demonstration (q1, using only returned passages)

**Question:** How many business days does a departing employee have to return Nimbus equipment under the current guide?

**Answer:** Five business days. The current guide says: "Return equipment within five business days after the final working day using the tracked Nimbus shipping label" [source-11-current-guide:619-941:831bead6, sources/source-11/current-guide.md]. That guide is "Version: 2026.2. Effective date: 2026-09-01" and "Supersedes previous-policy.md" [source-11-current-guide:0-306:13a089e8]. The ten-day figure that search also returned, "Equipment return was due within ten business days" [source-11-previous-policy:359-733:6358b75b], comes from a document marked "Status: historical" and "Superseded on 2026-09-01 by current-guide.md" [source-11-previous-policy:0-229:7599a261], so it does not apply to current departures.

**Limits of this answer:** the returned evidence did not include the Exceptions section, so this answer does not cover exceptions such as courier delays.

## Abstention demonstration (q5)

**Answer:** I can't answer this from the retrieved evidence. The returned passages mention "the tracked Nimbus shipping label" and "the courier", but none names a courier company.
