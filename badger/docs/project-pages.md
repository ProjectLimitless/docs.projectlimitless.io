# Project Pages

Project Pages allow your project to show all the statuses on a single page as
HTML. Every project that is developed for Project Limitless has a Badger page
and badge set up, see the
[ioRPC Status Page](https://www.projectlimitless.io/badger/iorpc) as an example.

## HTML Templating

Badger makes use of [Go's templating system](https://golang.org/pkg/html/template/)
and allows everything it can do.

## Available Objects

The `PageData` struct is sent to the page for rendering, the definition can be
found [on GitHub](https://github.com/ProjectLimitless/Badger/blob/master/src/badger/structs.go).

### .ProjectName

Provides the name of the project as specified in the `.bbproj` file.

### .Overall.Status

Combines the statuses from all the providers into one, if any of them have failed,
the overall status will show failed as well.

### .Providers

The map of configured providers and their results. Contains the provider's name
as the key and status as the value. The full definition of the `ProviderResult` is
[available on GitHub](https://github.com/ProjectLimitless/Badger/blob/master/src/badger/parsers/structs.go).

Iterating over the providers can be done as `{{ range $provider, $status := .Providers}}`
