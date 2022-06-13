#!/usr/bin/env python

import os
import pickle

import utils

parser = utils.training.add_args()
parser.set_defaults(logdir=os.environ.get("GROK_LOGDIR", "."))
hparams = parser.parse_args()
hparams.datadir = os.path.abspath(hparams.datadir)
hparams.logdir = os.path.abspath(hparams.logdir)

print(hparams)
with open('hparams.pkl', 'wb') as f:
    pickle.dump(hparams, f)
print(utils.training.train(hparams))
