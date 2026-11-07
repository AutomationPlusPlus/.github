# Contributing

Thanks for helping out. This guide is the default for every repository in the
AutomationPlusPlus organization. If a repository has its own `CONTRIBUTING.md`
or `AGENTS.md`, the more specific file wins.

By taking part you agree to follow our
[Code of Conduct](https://github.com/AutomationPlusPlus/.github/blob/main/CODE_OF_CONDUCT.md).

Please do not report security problems in public issues. Follow
[SECURITY.md](https://github.com/AutomationPlusPlus/.github/blob/main/SECURITY.md)
instead.

## Before you start

- For a bug, open an issue with the bug form first, so we can agree it is a bug.
- For a new feature or a larger change, open an issue with the feature form
  before writing code. That way nobody spends time on a change we cannot take.
- Questions go to GitHub Discussions, not issues. See
  [SUPPORT.md](https://github.com/AutomationPlusPlus/.github/blob/main/SUPPORT.md).

## Branching

- Development is trunk-based. `main` is always releasable, and nobody pushes
  to it directly.
- Fork the repository and work on a short-lived branch whose name starts with
  `feat/`, `fix/`, `docs/`, or `chore/`, followed by a short slug, for example
  `feat/restore-dry-run`.
- Open a pull request against `main`. Keep each pull request to one concern.
- Pull requests are squash-merged once checks pass and a maintainer approves.

## Commit messages: Conventional Commits

We use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
Release tooling reads them to choose the next version and write the changelog,
and CI checks them.

```text
<type>(<optional scope>): <short summary>

<optional body>

<optional footers, including Signed-off-by>
```

- Common types are `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`,
  and `build`.
- Mark a breaking change with `!` after the type (`feat!: ...`) or with a
  `BREAKING CHANGE:` footer.
- Keep commits small and focused. Say in the summary what the commit does.

## Developer Certificate of Origin (DCO)

We use the Developer Certificate of Origin instead of a Contributor License
Agreement. Every commit must carry a `Signed-off-by` line with your real name
and an email address you can be reached at. Signing off means you certify the
statement below for that commit.

Add the line by committing with `-s`:

```sh
git commit -s -m "fix: handle empty snapshot list"
```

If you forgot to sign off:

```sh
# the most recent commit
git commit --amend -s --no-edit
# every commit on your branch
git rebase --signoff main
```

Then force-push your branch (never `main`). A CI check rejects pull requests
with commits that are not signed off.

The full text of the Developer Certificate of Origin 1.1, from
<https://developercertificate.org/>:

```text
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

## Running the checks: `make ci`

Each code repository has a `Makefile` with a `ci` target that runs the same
checks as CI: linters, tests, secret and license scans, and anything else that
repository needs. Run it from the repository root before you open a pull
request:

```sh
make ci
```

The exact list of checks and the tools they need are in the `Commands` section
of that repository's `AGENTS.md`. A pull request is only reviewed once `make ci`
passes in CI.

## Pull requests

- Fill in the pull request template, including how you verified the change.
- Update docs, tests, and `AGENTS.md` in the same pull request as the code
  they describe.
- Do not add or update dependencies without asking first in an issue. Most
  repositories keep an allow list of dependencies, and the default answer is no.
- Never include secrets, real API keys, or customer data, including in tests,
  fixtures, logs, and screenshots. Use clearly fake placeholder values.

## How we use coding agents

Maintainers use AI coding agents for much of the day-to-day work. This is how
that works, and what it means for you.

- **Every repository has an `AGENTS.md`.** It holds the rules an agent must
  follow: commands, architecture and licensing rules, security rules, the
  definition of done, and what to never do. It is seeded from
  [`agents/AGENTS.template.md`](https://github.com/AutomationPlusPlus/.github/blob/main/agents/AGENTS.template.md)
  and is a useful map of the repository for human contributors too.
- **Agents never push to `main`.** They work on feature branches under a
  separate bot identity and open pull requests like anyone else.
- **A human reviews every agent pull request.** `CODEOWNERS` routes the
  sensitive paths (public API, licensing, crypto, restore, `AGENTS.md`, and
  `.github/`) to a maintainer, so those always get human review.
- **Agents stop and ask.** Adding a dependency, changing CI, changing a public
  interface, or anything not covered by the docs or an ADR is a human decision.
- **If you use an agent yourself,** point it at the repository's `AGENTS.md`.
  You are responsible for what you submit: review the change and run
  `make ci`, and remember that your sign-off certifies the DCO for the whole
  commit.
