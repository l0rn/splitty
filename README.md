
# Splitty the video by-chapter splitter

This Python script splits video files into chapters. It uses FFmpeg for video processing, so make sure you have it installed on your system.

## Usage

```bash
python split.py <video-files> [-mf <merge-first>] [-ml <merge-last>]
```

<video-files> are the video files to split.
<merge-first> is an optional argument specifying the number of chapters to merge into the first output file.
<merge-last> is an optional argument specifying the number of chapters to merge into the last output file.

## Dependencies

This script requires FFmpeg to be installed on your system. You can download it here.

## License

MIT