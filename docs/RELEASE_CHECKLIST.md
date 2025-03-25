## About
This document contains information on how to create and maintain releases for this project


## Stable Release
1. Make changes to any theme(-s)
2. Update [VERSIONS_ARCHIVE.md](../VERSIONS_ARCHIVE.md) :
   - Change old versions link from `*/releases/latest/download/*` to `*/releases/{tagname}/download/*`
   - Add new version with link to `*/releases/latest/download/*`
3. Add new version to table in [README.md #development-status](../README.md#development-status)
4. Commit changes and create a new tag following the next naming template:
   - `release-yyyymmdd` *(optional `-<codename>` at the end)*
5. Merge all the changes to `master` branch
6. Push all changes and the tag to remote
7. Create the Github release
8. That's it - Github Actions CI will now take care of all that's left, watch and **pray** 👏
