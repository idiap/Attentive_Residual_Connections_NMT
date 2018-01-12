'''
Copyright (c) 2017 Idiap Research Institute, http://www.idiap.ch/
Written by Lesly Miculicich <lmiculicich@idiap.ch>
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import codecs
import sys
import os
from matplotlib import font_manager

fontP = font_manager.FontProperties()
fontP.set_family('Droid Sans Fallback')
fontP.set_size(14)

arg = sys.argv[1:]

# read arguments
file_source = arg[0]
file_target = arg[1]
n_sent = int(arg[2])
	
# read files
align = np.load(file_target + "_align.npy")
source = codecs.open(file_source,"r","utf-8", errors='ignore')
target = codecs.open(file_target,"r")
previous = None
if os.path.isfile(file_target + "_prev_words.npy"):
	previous = np.load(file_target + "_prev_words.npy")

# read senteces
s_source = source.readlines()[n_sent-1].strip().split(" ")
s_target = target.readlines()[n_sent-1].strip().split(" ")
source.close()
target.close()

# Draw alignment matrix for all models. Draw matrix of attention for the attentive model

if not "attentive" in file_target:
	m_align = np.array(align[n_sent-1])[:-1,:-2].T
	m_align = np.insert(m_align, 0, np.zeros(m_align.shape[1]),0)
	fig, ax_2 = plt.subplots(figsize=(20, 5))
else:
	m_align = np.array(align[n_sent-1])[:-1,:-1].T
	fig, [ax, ax_2] = plt.subplots(2,1,sharex=True, figsize=(20, 10))
	shift = 2
	m_previous = np.zeros([len(previous[n_sent-1])-1, len(previous[n_sent-1][-1])-shift])
	for i in range(len(previous[n_sent-1])-1):
		line = previous[n_sent-1][i]
		m_previous[i,0:len(line)-shift] = line if shift == 0 else line[1:-1]

	heatmap = ax.pcolor(m_previous, cmap=plt.cm.Reds, alpha=0.8)
	ax.set_frame_on(False)
	ax.set_yticks(np.arange(m_previous.shape[0]) + 0.5, minor=False)
	ax.set_xticks(np.arange(m_previous.shape[1]) + 0.5, minor=False)
	ax.invert_yaxis()
	ax.xaxis.tick_top()
	ax.set_xticklabels(s_target, minor=False, size=15)
	ax.set_yticklabels(s_target, minor=False, size=15)
	ax.grid(False)
	for t in ax.xaxis.get_major_ticks():
		t.tick10n = False
		t.tick2On = False
	for t in ax.yaxis.get_major_ticks():
		t.tick1On = False
		t.tick2On = False
	for tick in ax.get_xticklabels():
		tick.set_rotation(20)

m_align=m_align[:len(s_source),:len(s_target)]

heatmap_2 = ax_2.pcolor(m_align, cmap=plt.cm.Blues, alpha=0.8)
ax_2.set_frame_on(False)
ax_2.set_yticks(np.arange(m_align.shape[0]) + 0.5, minor=False)
ax_2.set_xticks(np.arange(m_align.shape[1]) + 0.5, minor=False)
ax_2.invert_yaxis()
ax_2.xaxis.tick_top()
ax_2.set_xticklabels(s_target, minor=False, fontproperties=fontP, size=15)
ax_2.set_yticklabels(s_source, minor=False, size=15)
ax_2.grid(False)

for t in ax_2.xaxis.get_major_ticks():
	t.tick10n = False
	t.tick2On = False
for t in ax_2.yaxis.get_major_ticks():
	t.tick1On = False
	t.tick2On = False

#fig.savefig(str(n_sent)+".png")
plt.show()

