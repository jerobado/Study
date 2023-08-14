# How to use the DeepL API

```C#
using DeepL;

// Create a Translator object
var apiKey = "your api key here";
var translator = new Translator(apiKey);

// Translating text
var translatedText = await translator.TranslateTextAsync("The quick brown fox jumps over the lazy dog!", null, LanguageCode.Japanese);
Console.WriteLine(translatedText);
```
