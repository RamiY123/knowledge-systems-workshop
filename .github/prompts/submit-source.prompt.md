---
name: submit-source
description: Submit one completed workshop source through the participant's fork and a pull request when explicitly requested.
agent: agent
---

# Workshop utility: submit-source

Read instructions/submit-source.md in this repository and follow it for the participant's source.
Be verbose: explain the participant fork, trainer repository, submission branch,
files, Git operations, and actual result.
Explain each meaningful operation before executing it, show the scoped file list,
and finish with the commit, verified fork push, PR link, and any remaining blocker.
This is a submission utility, not another ingestion step. Do not complete missing
exercises. Invoking it requests export, fork creation/reuse, a scoped commit,
push to the participant fork, and a PR targeting the trainer main branch.
Preserve completed work in existing clones. Never push directly to trainer main.
The instructor merges before updating Studio; this skill must not approve or merge.

Read the source argument from the text accompanying this prompt.
