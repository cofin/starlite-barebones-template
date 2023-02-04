# Release Guide

This guide will walk you through the steps to release a new version of the project.

## Prerequisites
- [ ] Ensure you have the latest version of the `main` branch

## Steps
- [ ] Run `make pre-release` to bump the version, build the docs, and clean up stale files
- [ ] Draft a new release on GitHub, using the version number as the tag
- [ ] Update the `CHANGELOG.md` file with the release notes
- [ ] Commit the changes to `main` and push them to GitHub
- [ ] Publish the release on GitHub
- [ ] Ensure the GitHub Actions workflow for `release` has completed successfully
