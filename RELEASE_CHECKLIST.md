# Release Checklist

This checklist is for preparing `exhibit-interaction-diagram` as a GitHub-ready skill package.

## v0.1-alpha local packaging

- [x] Remove local `outputs/` from the publishable skill directory.
- [x] Remove `.DS_Store` files.
- [x] Add `.gitignore` for local outputs, system files, caches, and env files.
- [x] Add `LICENSE`.
- [x] Add README installation instructions.
- [x] Add README showcase images.
- [x] Add README demo GIF.
- [x] Add script to regenerate the demo GIF.
- [x] Add VHS tape for terminal demo recording.
- [x] Add skills.sh badge placeholder for the planned public repo.
- [x] Add marketplace metadata.
- [x] Keep stable showcase images in `examples/showcase/`.
- [x] Keep regression cases in `test-prompts.json`.
- [x] Keep structure check script in `scripts/check-test-prompts.py`.

## Before pushing to GitHub

- [ ] Confirm the final GitHub path is `logic0512/exhibit-interaction-diagram`.
- [ ] Run `python3 scripts/check-test-prompts.py`.
- [ ] Run Luban repo check.
- [ ] Confirm no private paths, temporary exports, working files, or customer files are included.

## After GitHub repository exists

- [ ] Test `npx skills add logic0512/exhibit-interaction-diagram` from the public repo.
- [ ] Add the real install output to release notes or README if needed.
- [ ] Check README rendering on GitHub, especially image paths.
- [ ] Check skills.sh badge after the repo is public and indexed.
- [ ] Check marketplace metadata if publishing through a plugin/marketplace channel.
- [ ] Tag `v0.1-alpha` only after install and README rendering are verified.
