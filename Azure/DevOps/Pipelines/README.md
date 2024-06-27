### `azure-pipelines.yml`

Sample YAML file for ASP.NET Core:

```yaml
# ASP.NET Core
# Build and test ASP.NET Core projects targeting .NET Core.
# Add steps that run tests, create a NuGet package, deploy, and more:
# https://docs.microsoft.com/azure/devops/pipelines/languages/dotnet-core

trigger:
- master

jobs:
- job: Linux
  pool:
    vmImage: 'ubuntu-latest'

  variables:
    buildConfiguration: 'Release'

  steps:
  - script: dotnet build --configuration $(buildConfiguration)
    displayName: 'dotnet build $(buildConfiguration)'

- job: Windows
  pool:
    vmImage: 'windows-latest'
  variables:
    buildConfiguration: 'Release'
  steps:
  - script: dotnet build --configuration $(buildConfiguration)
    displayName: 'dotnet build $(buildConfiguration)'
```


### References
- [Create your first pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=net%2Cbrowser)