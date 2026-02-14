# CharIN Unified Error Codes Contribution Guide

This document outlines the contribution process for the CharIN Unified Error Codes specification, a joint effort of CharIN Members and external parties.

Contributions are made via GitHub Issues and Pull Requests. All submissions will be reviewed regularly by the project maintainers.

---

## Table of Contents

- [CharIN Unified Error Codes Contribution Guide](#charin-unified-error-codes-contribution-guide)
  - [Table of Contents](#table-of-contents)
  - [Contribution Workflow Overview](#contribution-workflow-overview)
  - [Issues vs. Documentation Updates](#issues-vs-documentation-updates)
  - [Step 1: Open an Issue](#step-1-open-an-issue)
  - [Step 2: Create a Pull Request](#step-2-create-a-pull-request)
    - [Fork, Clone, and Set Up (first time only)](#fork-clone-and-set-up-first-time-only)
    - [Create a Branch and Make Changes](#create-a-branch-and-make-changes)
    - [Pull Request Requirements](#pull-request-requirements)
  - [Step 3: Review Process](#step-3-review-process)
    - [Issues](#issues)
    - [Pull Requests](#pull-requests)
  - [Step 4: Merge and Close](#step-4-merge-and-close)
  - [Documentation Format Example](#documentation-format-example)
  - [Developer Certificate of Origin (DCO)](#developer-certificate-of-origin-dco)
  - [Project Maintainers](#project-maintainers)
  - [Getting Help](#getting-help)

---

## Contribution Workflow Overview

Every contribution follows a structured lifecycle. The diagram below shows the end-to-end process:

```text
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   1. ISSUE              2. PULL REQUEST         3. MERGE            │
│   ──────────────────    ──────────────────      ──────────────────  │
│                                                                     │
│   Open a GitHub    ──▶  Create a PR with   ──▶  Maintainers       │
│   Issue describing      the agreed-upon         approve and merge   │
│   the proposal          documentation changes   the PR              │
│                                                                     │
│   Discussed offline     Reviewed offline        Issue is closed     │
│   and during working    (comment period)        automatically       │
│   group meetings                                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Key principle:** We always start with an Issue. The Issue is only closed once the corresponding Pull Request is reviewed, approved, and merged into the `main` branch.

---

## Issues vs. Documentation Updates

It is important to understand the difference between these two types of contributions:

|              | **Definition Issue**                                                                                             | **Documentation Update**                                                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **What**     | A proposal, question, or feedback about an error code definition (its meaning, scope, severity, telemetry, etc.) | A change to the specification text implementing an agreed-upon definition        |
| **When**     | Whenever you want to propose, challenge, or discuss a definition                                                 | After a definition has been discussed and agreed upon in a working group meeting |
| **How**      | Open a GitHub Issue                                                                                              | Create a Pull Request                                                            |

> **Rule of thumb:** If you are unsure about a definition or want to propose a change to *what* an error code means — open an **Issue**. If a definition has already been agreed upon and you are writing or updating the specification text — create a **Pull Request**.

---

## Step 1: Open an Issue

All new proposals, changes, or identified problems **must** start as a GitHub Issue.

1. Go to the project's **Issues** tab on GitHub.
2. Click **New Issue**.
3. Provide a clear title and sufficient technical detail.
4. If proposing a new definition or a change, include a clear proposal to establish a basis for discussion.

Before creating a new issue, please search the existing issues to ensure the topic has not already been raised.

**Issues are discussed during working group meetings and can also be commented on offline by anyone in the community.** We encourage everyone to share feedback, ask questions, and participate in discussions directly on the Issue — this helps build consensus before the meetings. Once the group reaches agreement on the definition, the next step is to document it via a Pull Request.

---

## Step 2: Create a Pull Request

Once a definition is agreed upon in a meeting, the agreed changes are documented and submitted as a Pull Request (PR).

### Fork, Clone, and Set Up (first time only)

1. **Fork the repository** — Go to the project page on GitHub and click **Fork** in the top-right corner.
2. **Clone your fork** to your computer:

   ```bash
   git clone https://github.com/YOUR-USERNAME/unified-error-codes.git
   cd unified-error-codes
   ```

3. **Add the original repository as upstream** (to stay in sync):

   ```bash
   git remote add upstream https://github.com/charinev/unified-error-codes.git
   ```

### Create a Branch and Make Changes

1. **Sync with the latest changes** before starting new work:

   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

2. **Create a new branch** — always work on a separate branch, not on `main`:

   ```bash
   git checkout -b my-change-description
   ```

   > Use a short, descriptive name like `fix-typo-in-error-codes` or `add-new-error-definition`.

3. **Make your changes** — Edit the files in the `specification/` folder. The specification is written in [reStructuredText (.rst)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) format. See the [Documentation Format Example](#documentation-format-example) below.

4. **Build and verify locally** — Make sure your changes look correct:

   ```bash
   docker run --rm -v $(pwd)/specification:/docs sphinxdoc/sphinx-latexpdf make latexpdf
   ```

   Open `specification/_build/latex/unifiederrorcodes.pdf` and check your changes. See the [How to Build the Specification Locally](README.md#how-to-build-the-specification-locally) section in the README for detailed build instructions.

5. **Stage and commit your changes:**

   ```bash
   git add .
   git commit -s -m "Short description of what you changed"
   ```

   > The `-s` flag adds a "Signed-off-by" line, which is **required** for all contributions.

6. **Push to your fork:**

   ```bash
   git push origin my-change-description
   ```

7. **Open a Pull Request:**
   1. Go to your fork on GitHub.
   2. You'll see a banner suggesting to open a Pull Request — click **Compare & pull request**.
   3. Write a clear title and description of your changes.
   4. Click **Create pull request**.

### Pull Request Requirements

- All PRs must be submitted against the `main` branch.
- All commits must include a `Signed-off-by` line (use `git commit -s`). See [DCO](#developer-certificate-of-origin-dco).
- The PR description should reference the related Issue (e.g., `Closes #42`).
- Build the specification locally and verify your changes before submitting. See [How to Build the Specification Locally](README.md#how-to-build-the-specification-locally) in the README.

---

## Step 3: Review Process

Issues and Pull Requests follow different review processes:

### Issues

- Issues are discussed **during working group meetings** and can also be **commented on offline** by anyone in the community.
- Community members are encouraged to post feedback, questions, and suggestions directly on the Issue at any time.
- The group reviews proposals, provides feedback, and works toward agreement.
- Once a definition is agreed upon, the Issue remains open until the corresponding PR is merged.

### Pull Requests

- When a PR is ready for review, the maintainers will **announce it to the group** and open an offline review period.
- All group members are encouraged to **review the PR and post comments within two weeks** of the announcement.
- After the review period, any comments that need resolution will be discussed (either offline or in the next meeting).
- Once all comments are resolved and the documentation is agreed upon, the maintainers will **approve and merge** the PR.

---

## Step 4: Merge and Close

- Once a PR is approved by the maintainers and any merge conflicts are resolved, it will be **merged into `main`**.
- Merged PRs are incorporated into the official specification draft.
- The related Issue is **closed** after the PR is merged (use `Closes #<issue-number>` in the PR description to automate this).

---

## Documentation Format Example

The specification is written in [reStructuredText (.rst)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) format and built with [Sphinx](https://www.sphinx-doc.org/).

Before writing new content, examine the existing `.rst` files in the `specification/` folder for style, structure, and examples to follow. Keeping a consistent format across the specification is important.

> **Note:** All `.rst` files must include the SPDX license header:
>
> ```rst
> .. SPDX-License-Identifier: CC-BY-4.0
> .. Copyright CharIN e.V. and Contributors
> ```

- **New to reStructuredText?** See the [Sphinx RST primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

---

## Developer Certificate of Origin (DCO)

By contributing to this repository, you agree to license your contributions under the Project License:

- Apache-2.0 for code contributions
- CC-BY-4.0 for documentation/specification contributions

All commits must include a Signed-off-by line (DCO).
Use: `git commit -s`

## Project Maintainers

The current maintainers for this repository, responsible for reviewing and merging contributions, are:

- Patricia Laskowsky (Working Group Leader)
  - GitHub: [@plaskows83](https://github.com/plaskows83)  
- Karol Nowacki (Working Group Deputy Leader)
  - GitHub: [@knowack1](https://github.com/knowack1)
- Anais Bonnard (Technical Project Manager, CharIN)
  - GitHub: [@AnaisBonnard](https://github.com/AnaisBonnard)

## Getting Help

- **New to Git/GitHub?** Start with these tutorials:
  - [GitHub Hello World](https://docs.github.com/en/get-started/quickstart/hello-world) — Create your first repository.
  - [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) — Understand branches and Pull Requests.
  - [Forking a Repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) — How to fork and clone.
  - [Creating a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) — Step-by-step PR guide.
- **New to reStructuredText?** See the [Sphinx RST primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).
- **Have a question?** Start a [GitHub Discussion](https://github.com/charinev/unified-error-codes/discussions) — it's the best place to ask questions and connect with the community.
