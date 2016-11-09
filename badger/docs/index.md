# Welcome to the Badger Documentation

## What is Badger

A server that combines multiple continuous integration tools' statuses into a
single badge with templating.

### Samples

[Badger HTML Page for ioRPC](https://www.projectlimitless.io/badger/iorpc)

[![Build status](https://www.projectlimitless.io/badger/iorpc/badge)](https://www.projectlimitless.io/badger/iorpc)

## Why Badger

Some projects are built for different platforms using different continuous
integration tools, each of them have their own build status badges that look
different. This tool creates a URL to embed that generates a single status badge
for each platform using the template you specify.

Project Limitless aims to be fully cross-platform and thus the build status for
each platform should be displayed.

## How Badger Works

On each request to the badge or status page, Badger makes calls to the specified
services to retrieve the statuses and renders the result.

## About the Documentation

This is part of the open-source Project Limitless documentation covering
everything developed for Project Limitless. In this documentation you will find
a [Getting Started](/getting-started) guide showing you how to use Badger for
your own project in less than 10 minutes.

## Contributing

If you find any errors or would like to improve the documentation, feel free
to open a pull request against the [Documentation GitHub Repo for Badger](https://www.github.com/ProjectLimitless/docs.projectlimitless.io)

## First Time Users

See the [Getting Started](/getting-started) guide.

## Essentials

* [Project Build Status](https://www.projectlimitless.io/badger/badger)
* [Project Limitless Documentation](https://docs.projectlimitless.io)
