# Theme Update Procedure

1. Make changes to any theme(-s)
2. Update [VERSIONS_ARCHIVE.md](../VERSIONS_ARCHIVE.md) :
   - Change old versions link from `*/releases/latest/download/*` to `*/releases/{tagname}/download/*`
   - Add new version with link to `*/releases/latest/download/*`
3. Add new version to table in [README.md #development-status](../README.md#development-status)
4. Commit and Create new tag. Name sample: `release-ddmmyyyyhhmm`
5. Push tag to remote and create **release**
6. ~~Attach <ins>ALL</ins> theme files *(Even if they don't have any changes)* to release to make `*/releases/latest/download/*` work properly~~
    > Files are now automatically attached to release with Github Actions
7. That's all, watch and **pray** 👏
