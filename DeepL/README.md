# DeepL
- is a nueral machine translation service  that was launched in August 2017 and is owned by Cologne-based DeepL SE.

# How to use the DeepL API

```C#
using DeepL;
using System.Text;

Console.OutputEncoding = Encoding.UTF8;

// Create a Translator object
var apiKey = "your api key here";
var translator = new Translator(apiKey);

// Translating text
var translatedText = await translator.TranslateTextAsync("The quick brown fox jumps over the lazy dog!", null, LanguageCode.Japanese);
Console.WriteLine(translatedText);
```

### References
- [DeepL Translator](https://en.wikipedia.org/wiki/DeepL_Translator)
- [Translate text](https://developers.deepl.com/docs/api-reference/translate)