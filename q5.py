#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below

###Answer examples
print "jack",distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'],set(['jack']),distsim.cossim_dense)
print "london",distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['london'],set(['london']),distsim.cossim_dense)
print "month",distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['month'],set(['month']),distsim.cossim_dense)
print "attack",distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['attack'],set(['attack']),distsim.cossim_dense)
print "happy",distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['happy'],set(['happy']),distsim.cossim_dense)
print "jail",distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jail'],set(['jail']),distsim.cossim_dense)
print "fantastic",distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['fantastic'],set(['fantastic']),distsim.cossim_dense)
