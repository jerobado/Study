# BackgroundService
- `BackgroundService` is a base class for implementing a long running `IHostedService`.

```C#
// SampleService.cs
namespace Sample.Services
{
    public class StudyBackgroundService : BackgroundService
    {
        private readonly IServiceProvider _serviceProvider;

        public StudyBackgroundService(IServiceProvider serviceProvider)
        {
            _serviceProvider = serviceProvider;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            while (!stoppingToken.IsCancellationRequested)
            {
                using var scope = _serviceProvider.CreateScope();
                var scopeProvider = scope.ServiceProvider;
                var context = scope.ServiceProvider.GetRequiredService<HealthDbContext>();

                var weight = new Weight
                {
                    Id = Guid.NewGuid(),
                    Value = rnd.Next(0, 100),
                    DateCreated = DateTime.UtcNow,
                    DateUpdated = DateTime.UtcNow
                };
                context.Weights.Add(weight);
                await context.SaveChangesAsync(stoppingToken);

                Console.WriteLine($"{weight.Id}: {weight.Value} has been added");

                await Task.Delay(TimeSpan.FromSeconds(5), stoppingToken);
            }
            
        }
    }
}
```

Register your background service

```C#
// Program.cs
builder.Services.AddHostedService<SampleService>();
```