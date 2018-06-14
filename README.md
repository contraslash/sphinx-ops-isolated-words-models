# Sphinx OPS Aphasia Models

This is the main repository to build an acoustic model for sphinx based on the 
[Open Speech Corpus Aphasia Corpus](http://openspeechcorpus.contraslash.com/aphasia/list/).

First execute the script `download_word_recordings.py`, this script will fetch all data from OPS.

Then execute the script `convert_mp4_to_wav.py`, to execute this script you must have [FFMpeg](https://www.ffmpeg.org/)
installed and on your path.

After you need to prepare sphinx configuration data, to achieve this:

Make sure you have [sphinxtrain](https://github.com/cmusphinx/sphinxtrain) installed on your pc
 
Then you can call the script `configure_sphinx.py`