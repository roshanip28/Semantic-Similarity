#!/usr/bin/env python
import distsim
from prettytable import PrettyTable
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
#x = PrettyTable()
x.field_names = ["Word", "1-Best", "5-Best", "10-Best"]
list1 = []
ct1 = 0
ct2 = 0
ct3 = 0
skip=0
with open('word-test.v3.txt') as f:
    f1=f.readlines()[1:]
#next(f1)
#next(f1)
for line in f1:
    #print line
    flag = 0
    if skip==0:
        if ":" in line:
            skip=1
            name=line.split()[1]
            continue
    if ":" in line:
        for item_in_list in list1:
            if item_in_list == 0:
                #print item_in_list
                ct1 += 1
            if item_in_list >= 0 and item_in_list <= 4:
                #print item_in_list
                ct2 += 1
            if item_in_list >= 0 and item_in_list <= 9:
                #print item_in_list
                ct3 += 1
        #print line.split()[1]
        #print list1, ct1, ct2, ct3
        #print list1
        if len(list1)!=0:
            #print float(ct1) / float(len(list1)), float(ct2) / float(len(list1)), float(ct3) / float(len(list1))
            ans1= round(float(ct1) / float(len(list1)),3)
            ans2= round(float(ct2) / float(len(list1)),3)
            ans3= round(float(ct3) / float(len(list1)),3)
            print name,":"
            print "1-Best: ",ans1," 5-Best: ",ans2," 10-Best: ",ans3
            #x.add_row([name, ans1, ans2, ans3])
            name=line.split()[1]
            #print name


        list1 = []
        ct1 = 0
        ct2 = 0
        ct3 = 0
        continue

    #print line,"----"
    words=line.split()
    #print words[0],words[1],words[3]
    #print words[2]
    w1 = word_to_vec_dict[words[0]]
    w2 = word_to_vec_dict[words[1]]
    w3 = word_to_vec_dict[words[3]]

    result = distsim.show_nearest(word_to_vec_dict,w1-w2+w3,set([words[0],words[1],words[3]]),distsim.cossim_dense)

    for a in range(0,10):
        #print result[a][0],line
        if result[a][0]==words[2]:
            #print words[2],"******************",result[a][0]
            list1.append(a)
            flag = 1
            break
    if flag == 0:
        list1.append(-1)
else:
    for item_in_list in list1:
        if item_in_list == 0:
            # print item_in_list
            ct1 += 1
        if item_in_list >= 0 and item_in_list <= 4:
            # print item_in_list
            ct2 += 1
        if item_in_list >= 0 and item_in_list <= 9:
            # print item_in_list
            ct3 += 1
    # print line.split()[1]
    #print list1, ct1, ct2, ct3
    if len(list1) != 0:
        # print float(ct1) / float(len(list1)), float(ct2) / float(len(list1)), float(ct3) / float(len(list1))
        ans1 = round(float(ct1) / float(len(list1)), 3)
        ans2 = round(float(ct2) / float(len(list1)), 3)
        ans3 = round(float(ct3) / float(len(list1)), 3)
        print name, ":"
        print "1-Best: ", ans1, " 5-Best: ", ans2, " 10-Best: ", ans3
       # x.add_row([name, ans1, ans2, ans3])
#print x
