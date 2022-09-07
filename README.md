# mkv2mp4
Script for converting MKV files to MP4 from a given directory

### Usage
`py mkv2mp4py.py`

### Config
The path for mkv files must be specified at the script:
`root = 'Series/'`

####  Options
- Comment the line 14 to disable the exclusion of mkv file after the transcode.
- Comment the line 15 to disable the timer.

### Output
The script will transcode the mkv file to mp4 and delete the previosly mkv file, keeping only the mp4. **A backup of the mkv files that will be transcode is recommended**.
