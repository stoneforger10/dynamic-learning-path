# StudioNet live proofs

Network: GenLayer StudioNet (chain 61999)

Contract: `0x50DbcECD604d7d0B0bA9Fe1b23c5Ce4a990D22a7`

Explorer: https://explorer-studio.genlayer.com/address/0x50DbcECD604d7d0B0bA9Fe1b23c5Ce4a990D22a7

The deployed source matches `contracts/DynamicLearningPath.py` byte-for-byte (SHA-256 `07c8b16f96c4bd9363a3a975411b0c856acb6ac99b3e786330ca5bef13cf5c80`).

## Finalized transactions

- Deployment: https://explorer-studio.genlayer.com/tx/0x7da8ef30993dfde550119475f33394f8aafa92763f30c4aa0ae062b058002fc0
- Program registration: https://explorer-studio.genlayer.com/tx/0xf4a9772a5da767680eaaa9e901ba58983a90836891e4d155bfda15b64558275a
- Fundamentals source commitment: https://explorer-studio.genlayer.com/tx/0xaa4e814f1a131c55ecf82e9234e1c686c3ef1ba5989f99a112cc13f95f34bb27
- Applications source commitment: https://explorer-studio.genlayer.com/tx/0xa47e582a5a5cba2015ea7d77073ec2b2bd366a662b6b8106656c576cd2af127f
- Project source commitment: https://explorer-studio.genlayer.com/tx/0x6539ffee6fc73f712be81b6efc0816b6d0bae2d0ddab08cfeeb5f38e34fc99a5
- Valid path (`VALID`, exact prerequisite vector, version 1): https://explorer-studio.genlayer.com/tx/0xb266966695d85977714e345cb5b07b7a63cdfc61b6a3ac0b471495e1cd7578d7
- Adversarial reversed path (`INVALID`, head unchanged): https://explorer-studio.genlayer.com/tx/0x1080678fa7095caaf292c8efaf0205af7421dbb5e253913359db993365c3a3d4

The valid packet records HTTP 200 for all three sources, exact SHA-256 matches, prerequisite vector `applications -> fundamentals`, `project -> applications`, and a version-1 path `fundamentals, applications, project`. The reversed-order packet independently fetched the same sources, reached `INVALID`, and left the program at version 1.
