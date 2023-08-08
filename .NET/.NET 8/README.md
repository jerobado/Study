# .NET 8

### Time abstraction
- new `TimeProvider`` and `ITimer` interface add _time abstraction_ functionality

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

# Resources
- [What's new in .NET 8](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-8)