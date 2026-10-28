"""Generate thin command adapters; the procedure lives only in steps/*.md."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def expected_files():
    config = json.loads((ROOT / "workshop.json").read_text(encoding="utf-8"))
    for command in config["commands"] + config.get("utility_commands", []):
        name, guide = command["name"], command["guide"]
        if not (ROOT / guide).is_file():
            raise ValueError(f"Missing guide: {guide}")
        description = f"Perform only the {name} step for an assigned workshop source when the participant explicitly requests it."
        body = f"""# Workshop: {name}

This is a hands-on workshop. Be verbose: explain purpose and planned actions,
narrate meaningful operations, show commands and representative before/after
examples, and summarize actual results. Teach decisions without hidden reasoning.

Read WORKSHOP_MODE.md in the project root, then {guide}.
Resolve the source from the participant's arguments (example: source-01).
Apply the guide to only that source. Save files only under workspace/<source>/.
Check prerequisites; if missing, explain and stop instead of doing earlier steps.
Perform only this step. End with output locations, validation results, and a
participant inspection checklist. Do not start the next step automatically.
"""
        if command in config.get("utility_commands", []):
            description = f"Submit one completed workshop source through the participant's fork and a pull request when explicitly requested."
            body = f"""# Workshop utility: {name}

Read {guide} in this repository and follow it for the participant's source.
Be verbose: explain the participant fork, trainer repository, submission branch,
files, Git operations, and actual result.
Explain each meaningful operation before executing it, show the scoped file list,
and finish with the commit, verified fork push, PR link, and any remaining blocker.
This is a submission utility, not another ingestion step. Do not complete missing
exercises. Invoking it requests export, fork creation/reuse, a scoped commit,
push to the participant fork, and a PR targeting the trainer main branch.
Preserve completed work in existing clones. Never push directly to trainer main.
The instructor merges before updating Studio; this skill must not approve or merge.
"""
        front = f"---\nname: {name}\ndescription: {description}\n"
        yield f".agents/skills/{name}/SKILL.md", front + "---\n\n" + body
        yield f".agents/skills/{name}/agents/openai.yaml", "policy:\n  allow_implicit_invocation: false\n"
        yield f".claude/skills/{name}/SKILL.md", front + 'disable-model-invocation: true\nargument-hint: "source-01"\n---\n\n' + body + "\nParticipant arguments: $ARGUMENTS\n"
        yield f".github/prompts/{name}.prompt.md", front + "agent: agent\n---\n\n" + body + "\nRead the source argument from the text accompanying this prompt.\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    mismatches = []
    for relative, content in expected_files():
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                mismatches.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if mismatches:
        raise SystemExit("Outdated command adapters: " + ", ".join(mismatches))
    print("Command adapters verified." if args.check else "Generated lab and utility adapters for three environments.")


if __name__ == "__main__":
    main()
