# Modules

Modules are dynamically loaded assemblies that implement a part of the execution
chain. All modules implement the `IModule` interface from
[Limitless.Runtime](https://docs.projectlimitless.io/Limitless.Runtime).

## Configuration

A module can implement any configuration that can be loaded from a TOML file. The
module loader will pass the parsed configuration to your module in the
`Configure(dynamic settings)` method. The configuration will be of the `Type`
as returned by `GetConfigurationType`.

### GetConfigurationType

Must return the `typeof()` for the configuration class of your module.

## Building your own Module

TODO: Once modules have been locked down, this will be written as a tutorial
