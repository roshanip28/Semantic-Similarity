#!/usr/bin/env python
import distsim

# you may have to replace this line if it is too slow 
word_to_ccdict = distsim.load_contexts("nytcounts.4k")


### provide your answer below

###Answer examples
print "jack",distsim.show_nearest(word_to_ccdict, word_to_ccdict['jack'],set(['jack']),distsim.cossim_sparse)
print "london",distsim.show_nearest(word_to_ccdict, word_to_ccdict['london'],set(['london']),distsim.cossim_sparse) #london is a proper noun: Name
print "month",distsim.show_nearest(word_to_ccdict, word_to_ccdict['month'],set(['month']),distsim.cossim_sparse) # month is a common noun
print "attack",distsim.show_nearest(word_to_ccdict, word_to_ccdict['attack'],set(['attack']),distsim.cossim_sparse) #attack is a verb
print "happy",distsim.show_nearest(word_to_ccdict, word_to_ccdict['happy'],set(['happy']),distsim.cossim_sparse) #happy is an adjective
print "jail",distsim.show_nearest(word_to_ccdict, word_to_ccdict['jail'],set(['jail']),distsim.cossim_sparse)
print "fantastic",distsim.show_nearest(word_to_ccdict, word_to_ccdict['fantastic'],set(['fantastic']),distsim.cossim_sparse) #six
