# harexporter

This script extracts any file from a HAR file.

## How to use

Execute the following command.

```bash
python src/harexporter.py [HAR file path] [Export URL Pattern]
```

## Example

Example of exporting any jpg files, which has a specific path and a specific CDN, from a HAR file.

```bash
python src/harexporter.py Exported_From_Chrome.har "https://cdn.example.com/file/path/*.jpg"
```
