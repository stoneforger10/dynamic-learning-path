# Architecture

The contract persists bounded course URLs and exact response hashes. A path attempt first binds a current parent version/root and complete course permutation. Leader and validators separately fetch each body and derive a prerequisite map. Only exact equality of the full report can advance the path.

Unlike a generic propose/finalize/certificate contract, the unit of state is an ordered curriculum revision; no certificate can be consumed or reused.
