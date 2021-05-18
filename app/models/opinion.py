class Opinion:
    
    
    
    selectors =  {
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__col:has(> div[class*=\"positives\"]) > div.review-feature__item",1],
    "cons": ["div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item",1],
    "purchased": ["div.review-pz"],
    "submit_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "useful": ["span[id^='votes-yes']"],
    "useless": ["span[id^='votes-no']"]
}

    def __init__(self, opinionId=None, author=None, recommendation=None, stars=None, content=None, pros=None, cons=None,
                 purchased =None, submit_date=None, purchase_date=None, useful=None, useless=None):
        self.opinionId = opinionId
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.purchased = purchased
        self.submit_date = submit_date
        self.purchase_date = purchase_date
        self.useful = useful
        self.useless = useless
