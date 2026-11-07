# Security policy

This policy applies to every repository in the AutomationPlusPlus organization
unless a repository has its own `SECURITY.md`.

## Reporting a vulnerability

Please report vulnerabilities privately through
[GitHub private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability):

1. Open the affected repository on GitHub.
2. Go to the **Security** tab.
3. Select **Report a vulnerability** and fill in the form.

Do not open a public issue, discussion, or pull request for a security problem.

If you cannot use GitHub private vulnerability reporting, contact us at
**TODO: add a security contact email (maintainer to fill in)**.

## What to include

- The affected repository, product, and version (the output of the product's
  `version` command, where it has one).
- What the problem is and what an attacker could do with it.
- Steps to reproduce, or a proof of concept.
- Any suggested fix or mitigation you have.

Never include real API keys, tokens, passwords, or customer data in a report.
Replace them with placeholder values. If a report needs a support bundle,
generate it with the product's support bundle command, which redacts secrets.

## What happens next

1. We confirm we received the report and start investigating.
2. We work with you on the details and agree on a fix and a release.
3. We publish the fix and a GitHub Security Advisory, requesting a CVE where
   one applies, and list the fix in the Security section of the release notes.
   We credit you in the advisory if you would like to be credited.

Our target for fixing critical vulnerabilities is 7 days.

## Coordinated disclosure

We follow a 90-day coordinated disclosure window. Please give us 90 days from
your report to release a fix before you disclose the vulnerability publicly.
If a fix ships sooner, we can agree on an earlier disclosure date together.

## Supported versions

Supported versions and their end-of-life dates are listed on each product's
support page: **TODO: add the support page link (maintainer to fill in)**.
