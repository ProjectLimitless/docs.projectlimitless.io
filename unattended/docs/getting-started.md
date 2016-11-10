# Getting Started

*Tutorial length: ~30 minutes*

!!! Warning
    You must first set up an Unattended Server. Without one, you won't be able
    to check and apply updates. Follow the
    [Unattended Server Getting Started Guide now](https://docs.projectlimitless.io/unattended-server).

!!! Note
    No binary builds are currently available for Unattended, but compiling is
    very simple, all you need is C# with NuGet available.

## Installation

You can use [Microsoft Visual Studio 2015 Community Edition](https://www.visualstudio.com/vs/community/), [MonoDevelop](http://www.monodevelop.com/) or any other editor / IDE to follow
this guide as it includes nothing specific to an environment.

## Get the code

```sh
> git clone https://github.com/ProjectLimitless/Unattended.git Limitless.Unattended
```

Open the solution `Limitless.Unattended.sln` after cloning.

## Building

### Visual Studio

From the menu, select `Build->Build Solution`. That should restore NuGet packages
and compile Unattended with the sample application.

### MonoDevelop

From the menu, select `Build->Build All`. That should restore NuGet packages
and compile Unattended with the sample application.

## Running

1. Right-click on the `Unattended` project in your solution and select
`Set as Startup project`.
2. Create a new folder under `Limitless.Unattended\SampleApplication\bin\Debug`
named `20161109.0` and copy the current contents of the debug directory into
the new directory. This sets the 'last version' of the target application and
should be taken care of by the application installer.
3. Run the application (`Debug->Start Debugging` in Visual Studio and
`Run->Start Debugging` in MonoDevelop).

## Output

```sh
2016-11-09 23:16:20|INFO|Limitless.Unattended.Unattended.setup|Update strategy set as 'prompt'
2016-11-09 23:16:20|INFO|Limitless.Unattended.Unattended.setup|Update interval set as 'daily'
2016-11-09 23:16:22|INFO|Limitless.Unattended.Unattended.GetAvailableUpdates|Checking for updates...
2016-11-09 23:16:22|INFO|Limitless.Unattended.Unattended.GetAvailableUpdates|Update available for sampleapp. Version 1.0.0.1 (demo-BxDsP12ONMZAwpZ2KNrtL7TjKNNip0ck)
2016-11-09 23:16:22|INFO|Limitless.Unattended.Unattended.ProcessUpdates|1 update available
2016-11-09 23:16:23|INFO|Limitless.Unattended.Unattended.ProcessUpdates|Downloading update for sampleapp.v1.0.0.1.zip (Size 0.00241 MB) from 'http://unattendedserver.local/packages/sampleapp.v1.0.0.1.zip'
2016-11-09 23:16:23|INFO|Limitless.Unattended.Unattended.ProcessUpdates|Download completed for sampleapp.v1.0.0.1.zip. Checking integrity.
2016-11-09 23:16:23|INFO|Limitless.Unattended.Unattended.ProcessUpdates|Verified integrity of downloaded file for package sampleapp.v1.0.0.1.zip
2016-11-09 23:16:24|INFO|Limitless.Unattended.Unattended.ProcessUpdates|Target updated. New application directory is 'E:\Testing\samples\Win.Unattended\SampleApplication\bin\Debug\20161109.0\SampleApplication.exe'
2016-11-09 23:16:24|INFO|Limitless.Unattended.Unattended.Run|Task created to check for updates
2016-11-09 23:16:24|INFO|Limitless.Unattended.Unattended.IoServer_CommandResultReceived|ioRPC - Client Result: 'CanUpdate - '
2016-11-09 23:16:24|INFO|Limitless.Unattended.Unattended.Run|Start main loop...
2016-11-09 23:16:25|DEBUG|Limitless.Unattended.Unattended.Run|Loop update with ping
2016-11-09 23:16:25|INFO|Limitless.Unattended.Unattended.IoServer_CommandResultReceived|ioRPC - Client Result: 'Ping - Pong Version 1.0.0.0'
...
2016-11-09 23:16:44|INFO|Limitless.Unattended.Unattended.IoServer_CommandResultReceived|ioRPC - Client Result: 'CanUpdate - True'
2016-11-09 23:16:44|INFO|Limitless.Unattended.Unattended.ShutdownTargetApplication|Shutting down target application...
2016-11-09 23:16:44|INFO|Limitless.Unattended.Unattended.IoServer_Exited|ioRPC - Client exited
2016-11-09 23:16:45|INFO|Limitless.Unattended.Unattended.StartTargetApplication|Starting target application...
2016-11-09 23:16:46|INFO|Limitless.Unattended.Unattended.IoServer_CommandResultReceived|ioRPC - Client Result: 'Ping - Pong Version 1.0.0.1'
2016-11-09 23:16:48|INFO|Limitless.Unattended.Unattended.ShutdownTargetApplication|Shutting down target application...
2016-11-09 23:16:48|INFO|Limitless.Unattended.Unattended.IoServer_CommandResultReceived|ioRPC - Client Result: 'Exit - '
2016-11-09 23:16:48|INFO|Limitless.Unattended.Unattended.IoServer_Exited|ioRPC - Client exited
2016-11-09 23:16:49|DEBUG|Limitless.Unattended.Unattended.ShutdownTargetApplication|Target application shut down
```

Reading through the logs you will see:

1. The start of the target application
2. The query for an update
3. The download of the update
4. The updating of the target application
5. Querying the target application if the update can be applied
6. Around 20 seconds later the target replies with `true` and the target is
restarted running the new `1.0.0.1` version.

## Conclusion

You now have a sample application running that can update itself whenever a new
update is available. Use the sections on the left to learn more about the
configuration of an update manifest and the Unattended daemon process.
