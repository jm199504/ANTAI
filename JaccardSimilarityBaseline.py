# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:27:29 2019

@author: cip_h
"""


from getSimilarity import Similarity

test_dict = {'Alen':{'apple','box','cub'}, 'Bob':{'apple','watch'}, 'Caeser':{'watch','egg'}}
user_list = ['Alen', 'Bob']

class JS_model():
    #Make Recommandation based on Jaccard Similarity
    def __init__(self, output_file):
        self.output_file = output_file
        
    def get_user_similarity_score(self, userlist, user_item_dict):
    #Compute JS with regulartion:
    
    #iterate in test_users, 
    #find out anyone who have bought any the same item to build friend relationship
        complete_cnt = 0
        similarity_scores = []
        for user in userlist:
            user_buy_items = user_item_dict[user]
            friends = []
            for friend, friend_buy_items in user_item_dict.items():
                if(friend != user):
                    if len(user_buy_items & friend_buy_items) > 0:
                        friends.append(friend)
            
            similarity_scores_row = []
            for friend in friends:
                #Calculate Jaccard similarity bettween test_user and his or her friends
                simi = Similarity()
                score = simi.jaccard_similarity(user_item_dict[user], user_item_dict[friend])
                similarity_scores_row.append((friend , score))
                
            similarity_scores_row.sort(reverse = True, key = lambda x : x[1])
            
            #save only top 20 JS friends
            similarity_scores.append(similarity_scores_row[0:min(len(similarity_scores_row), 20)])
            complete_cnt += 1
            print('complete cnt:{}'.format(complete_cnt))
        print(similarity_scores)
        with open(self.output_file, 'w') as fw:
                fw.write('\n'.join([','.join([str(p[0]) + ',' + str(p[1]) for p in row]) for row in similarity_scores]))
            
    #get_recommend_item(user_id):
    #get all related items (userself and his or her friends's)
    #iterate among related items
        #iterate among friends
            #calculate item_score
    
    #return top 30 item_score

model = JS_model('./TEST')
model.get_user_similarity_score(user_list, test_dict)

    