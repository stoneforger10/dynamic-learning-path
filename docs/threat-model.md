# Threat model

Handled: altered page body, source unavailability, HTTP failure, truncated/invalid text, ambiguous or outside-catalog prerequisites, contradictory order, stale parent, replayed attempt, wrong owner, and validator disagreement.

Limitations: a malicious source publisher can put false requirements in its own page; SHA-256 proves byte identity, not institutional authenticity. Use official publisher URLs for real deployments. The contract does not infer credit or learner completion.
