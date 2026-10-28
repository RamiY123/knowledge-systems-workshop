# Submit one completed source through your fork

Use `$submit-source source-01` (Codex) or `/submit-source source-01`
(Claude Code / Copilot). Invocation requests export, creation or reuse of the
participant's fork, a scoped commit, a push to that fork, and a pull request to
the trainer's main branch. It does not request a merge or instructor privileges.
Read WORKSHOP_MODE.md and CONTRIBUTING.md. Explain every meaningful action before
executing it, show the source-specific files, and finish with the verified PR URL.

## 1. Identify the source, account, and repositories

Resolve the assigned source using WORKSHOP_MODE.md. Inspect Git status, current
branch, remote URLs, and existing local commits. Never read .env or display tokens.
The trainer repository is `RamiY123/knowledge-systems-workshop`, base branch `main`.
Verify its identity against the remote and GitHub fork parent information. If this
is a different workshop repository, ask the trainer which upstream is intended.
Use the participant's authenticated GitHub account, never the trainer's account.
If GitHub CLI is available, `gh auth status` and `gh api user --jq .login` identify
the account without printing a token. For missing authentication, guide the
participant through sign-in and resume afterward. Never request a token in chat.

Participants need read access to the trainer repository and permission to fork it.
A fork does not bypass private-repository or organization restrictions. If GitHub
blocks access/forking, report the exact blocker and stop for the trainer. Do not
change visibility, permissions, or publish a disconnected copy as a workaround.
A connector or GitHub web UI can substitute for gh when available. If only manual
GitHub steps are possible, explain them and preserve the completed local artifacts.

## 2. Create or reuse the participant's fork without recloning

Inspect whether the authenticated user already owns a fork of the trainer repo.
Reuse it only after verifying its parent. Otherwise create the fork in their account,
without cloning or letting gh automatically rename remotes:

```sh
gh repo fork RamiY123/knowledge-systems-workshop --clone=false --remote=false
```

Resolve the fork's actual URL and owner from GitHub; do not assume its name.
Fetch/push Git authentication must also belong to the participant. Never embed
credentials in remote URLs. Choose HTTPS or SSH consistent with their working setup.

For a clone of the participant's fork, keep origin and add/reuse upstream for the
trainer repository. For a clone of the trainer repo, keep origin pointing at the
trainer and add/reuse a remote named fork for the participant's fork. The trainer
remote may therefore be origin or upstream; the push remote may be fork or origin.
Verify both URLs and announce their roles explicitly. Do not silently rename or
replace an existing remote. If the name is occupied by another repo, choose a free
name and explain it. Never push to the trainer repo or either repository's main.
Existing ignored workspace artifacts stay in the same local folder.

## 3. Validate and export the finished work

Require all eleven steps complete with current artifacts. Run
`tools/export_submission.py <source>` using `.venv/Scripts/python.exe` on Windows
or `.venv/bin/python` on macOS. Export makes no embedding API call and must not
complete missing exercises. If an export already exists, compare its IDs, text,
metadata, vectors, model, and dimensions against current artifacts and compare its
review with evaluation/review.md. Reuse only matching files. Stop on a mismatch
rather than silently replacing a previous submission.

Show document/passage counts and the exact paths under submissions/<source>/.
Check for accidental credentials without echoing their contents. Keep .env,
.venv, workspace, local SQLite, and other sources out of the submission.

## 4. Create a submission branch and scoped commit

Fetch the verified trainer remote. Unrelated staged or tracked changes must be
preserved and resolved by the participant before branch integration. Do not stash,
reset, clean, or discard them. Ignore unrelated untracked/local workspace files.
Inspect commits since the merge base with the trainer's main: local-only changes
must be limited to submissions/<source>/. Stop if unrelated commits would enter the PR.
Also check remote changes to the assigned submission folder since that merge base.
If the trainer branch already contains a different submission for this source,
stop for an ownership conflict even if Git could merge it automatically.

Create `codex/submit-<source>` from the current checkout, preserving any existing
source-only commit. On repeat invocation, reuse a verified matching submission
branch/PR. If that name belongs to unrelated or already-merged work, use a fresh
suffix. Never overwrite an existing branch. Explain that branch creation preserves
ignored participant files and avoids pushing directly to main.

Stage only submissions/<source>/, inspect all staged paths, and commit with a
message such as `Submit source-01 knowledge`. Do not create an empty commit.
With the tracked working tree clean, merge the fetched trainer main into this
submission branch if needed. Use a normal merge to preserve already-pushed commits.
Abort a newly started merge on conflict and report the paths, retaining the source
commit. Never select ours/theirs automatically or rewrite history.

Before pushing, compare trainer-main...HEAD and inspect the complete changed-file
list. It must contain only the assigned source's bundle.json and review.md. Confirm
that the actual bundle still matches the completed artifacts. If the diff is empty,
check whether the contribution was already merged and report that instead of
creating a duplicate PR.

## 5. Push to the fork and open the pull request

Push the branch explicitly to the verified fork remote:
`git push -u <fork-remote> HEAD:refs/heads/<submission-branch>`.
Replace placeholders with the verified values. Never force-push. If rejected,
fetch the fork branch and inspect its commits. Stop on divergence or unexpected
changes; do not keep retrying or overwrite remote work.

Verify that the pushed commit is contained in that fork branch. Look for an
existing open PR with this exact fork, head branch, trainer repo, and base main.
Reuse it on retries. Otherwise create the PR with an explicit destination:

```sh
gh pr create --repo RamiY123/knowledge-systems-workshop --base main --head <participant-login>:<submission-branch> --title "Submit source-01 knowledge" --body-file <local-body-file>
```

Write the PR body as a UTF-8 file under workspace/<source>/, not shell interpolation.
Include the source ID, document/passage counts, embedding model/dimensions, actual
validation/retrieval results, and limitations. Never invent successful checks.
Verify the returned PR's base, fork/head, changed files, and open state. If running
in Codex with an attach-artifact tool, attach the created or resumed PR to this chat.
Creating a fork or PR can be retried after transient failure only after inspecting
whether the previous attempt already succeeded. Never duplicate a PR blindly.

## 6. Report the handoff

Show the participant: fork URL, branch, commit, PR link, and actual submission
status. A pushed fork alone is not imported knowledge. Explain: **the instructor
merges the PR into main, then runs update-studio**. Do not approve, merge, or run
Studio updates from the participant skill. Participants need no direct write access
to the trainer repository and do not perform a separate code-review exercise.
If the PR could not be opened, say 'pushed to fork; PR pending' with the exact next
step. End with an inspection checklist: right source, right destination, only the
two expected files, and no credentials.
