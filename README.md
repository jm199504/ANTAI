## ANTAI (Jimmy.Guo)

**Method - 1**

***1. Find the other users who have the same items with user_A to build friend relationship***

***2. Calculate the Jaccard distance of user_A and his friends***

***3. Calculate the score of each item of user_A based on friend community***

***4. Ranking the score of all items which the user may consider to buy them***

**Example:**

User A : (Item a，Item c,Item d)

User B : (Item a，Item b,Item e)

User C : (Item b，Item c,Item f)

User D : (Item a，Item c,Item g)

User E : (Item e，Item f,Item g)

Purpose: Predict User A will buy what items

Firstly, finding A's friends who have one of the same item,  and resulting as user B, C and D.

① A's friends = {B,C,D}

Secondly, calculating the score of each items of user A, using Jaccard distance between friends.

②Jaccard(A,B) = {A.items ∩ B.items} / {A.items ∪ B.items} = {a} / {a,c,d,b,e} = 1/5

 Jaccard(A,C) = {A.items ∩ C.items} / {A.items ∪ C.items} = {c} / {a,c,d,b,f} = 1/5
 
 Jaccard(A,D) = {A.items ∩ D.items} / {A.items ∪ D.items} = {a,c} / {a,c,d,g} = 1/2
 
Next, calculating the score of each item of user A.

③Score(a) += {if a in friends'items} * Jaccard(A,friends) => Score(a) = Jaccard(A,B) + Jaccard(A,D) = 1/5 + 1/2 = 7/10

③Score(c) += {if c in friends'items} * Jaccard(A,friends) => Score(c) = Jaccard(A,C) + Jaccard(A,D) = 1/5 + 1/2 = 7/10

③Score(d) += {if d in friends'items} * Jaccard(A,friends) => Score(d) = 0

Finally, ranking the score of user A's all itemms.

④ a = c > d > b = e = f =g
