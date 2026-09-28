# DynamicLearningPath

> Historical graph-ordering experiment; **not a separate Builder resubmission**. Its distinct successor is [CurriculumDriftSentinel](https://github.com/stoneforger10/curriculum-drift-sentinel), a permissionless, evidence-bound syllabus pause gate. The Explorer links below prove only this historical contract, not the successor.

A catalog-bound learning-path scheduler for GenLayer. It evaluates whether an ordered course pathway obeys prerequisites stated in the referenced course descriptions. It does **not** grade learners, issue credentials, or certify educational quality.

## Why this is an Intelligent Contract

A plain graph database can enforce prerequisites only after a trusted actor enters the edges. This contract instead lets the leader and validators independently fetch the exact course documents, verify full-body SHA-256 commitments, and derive explicit mandatory prerequisites from their contents. The complete report—including HTTP status, response hashes, hash matches, normalized prerequisite vector, ordering decision, and report root—must match exactly. `UNKNOWN` never advances a path.

## Workflow

```text
create program → register 2–6 source-bound courses → submit full ordering
→ independently fetch every source → normalize prerequisites
→ exact validator agreement → VALID path revision / INVALID or INCONCLUSIVE attempt
```

There is no reusable approval certificate or one-time consumption gate. Each attempt is immutable and bound to the contract, program, owner, parent version/root, full ordering, and catalog source commitments. Only `VALID` advances the path and creates an append-only snapshot. Invalid, unavailable, ambiguous, stale, or hash-mismatched evidence cannot advance it.

## Boundaries

The source publisher controls its course description. The contract verifies what the pinned document says, not whether the institution really offers the course or whether a learner completed it. For production, register official catalog URLs. Demo fixtures are explicitly synthetic.

## Commands

```powershell
genvm-lint check contracts/DynamicLearningPath.py --json
pytest tests/direct -q
genlayer network set studionet
genlayer deploy --contract contracts/DynamicLearningPath.py
```

StudioNet is gasless. Verify `FINALIZED` and leader `SUCCESS` before citing any transaction.

## Security

Owner-only registration and path evaluation; immutable per-program course entries; exact course permutations; SHA-256 body commitments; bounded responses; fail-closed `UNKNOWN`; no confidence tolerance; exact decision equality; unique attempts; parent-root locking. See `docs/threat-model.md`.
