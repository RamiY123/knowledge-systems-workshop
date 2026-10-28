# Submit your source to the workshop demo

Each participant works on one assigned source using their own GitHub account.
You need read access and permission to fork the workshop repository. You do not
need write access to the trainer repo, the private app, Java, Node, or Docker.
For a private repository, the trainer must enable the necessary access/fork policy.

## Before the workshop

1. Sign in to GitHub with your own account and open the trainer repository.
2. Choose **Fork** and create your own fork. If unavailable, ask the trainer to
   resolve repository access; do not create a public copy of private content.
3. Clone your fork and open the folder in your AI environment. Follow PREPARATION.md.
4. Complete the eleven steps for your assigned source, one at a time.

Already cloned the trainer repository? Keep your folder and completed work.
The submit-source skill can create your fork and add it as a separate push remote.

## Submit from your AI environment

After the eleven steps, invoke:

- Codex: `$submit-source source-01`
- Claude Code / VS Code Copilot: `/submit-source source-01`

Replace source-01 with your assigned ID. The skill explains each operation:

1. Verify your account and create or reuse your fork.
2. Validate and export bundle.json and review.md into submissions/<source>/.
3. Create a submission branch and commit only those two files.
4. Push to your fork and open a PR targeting the trainer's main.
5. Show the PR link and any remaining blocker.

Check the PR's destination and changed files. The instructor merges it; participants
do not perform a separate review exercise. Sending a PR does not immediately add
the knowledge to Studio. Do not push to the trainer's main or force-push. Stop on
source ownership conflicts rather than overwriting another contribution.
Keep .env, .venv, workspace, and local databases out of Git. Enter keys privately.

If automatic GitHub operations are unavailable, create the fork in GitHub, push
only the submission branch using your own Git credentials, then choose **Contribute
> Open pull request** on your fork. Select the trainer repo, base main, and your
submission branch. Preserve local work while resolving authentication problems.

## Instructor collection

Assign one unique source per participant. Merge the submitted PRs into main, then
run `$update-studio` or `/update-studio` from the private app or parent workspace.
It fast-forwards the dedicated .workshop-live checkout and verifies the local source
catalog. Refresh Studio's source list. Existing passage embeddings travel inside
JSON bundles; no SQLite merge or re-embedding is required.

Workflow: **participant fork and PR; instructor merge, update-studio, Refresh**.
The lab's retrieval review file is a learning artifact, separate from GitHub review.

Before the next event, archive the completed main with a Git tag and remove
submissions in a normal cleanup commit. Never reset or force-push history.
The app accepts schema version 1, text-embedding-3-small at 512 dimensions, up to
500 chunks per source and 100 sources. Historical evidence requires checking
version and applicability when answering.
