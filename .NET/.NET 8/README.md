# .NET 8

### Time abstraction
- new `TimeProvider` and `ITimer` interface add _time abstraction_ functionality

### New methods with random

**GetItems&lt;T>()**
- `System.Random.GetItems`
- `System.Security.Cryptography.RandomNumberGenerator.GetItems`

**Shuffle&lt;T>()**
- `Random.Shuffle`
-  `RandomNumberGenerator.Shuffle<T>(Span<T>)`

### Data validation

New data validation attributes intended for validation scenarios in cloud-native services:
- `RangeAttribute.MinimumIsExclusive`
- `RangeAttribute.MaximumIsExclusive`
- `System.ComponentModel.DataAnnotations.LengthAttribute`
- `System.ComponentModel.DataAnnotations.Base64StringAttribute`
- `System.ComponentModel.DataAnnotations.AllowedValuesAttribute`
- `System.ComponentModel.DataAnnotations.DeniedValuesAttribute`

### Cryptogaphy
- .NET 8 adds support for the SHA-3 hashing primitives
- SHA-3 is currently supported by Linux with OpenSSL 1.1.1 or later and Windows 11 Build 25324 or later

### Simplified output paths
- the new, simplified output path structure gathers all build outputs into a common location, which makes it easier for tooling to anticipate

To opt into the new output path format, use one of the following properties in your _Directory.Build.props_ file:

- Add an `ArtifactsPath` property with a value of `$(MSBuildThisFileDirectory)artifacts` (or whatever you want the folder location to be), OR
- To use the default location, simply set the `UseArtifactsOutput` property to true.

### `dotnet publish` and `dotnet pack` assets

Since the `dotnet publish` and `dotnet pack` commands are intended to produce production assets, they now produce Release assets by default.

The following output shows the different behavior between dotnet build and dotnet publish, and how you can revert to publishing Debug assets by setting the PublishRelease property to false.

```cmd
/app# dotnet new console
/app# dotnet build
  app -> /app/bin/Debug/net8.0/app.dll
/app# dotnet publish
  app -> /app/bin/Release/net8.0/app.dll
  app -> /app/bin/Release/net8.0/publish/
/app# dotnet publish -p:PublishRelease=false
  app -> /app/bin/Debug/net8.0/app.dll
  app -> /app/bin/Debug/net8.0/publish/
```

# Resources
- [What's new in .NET 8](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-8)