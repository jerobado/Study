/*
 * 1. Create a regex pattern
 * 2. Use Match() method find pattern in ProjectDescription
 * 3. If Match.Success, remove matched pattern in ProjectDescription using String.Replace() method
 */


using System;
using System.Text.RegularExpressions;


namespace RegexTutorial
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("C# Regular Expression\n");

            // OKAY
            //var sampleText = "BA8234732 - Gerol Bado Project";
            //var sampleText = "INC8234732 - Gerol Bado Project";
            //var sampleText = "LINK034 - Gerol Bado Project";
            //var sampleText = "REQ298374892374983274 - Gerol Bado Project";
            //var sampleText = "ADMINISTRATION";
            //var sampleText = "BakerAsssyt Support";
            //var sampleText = "SC8234732 Gerol Bado Project";
            //var sampleText = "BA192783 Support";
            //var sampleText = "LINK09 Gerol Bado Project";
            //var sampleText = "S589374- Gerol Bado Project";
            //var sampleText = "S589374 -Gerol Bado Project";
            //var sampleText = "NOC Intake System";
            //var sampleText = "PDcalendar DLL";
            //var sampleText = "00000014 - Gerol Bado Project";
            //var sampleText = "Gerol Bado Project";
            //var sampleText = "00000015 Gerol Bado Project";
            //var sampleText = " 372 BakerWorld to SharePoint 2019";
            //var sampleText = "000 - My PBS21";
            //var sampleText = "007 - My BitLocker";
            //var sampleText = "1234  - Gerol Bado Project";


            var sampleText = "Zero pattern!";
            //var sampleText = "SC23423 Legal Knowhow Portal";

            Console.WriteLine(sampleText);
            Console.WriteLine(TrimProjectDescription(sampleText));

        }


        static string TrimProjectDescription(string projectDescription)
        {
            var digitPattern = @"\s*\d+";                   // i.e. 000, 0000123, ' 372'
            var alphanumericPattern = @"([A-Z]+\d+)";       // i.e. S584931, BA378232, LINK014
            var dashspacePattern = @"(\s*-*\s*)";           // i.e. ' - ', '- ', ' -', ' '

            var pattern = $"^({digitPattern}|{alphanumericPattern}){dashspacePattern}";
            var regex = new Regex(pattern);

            var match = regex.Match(projectDescription);

            if (match.Success)
            {
                return projectDescription.Replace(match.Value, "");
            }
            else
            {
                return projectDescription;
            }

        }



    }
}
