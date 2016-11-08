# Welcome to the ioRPC Documentation

## What is ioRPC

ioRPC is a minimalistic cross-platform remote procedure call library that works
over the standard input/output of processes. It allows one process to send and
receive commands from another using the standard console input and output
(think `Console.WriteLine` and `Console.ReadLine`).

## Why ioRPC

For [Unattended updates](https://www.github.com/ProjectLimitless/Unattended) I
required a way to ask the process that needs to be updated for permission before
the update is applied as well as be able to control that process. Other update
libraries did not satisfy that requirement and Unattended and ioRPC was born.

## When to use ioRPC

When you require Inter-process communication (IPC) on .NET across Windows, Linux
and macOS for controlling a subprocess. Pipes would be better, but is unsupported
on Mono. It [seems pipes have been added to .NET Core](https://docs.microsoft.com/en-us/dotnet/core/api/system.io.pipes#System_IO_Pipes),
but unfortunately Project Limitless cannot yet run on .NET Core.

## How ioRPC Works

There are two parts to an ioRPC capable application, the server and client. The
server is the application in control and is responsible for managing the
lifecycle of the client.

### Command flow

1. The ioRPC server starts
2. It launches the client process and binds to the standard in and out of the child process.
3. Commands are sent to the client using XML and `Console.WriteLine`.
4. The client receives the XML command using `Console.ReadLine` and deserializes it.
5. The deserialized command is executed (with parameters).
6. The result is written back to the server by means of `Console.WriteLine`.

Async results can be sent back at any time by using `Console.WriteLine` and the
proper XML structure.

## About the Documentation

This is part of the open-source Project Limitless documentation covering
everything developed for Project Limitless. In this documentation you will find
a [Getting Started](/getting-started) guide showing you how to use ioRPC in your own project in less
than 10 minutes.

## Contributing

If you find any errors or would like to improve the documentation, feel free
to open a pull request against the [Documentation GitHub Repo for ioRPC](https://www.github.com/ProjectLimitless/docs.projectlimitless.io)

## First Time Users

See the [Getting Started](/getting-started) guide.

## Essentials

* [NuGet](https://www.nuget.org/packages/Limitless.ioRPC/)
* [Project Build Status](https://www.projectlimitless.io/badger/iorpc)
* [Project Limitless Documentation](https://docs.projectlimitless.io)
