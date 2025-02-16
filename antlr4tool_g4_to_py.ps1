# Define the path to the ANTLR4 jar file and the grammar file
$rootPath = "C:\UserData\antlr4_sql"
$antlr4JarPath = "$rootPath\packages\antlr-4.13.2-complete.jar"
$grammarFilePath = "$rootPath\tdh\grammar\HiveParser.g4"
$grammarLibPath = "$rootPath\tdh\grammar\HiveLexer.g4"
$outputDirectory = "$rootPath\tdh\antlr4"

# Ensure the output directory exists
if (-Not (Test-Path $outputDirectory)) {
    New-Item -ItemType Directory -Path $outputDirectory
}

# Compile the grammar file to generate Python code
# echo "java -jar $antlr4JarPath -Dlanguage=Python3 -o $outputDirectory -listener -visitor $grammarFilePath -lib $grammarLibPath"
java -jar $antlr4JarPath -Dlanguage=Python3 -o $outputDirectory -listener -visitor  $grammarLibPath $grammarFilePath 

Write-Host "ANTLR4 grammar compiled successfully. Generated files are in $outputDirectory"