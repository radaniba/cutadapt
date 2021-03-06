from __future__ import print_function, division

from cutadapt.seqio import ColorspaceSequence
from cutadapt.adapters import ColorspaceAdapter, PREFIX
from cutadapt.scripts.cutadapt import RepeatedAdapterMatcher

def test_cs_5p():
	read = ColorspaceSequence("name", b"0123", b"DEFG", b"T")
	adapter = ColorspaceAdapter(b"CG", PREFIX, 0.1)
	cutter = RepeatedAdapterMatcher([adapter])
	matches = cutter.find_match(read)
	# no assertion here, just make sure the above code runs without
	# an exception
