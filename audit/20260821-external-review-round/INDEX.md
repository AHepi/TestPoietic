# External Review Round — 2026-08-21

Six unsealed records reviewed blind by six different external model families
(Ollama cloud), each finding adjudicated by an arbiter from a DIFFERENT
family. Reviewers saw the record and the frozen anchors; arbiters saw the
finding and the quoted record text, not the reviewer's reasoning.

Pairing (reviewer -> arbiter):

- PIN-VE-v1:    deepseek-v4-pro:0813 -> glm-5.2          REVISE, 2 MINOR — 2/2 CONFIRMED, both repaired
- PIN-SUB-v1:   glm-5.2 -> deepseek-v4-pro:0813          PASS, 3 MINOR — 3/3 CONFIRMED, all repaired
- PIN-ROLE-v1:  kimi-k2.6 -> mistral-large-3:675b        REVISE, 1 MAJOR — 1/1 CONFIRMED, repaired
- PIN-EPIST-v1: mistral-large-3:675b -> kimi-k2.6        REVISE, 5 findings — 0/5 confirmed, ALL REFUTED with quoted evidence; record stands as drafted
- BRV-v1:       minimax-m3 -> kimi-k2.7-code             REVISE, 1 MAJOR + 2 MINOR — 3/3 CONFIRMED, all repaired
- PIN-CONS-v1:  kimi-k2.7-code -> minimax-m3             REVISE, 1 BLOCKER + 2 MAJOR + 2 MINOR — 5/5 CONFIRMED, all repaired

Totals: 19 findings raised, 14 confirmed and repaired, 5 refuted.
All six records moved DRAFT_PENDING_REVIEW -> REVIEWED_PENDING_OWNER_SEAL.
Nothing sealed (owner-only); nothing merged.

## File pins (sha256 of bytes in this directory)

- PIN-VE-V1.md: 6cacc2f73af4689182495ce486d32071bdacfda5fe6bcb69c1dfe06a3dcd173d
- PIN-VE-V1.arbiter.md: 2a9d80161a5686b7434f7c4a37ee479ef2073fba87529203ce08f8f43573b9c7
- PIN-SUB-V1.md: 05d89cf65f74fd3bbe7c1e1228c1eacc12b81ed0f0a42e6ed31c77666a5fe86a
- PIN-SUB-V1.arbiter.md: ba7b3d1f976c438955065afe02cd78006694ae1bb22e958554ee4d645928b0b7
- PIN-ROLE-V1.md: a26417c7657d87bde013d36eeefff92bb4e55ba51b350398582da6e8576414be
- PIN-ROLE-V1.arbiter.md: 0d66d3a65d0715527603105ff656a25f2bc460fa486df5027851947285443a75
- PIN-EPIST-V1.md: e4c61b5bf844c7b7c040b9c7697d3e956388b0de2708e2f51e0ae35b7716ceba
- PIN-EPIST-V1.arbiter.md: 5ca9afdd8da4c1105676bbcc88a776429ccbdbd74afefb2b61d43053cbacde55
- BRV-V1.md: 380696794489de34ab1738ff5f9eda55be03fc8bbe6a77e7945d17e6954066a4
- BRV-V1.arbiter.md: 5b937005ef842c3aa5d9f622df8f7d854f618735f76af16e8bb1bac96a67454e
- PIN-CONS-V1.md: d8849c701e9eb5fb1b3486c90db55c957fd895333e1ee302687232d906706f57
- PIN-CONS-V1.arbiter.md: 2bfd021764e20e8c8b25a55d98919633d954513f7200ef15c8716c83086f73fa

## Known artifact notes

- PIN-SUB-V1.md (review): the reviewer model's NOTES section ends
  mid-sentence (model output terminated); the verdict and all three
  findings are complete. Preserved byte-identical, not repaired.

## Full-sweep ledgers (not in repo)

The six-model full-repo shuttle sweeps (profile testpoietic-rps-v1,
run_id 20260821T042622Z, seed 17, 3 votes/chunk) were interrupted by
sandbox recycling and superseded by the targeted round above. Their
hash-chained ledgers are retained off-repo; sha256:

- deepseek-v4-pro:0813: 9eab8091bda1a6b274388a882b443bf6819a1fe172e7d9aa9bc043ccc3e20f4a
- glm-5.2: b303e2f55138097715e6f2360a78e8ecea114ee98c0cea4b986f51ffc2cbef69
- mistral-large-3:675b: 10fa978a20958ffba5aa72ee2cb2c8b6cd6b3293d38ec9adc426d8e3f81cf90b
- minimax-m3: bb3ee0b02e725cd4e971a929b8a0eb86d6dd347f56260000bd695c4c42a6c235
- kimi-k2.7-code: 94486f7291dee1ef1aa6f81fbf4378d7e6f46ccb3778e68dc1d665030d22d8f1
