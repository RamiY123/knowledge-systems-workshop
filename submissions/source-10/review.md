# Retrieval review: source-10

Real searches run with `tools/retrieval.py search` (text-embedding-3-small, 512 dims, exact cosine, top 5). Scores are similarities, not confidence probabilities. Judgements below use only the returned passages saved in `evaluation/search-*.json`.

## q1: How many weeks of company-paid parental leave can an eligible employee take under the current policy?

- **Answerable per collect step:** True
- **Evidence file:** `evaluation/evaluation\search-81b6aab488b7.json` (18 query tokens)

| Rank | Score | Version | Section | Chunk |
|---|---|---|---|---|
| 1 | 0.6788 | 2026.2 | Company benefit | `source-10-current-policy:324-640:687595cb` |
| 2 | 0.5710 | 2025.1 | Nimbus parental leave and return planning - historical | `source-10-previous-policy:0-931:76e4193d` |
| 3 | 0.5384 | 2026.2 | Taking leave | `source-10-current-policy:642-969:b58be6e2` |
| 4 | 0.5373 | 2026.2 | Nimbus parental leave and return planning | `source-10-current-policy:0-178:823a5b1f` |
| 5 | 0.4896 | 2026.2 | Applicability | `source-10-current-policy:180-322:3a1fe674` |

- **Relevance:** Relevant and supported. Rank 1 is the current "Company benefit" chunk.
- **What it supports:** States 12 weeks of company-paid parental leave for employees with six completed months of service. Pay basis and bonus exclusion are also stated.
- **Missing or risky:** None for the question. Risk: the historical policy chunk (8 weeks) ranks 2nd. Without version metadata it is easy to mix up.

## q2: What was the company parental leave benefit before 2026-09-01, and how much service was required?

- **Answerable per collect step:** True
- **Evidence file:** `evaluation/evaluation\search-e0b563abc3c4.json` (23 query tokens)

| Rank | Score | Version | Section | Chunk |
|---|---|---|---|---|
| 1 | 0.6745 | 2026.2 | Company benefit | `source-10-current-policy:324-640:687595cb` |
| 2 | 0.6682 | 2025.1 | Nimbus parental leave and return planning - historical | `source-10-previous-policy:0-931:76e4193d` |
| 3 | 0.5909 | 2026.2 | Nimbus parental leave and return planning | `source-10-current-policy:0-178:823a5b1f` |
| 4 | 0.4951 | 2026.2 | Taking leave | `source-10-current-policy:642-969:b58be6e2` |
| 5 | 0.4557 | 2026.2 | Applicability | `source-10-current-policy:180-322:3a1fe674` |

- **Relevance:** Relevant, supported, but ranking alone would mislead. Rank 1 is the CURRENT benefit (0.6745), only 0.0063 above the historical policy (0.6682). The question asks about before 2026-09-01.
- **What it supports:** The historical chunk states eight weeks after twelve completed months of service and says it was superseded on 2026-09-01.
- **Missing or risky:** None. The correct passage is rank 2, so the answer must be chosen using version/effective-date metadata, not rank.

## q3: What does a manager need to do and record when an employee returns on an 80% schedule?

- **Answerable per collect step:** True
- **Evidence file:** `evaluation/evaluation\search-b6cdb2d7c1de.json` (20 query tokens)

| Rank | Score | Version | Section | Chunk |
|---|---|---|---|---|
| 1 | 0.6637 | 2026.2 | Return arrangement | `source-10-current-policy:971-1240:72269a4b` |
| 2 | 0.5413 | 1.0 | Return handover checklist | `source-10-operational-record:0-1123:a0242be3` |
| 3 | 0.4040 | 2026.2 | Taking leave | `source-10-current-policy:642-969:b58be6e2` |
| 4 | 0.3924 | 2025.1 | Nimbus parental leave and return planning - historical | `source-10-previous-policy:0-931:76e4193d` |
| 5 | 0.3695 | 2026.2 | Nimbus parental leave and return planning | `source-10-current-policy:0-178:823a5b1f` |

- **Relevance:** Relevant and supported. Ranks 1 and 2 are the "Return arrangement" chunk and the handover checklist.
- **What it supports:** Policy: the manager and People Operations record the schedule before return. Checklist: record an agreed 80% schedule in the personnel case and publish only availability in the team calendar.
- **Missing or risky:** The policy chunk also mentions a vacation table in source-01, which was not retrieved and is outside this source. The checklist applies from 2026-10-09 (version 1.0) and supplements, not replaces, the policy.

## q4: If a placement is unexpected and there was no eight weeks' notice, is the employee still eligible?

- **Answerable per collect step:** True
- **Evidence file:** `evaluation/evaluation\search-976cd7fa9877.json` (20 query tokens)

| Rank | Score | Version | Section | Chunk |
|---|---|---|---|---|
| 1 | 0.6203 | 2026.2 | Taking leave | `source-10-current-policy:642-969:b58be6e2` |
| 2 | 0.5247 | 2026.2 | Return arrangement | `source-10-current-policy:971-1240:72269a4b` |
| 3 | 0.4997 | 2025.1 | Nimbus parental leave and return planning - historical | `source-10-previous-policy:0-931:76e4193d` |
| 4 | 0.4666 | 2026.2 | Applicability | `source-10-current-policy:180-322:3a1fe674` |
| 5 | 0.4417 | 2026.2 | Company benefit | `source-10-current-policy:324-640:687595cb` |

- **Relevance:** Relevant and supported. Rank 1 is "Taking leave".
- **What it supports:** States that lack of eight weeks' notice does not itself remove eligibility for an unexpected placement.
- **Missing or risky:** The chunk does not restate the other eligibility conditions. The six-month service requirement is in the "Company benefit" chunk, which ranks only 5th.

## q5: What is the statutory maximum parental leave in Germany that can be added to the company benefit?

- **Answerable per collect step:** False
- **Evidence file:** `evaluation/evaluation\search-489b07a56825.json` (18 query tokens)

| Rank | Score | Version | Section | Chunk |
|---|---|---|---|---|
| 1 | 0.5723 | 2026.2 | Company benefit | `source-10-current-policy:324-640:687595cb` |
| 2 | 0.5109 | 2025.1 | Nimbus parental leave and return planning - historical | `source-10-previous-policy:0-931:76e4193d` |
| 3 | 0.4658 | 2026.2 | Nimbus parental leave and return planning | `source-10-current-policy:0-178:823a5b1f` |
| 4 | 0.4600 | 2026.2 | Taking leave | `source-10-current-policy:642-969:b58be6e2` |
| 5 | 0.3967 | 2026.2 | Applicability | `source-10-current-policy:180-322:3a1fe674` |

- **Relevance:** Not supported, as expected for an unanswerable question. The top results are generic benefit passages; similarity returns the nearest chunks even when none answers.
- **What it supports:** Nothing states a statutory maximum for Germany or anywhere else. The "Applicability" chunk (rank 5) only says statutory entitlements require individual People Operations review.
- **Missing or risky:** The source never gives a legal maximum. The chunk "Local entitlement interaction", which warns not to infer a legal maximum, was NOT among the 5 returned, so that warning could not be cited from retrieved evidence. Correct outcome: abstain.

## Cited answer demonstration (using only returned passages)

### q2: What was the company parental leave benefit before 2026-09-01, and how much service was required?

Before 2026-09-01 the company benefit was **eight weeks**, available after **twelve completed months of service** [`source-10-previous-policy:0-931:76e4193d`, previous-policy.md, v2025.1, status historical]. That policy was superseded on 2026-09-01 by the current policy [`source-10-previous-policy:0-931:76e4193d`]. The current policy (v2026.2, effective 2026-09-01) now allows 12 weeks after six completed months [`source-10-current-policy:324-640:687595cb`, current-policy.pdf], but that applies from 2026-09-01 and is not the answer to this question.

Note: the current-policy chunk ranked first, so picking the top result would have given the wrong answer. The effective date and "historical" status settled it.

### q5: What is the statutory maximum parental leave in Germany that can be added to the company benefit? (abstain)

I cannot answer this from the retrieved evidence. No returned passage states a statutory maximum for Germany or any other jurisdiction. The only related text says statutory entitlements require individual People Operations review [`source-10-current-policy:180-322:3a1fe674`, current-policy.pdf].

### Citation verification

All 11 quoted phrases used in this review were checked in code and found verbatim in the returned text of the cited chunk for that question.

## Limitations

- Only 5 questions, all written from this source; this is a small spot check of retrieval, not a benchmark.
- top_k is 5, so a relevant chunk ranked 6th or lower is invisible to the answer step.
- Review judgements are the agent's; the participant should confirm them against the originals.
