# Welcome to the Unattended Documentation

## What is Unattended

A simple update library for .NET and Mono. Capable of rolling back on failure
as well as asking the application being updated if it is allowed to do so.

## Why Unattended

For the core application in Project Limitless I required a way to:

* Update any (many) modules and pieces separately, automatically
* The core must check with the user / service if it is allowed to restart and
apply the update. This is so that an update never breaks a user interaction.
* If the update fails to start, roll back to the last working version
* Must be completely cross-platform

None of the libraries I found satisfied all the above, which is why Unattended
was born.

## When to use Unattended

When you need an open source update solution for an executable and its
dependencies, or need any of the features listed under
[Why Unattended](#why-unattended).

## How Unattended Works

1. When the Unattended service daemon is started, the application executable is
run using a subprocess.
2. The update configurations are loaded from the specified directory.
3. Update configurations specify all libraries and files that should be checked
for updates as well as how often and where.
4. According to the update schedule, the service daemon will check if updates
are available.
5. If an update is found, the daemon will create a new 'latest' directory for
the application and make a clone of the current files into that directory.
6. Once the clone is completed, the updated files are inserted into the newly
created 'latest' directory.
7. Using ioRPC, Unattended checks with the application if it is Ok to restart it
with the update applied.
8. Once the application returns the Ok to Unattended, the application if stopped
and restarted.
9. If the application fails to start after an update, the previous version is
started and the application if notified of the failure with details.

To learn more about configuring updates, see the
[Update Manifests](/update-manifests).

*The update strategy is inspired by
[how CoreOS Updates work](https://coreos.com/os/docs/latest/update-strategies.html)*.

## The Update Server

A basic (but complete) server to serve the updates is available as a separate
project [Unattended Server](https://github.com/ProjectLimitless/UnattendedServer).
It is built using the [Yii Framework](http://www.yiiframework.com/) and
[PHP](http://www.php.net).

## About the Documentation

This is part of the open source Project Limitless documentation covering
everything developed for Project Limitless. In this documentation you will find
a [Getting Started](/getting-started) guide showing you how to use Unattended in
your own project in less than 30 minutes. It **does not cover the server**, those can
be found under the
[Unattended Server documentation](https://docs.projectlimitless.io/unattended-server).

## Contributing

If you find any errors or would like to improve the documentation, feel free
to open a pull request against the [Project Limitless Documentation GitHub Repository](https://www.github.com/ProjectLimitless/docs.projectlimitless.io).

## First Time Users

See the [Getting Started](/getting-started) guide.

## Essentials

* [Project Build Status](https://www.projectlimitless.io/badger/unattended)
* [Project Limitless Documentation](https://docs.projectlimitless.io)
