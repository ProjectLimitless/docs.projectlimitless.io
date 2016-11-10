# Configuring the Unattended Service Daemon

The daemon is configured by using the standard .NET XML configuration file
located with the `.exe` named `Limitless.Unattended.ServiceDaemon.exe.config`.

## clientid

The client ID is a unique identifier for this instance of Unattended.

## configurationDirectory

The directory where the [Update Manifests](/update-manifests) can be found.

## strategy

The update strategy determines what to do when an update is available.

### prompt

Query the target application to ask for permission to apply the update and restart
the application.

### restart

Apply the update and restart the application as soon as the update is ready. This
is the default.

## interval

When to check for updates.

### daily

Check once a day.

### hourly

Check once an hour. This is the default.

## channel

The update channel to check. Currently options are `stable` and `beta`.

## basePath

The directory containing the target application.

## filename

The filename of the target application.

## parameters

Parameters to pass to the target application when launching.
