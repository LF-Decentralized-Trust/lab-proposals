# Branch rulesets

`main.json` is the ruleset for the default branch, in the format GitHub's
ruleset export and REST API use. It is not applied automatically; apply or
update it with:

```sh
# first time
gh api --method POST repos/LF-Decentralized-Trust/lab-proposals/rulesets --input .github/rulesets/main.json
# afterwards, with the id from `gh api repos/LF-Decentralized-Trust/lab-proposals/rulesets`
gh api --method PUT repos/LF-Decentralized-Trust/lab-proposals/rulesets/<id> --input .github/rulesets/main.json
```

What it enforces on `main`:

- Changes arrive by pull request; the branch cannot be deleted or force-pushed.
- Two approving reviews, with stale approvals dismissed when new commits are
  pushed, and at least one approval from a code owner (`CODEOWNERS`).
- The `steward-approvals` status check must pass. That check (see
  `.github/workflows/steward-approvals.yml`) only passes once two distinct
  members of the `tac` and/or `lab-stewards` teams have approved, so the real
  gate is *two steward approvals*, not just two approvals. Two from the same
  team is fine.
- Repository admins can bypass the ruleset, so staff can still maintain the
  repository itself (templates, workflows, this file) without a steward vote.
  Remove the `bypass_actors` entry to make the rule absolute.

The organization-level `DCO` ruleset applies on top of this one.
