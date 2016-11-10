# Publishing updates

The server is incredibly basic. It only provides a way to add and remove updates,
most of the data needs to be entered manually. The goal is to eventually provide
an API for CI/CD tools to publish updates to. You can follow
[Issue #2](https://github.com/ProjectLimitless/UnattendedServer/issues/2) for
updates.

When you publish an update with the same Application ID but a newer version, only
the newer version will be available to Unattended.

*This document omits self-explanatory fields*

## Live updates

To see the current updates that are live, visit the Manage page available by
clicking on the 'Updates' link in the navigation bar.

## Adding a New Update

Click 'Publish new Update' in the navigation bar in the top right.

### Track

This is the update channel for the update. By default, `Stable` and `Beta` is
available.

### Application ID

This is a unique ID for your application / module / package. This ID is the same
ID you must use when
[configuring Unattended manifests](https://docs.projectlimitless.io/unattended/update-manifests#appid).

### SHA256 Hash

This hash is required to verify the integrity of the package after download. If
the hash and downloaded file's hashes don't match, the update is discarded.

**Generating the hash on Linux**

```sh
> sha256sum [filename]
```

**Generating the hash on Windows**

[Using PowerShell](https://technet.microsoft.com/en-us/library/dn520872.aspx)

*There are more tools available online.*
