# Getting Started

*Tutorial length: ~10 minutes*

!!! Note
    There are currently no binary builds available for Badger, but fear not,
    building is a single command when you have [Go](https://golang.org) installed.


## Installation

### Go

You'll need Go installed to build Badger, follow their thorough
[official installation guide](https://golang.org/doc/install).

## Get the Code

```sh
> git clone https://github.com/ProjectLimitless/Badger.git Limitless.Badger
```

## Building on Linux

```sh
> cd Limitless.Badger/
> make
> ./bin/badger
```

### Testing on Linux

```sh
> cd Limitless.Badger/
> make test
```

## Building on Windows

!!! Note
    The Windows 'Make.cmd' script temporarily changes your GOPATH to the vendor
    directory. It is reverted after compiling.

```sh
> cd Limitless.Badger
> Make.cmd
> bin\badger.exe
```

## Running the Server

Open [http://127.0.0.1:8000/sample](http://127.0.0.1:8000/sample) in your browser
for the status page or
[http://127.0.0.1:8000/sample/badge](http://127.0.0.1:8000/sample/badge) for the
badge

## Basic Configuration

See the `config.json` file in the root. This file is simple and used for
configuring the server and logs.

## Required Folder Structure

### projects/

All project `*.bbproj` file must be in this directory. See the
[Project File Format](/project-file-format) section for more information.

### pages/

Project pages are stored here, see the [Project Pages](/project-pages) section
for more information.
