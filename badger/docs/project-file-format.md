# The Project File Format

## Name

```json
"name": "Sample"
```

Specifies the name of the project. Also used in the page title.

## Statuses

```json
"Statuses": [
    {
        "Type": "Build",
        "Provider": "AppVeyor",
        "Url": "http://ci.appveyor.com/api/projects/donovansolms/ioRPC"
    }
    ...
    ...
],
```

The statuses section defines the integration statuses to fetch from the specified
`Url`s. You can specify as many statuses as you want. The `Url` should point to
the API page which usually contains JSON or XML.

!!! note
    Currently, only 'AppVeyor' and 'TravisCI' providers are available as well as
    only the 'Build' type. Feel free to
    [create a new issue](https://github.com/ProjectLimitless/Badger/issues) if you
    would like to see your favourite tool included.

## Badge

```json
"Badge": {
    "Template": {
        "Background": "sample/background.png",
        "Badges": {
            "Passing": "build-passing.png",
            "Failing": "build-failing.png",
            "Unknown": "build-unknown.png"
        }
    },
    "Overlays": [
        {
            "Provider": "AppVeyor",
            "Position": {
                "Left": 130,
                "Top": 30
            }
        }
    ]
}
```

### Template

This section defines the look of the template. If the background image is not
found, Badger attempts to use `badges/default.png` as the template.

### Overlays

The overlays specify where `Template.Badges.Passing`, `Template.Badges.Failing`
and `Template.Badges.Unknown` should be positioned on top of `Template.Background`
for the given provider.

`Provider` must match those specified in [Statuses](/project-file-format/#statuses).

## Page

```json
"Page": {
    "Template": "sample/page.html"
}
```

Specifies the template for the project page. If the specified page could not be
found, Badger tries to use `pages/default.html` as the template. See the next
section on [project pages](/project-pages) for more information.
