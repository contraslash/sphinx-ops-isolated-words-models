# Sphinx OPS Aphasia Models

This is the main repository to build an acoustic model for sphinx based on the 
[Open Speech Corpus Aphasia Corpus](http://openspeechcorpus.contraslash.com/aphasia/list/).

First execute the script `download_word_recordings.py`, this script will fetch all data from OPS.

Then execute the script `convert_mp4_to_wav.py`, to execute this script you must have [FFMpeg](https://www.ffmpeg.org/)
installed and on your path.

After you need to prepare sphinx configuration data, to achieve this:
 
Then you can call the script `configure_sphinx.py`, this script will configure almost all the files required by sphinx,
but to create a custom language model you need to execute `generate_language_model.sh`.

Make sure you have [sphinxtrain](https://github.com/cmusphinx/sphinxtrain) installed on your pc

Now execute

```bash
sphinxtrain -t ops_aphasia setup
```

After this in your etc folder you will have a full structure or what you need for your project

Please check [this link](https://cmusphinx.github.io/wiki/tutorialam/#setting-up-the-training-scripts) for further 
information.

Search for `$CFG_HMM_TYPE` and select `.semi`
If you are on a multicore machine change `$CFG_QUEUE_TYPE` to `Queue::POSIX` and `$CFG_NPART` and `$DEC_CFG_NPART` to your machine cores

Then execute the train

```bash
sphinxtrain run
```

This could take some time.

To check the results

```bash

pocketsphinx_continuous -hmm model_parameters/ops_aphasia.ci_semi/ -lm etc/ops_aphasia.lm.DMP -dict etc/ops_aphasia.dic -inmic yes   
```
