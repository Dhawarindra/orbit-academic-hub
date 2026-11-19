# Working on Orbit

- Work in the existing checkout. Check the branch and working tree first. Preserve other contributors’ changes. Commit, push, or open a PR only when requested. Use human review before merging into main.
- Implement only the milestone explicitly authorized by the user. The release baseline is PRD v0.2.1, with 48 P0 functional requirements and their active quality gates. P1/P2 and public deployment require a separate scope decision.
- Read the relevant PRD, the [architecture index](ORBIT_ARCH_v0.1/ARCH-INDEX.md), the [test matrix](ORBIT_ARCH_v0.1/ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md), and the [open decisions](ORBIT_ARCH_v0.1/ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md). Preserve both versioned documentation packages.
- Keep original FR, BR, NFR, AC and test IDs. For a proposed scope change, record the reason, affected consumers, baseline version, decision and related tests for human review before implementing it. Maintain the decision log and traceability matrix in the approved next revision.
- Keep academic rules in explainable Python domain functions, request handling in Flask, rendering in Jinja and data access in the repository. Use synthetic data with provenance and explicit confirmation for future actual-grade writes.
- Use the local runner documented in the README. Keep debug off, bind loopback, and keep secrets, databases, exports and personal records out of Git.
- Add meaningful boundary tests for the authorized behavior. Run `python -m unittest discover -s tests -v` from the repository root and report actual outcomes, including skipped or pending checks. A second member should reproduce the setup and explain the code before release.
