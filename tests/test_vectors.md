# Test vectors

1. With three matching catalog bodies, `fundamentals,applications,project` can advance.
2. With those same bodies, `project,applications,fundamentals` is `INVALID`, never advances.
3. A response-hash mismatch or unavailable source is `INCONCLUSIVE`, never advances.
4. Unknown, conditional, or outside-catalog prerequisites are `UNKNOWN`, never advance.
5. A reused attempt ID, changed parent root, or unauthorized caller reverts.
