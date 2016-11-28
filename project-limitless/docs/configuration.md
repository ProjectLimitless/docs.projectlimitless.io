# Configuration

The configuration is built up by loading the Core configuration, the module
configurations and then merging the User configuration over it. The User
configuration can override any setting in Core or Modules - anything not
overwritten will use the defaults from Core of the module.

## Why TOML?

**T**om's **O**bvious, **M**inimal **L**anguage ([GitHub](https://github.com/toml-lang/toml))
is a language specifically designed for configuring software. It is both easy to
read for humans and parse for robots. It was chosen over JSON and XML as it is
far less error prone and allows comments.

## Core

### Name `(string)`

The default name of the system. Also serves as the default trigger word.

### EnabledModules `(string[])`

The list of modules that should be loaded for use. Only the name ** excluding**
extension.

## Modules

The module configuration documentation is available under the [Modules](/modules)
section.
