# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:27:29 2019

@author: cip_h
"""
from getSimilarity import Similarity


class JS_model():
    '''
        基于集合相似度的推荐模型
    '''
    def __init__(self):
        '''
            初始化JS_model对象
            user_similarity_scores---用户的朋友集合相似度
            user_recommand_items-----用户的推荐物品集合
            simi---------------------实例化的集合相似度计算模型
        '''
        self.user_similarity_scores = []
        self.user_recommand_items = []
        self.simi = Similarity()
        return None
        
    def get_recommand_items(self, top_n_friends, userlist, user_item_dict):
        '''
            获得推荐物品
            top_n_friends---选择前n大集合相似度的朋友
            userlist--------输入需要推荐物品的用户列表
            user_item_dict--所有用户物品购买记录的字典
        '''
        for complete_cnt, user in enumerate(userlist):
            friends_similarity_scores = []
            recommand_items = []
    
            user_buy_items = user_item_dict[user]
            items_related = user_buy_items.copy()
            
            for friend, friend_buy_items in user_item_dict.items():
                if (friend != user) and len(user_buy_items & friend_buy_items) > 0:
                    #遍历user_item_dict字典中的所有用户，如果user与friend所购买的物品存在交集，则计算集合相似度
                    score = self.simi.jaccard_similarity(user_item_dict[user], user_item_dict[friend])
                    friends_similarity_scores.append((friend , score))

            #判断该user是否有朋友
            if len(friends_similarity_scores) == 0:
                print('user {} has no friends!'.format(user))
                print('so we recommand what the user buy before!')
                recommand_items = list(user_buy_items)
                #推荐给用户之前买过的物品
            else:
                friends_similarity_scores.sort(reverse = True, key = lambda x : x[1])
                friends_similarity_scores = friends_similarity_scores[0:min(len(friends_similarity_scores), top_n_friends)]
                #save only top n score friends
                #只选出前top n个朋友
                
                for friend, score in friends_similarity_scores:
                    #将朋友购买过的物品加入相关物品集合中
                    for item in user_item_dict[friend]:
                        items_related.add(item)
                
                #计算每个物品的得分
                items_scores = []
                for item in items_related:
                    item_score = 0
                    for friend, score in friends_similarity_scores:
                        #如果朋友购买过该物品，则加上该朋友分
                        if item in user_item_dict[friend]:
                            item_score += score
                    items_scores.append((item, item_score))
                
                #选择物品得分最高的前30个物品作为土建物品
                items_scores.sort(reverse = True, key = lambda x : x[1])
                recommand_items = [item for item, score in items_scores[0:min(len(items_scores), 30)]]
            
            self.user_recommand_items.append(recommand_items)
            self.user_similarity_scores.append(friends_similarity_scores)

            print('complete cnt:{}'.format(complete_cnt))
        
        
        def evaluate():
            #待实现
            raise 'Not Implemented!'
        
    
if __name__ == '__main__':
    
    #单元测试数据
    test_dict = {'Alen':{'apple','box','cub'}, 'Bob':{'apple','watch'}, 'Caeser':{'watch','egg'}}
    user_list = ['Alen', 'Bob']
    
    model = JS_model()
    model.get_recommand_items(20, user_list, test_dict)
    similarity_scores = model.user_similarity_scores
    print(similarity_scores)
    
    items = model.user_recommand_items
    print(items)

#    output_file = './TEST'
#    with open(output_file, 'w') as fw:
#            fw.write('\n'.join([','.join([str(p[0]) + ',' + str(p[1]) for p in row]) for row in similarity_scores]))    