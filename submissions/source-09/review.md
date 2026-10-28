# Retrieval review - source-09

Every quotation below was checked against the text that retrieval actually returned for that question: 11 citations verified, 0 unverifiable.
Scores are cosine similarities, not confidence probabilities.

## q1 - expected answerable

> What is the current calendar-year ceiling for courses and certification exams, and what approval is required before purchase?

**Verdict:** ANSWERABLE from the returned evidence, but not from the top hit.

| Rank | Score | Document | Section | Authority | Holds answer |
| ---: | ---: | --- | --- | --- | --- |
| 1 | 0.6126 | current-policy | Eligibility and reimbursement | current | no |
| 2 | 0.5743 | current-policy | Applicability + Annual allowances | current | yes |
| 3 | 0.5647 | operational-record | (front matter) | supplements | no |
| 4 | 0.5433 | operational-record | (untitled body) | supplements | no |
| 5 | 0.5189 | current-policy | (front matter) | current | no |

**Relevance.** Rank 1 (Eligibility and reimbursement, 0.6126) is about claiming and eligibility, not about ceilings; it does not contain the figure. The answer sits at rank 2 (0.5743). With top_k=1 this question would have been answered wrongly or not at all.

**Evidence used.**

- rank 2 - `source-09__current-policy#00190-00612#0587b52e` - `sources/source-09/current-policy.html` (version 2026.2): "USD 900"
- rank 2 - `source-09__current-policy#00190-00612#0587b52e` - `sources/source-09/current-policy.html` (version 2026.2): "Manager before purchase"
- rank 2 - `source-09__current-policy#00190-00612#0587b52e` - `sources/source-09/current-policy.html` (version 2026.2): "part-time monetary limits are prorated by contracted full-time fraction"

**Missing information.** Nothing for the question as asked. Note the retrieved chunk also states the conference ceiling, which the policy says does not create a second entitlement; resolving that fully needs source-01, outside this assignment.

## q2 - expected answerable

> How many paid study days are granted under the current policy, and how many were granted before 2026-09-01?

**Verdict:** ANSWERABLE, and only by combining two documents of different vintage.

| Rank | Score | Document | Section | Authority | Holds answer |
| ---: | ---: | --- | --- | --- | --- |
| 1 | 0.6283 | previous-policy | Historical scope + Terms before 2026-09-01 | superseded 2026-09-01 | yes |
| 2 | 0.5388 | current-policy | Exceptions | current | no |
| 3 | 0.5312 | current-policy | Applicability + Annual allowances | current | yes |
| 4 | 0.5147 | current-policy | (front matter) | current | no |
| 5 | 0.5059 | previous-policy | (front matter) | superseded 2026-09-01 | yes |

**Relevance.** Rank 1 is the historical chunk and rank 3 is the current one. Both were returned, and each carries metadata saying which period it governs, so the two figures can be reported as a change rather than a contradiction. Note where the supersession is known from: the rank-1 chunk's own TEXT never says it is superseded - that fact reaches it through the metadata inherited in the carry-metadata step (superseded_on 2026-09-01). The sentence stating it in prose lives in the front-matter chunk, which happened to be returned too, at rank 5. Had it not been returned, the metadata alone would still have carried the authority.

**Evidence used.**

- rank 1 - `source-09__previous-policy#00240-00759#d2a70bee` - `sources/source-09/previous-policy.md` (version 2025.1): "Paid study time was two working days"
- rank 3 - `source-09__current-policy#00190-00612#0587b52e` - `sources/source-09/current-policy.html` (version 2026.2): "| Paid study time | 3 working days | Manager scheduling agreement |"
- rank 5 - `source-09__previous-policy#00000-00238#806abe4a` - `sources/source-09/previous-policy.md` (version 2025.1): "Superseded on 2026-09-01 by current-policy.html"

**Missing information.** Nothing for the question as asked.

## q3 - expected answerable

> A provider cancels a course that was already paid for and approved. What must the employee attach, and what happens to the course balance for that year?

**Verdict:** ANSWERABLE from the supplemental notice only - again at rank 2, not rank 1.

| Rank | Score | Document | Section | Authority | Holds answer |
| ---: | ---: | --- | --- | --- | --- |
| 1 | 0.6543 | current-policy | Eligibility and reimbursement | current | no |
| 2 | 0.6239 | operational-record | (untitled body) | supplements | yes |
| 3 | 0.5743 | operational-record | (front matter) | supplements | no |
| 4 | 0.4923 | previous-policy | Historical scope + Terms before 2026-09-01 | superseded 2026-09-01 | no |
| 5 | 0.4781 | current-policy | Applicability + Annual allowances | current | no |

**Relevance.** Rank 1 (0.6543) is the policy's own reimbursement section, which never mentions cancellation. The notice body at rank 2 (0.6239) is the only passage that answers it. A system that consulted the policy alone, or that trusted its top hit, would have answered confidently and wrongly.

**Evidence used.**

- rank 2 - `source-09__operational-record#00206-00744#42ac7539` - `sources/source-09/operational-record.md` (version 1.0): "attach the cancellation and refund evidence to the original claim"
- rank 2 - `source-09__operational-record#00206-00744#42ac7539` - `sources/source-09/operational-record.md` (version 1.0): "Finance restores the refunded amount to the same year's course balance once the refund settles"

**Missing information.** The notice does not say how long the refund settlement takes, nor what happens if it settles in the following calendar year.

## q4 - expected answerable

> An approved certification exam is failed. Is the original attempt still reimbursable, and what is required for a second attempt?

**Verdict:** ANSWERABLE, and here the top hit is the right one.

| Rank | Score | Document | Section | Authority | Holds answer |
| ---: | ---: | --- | --- | --- | --- |
| 1 | 0.6447 | current-policy | Eligibility and reimbursement | current | yes |
| 2 | 0.5091 | operational-record | (untitled body) | supplements | no |
| 3 | 0.4394 | operational-record | (front matter) | supplements | no |
| 4 | 0.3784 | current-policy | Applicability + Annual allowances | current | no |
| 5 | 0.3704 | current-policy | (front matter) | current | no |

**Relevance.** Rank 1 (0.6447) contains both halves of the answer. Ranks 2-5 drop to 0.51 and below, so the gap between the answer and the noise is wider than in any other question.

**Evidence used.**

- rank 1 - `source-09__current-policy#00941-01238#c7662295` - `sources/source-09/current-policy.html` (version 2026.2): "A failed exam remains eligible if it was approved"
- rank 1 - `source-09__current-policy#00941-01238#c7662295` - `sources/source-09/current-policy.html` (version 2026.2): "a second attempt requires fresh approval and uses the remaining annual balance"

**Missing information.** Nothing for the question as asked.

## q5 - expected UNSUPPORTED

> Which external training providers are pre-approved by Nimbus, and is there a preferred vendor list?

**Verdict:** NOT ANSWERABLE. The correct outcome is to abstain.

| Rank | Score | Document | Section | Authority | Holds answer |
| ---: | ---: | --- | --- | --- | --- |
| 1 | 0.5537 | current-policy | (front matter) | current | no |
| 2 | 0.5535 | operational-record | (untitled body) | supplements | yes |
| 3 | 0.5424 | previous-policy | (front matter) | superseded 2026-09-01 | no |
| 4 | 0.5209 | current-policy | Applicability + Annual allowances | current | no |
| 5 | 0.4634 | previous-policy | Historical scope + Terms before 2026-09-01 | superseded 2026-09-01 | no |

**Relevance.** Retrieval returned five passages, as it always will. The top score is 0.5537, which is HIGHER than the score of the chunk that actually answered q1 (0.5743 at rank 2 - comparable, not distinguishable). The word 'vendor' does appear at rank 2, but inside a sentence about a voucher's validity period, not a list of approved providers. Lexical proximity is not evidence.

**Evidence used.**

- rank 2 - `source-09__operational-record#00206-00744#42ac7539` - `sources/source-09/operational-record.md` (version 1.0): "Reimbursement does not extend the vendor's validity period"

**Missing information.** Everything the question asks for. No returned passage names a training provider, an approval list, or a procurement preference. The source collection contains no such information, so no amount of re-querying will surface it.

## Answer demonstration (retrieved passages only)

Question q2: How many paid study days are granted under the current policy, and how many were granted before 2026-09-01?

Under the current policy (version 2026.2, effective 2026-09-01), paid study time is **3 working days** per calendar year, granted by manager scheduling agreement.
Before 2026-09-01 the previous policy (version 2025.1) granted **two working days**. That document is superseded and applies only to the earlier period.
Both figures are stated for full-time employees; part-time monetary limits are prorated by contracted full-time fraction.

Citations:

- `source-09__previous-policy#00240-00759#d2a70bee` (sources/source-09/previous-policy.md, version 2025.1, effective 2025-01-01)
- `source-09__current-policy#00190-00612#0587b52e` (sources/source-09/current-policy.html, version 2026.2, effective 2026-09-01)
- `source-09__previous-policy#00000-00238#806abe4a` (sources/source-09/previous-policy.md, version 2025.1, effective 2025-01-01)

No source file was reopened while composing this answer; it uses only the passages retrieval returned.

## Abstention demonstration

Question q5: Which external training providers are pre-approved by Nimbus, and is there a preferred vendor list?

I cannot answer this from the prepared knowledge. None of the five retrieved passages names an approved or preferred training provider. The policy governs ceilings, approvals, eligibility and exceptions; it never addresses provider selection. Answering would require inventing the list.

A correct abstention is a successful outcome, not a gap in the system.

## What this run shows

- In 2 of the 4 answerable questions (q1, q3) the answer-bearing chunk was at rank 2, not rank 1. top_k=5 covered the difference; top_k=1 would not have.
- The highest score for the unanswerable question (0.5537) is in the same band as the scores of real answers (0.5743 for q1's answer chunk). A similarity threshold would therefore not separate answerable from unanswerable here.
- q2 was answerable only because both the current and the superseded document were kept AND labelled. Deleting the old figure would have lost the comparison; keeping it unlabelled would have made the two figures look like a contradiction.
- q3 was answerable only from the supplemental notice. A pipeline that indexed the policy alone would have returned a confident, wrong answer.

