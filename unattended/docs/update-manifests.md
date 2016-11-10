# Update Manifests

The **U**nattended **U**pdate **M**anifest files (*.uum) specify a single update
per file. The package downloaded from the server can, however, contain multiple
files.

## AppID

The app ID is the unique ID assigned to the executable / library / module that
is used by the server to determine the application to update. This is the same
when configuring the update's [Application ID](https://docs.projectlimitless.io/unattended-server/publishing-updates#applicationid)
on the server.

## AppPath

Specifies the executable / library / module that is affected by the update. It
**must** be a .NET versioned assembly or executable.

## ServerUri

The complete address of the Unattended Server, must include protocol as well,
ex. `http://unattendedserver.local`.

## Paths

All manifest files must be saved in a single path and referenced by
[the daemon's config](/configuration#configurationdirectory).
