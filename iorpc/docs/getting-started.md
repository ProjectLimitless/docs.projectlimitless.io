# Getting Started

*Tutorial length: ~10 minutes*

You can use [Microsoft Visual Studio 2015 Community Edition](https://www.visualstudio.com/vs/community/), [MonoDevelop](http://www.monodevelop.com/) or any other editor / IDE to follow
this guide as it includes nothing specific to an environment.

!!! Tip
    The fastest way to try out ioRPC is to download the source and run the [sample application](https://github.com/ProjectLimitless/ioRPC/tree/master/Samples)

## Installation

* Create a new `Console Application` and name it `SampleServer`

This will serve as the ioRPC **server**. Using the NuGet Package Manager,
install [ioRPC](https://www.nuget.org/packages/Limitless.ioRPC/).

* Add another new `Console Application` and name it `CalculatorClient`

This will serve as the ioRPC **client**. Also install [ioRPC](https://www.nuget.org/packages/Limitless.ioRPC/)
from NuGet to the client.

## The Calculator Client

* Create a simple `Calculator` class

```csharp
public class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }
}
```

* Register the `Calculator` as the RPC Handler

```csharp
static void Main(string[] args)
{
    Calculator calc = new Calculator();
    Client client = new Client(calc);
    client.Listen();
}
```

## The Server

The server requires slightly more work to get running.

```csharp
static void Main(string[] args)
{
    ProcessStartInfo startInfo = new ProcessStartInfo();
    // For the demo, I'm hardcoding the path the calculator client
    startInfo.FileName = @"C:\Projects\iorpc-client\bin\Debug\CalculatorClient.exe";

    using (Server ioServer = new Server(startInfo))
    {
        ioServer.CommandResultReceived += Iorpc_CommandResultReceived;
        ioServer.Start();

        Console.WriteLine("[SampleServer] Server Started...");

        while (Console.KeyAvailable == false)
        {
            Console.WriteLine("[SampleServer] Server Running...");
            Thread.Sleep(1000);

            ioCommand add = new ioCommand("Add");
            add.Parameters.Add(7);
            add.Parameters.Add(5);
            ioServer.Execute(add);
        }
        ioCommand exit = new ioCommand("Exit");
        ioServer.Execute(exit);
    }
    Console.WriteLine("[SampleServer] Done. Press any key to exit.");
    Console.ReadLine();
}

private static void Iorpc_CommandResultReceived(object sender, Limitless.ioRPC.Events.ioEventArgs e)
{
    Console.WriteLine("[SampleServer] Received RPC Call Result: fn({0}) {1}", e.CommandName, e.Data);
}
```

!!! warning
    Ensure you compile the child application before trying to run the server

* Run the server

You should see the result from the calculator every second, press any key to
stop and exit.

```bash
[SampleServer] Server Started...
[SampleServer] Server Running...
[SampleServer] Received RPC Call Result: fn(Add) 12
[SampleServer] Server Running...
[SampleServer] Received RPC Call Result: fn(Add) 12
[SampleServer] Server Running...
[SampleServer] Received RPC Call Result: fn(Add) 12
[SampleServer] Server Running...
[SampleServer] Received RPC Call Result: fn(Add) 12
[SampleServer] Received RPC Call Result: fn(Exit)
[SampleServer] Done. Press any key to exit.
```

* Update the Calculator

On your own, add a subtract call to the calculator and execute the function
using your server.

* As easy as that

That is all you need to run ioRPC. You can see the [sample application](https://github.com/ProjectLimitless/ioRPC/tree/master/Samples)
for the use of async results.
